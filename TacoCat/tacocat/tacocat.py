import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from .properties import HT9Props
#import HT9Props
from .calculations import HexDhCal
#import HexDhCal
from .calculations import HegNu
#import HegNu
from .calculations import TempBulkCal
#import TempBulkCal
from .tacocat_read_in_file import Fuel_Type, Coolant, Hc, HotF, Reactor_Title, Qth, Tbulkin
from scipy.integrate import trapz
from scipy.integrate import quad
from .properties.Fuel_Props import Fuel_props

#Assumptions
#1. The core thermal production is assumed to set after heat deposition
#(i.e. gamma isn't relevant)

#----------------------------------------------------------------------------------#
## Print Logicals for saving plots and data files (0 - save, 1 or higher - do not save)

print_logic = 1
data_logic = 1

#----------------------------------------------------------------------------------#
## General Core Information

#Read in parameters
#Fuel_Type = Fuel_Type
Coolant_Type = Coolant
#Hc = Hc
#HotF = HotF

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
Qth = Qth
Tbulkin = Tbulkin #Bulk Temperature of NaK at the Inlet - C
U_Zr10 = {
	"kfuel": 22, #Thermal Conductivity of Fuel - W/m-C @ 1000 C
	"Tmelt": 1160.00 #Melting temperature - C
}

UC = {
	"kfuel": 23, #Thermal Conductivity of Fuel - W/m-C
	"Tmelt": 2506.85 #Melting temperature - C (2780 K)
}

UO2 = {
	"kfuel": 3.6, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2800 #Melting Temperature - C
}

PuO2 = {
	"kfuel": 4.3, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2374 #Melting Temperature - C
}

ThO2 = {
	"kfuel": 5.76, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 3378 #Melting Temperature - C
}

UN = {
	"kfuel": 21, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2800 #Melting Temperature - C
}

U3Si2 = {
	"kfuel": 15, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 1665 #Melting Temperature - C
}

MOX = {
	"kfuel": 3.7, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2774 #Melting Temperature - C
	#MOX values are for 94% UO2 and 6% PuO2
}

U = {
	"kfuel": 32, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 1133 #Melting Temperature - C
}

Fuel_props = {
	"U_Zr10": U_Zr10,
	"UC": UC,
	"UO2": UO2,
	"PuO2": PuO2,
	"ThO2": ThO2,
	"UN": UN,
	"U3Si2": U3Si2,
	"MOX": MOX,
	"U": U
}


#----------------------------------------------------------------------------------#
## Material Properties

#Thermal Fluid Properties of Coolants
#CoolantUsed = int(input('Enter the number for the coolant you would like to use: 1. NaK 2. FLiBe 3. FLiNaK 4. NaF_ZrF4:  '))

if Coolant_Type == "NaK":
	from .properties import NaK_Prop
	rhoNa = NaK_Prop.rhoNa(Tbulkin + 273.15)
	rhoK = NaK_Prop.rhoK(Tbulkin + 273.15)
	invrhoNaK = 0.22/rhoNa + 0.78/rhoK
	rho = 1/invrhoNaK #kg/m^3
	CpNa = NaK_Prop.CpNa(Tbulkin + 273.15)
	CpK = NaK_Prop.CpK(Tbulkin + 273.15)
	Cp = (10**3)*(0.22*CpNa + 0.78*CpK) #J/kg-K
	k = NaK_Prop.k(Tbulkin + 273.15)
	nu = NaK_Prop.nu(Tbulkin + 273.15)
	TmeltCoolant = -12.6 #Melting Temperature of NaK - C
	Tboil = 784.00 #Boiling Temperature of NaK - C
elif Coolant_Type == "FLiBe":
	from .properties import FLiBe_Prop
	rho = FLiBe_Prop.rho(Tbulkin + 273.15)
	Cp = FLiBe_Prop.Cp(Tbulkin + 273.15)
	k = FLiBe_Prop.k(Tbulkin + 273.15)
	nu = FLiBe_Prop.nu(Tbulkin + 273.15)
	TmeltCoolant = 459 #Melting Temperature of FLiBe - C
	Tboil = 1430 #Boiling Temperature of FLiBe - C
