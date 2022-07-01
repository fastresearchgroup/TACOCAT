import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import HT9Props as clad
import HexDhCal as Geom
import HegNu as Nu
import TempBulkCal as TempBulk
import TACOCAT_Read_In_File as TCinput
from scipy.integrate import trapz
from scipy.integrate import quad
from Fuel_Props import Fuel_props
from Geometry_Value import Core_Geometry

#Assumptions
#1. The core thermal production is assumed to set after heat deposition
#(i.e. gamma isn't relevant)

#----------------------------------------------------------------------------------#
## Print Logicals for saving plots and data files (0 - save, 1 or higher - do not save)

print_logic = TCinput.print_logic
data_logic = TCinput.data_logic

#----------------------------------------------------------------------------------#
## General Core Information

#Read in parameters
Fuel_Type = TCinput.Fuel_Type
Coolant_Type = TCinput.Coolant
Geometry_Type = TCinput.Geometry
Hc = TCinput.Hc
HotF = TCinput.HotF

# Geometry - Core
steps = 36 #Needs to be changed, filler for z
z = np.linspace(-Hc/2,Hc/2,steps) #this needs to be a numpy array of position along the core in - m
Ar = 33.8/100 #Active Radius of the core - m
Ac = (2*(Ar**2)*np.pi/(3*3**0.5))**0.5 #Length of Hexagonal Size - m

# Geometry - Fuel
FoD = 0.58/100 #Fuel Outer Diameter - m
FoCD = 0.64/100 #Cladding Outer Diameter - m
WoD = 0.1/100 #Wire Wrap Diamerer - m
PtoD = 1.18 #Pitch to Diameter Ratio
NFuel = 1951 #Number of Fuel Rods

# Core Parameter - Inputs
Qth = TCinput.Qth
Tbulkin = TCinput.Tbulkin #Bulk Temperature of coolant at the Inlet - C
Uinlet = TCinput.Uinlet #average inlet velocity in a subchannel - m/s

#----------------------------------------------------------------------------------#
## Material Properties

#Thermal Fluid Properties of Coolants
#CoolantUsed = int(input('Enter the number for the coolant you would like to use: 1. NaK 2. FLiBe 3. FLiNaK 4. NaF_ZrF4:  '))

if Coolant_Type == "NaK":
	import TACOCAT.src.NaK_Prop as fluid
	rho_Na = fluid.rhoNa(Tbulkin + 273.15)
	rho_K = fluid.rhoK(Tbulkin + 273.15)
	invrhoNaK = 0.22/rho_Na + 0.78/rho_K
	rho = 1/invrhoNaK #kg/m^3
	CpNa = fluid.CpNa(Tbulkin + 273.15)
	CpK = fluid.CpK(Tbulkin + 273.15)
	Cp = (10**3)*(0.22*CpNa + 0.78*CpK) #J/kg-K
	k = fluid.k(Tbulkin + 273.15)
	nu = fluid.nu(Tbulkin + 273.15)
	TmeltCoolant = -12.6 #Melting Temperature of NaK - C
	Tboil = 784.00 #Boiling Temperature of NaK - C
elif Coolant_Type == "FLiBe":
	import TACOCAT.src.FLiBe_Prop as fluid
	rho = fluid.rho(Tbulkin + 273.15)
	Cp = fluid.Cp(Tbulkin + 273.15)
	k = fluid.k(Tbulkin + 273.15)
	nu = fluid.nu(Tbulkin + 273.15)
	TmeltCoolant = 459 #Melting Temperature of FLiBe - C
	Tboil = 1430 #Boiling Temperature of FLiBe - C
elif Coolant_Type == "FLiNaK":
	import TACOCAT.src.FLiNaK_Prop as fluid
	rho = fluid.rho(Tbulkin + 273.15)
	Cp = fluid.Cp(Tbulkin + 273.15)
	k = fluid.k(Tbulkin + 273.15)
	nu = fluid.nu(Tbulkin + 273.15)
	TmeltCoolant = 454 #Melting Temperature of FLiNaK - C
	Tboil = 1570 #Boiling Temperature of FLiNaK - C
elif Coolant_Type == "NaF_ZrF4":
	import TACOCAT.src.NaF_ZrF4_Prop as fluid
	rho = fluid.rho(Tbulkin + 273.15)
	Cp = fluid.Cp(Tbulkin + 273.15)
	k = fluid.k(Tbulkin + 273.15)
	nu = fluid.nu(Tbulkin + 273.15)
	TmeltCoolant = 500 #Melting Temperature of NaF_ZrF4 - C
	Tboil = 1350 #Boiling Temperature of NaF_ZrF4 - C

Pr = Cp*nu*rho/k #Prandtl Number Calculation

#Thermal Conductivity of Cladding - W/m-K @ 300 C
kclad = clad.k(Tbulkin + 273.15)

#----------------------------------------------------------------------------------#
## Core Geometry Calculations
# Geometric Calculations
CVol = Core_Geometry[Geometry_Type]["FaceArea"]*Hc #Volume of the core - m^3

#----------------------------------------------------------------------------------#
## Core Parameter Calculations 

