  
# Sierra Tutwiler
# Last Modified: 6/2/2020
# Verify fluid properties for Flibe
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import os
import sys
sys.path.insert(0,'..') #This adds the ability to call flibe props from the main folder
sys.path.insert(0,'./Flibe') #Looking for data in a subfolder
import numpy as np 
from pathlib import Path 
import matplotlib.pyplot as plt  
import FLiBe_Prop
import Flibe_Cp_Verification_Data
import pandas as pd

path = os.getcwd()

steps = 700

T = np.linspace(550,1250,steps)
T2 = np.linspace(700,1200,steps)

Rho = np.zeros(steps)
Nu = np.zeros(steps)
Cp = np.zeros(steps)
K = np.zeros(steps)

for i in range(0,steps):
	Rho[i] = FLiBe_Prop.rho(T[i])
	Nu[i] = FLiBe_Prop.nu(T2[i])*1000
	Cp[i] = FLiBe_Prop.Cp(T2[i])
	K[i] = FLiBe_Prop.k(T2[i])

linestyles = ['None','--','None',':','None','-','--','-.']
markers = ['D', 'None', '^', 'None', 's', 'None', 'None', 'None']
colors = ['blue','purple','darkgreen','fuchsia','firebrick','darkorange','lime','cornflowerblue']
filelist = ['Blanke_1956','Cantor_1968','Cantor_1973','Gierszewski_1980','Janz_1974','Janz_1974_1988','Zaghoul_2003','Recommended']
k = 1
L = 0
fig1 = plt.figure(k, figsize=(10,8))
for f in filelist:
	densitydataframes = pd.read_csv(Path(path + '/Flibe/Density/Romatoski_Flibe_Density_' + f + '.csv'))
	df = pd.DataFrame(densitydataframes)
	plt.plot(df['Temp'], df['Density'], label=f, linestyle=linestyles[L], color=colors[L], marker=markers[L])
	L = L + 1
plt.plot(T,Rho,'r--', label='Density Used', linewidth=3, dashes=(10,20))
plt.title('Flibe Density')
plt.xlabel('Temperature - K')
plt.ylabel('Density - kg/m^3')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

linestyles2 = ['--','None','None','-','--','--',':','None']
markers2 = ['^', 's', 'x', 'None', 'None', 'o','None', '+']
colors2 = ['purple','dodgerblue','salmon','cyan','slategray','yellowgreen','blue','darkorange']
filelist2 = ['Abe_1981_67','Blanke_1956_62','Blanke_1956_69-31','Cantor_1968_66-34','Cantor_1969_64-36','Cohen_1956_69-31','Gierszewski_1980_66-34','Janz_1974_64-36']
L = 0
fig2 = plt.figure(k, figsize=(10,8))
for f in filelist2:
	viscositydataframes = pd.read_csv(Path(path + '/Flibe/Viscosity/Romatoski_Flibe_Viscosity_' + f + '.csv'))
	df = pd.DataFrame(viscositydataframes)
	plt.plot(df['Temp'], df['Vis'], label=f, linestyle=linestyles2[L], color=colors2[L], marker=markers2[L])
	L = L + 1
plt.plot(T2,Nu,'r--', label='Viscosity Used', linewidth=3, dashes=(10,20))
plt.xlabel('Temperature - K')
plt.ylabel('Viscosity - N/m^2/s')
plt.title('Flibe Viscosity')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

Cp1 = np.zeros(steps)
Cp2 = np.zeros(steps)
Cp3 = np.zeros(steps)
Cp4 = np.zeros(steps)
Cp5 = np.zeros(steps)
Cp6 = np.zeros(steps)
Cp7 = np.zeros(steps)

for i in range(0,steps):
	Cp1[i] = Flibe_Cp_Verification_Data.Cp1(T2[i])
	Cp2[i] = Flibe_Cp_Verification_Data.Cp2(T2[i])
	Cp3[i] = Flibe_Cp_Verification_Data.Cp3(T2[i])
	Cp4[i] = Flibe_Cp_Verification_Data.Cp4(T2[i])
	Cp5[i] = Flibe_Cp_Verification_Data.Cp5(T2[i])
	Cp6[i] = Flibe_Cp_Verification_Data.Cp6(T2[i])
	Cp7[i] = Flibe_Cp_Verification_Data.Cp7(T2[i])

fig3 = plt.figure(k, figsize=(10,8))
plt.plot(T2,Cp,'r--', label='Specific Heat Capacity Used', linewidth=3, dashes=(10,20))
plt.plot(T2,Cp1,'k--', label='2343')
plt.plot(T2,Cp2,'c--', label='2347')
plt.plot(T2,Cp3,'g--', label='2369')
plt.plot(T2,Cp4,'m--', label='2380')
plt.plot(T2,Cp5,'b--', label='2386')
plt.plot(T2,Cp6,'y--', label='2390')
plt.plot(T2,Cp7, linestyle='--', color='tab:brown',label='2414')
plt.xlabel('Temperature - K')
plt.ylabel('Specific Heat - J/kg-K')
plt.ylim(2300, 2450)
plt.title('Flibe Specific Heat Capacity')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

linestyles3 = ['-','None','None',':']
markers3 = ['None', 's', '^', 'None']
colors3 = ['green','darkgoldenrod','mediumorchid','blue']
filelist3 = ['Empirical','ORNL-4344','ORNL-4396','Recommended']
L = 0
fig4 = plt.figure(k, figsize=(10,8))
for f in filelist3:
	kdataframes = pd.read_csv(Path(path + '/Flibe/ThermalConductivity/Romatoski_Flibe_Thermal_Conductivity_' + f + '.csv'))
	df = pd.DataFrame(kdataframes)
	plt.plot(df['Temp'], df['K'], label=f, linestyle=linestyles3[L], color=colors3[L], marker=markers3[L])
	L = L + 1
plt.plot(T2,K,'r--',label='Thermal Conductivity Used', dashes=(10,20), linewidth=3)
plt.xlabel('Temperature - K')
plt.ylabel('Thermal Conductivity - W/m-K')
plt.title('Thermal Conductivity')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

plt.show()