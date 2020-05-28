# Sierra Tutwiler
# Last Modified: 5/22/2020
# Verify fluid properties for Flibe
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import os
import sys
sys.path.insert(0,'..') #This adds the ability to call flibe props from the main folder
sys.path.insert(0,'./Flibe') #Looking for data in a subfolder
import numpy as np 
import matplotlib.pyplot as plt  
import FLiBe_Prop
import Flibe_Cp_Verification_Data
import pandas as pd
from pathlib import Path

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

path = os.getcwd()
data1 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Blanke_1956.csv'))
df1 = pd.DataFrame(data1, columns=['Temp','Density'])
data2 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Cantor_1968.csv'))
df2 = pd.DataFrame(data2, columns=['Temp','Density'])
data3 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Cantor_1973.csv'))
df3 = pd.DataFrame(data3, columns=['Temp','Density'])
data4 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Gierszewski_1980.csv'))
df4 = pd.DataFrame(data4, columns=['Temp','Density'])
data5 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Janz_1974.csv'))
df5 = pd.DataFrame(data5, columns=['Temp','Density'])
data6 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Janz_1974_1988.csv'))
df6 = pd.DataFrame(data6, columns=['Temp','Density'])
data7 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Recommended.csv'))
df7 = pd.DataFrame(data7, columns=['Temp','Density'])
data8 = pd.read_csv(Path(path + '\Flibe\Density\Romatoski_Flibe_Density_Zaghoul_2003.csv'))
df8 = pd.DataFrame(data8, columns=['Temp','Density'])

fig1 = plt.figure(1, figsize=(10,8))
ax = fig1.add_subplot()
df1.plot(x='Temp', y='Density', label='Blanke 1956', ax=ax, kind='scatter', marker='D', color='blue', figsize=(10,8))
df2.plot(x='Temp', y='Density', label='Cantor 1968', ax=ax, linestyle='--', color='purple')
df3.plot(x='Temp', y='Density', label='Cantor 1973', ax=ax, marker='^', kind='scatter', color='darkgreen')
df4.plot(x='Temp', y='Density', label='Gierszewski 1980', ax=ax, linestyle=':', color='fuchsia')
df5.plot(x='Temp', y='Density', label='Janz 1974', ax=ax, kind='scatter', marker='s',color='firebrick')
df6.plot(x='Temp', y='Density', label='Janz 1974/1988', ax=ax, linestyle='--', color='darkorange')
df7.plot(x='Temp', y='Density', label='Recommended', ax=ax, linestyle='-.', color='cornflowerblue')
df8.plot(x='Temp', y='Density', label='Zaghoul 2003', ax=ax, linestyle='--', color='lime')
plt.plot(T,Rho,'r--', label='Density Used', linewidth=3, dashes=(10,20))
plt.xlabel('Temperature - K')
plt.ylabel('Density - kg/m^3')
plt.legend(loc='upper right')
plt.grid()
plt.title('Flibe Density')
plt.show()

data9 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Abe_1981_67.csv'))
df9 = pd.DataFrame(data9, columns=['Temp','Vis'])
data10 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Blanke_1956_62.csv'))
df10 = pd.DataFrame(data10, columns=['Temp','Vis'])
data11 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Blanke_1956_69-31.csv'))
df11 = pd.DataFrame(data11, columns=['Temp','Vis'])
data12 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Cantor_1969_64-36.csv'))
df12 = pd.DataFrame(data12, columns=['Temp','Vis'])
data13 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Cohen_1956_69-31.csv'))
df13 = pd.DataFrame(data13, columns=['Temp','Vis'])
data14 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Gierszewski_1980_66-34.csv'))
df14 = pd.DataFrame(data14, columns=['Temp','Vis'])
data15 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Janz_1974_64-36.csv'))
df15 = pd.DataFrame(data15, columns=['Temp','Vis'])
data16 = pd.read_csv(Path(path + '\Flibe\Viscosity\Romatoski_Flibe_Viscosity_Cantor_1968_66-34.csv'))
df16 = pd.DataFrame(data16, columns=['Temp','Vis'])


fig2 = plt.figure(1, figsize=(10,8))
ax = fig2.add_subplot()
df9.plot(x='Temp', y='Vis', label='Abe 198 (67.2-32.8)', ax=ax, marker='^', linestyle='--', color='purple')
df10.plot(x='Temp', y='Vis', label='Blanke 1956 (62.67-37.33)', ax=ax, marker='s', kind='scatter', color='dodgerblue')
df11.plot(x='Temp', y='Vis', label='Blanke 1956 (69-31)', ax=ax, marker='x', kind='scatter', color='salmon')
df12.plot(x='Temp', y='Vis', label='Cantor 1969 (64-36)', ax=ax, linestyle='-.', color='slategray')
df13.plot(x='Temp', y='Vis', label='Cohen 1956 (69-31)', ax=ax, marker='o', linestyle='--', color='yellowgreen')
df14.plot(x='Temp', y='Vis', label='Gierszewski 1980 (66-34)', ax=ax, linestyle=':', color='blue')
df15.plot(x='Temp', y='Vis', label='Janz 1974 (64-36)', ax=ax, marker='+', kind='scatter', color='darkorange')
df16.plot(x='Temp', y='Vis', label='Cantor 1968 (66-34)', ax=ax, linestyle='-', color='cyan')
plt.plot(T2,Nu,'r--', label='Viscosity Used', linewidth=3, dashes=(10,20))
plt.xlabel('Temperature - K')
plt.ylabel('Viscosity - N/m^2/s')
plt.title('Flibe Viscosity')
plt.legend(loc='upper right')
plt.grid()
plt.show()

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

fig3 = plt.figure(1, figsize=(10,8))
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
plt.show()


data17 = pd.read_csv(Path(path + '\Flibe\ThermalConductivity\Romatoski_Flibe_Thermal_Conductivity_Empirical.csv'))
df17 = pd.DataFrame(data17, columns=['Temp','K']) 
data18 = pd.read_csv(Path(path + '\Flibe\ThermalConductivity\Romatoski_Flibe_Thermal_Conductivity_ORNL-4344.csv'))
df18 = pd.DataFrame(data18, columns=['Temp','K']) 
data19 = pd.read_csv(Path(path + '\Flibe\ThermalConductivity\Romatoski_Flibe_Thermal_Conductivity_ORNL-4396.csv'))
df19 = pd.DataFrame(data19, columns=['Temp','K']) 
data20 = pd.read_csv(Path(path + '\Flibe\ThermalConductivity\Recommended.csv'))
df20 = pd.DataFrame(data20, columns=['Temp','K']) 


fig4 = plt.figure(1, figsize=(10,8))
ax = fig4.add_subplot()
df17.plot(x='Temp', y='K', label='Empirical', ax=ax, linestyle='-', color='green')
df18.plot(x='Temp', y='K', label='ORNL-4344', ax=ax, kind='scatter', marker='s', color='darkgoldenrod', s=30)
df19.plot(x='Temp', y='K', label='ORNL-4396', ax=ax, kind='scatter', marker='^', color='mediumorchid')
df20.plot(x='Temp', y='K', label='Recommended', ax=ax, linestyle=':', color='blue', linewidth=2)
plt.plot(T2,K,'r--',label='Thermal Conductivity Used', dashes=(10,20), linewidth=3)
plt.xlabel('Temperature - K')
plt.ylabel('Thermal Conductivity - W/m-K')
plt.title('Thermal Conductivity')
plt.legend(loc='upper right')
plt.grid()
plt.show()
