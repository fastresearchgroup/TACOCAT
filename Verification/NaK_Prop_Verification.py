import os
import sys
sys.path.insert(0,'..')
sys.path.insert(0, './Nak')
import numpy as np
from pathlib import Path 
import matplotlib.pyplot as plt
import NaK_Prop
import pandas as pd

path = os.getcwd()

steps = 27

T = np.linspace(0, 1300, steps)
T2 = np.linspace(273, 1573, steps)

rhoNa = np.zeros(steps)
rhoK = np.zeros(steps)
invrhoNaK = np.zeros(steps)
Rho = np.zeros(steps)
CpNa = np.zeros(steps)
CpK = np.zeros(steps)
Cp = np.zeros(steps)
K = np.zeros(steps)
Nu = np.zeros(steps)



for i in range(0,steps):
	rhoNa[i] = NaK_Prop.rhoNa(T[i])
	rhoK[i] = NaK_Prop.rhoK(T[i])
	invrhoNaK[i] = 0.22/rhoNa[i] + 0.78/rhoK[i]
	Rho[i] = 1/invrhoNaK[i] #kg/m^3
	CpNa[i] = NaK_Prop.CpNa(T[i])
	CpK[i] = NaK_Prop.CpK(T[i])
	Cp[i] = (10**3)*(0.22*CpNa[i] + 0.78*CpK[i]) #J/kg-K
	K[i] = NaK_Prop.k(T[i]) #W/m-K
	Nu[i] = NaK_Prop.nu(T[i])*10**7 #m^2/s

k =1 
fig1 = plt.figure(k, figsize=(10,8))
densitydataframe = pd.read_csv(Path(path + '/Nak/Nak_Data_IAEA.csv'))
df = pd.DataFrame(densitydataframe)
plt.plot(df['Temp C'], df['Density'], label='IAEA', linestyle='None', color='blue', marker='^')
plt.plot(T,Rho, 'r--', label='Density Used')
plt.xlabel('Temperature - C')
plt.ylabel('Density - kg/m^3')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

fig2 = plt.figure(k, figsize=(10,8))
cpdataframe = pd.read_csv(Path(path + '/Nak/Nak_Data_IAEA.csv'))
df = pd.DataFrame(cpdataframe)
plt.plot(df['Temp C'], df['Cp'], label='IAEA', linestyle='None', color='blue', marker='^')
plt.plot(T,Cp, 'r--', label='Specific Heat Capacity Used')
plt.xlabel('Temperature - C')
plt.ylabel('Specific Heat Capacity - J/kg-K')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

fig3 = plt.figure(k, figsize=(10,8))
viscositydataframe = pd.read_csv(Path(path + '/Nak/Nak_Data_IAEA.csv'))
df = pd.DataFrame(viscositydataframe)
plt.plot(df['Temp C'], df['Nu'], label='IAEA', linestyle='None', color='blue', marker='^')
plt.plot(T,Nu, 'r--', label='Viscosity Used')
plt.xlabel('Temperature - C')
plt.ylabel('Viscosity - m^2/s')
plt.legend(loc='upper right')
plt.grid()
k = k + 1

fig4 = plt.figure(k, figsize=(10,8))
kdataframe = pd.read_csv(Path(path + '/Nak/Nak_Data_IAEA.csv'))
df = pd.DataFrame(kdataframe)
plt.plot(df['Temp C'], df['K'], label='IAEA', linestyle='None', color='blue', marker='^')
plt.plot(T,K, 'r--', label='Thermal Conductivity Used')
plt.xlabel('Temperature - C')
plt.ylabel('Thermal Conductivity - W/m-K')
plt.legend(loc='upper right')
plt.grid()

plt.show()