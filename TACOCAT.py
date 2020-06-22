import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import NaK_Prop
import HT9Props
import HexDhCal
import HegNu
import TempBulkCal
from scipy.integrate import trapz
from scipy.integrate import quad

#Assumptions
#1. The core thermal production is assumed to set after heat deposition
#(i.e. gamma isn't relevant)

#User Input to define function (replacing Read in the core...)
#FluxPro = input('Define a function') #Flux Profile

#----------------------------------------------------------------------------------#
## Print Logical for saving plots or not (0 - save plots, 1 or higher - do not save plots)

print_logic = 1

#----------------------------------------------------------------------------------#
##General Core Information

#Geometry - Core
Hc = 0.35 #Active Height of Core is 2m
steps = 36 #Needs to be changed, filler for z
z = np.linspace(-Hc/2,Hc/2,steps) #this needs to be a numpy array of position along the core in - m
Ar = 33.8/100 #Active Radius of the core - m
Ac = (2*(Ar**2)*np.pi/(3*3**0.5))**0.5 #Length of Hexagonal Size - m

#Geometry - Fuel
FoD = 0.58/100 #Fuel Outer Diameter - m
FoCD = 0.64/100 #Cladding Outer Diameter - m
WoD = 0.1/100 #Wire Wrap Diamerer - m
PtoD = 1.18 #Pitch to Diameter Ratio
NFuel = 1951 #Number of Fuel Rods

#Core Parameter - Inputs
Qth = 3*10**6 #Core Thermal Production - W
Tmelt = 1160.00 #Melting temperature of UPu-Zr10 - C
Tboil = 784.00 #Boiling Temperature of NaK - C
Tbulkin = 550.00 #Bulk Temperature of NaK at the Inlet - C
Tbulk = np.zeros(steps) #Initialize Bulk Temperature of Coolant - C

##Material Properties

#Thermal Fluid Properties of NaK
rhoNa = NaK_Prop.rhoNa(Tbulkin + 273.15)
rhoK = NaK_Prop.rhoK(Tbulkin + 273.15)
CpNa = NaK_Prop.CpNa(Tbulkin + 273.15)
CpK = NaK_Prop.CpK(Tbulkin + 273.15)
Cp = (10**3)*(0.22*CpNa + 0.78*CpK) #J/kg-K
k = NaK_Prop.k(Tbulkin + 273.15)
nu = NaK_Prop.nu(Tbulkin + 273.15)
invrhoNaK = 0.22/rhoNa + 0.78/rhoK
rho = 1/invrhoNaK #kg/m^3
Pr = Cp*nu*rho/k #Prandtl Number Calculation

#Thermal Conductivity of Cladding - W/m-K @ 300 C
kclad = HT9Props.k(Tbulkin + 273.15)
kfuel = 22 #Thermal Conductivity of Fuel - W/m-K @ 1000 C

##Core Geometry Calculations
#Geometric Calculations
CVol = HexDhCal.Ha(Ac)*Hc #Volume of the core - m^3
Uinlet = 0.0375

#HexDhCal is copied above, error when ran as module

##Core Parameter Calculations 

#Hottest Channel Factor Calculation
HotF = 1.5

#Power Density and Linear Generation Calculations
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

Tbulk[0] = Tbulkin
FluxPro = np.zeros(steps)
FluxPro[:] = np.cos((np.pi/Hc)*z[:])
#plt.plot(z,FluxPro, 'c')
#plt.grid()
#plt.show()

for i in range(1,steps):
	Tbulk[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlin)/(Cp*Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) #Bulk Temperature of Coolant - C

TbulkHotF = np.zeros(steps)
TbulkHotF[0] = Tbulkin

#Bulk Temperature of Coolant - C
for i in range(1,steps):
	TbulkHotF[i] = Tbulkin + (np.trapz(FluxPro[0:i+1],z[0:i+1])*NFuel*qlinHotF)/(Cp*Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) #Bulk Temperature of Coolant - C


# Bulk Temperature of Coolant in Hottest Channel - C
Tcl = np.zeros(steps)
for i in range(0,steps):
	Tcl[i] = Tbulk[i] + ((FluxPro[i]*qlin)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*kfuel)) + (1/kclad)*np.log(FoCD/FoD)) #+ (qlin/(mdot*Cp))*quad(FluxPro, 1, 8)

