# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for Nafzirf
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin


import os
import sys
sys.path.insert(0,'..') #This adds the ability to call nafzirf props from the main folder
sys.path.insert(0,'./Nafzirf') #Looking for data in a subfolder
import numpy as np 
import matplotlib.pyplot as plt  
import NaF_ZrF4_Prop
import Nafzirf_Verification_Data
import pandas as pd
from pathlib import Path

path = os.getcwd()

steps = 700

T = np.linspace(550,1250,steps)
T2 = np.linspace(700,1200,steps)

Rho = np.zeros(steps)
Nu = np.zeros(steps)
Cp = np.zeros(steps)
K = np.zeros(steps)

for i in range(0,steps):
	Rho[i] = NaF_ZrF4_Prop.rho(T[i])
	Nu[i] = NaF_ZrF4_Prop.nu(T2[i])*1000
	Cp[i] = NaF_ZrF4_Prop.Cp(T2[i])
	K[i] = NaF_ZrF4_Prop.k(T2[i])

rho1 = np.zeros(steps)
rho2 = np.zeros(steps)
rho3 = np.zeros(steps)
rho4 = np.zeros(steps)
rho5 = np.zeros(steps)
rho6 = np.zeros(steps)
rho7 = np.zeros(steps)
rho8 = np.zeros(steps)
rho9 = np.zeros(steps)
rho10 = np.zeros(steps)
rho11 = np.zeros(steps)
rho12 = np.zeros(steps)
rho13 = np.zeros(steps)

for i in range(0,steps):
	rho1[i] = Nafzirf_Verification_Data.rho1(T[i])
	rho2[i] = Nafzirf_Verification_Data.rho2(T[i])
	rho3[i] = Nafzirf_Verification_Data.rho3(T[i])
	rho4[i] = Nafzirf_Verification_Data.rho4(T[i])
	rho5[i] = Nafzirf_Verification_Data.rho5(T[i])
	rho6[i] = Nafzirf_Verification_Data.rho6(T[i])
	rho7[i] = Nafzirf_Verification_Data.rho7(T[i])
	rho8[i] = Nafzirf_Verification_Data.rho8(T[i])
	rho9[i] = Nafzirf_Verification_Data.rho9(T[i])
	rho10[i] = Nafzirf_Verification_Data.rho10(T[i])
	rho11[i] = Nafzirf_Verification_Data.rho11(T[i])
	rho12[i] = Nafzirf_Verification_Data.rho12(T[i])
	rho13[i] = Nafzirf_Verification_Data.rho13(T[i])

k = 1
fig1 = plt.figure(k, figsize=(10,8))
plt.plot(T,Rho,'r--', label='NaF-ZrF4 Density Used', linewidth=3, dashes=(10,20))
plt.plot(T,rho1, label='42.2% NaF 58.8% ZrF4', linestyle='--', color='maroon')
plt.plot(T,rho2, label='48% NaF 52% ZrF4', linestyle='--', color='darkorange')
plt.plot(T,rho3,'k--', label='50% NaF 50% ZrF4', linestyle='--', color='gold')
plt.plot(T,rho4,'k--', label='50% NaF 50% ZrF4', linestyle='--', color='greenyellow')
plt.plot(T,rho5,'k--', label='52% NaF 48% ZrF4', linestyle='--', color='darkgreen')
plt.plot(T,rho6,'k--', label='53% NaF 47% ZrF4', linestyle='--', color='aqua')
plt.plot(T,rho7,'k--', label='54.1% NaF 45.9% ZrF4', linestyle='--', color='dodgerblue')
plt.plot(T,rho8,'k--', label='57% NaF 43% ZrF4', linestyle='--', color='navy')
plt.plot(T,rho9,'k--', label='57% NaF 43% ZrF4', linestyle='--', color='grey')
plt.plot(T,rho10,'k--', label='59.5% NaF 40.5% ZrF4', linestyle='--', color='darkviolet')
plt.plot(T,rho11,'k--', label='59.5% NaF 40.5% ZrF4', linestyle='--', color='magenta')
plt.plot(T,rho12,'k--', label='66.7% NaF 33.3% ZrF4', linestyle='--', color='rosybrown')
plt.plot(T,rho13,'k--', label='81% NaF 19% ZrF4', linestyle='--', color='black')
plt.xlabel('Temperature - K')
plt.ylabel('Density - kg/m^3')
plt.legend(loc='upper right')
plt.grid()
plt.title('Density Used')
k = k +1

