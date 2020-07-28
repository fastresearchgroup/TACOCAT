# Sierra Tutwiler
# Last Modified: 5/22/2020
# Verify fluid properties for Flinak
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import os
import sys
sys.path.insert(0,'..') #This adds the ability to call flinak prop from the main folder
sys.path.insert(0,'./Flinak') #Looking for data in a subfolder
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt  
import FLiNaK_Prop
import Flinak_Verification_Data
import pandas as pd

path = os.getcwd()

steps = 700

T = np.linspace(500,1100,steps)
T2 = np.linspace(700,1250,steps)

Rho = np.zeros(steps)
Nu = np.zeros(steps)
Cp = np.zeros(steps)
K = np.zeros(steps)

for i in range(0,steps):
	Rho[i] = FLiNaK_Prop.rho(T[i]+273.15)
	Nu[i] = FLiNaK_Prop.nu(T2[i])*1000
	Cp[i] = FLiNaK_Prop.Cp(T2[i])
	K[i] = FLiNaK_Prop.k(T2[i])

linestyles = ['--','-','--','--']
colors = ['blue','firebrick','yellowgreen','purple']
filelist = ['2579_3-0_624xT','2603-0_669xT','2655_64-0_68xT','2729_29-0_73xT']
labels = ['2579.3-0.624*T[K]','2603-0.669*T[K]','2655.64-0.68*T[K]','2729.29-0.73*T[K]']
k = 1
L = 0
fig1 = plt.figure(k, figsize=(10,8))
for f in filelist:
	densitydataframes = pd.read_csv(Path(path + '/Flinak/Density/Romatoski_Flinak_Density_' + f + '.csv'))
	df = pd.DataFrame(densitydataframes)
	plt.plot(df['Temp'], df['Density'], label=labels[L], linestyle=linestyles[L], color=colors[L])
	L = L + 1
plt.plot(T,Rho,'r--', label='Density Used', dashes=(10,20), linewidth=3)
plt.xlabel('Temperature - C')
plt.ylabel('Density - kg/m^3')
plt.title('Flinak Density')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

linestyles2 = ['--','-.','--','-','--','-.','None',':']
markers2 = ['None', 'None', 'None', 'None', 'None', 'None','s', 'None']
colors2 = ['yellowgreen','firebrick','cornflowerblue','darkorange','darkturquoise','magenta','salmon','purple']
filelist2 = ['0_04','0_025','0_0249','0_0623','0_1113','1_633','Cohen_1956_1957','e']
labels2 = ['0.04*exp(4170/T[K])','0.025*exp(4790/T[K])','0.0249*exp(4476/T[K])','0.0623*exp(3921.4/T[K])','0.1113*exp(3379/T[K])','1.633*exp(-2762.9/T[K]+3.1095E6/T^2[K])','Cohen 1956/1957','exp(-3.0489)*exp (3847/T[K])']
L = 0
fig2 = plt.figure(k, figsize=(10,8))
for f in filelist2:
	viscositydataframes = pd.read_csv(Path(path + '/Flinak/Viscosity/Romatoski_Flinak_Viscosity_' + f + '.csv'))
	df = pd.DataFrame(viscositydataframes)
	plt.plot(df['Temp'], df['Vis'], label=labels2[L], linestyle=linestyles2[L], color=colors2[L], marker=markers2[L])
	L = L + 1
plt.plot(T2,Nu,'r--', label='Viscosity Used', dashes=(10,10), linewidth=2.5)
plt.xlabel('Temperature - K')
plt.ylabel('Viscosity - N/m^2/s')
plt.title('Flinak Viscosity')
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
Cp8 = np.zeros(steps)
Cp9 = np.zeros(steps)

for i in range(0,steps):
	Cp1[i] = Flinak_Verification_Data.Cp1(T2[i])
	Cp2[i] = Flinak_Verification_Data.Cp2(T2[i])
	Cp3[i] = Flinak_Verification_Data.Cp3(T2[i])
	Cp4[i] = Flinak_Verification_Data.Cp4(T2[i])
	Cp5[i] = Flinak_Verification_Data.Cp5(T2[i])
	Cp6[i] = Flinak_Verification_Data.Cp6(T2[i])
	Cp7[i] = Flinak_Verification_Data.Cp7(T2[i])
	Cp8[i] = Flinak_Verification_Data.Cp8(T2[i])
	Cp9[i] = Flinak_Verification_Data.Cp9(T2[i])

fig3 = plt.figure(k, figsize=(10,8))
plt.plot(T2,Cp,'r--', label='Specific Heat Capacity Used',linewidth=3, dashes=(10,20))
plt.plot(T2,Cp1,label='Janz and Tomkins (1981)', linestyle='--', color='maroon')
plt.plot(T2,Cp2,label='Ambrosek et al. (2009), Serrano-Lopez et al. (2013)', linestyle='--', color='darkorange')
plt.plot(T2,Cp3,label='Sohal et al. (2010', linestyle='--', color='goldenrod')
plt.plot(T2,Cp4,label='Davis (2005)', linestyle='--', color='yellowgreen')
plt.plot(T2,Cp5,label='Grimes et al. (1958)', linestyle='--', color='darkgreen')
plt.plot(T2,Cp6,label='Hoffman et al. (1955), Vriesema (1979)', linestyle='--', color='dodgerblue')
plt.plot(T2,Cp7,label='Allen (2010)', linestyle='--', color='navy')
plt.plot(T2,Cp8,label='Holcomb and Cetiner (2010), Yoder (2014)', linestyle='--', color='darkviolet')
plt.plot(T2,Cp9,label='Grele and Gedeon (1954)', linestyle='--', color='grey')
plt.xlabel('Temperature - K')
plt.ylabel('Specific Heat - J/kg-K')
plt.title('Flinak Specific Heat Capacity')
plt.legend(loc='lower right')
plt.grid()
k = k + 1

k1 = np.zeros(steps)
for i in range(0,steps):
	k1[i] = Flinak_Verification_Data.k1(T2[i])

fig4 = plt.figure(k, figsize=(10,8))
plt.plot(T2,K,'r--', label='Thermal Conductivity Used (Smirnov)')
plt.plot(T2,k1,'b--', label='Khokhlov et al. (2009)')
plt.xlabel('Temperature - K')
plt.ylabel('Thermal Conductivity - W/m-K')
plt.title('Flinak Thermal Conductivity')
plt.legend(loc='upper right')
plt.grid()
plt.show()