# Power Density and Linear Generation Calculations
Qavgp = Qth/CVol #Average Power Density Calculation - W/m^3
qlin = Qth/(NFuel*Hc) # Average Rod Linear Energy Generation Rate - W/m
qlinHotF = qlin*HotF # Hottest Channel Linear Energy Generation Rate - W/m
qppco = qlin/(np.pi*FoCD) # Average heat flux at rod/coolant interface - W/m^2

# Coolant Calculations
mdot = Uinlet*rho*Core_Geometry[Geometry_Type]["CoolantFlowArea"] # Mass flow rate for the fluid - kg/s
Pe = (Uinlet*Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"]/nu)*Pr # Peclet Number for Fluid
Nu = Nu.Nu(PtoD,Pe)
h = Nu*k/Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"] #Heat Transfer Coefficient for Rod Bundles - W/m^2 - C

#Core Temperature Calculations
#Call axial bulk temperature distribution calculation

FluxPro = np.zeros(steps)
FluxPro[:] = np.cos((np.pi/Hc)*z[:])

Tbulk = np.zeros(steps) #Initialize Bulk Temperature of Coolant - C
Tbulk[0] = Tbulkin
TbulkHotF = np.zeros(steps)
TbulkHotF[0] = Tbulkin
for i in range(1,steps):
    # Bulk Temperature of Coolant in Average Channel - C
	Tbulk[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlin)/(Cp*Uinlet*rho*Core_Geometry[Geometry_Type]["CoolantFlowArea"]) #Bulk Temperature of Coolant - C
    # Bulk Temperature of Coolant in Hottest Channel - C
	TbulkHotF[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlinHotF)/(Cp*Uinlet*rho*Core_Geometry[Geometry_Type]["CoolantFlowArea"]) #Bulk Temperature of Coolant - C

Tcl = np.zeros(steps)
TclHotF = np.zeros(steps)
for i in range(0,steps):
    # Centerline Temperature of Fuel in Average Channel - C
	Tcl[i] = Tbulk[i] + ((FluxPro[i]*qlin)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*Fuel_props[Fuel_Type]["kfuel"])) + (1/kclad)*np.log(FoCD/FoD))
    # Centerline Temperature of Fuel in Hottest Channel - C
	TclHotF[i] = TbulkHotF[i] + ((FluxPro[i]*qlinHotF)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*Fuel_props[Fuel_Type]["kfuel"])) + (1/kclad)*np.log(FoCD/FoD))

Tavg = (Tbulk[0] + Tbulk[steps-1])/2
THotFavg = (TbulkHotF[0] + TbulkHotF[steps-1])/2
if Coolant_Type == "NaK":
	rhoNamax = fluid.rhoNa(Tbulk[steps-1] + 273.15)
	rhoKmax = fluid.rhoK(Tbulk[steps-1] + 273.15)
	CpNamax = fluid.CpNa(Tbulk[steps-1] + 273.15)
	CpKmax = fluid.CpK(Tbulk[steps-1] + 273.15)
	Cpmax = (10**3)*(0.22*CpNamax + 0.78*CpKmax) #J/kg-K
	kmax = fluid.k(Tbulk[steps-1] + 273.15)
	numax = fluid.nu(Tbulk[steps-1] + 273.15)
	invrhoNaKmax = 0.22/rhoNamax + 0.78/rhoKmax
	rhomax = 1/invrhoNaKmax #kg/m^3
elif Coolant_Type == "FLiBe":
	rhomax = fluid.rho(Tbulk[steps-1] + 273.15)
	Cpmax = fluid.Cp(Tbulk[steps-1] + 273.15)
	kmax = fluid.k(Tbulk[steps-1] + 273.15)
	numax = fluid.nu(Tbulk[steps-1] + 273.15)
elif Coolant_Type == "FLiNaK":
	rhomax = fluid.rho(Tbulk[steps-1] + 273.15)
	Cpmax = fluid.Cp(Tbulk[steps-1] + 273.15)
	kmax = fluid.k(Tbulk[steps-1] + 273.15)
	numax = fluid.nu(Tbulk[steps-1] + 273.15)
elif Coolant_Type == "NaF_ZrF4":
	rhomax = fluid.rho(Tbulk[steps-1] + 273.15)
	Cpmax = fluid.Cp(Tbulk[steps-1] + 273.15)
	kmax = fluid.k(Tbulk[steps-1] + 273.15)
	numax = fluid.nu(Tbulk[steps-1] + 273.15)
Prmax = Cpmax*numax*rhomax/kmax #Prandtl Number Calculation

#Max and Averaged quantities with calculated outlet temperature
Pravg = (Pr + Prmax)/2 # Average Prandtl Number in a inner channel
rhoavg = (rho + rhomax)/2 # Average density number in a inner channel
Uoutlet = mdot/(rhomax*Core_Geometry[Geometry_Type]["CoolantFlowArea"]) # Outlet Velocity in a inner channel
Uavg = (Uinlet + Uoutlet)/2 # Average velocity in a inner channel
Pemax = Prmax*Uoutlet*FoCD/numax # Max Peclet number in a inner channel
Peavg = (Pe + Pemax)/2 # Average Peclect number in a inner channel
Re1 = Peavg/Pravg # Average Reynolds number in a inner channel