elif Coolant_Type == "FLiNaK":
	from .properties import FLiNaK_Prop
	rho = FLiNaK_Prop.rho(Tbulkin + 273.15)
	Cp = FLiNaK_Prop.Cp(Tbulkin + 273.15)
	k = FLiNaK_Prop.k(Tbulkin + 273.15)
	nu = FLiNaK_Prop.nu(Tbulkin + 273.15)
	TmeltCoolant = 454 #Melting Temperature of FLiNaK - C
	Tboil = 1570 #Boiling Temperature of FLiNaK - C
elif Coolant_Type == "NaF_ZrF4":
	from .properties import NaF_ZrF4_Prop
	rho = NaF_ZrF4_Prop.rho(Tbulkin + 273.15)
	Cp = NaF_ZrF4_Prop.Cp(Tbulkin + 273.15)
	k = NaF_ZrF4_Prop.k(Tbulkin + 273.15)
	nu = NaF_ZrF4_Prop.nu(Tbulkin + 273.15)
	TmeltCoolant = 500 #Melting Temperature of NaF_ZrF4 - C
	Tboil = 1350 #Boiling Temperature of NaF_ZrF4 - C

Pr = Cp*nu*rho/k #Prandtl Number Calculation

#Thermal Conductivity of Cladding - W/m-K @ 300 C
kclad = HT9Props.k(Tbulkin + 273.15)

#----------------------------------------------------------------------------------#
## Core Geometry Calculations
# Geometric Calculations
CVol = HexDhCal.Ha(Ac)*Hc #Volume of the core - m^3
Uinlet = 0.0375

#----------------------------------------------------------------------------------#
## Core Parameter Calculations 

# Power Density and Linear Generation Calculations
Qavgp = Qth/CVol #Average Power Density Calculation - W/m^3
qlin = Qth/(NFuel*Hc) # Average Rod Linear Energy Generation Rate - W/m
qlinHotF = qlin*HotF # Hottest Channel Linear Energy Generation Rate - W/m
qppco = qlin/(np.pi*FoCD) # Average heat flux at rod/coolant interface - W/m^2

# Coolant Calculations
mdot = Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD) # Mass flow rate for the fluid - kg/s
Pe = (Uinlet*HexDhCal.Dh1(HexDhCal.A1(PtoD,FoCD,WoD),HexDhCal.P1(FoCD,WoD))/nu)*Pr # Peclet Number for Fluid
Nu = HegNu.Nu(PtoD,Pe)
h = Nu*k/HexDhCal.Dh1(HexDhCal.A1(PtoD,FoCD,WoD),HexDhCal.P1(FoCD,WoD)) #Heat Transfer Coefficient for Rod Bundles - W/m^2 - C

#Core Temperature Calculations
#Call axial bulk temperature distribution calculation

FluxPro = np.zeros(steps)
FluxPro[:] = np.cos((np.pi/Hc)*z[:])

Tbulk = np.zeros(steps) #Initialize Bulk Temperature of Coolant - C
Tbulk[0] = Tbulkin
TbulkHotF = np.zeros(steps)
TbulkHotF[0] = Tbulkin
for i in range(1,steps):
	Tbulk[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlin)/(Cp*Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) #Bulk Temperature of Coolant - C
	TbulkHotF[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlinHotF)/(Cp*Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) #Bulk Temperature of Coolant - C

# Bulk Temperature of Coolant in Hottest Channel - C
Tcl = np.zeros(steps)
TclHotF = np.zeros(steps)
for i in range(0,steps):
	Tcl[i] = Tbulk[i] + ((FluxPro[i]*qlin)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*Fuel_props[Fuel_Type]["kfuel"])) + (1/kclad)*np.log(FoCD/FoD))
	TclHotF[i] = TbulkHotF[i] + ((FluxPro[i]*qlinHotF)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*Fuel_props[Fuel_Type]["kfuel"])) + (1/kclad)*np.log(FoCD/FoD))