TclHotF = np.zeros(steps)
for i in range(0,steps):
	TclHotF[i] = TbulkHotF[i] + ((FluxPro[i]*qlinHotF)/(2*np.pi))*((1/(h*(FoCD/2))) + (1/(2*kfuel)) + (1/kclad)*np.log(FoCD/FoD))


'''
plt.figure(2)
plt.plot(z,Tcl, 'r')
plt.grid()

plt.show()
'''


Tavg = (Tbulk[0] + Tbulk[steps-1])/2
THotFavg = (TbulkHotF[0] + TbulkHotF[steps-1])/2
rhoNamax = NaK_Prop.rhoNa(Tbulk[steps-1] + 273.15)
rhoKmax = NaK_Prop.rhoK(Tbulk[steps-1] + 273.15)
CpNamax = NaK_Prop.CpNa(Tbulk[steps-1] + 273.15)
CpKmax = NaK_Prop.CpK(Tbulk[steps-1] + 273.15)
Cpmax = (10**3)*(0.22*CpNamax + 0.78*CpKmax) #J/kg-K
kmax = NaK_Prop.k(Tbulk[steps-1] + 273.15)
numax = NaK_Prop.nu(Tbulk[steps-1] + 273.15)
invrhoNaKmax = 0.22/rhoNamax + 0.78/rhoKmax
rhomax = 1/invrhoNaKmax #kg/m^3
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

h = 6.5
w = 4.5
lw = 2.5
fs = 12

k = 1
plt.figure(k, figsize=(h,w))
plt.plot(z,Tbulk,'r--',linewidth = lw,label=r'$T_{bulk}$')
plt.plot(z,TbulkHotF,'k--',linewidth = lw, label=r'$T_{bulk-HF}$')
plt.plot(z,Tcl, 'g-',linewidth = lw, label=r'$T_{cl}$')
plt.plot(z,TclHotF, 'c-',linewidth = lw, label=r'$T_{cl-HF}$')
plt.axhline(y=785.0,xmin = 0, xmax = 1, color = 'r',linewidth = lw, label='NaK Boiling Temp')
plt.legend(loc='center left')
plt.xlabel('Axial Height - m',fontsize = fs)
plt.ylabel('Temperature - C',fontsize = fs)
plt.grid()
fig = 'TACOCAT_Axial_Temperatures'
if print_logic == 0:
    plt.savefig(fig + '.png', dpi = 300, format = "png",bbox_inches="tight")
    plt.savefig(fig + '.eps', dpi = 300, format = "eps",bbox_inches="tight")
    plt.savefig(fig + '.svg', dpi = 300, format = "svg",bbox_inches="tight")
k = k + 1

plt.figure(k, figsize=(7.5,5.5))
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
## Create data files for run

df1 = pd.DataFrame([[Tbulk[0]], [Tbulk[steps-1]], [Tavg], [TbulkHotF[steps-1]], [THotFavg], [Tcl[steps-1]], [TclHotF[steps-1]]], index=['Inlet Bulk Temperature', 'Outlet Bulk Temperature', 'Average Bulk Temperature', 'Outlet Bulk Temperature - Hot Channel', 'Average Coolant Temperature - Hot Channel', 'Highest Fuel Centerline Temperature', 'Highest Fuel Centerline Temperature - Hottest Channel'], columns=['Temperature - C'])
df1.to_excel("TACOCAT_table.xlsx")
df2 = pd.DataFrame({'z': z, 'Tbulk': Tbulk, 'TbulkHotF': TbulkHotF, 'Tcl': Tcl, 'TclHotF': TclHotF, 'Flux Profile': FluxPro, 'Fuel Melting Temperature': Tmelt, 'Coolant Boiling Temperature': Tboil})
df2.to_csv('TACOCATData.csv') 
print(df2)

#data = {'Data' : ['Inlet Bulk Temperature', 'Outlet Bulk Temperature', 'Average Bulk Temperature', 'Average Bulk Temperature', 'Outlet Bulk Temperature - Hot Channel', 'Average Coolant Temperature - Hot Channel', 'Highest Fuel Centerline Temperature', 'Highest Fuel Centerline Temperature - Hottest Channel'], 'Temperature - C': [Tbulk[0], Tbulk[steps-1], Tavg, TbulkHotF[steps-1], THotFavg, Tcl[steps-1], TclHotF[steps-1]]}
#df2 = pd.DataFrame()
#df2.to_csv('TACOCAT.csv')