linestyles = ['None','None','None']
markers = ['s', 'D', '^']
colors = ['firebrick','cornflowerblue','darkgreen']
filelist = ['Cohen_Janz_50-50','Cohen_Janz_53-47','Grande_50-50']
L = 0
fig2 = plt.figure(k, figsize=(10,8))
for f in filelist:
	viscositydataframes = pd.read_csv(Path(path + '/Nafzirf/Viscosity/Romatoski_Nafzirf_Viscosity_' + f + '.csv'))
	df = pd.DataFrame(viscositydataframes)
	plt.plot(df['Temp'], df['Vis'], label=f, linestyle=linestyles[L], color=colors[L], marker=markers[L])
	L = L + 1
plt.plot(T2,Nu,'r--', label='Viscosity Used')
plt.xlabel('Temperature - K')
plt.ylabel('Viscosity - N/m^2/s')
plt.title('NaF-ZrF4 Viscosity')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

Cp1 = np.zeros(steps)
Cp2 = np.zeros(steps)
Cp3 = np.zeros(steps)
Cp4 = np.zeros(steps)

for i in range(0,steps):
	Cp1[i] = Nafzirf_Verification_Data.Cp1(T2[i])
	Cp2[i] = Nafzirf_Verification_Data.Cp2(T2[i])
	Cp3[i] = Nafzirf_Verification_Data.Cp3(T2[i])
	Cp4[i] = Nafzirf_Verification_Data.Cp4(T2[i])

fig3 = plt.figure(1, figsize=(10,8))
plt.plot(T2,Cp,'r--', label='Specific Heat Capacity Used', linewidth=3, dashes=(10,20))
plt.plot(T2,Cp1,'m--', label='50% NaF 50% ZrF4')
plt.plot(T2,Cp2,'g--', label='53% NaF 47% ZrF4')
plt.plot(T2,Cp3,'k:', label='57% NaF 43% ZrF4')
plt.plot(T2,Cp4,'b--', label='59.5% NaF 40.5% ZrF4', dashes=(5,10))
plt.xlabel('Temperature - K')
plt.ylabel('Specific Heat - J/kg-K')
plt.title('NaF-ZrF4 Specific Heat Capacity')
plt.legend(loc='upper right')
plt.grid()
plt.show()
k = k + 1

k1 = np.zeros(steps)
k2 = np.zeros(steps)
k3 = np.zeros(steps)
k4 = np.zeros(steps)
k5 = np.zeros(steps)
k6 = np.zeros(steps)
k7 = np.zeros(steps)
k8 = np.zeros(steps)
k9 = np.zeros(steps)
k10 = np.zeros(steps)

for i in range(0,steps):
	k1[i] = Nafzirf_Verification_Data.k1(T2[i])
	k2[i] = Nafzirf_Verification_Data.k2(T2[i])
	k3[i] = Nafzirf_Verification_Data.k3(T2[i])
	k4[i] = Nafzirf_Verification_Data.k4(T2[i])
	k5[i] = Nafzirf_Verification_Data.k5(T2[i])
	k6[i] = Nafzirf_Verification_Data.k6(T2[i])
	k7[i] = Nafzirf_Verification_Data.k7(T2[i])
	k8[i] = Nafzirf_Verification_Data.k8(T2[i])
	k9[i] = Nafzirf_Verification_Data.k9(T2[i])
	k10[i] = Nafzirf_Verification_Data.k10(T2[i])


fig4 = plt.figure(k, figsize=(10,8))
plt.plot(T2,K,'r--',label='Thermal Conductivity Used',linewidth=3, dashes=(10,20))
plt.plot(T2,k1,label='42.2% NaF 58.8% ZrF4', linestyle='--', color='maroon')
plt.plot(T2,k2,label='48% NaF 52% ZrF4', linestyle='--', color='darkorange')
plt.plot(T2,k3,label='50% NaF 50% ZrF4', linestyle='--', color='goldenrod')
plt.plot(T2,k4,label='52% NaF 48% ZrF4', linestyle='--', color='yellowgreen')
plt.plot(T2,k5,label='53% NaF 47% ZrF4', linestyle='--', color='darkgreen')
plt.plot(T2,k6,label='54.1% NaF 45.9% ZrF4', linestyle='--', color='dodgerblue')
plt.plot(T2,k7,label='57% NaF 43% ZrF4', linestyle='--', color='navy')
plt.plot(T2,k8,label='59.5% NaF 40.5% ZrF4', linestyle='--', color='darkviolet')
plt.plot(T2,k9,label='66.7% NaF 33.3% ZrF4', linestyle='--', color='grey')
plt.plot(T2,k10,label='81% NaF 19% ZrF4', linestyle='--', color='rosybrown')
plt.xlabel('Temperature - K')
plt.ylabel('Thermal Conductivity - W/m-K')
plt.title('NaF-ZrF4 Thermal Conductivity')
plt.legend(loc='upper right')
plt.grid()
plt.show()