Tavg = (Tbulk[0] + Tbulk[steps-1])/2
THotFavg = (TbulkHotF[0] + TbulkHotF[steps-1])/2
if Coolant_Type == "NaK":
	rhoNamax = NaK_Prop.rhoNa(Tbulk[steps-1] + 273.15)
	rhoKmax = NaK_Prop.rhoK(Tbulk[steps-1] + 273.15)
	CpNamax = NaK_Prop.CpNa(Tbulk[steps-1] + 273.15)
	CpKmax = NaK_Prop.CpK(Tbulk[steps-1] + 273.15)
	Cpmax = (10**3)*(0.22*CpNamax + 0.78*CpKmax) #J/kg-K
	kmax = NaK_Prop.k(Tbulk[steps-1] + 273.15)
	numax = NaK_Prop.nu(Tbulk[steps-1] + 273.15)
	invrhoNaKmax = 0.22/rhoNamax + 0.78/rhoKmax
	rhomax = 1/invrhoNaKmax #kg/m^3
elif Coolant_Type == "FLiBe":
	rhomax = FLiBe_Prop.rho(Tbulk[steps-1] + 273.15)
	Cpmax = FLiBe_Prop.Cp(Tbulk[steps-1] + 273.15)
	kmax = FLiBe_Prop.k(Tbulk[steps-1] + 273.15)
	numax = FLiBe_Prop.nu(Tbulk[steps-1] + 273.15)
elif Coolant_Type == "FLiNaK":
	rhomax = FLiNaK_Prop.rho(Tbulk[steps-1] + 273.15)
	Cpmax = FLiNaK_Prop.Cp(Tbulk[steps-1] + 273.15)
	kmax = FLiNaK_Prop.k(Tbulk[steps-1] + 273.15)
	numax = FLiNaK_Prop.nu(Tbulk[steps-1] + 273.15)
elif Coolant_Type == "NaF_ZrF4":
	rhomax = NaF_ZrF4_Prop.rho(Tbulk[steps-1] + 273.15)
	Cpmax = NaF_ZrF4_Prop.Cp(Tbulk[steps-1] + 273.15)
	kmax = NaF_ZrF4_Prop.k(Tbulk[steps-1] + 273.15)
	numax = NaF_ZrF4_Prop.nu(Tbulk[steps-1] + 273.15)
Prmax = Cpmax*numax*rhomax/kmax #Prandtl Number Calculation

#Max and Averaged quantities with calculated outlet temperature
Pravg = (Pr + Prmax)/2 # Average Prandtl Number in a inner channel
rhoavg = (rho + rhomax)/2 # Average density number in a inner channel
Uoutlet = mdot/(rhomax*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) # Outlet Velocity in a inner channel
Uavg = (Uinlet + Uoutlet)/2 # Average velocity in a inner channel
Pemax = Prmax*Uoutlet*FoCD/numax # Max Peclet number in a inner channel
Peavg = (Pe + Pemax)/2 # Average Peclect number in a inner channel
Re1 = Peavg/Pravg # Average Reynolds number in a inner channel

M = ((1.034/(PtoD**0.124))+(29.7*(PtoD**6.94)*Re1**0.086)/(HexDhCal.LeadW(FoCD,WoD)/FoCD)**2.239)**0.885
fsm = 0.316*Re1**(-0.25)
dP = M*fsm*(Hc/HexDhCal.Dh1(HexDhCal.A1(PtoD,FoCD,WoD),HexDhCal.P1(FoCD,WoD)))*0.5*rhoavg*Uavg**2

#Heat Load Calculation
QPri = Uavg*rhoavg*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)*((Cp + Cpmax)/2)*(Tbulk[steps-1]-Tbulk[0])

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
fig = Reactor_Title + '_Axial_Temperatures'
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

title_data = Reactor_Title + "_table"
if data_logic == 0:
	df1.to_excel(title_data + ".xlsx")
	df2.to_csv(title_data + '.csv') 

print(df2)