if Geometry_Type == "Hexagonal":
	M = ((1.034/(PtoD**0.124))+(29.7*(PtoD**6.94)*Re1**0.086)/(Geom.LeadW(FoCD,WoD)/FoCD)**2.239)**0.885 #modifier
else:
	M = 1
fsm = 0.316*Re1**(-0.25)
dP = M*fsm*(Hc/Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"])*0.5*rhoavg*Uavg**2

#Heat Load Calculation
QPri = Uavg*rhoavg*Core_Geometry[Geometry_Type]["CoolantFlowArea"]*((Cp + Cpmax)/2)*(Tbulk[steps-1]-Tbulk[0])

#----------------------------------------------------------------------------------#
## Report out - Core Parameters
## Print out

print('--------------------------------------------------------')
print('Heat Load:',QPri/10**6,'MW')
print('Average Power Density:',Qavgp/10**6,'MW/m^3')
print('Average Linear Energy Gen Rate per Rod:',qlin/10**3,'kW/m')
print('Average Heat Flux at Interface:',qppco/10**6,'MW/m^2')
print('Hot Channel Factor:',HotF)
print('Mass Flow Rate:',mdot,'kg/s')
print('Velocity:',Uinlet,'m/s')
print('Inlet Bulk Temperature:',Tbulk[0],'C')
print('Outlet Bulk Temperature:',Tbulk[steps-1],'C')
print('Average Bulk Temperature:',Tavg,'C')
print('Outlet Bulk Temperature - Hot Channel',TbulkHotF[steps-1],'C')
print('Average Coolant Temperature - Hot Channel:',THotFavg,'C')
print('Highest Centerline Temperature:',Tcl[steps-1],'C')
print('Highest Centerline Temperature - Hottest Channel:',TclHotF[steps-1],'C')
print('Pressure Drop - Bundle:',dP,'Pa')
print('--------------------------------------------------------')

#----------------------------------------------------------------------------------#
## Report out - Core Parameters
## Create data files for each run and print out the data

df1 = pd.DataFrame([[Tbulk[0]], [Tbulk[steps-1]], [Tavg], [TbulkHotF[steps-1]], [THotFavg], [Tcl[steps-1]], [TclHotF[steps-1]]], index=['Inlet Bulk Temperature', 'Outlet Bulk Temperature', 'Average Bulk Temperature', 'Outlet Bulk Temperature - Hot Channel', 'Average Coolant Temperature - Hot Channel', 'Highest Fuel Centerline Temperature', 'Highest Fuel Centerline Temperature - Hottest Channel'], columns=['Temperature - C'])
df2 = pd.DataFrame({'z': z, 'Tbulk': Tbulk, 'TbulkHotF': TbulkHotF, 'Tcl': Tcl, 'TclHotF': TclHotF, 'Flux Profile': FluxPro, 'Fuel Melting Temperature': Fuel_props[Fuel_Type]["Tmelt"], 'Coolant Boiling Temperature': Tboil})

title_data = TCinput.Reactor_Title + "_table"
if data_logic == 0:
	df1.to_excel(title_data + ".xlsx")
	df2.to_csv(title_data + '.csv') 

#----------------------------------------------------------------------------------#
## Report out - Core Parameters
## Plots

h = 10
w = 8

lw = 2.5
fs = 14

k = 1
plt.figure(k, figsize=(h,w))
plt.plot(z,Tbulk,'r--',linewidth = lw,label=r'$T_{bulk}$')
plt.plot(z,TbulkHotF,'k--',linewidth = lw, label=r'$T_{bulk-HF}$')
plt.plot(z,Tcl, 'g-',linewidth = lw, label=r'$T_{cl}$')
plt.plot(z,TclHotF, 'c-',linewidth = lw, label=r'$T_{cl-HF}$')
plt.axhline(y=Tboil, xmin = 0, xmax = 1, color = 'r',linewidth = lw, label='Coolant Boiling Temp')
plt.axhline(y=TmeltCoolant, xmin = 0, xmax = 1, color = 'b',linewidth = lw, label='Coolant Melting Temp')
plt.legend(loc='center left')
plt.xlabel('Axial Height - m',fontsize = fs)
plt.ylabel('Temperature - C',fontsize = fs)
plt.grid()
fig = TCinput.Reactor_Title + '_Axial_Temperatures'
if print_logic == 0:
    plt.savefig(fig + '.png', dpi = 300, format = "png",bbox_inches="tight")
    plt.savefig(fig + '.eps', dpi = 300, format = "eps",bbox_inches="tight")
    plt.savefig(fig + '.svg', dpi = 300, format = "svg",bbox_inches="tight")
k = k + 1

plt.figure(k, figsize=(h,w))
plt.plot(z,FluxPro, 'k-')
plt.suptitle('Axial Core Flux Profile')
plt.ylabel('Normalized Height')
plt.xlabel('Normalized Flux')
plt.grid()
k = k + 1

plt.show()