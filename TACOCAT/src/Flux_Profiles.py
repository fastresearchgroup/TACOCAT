import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import math
import os
import sys
sys.path.insert(0,'../..') #This adds the ability to pull Flux profiles from the main folder
from pathlib import Path
import TACOCAT_Read_In_File as TCinput

steps = 36
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)
k = 1

#Flat Line Flux Profile (x = 1)
FlatLineFlux = np.zeros(steps)
FlatLineFlux[:] = 1
plt.figure(k)
plt.plot(z,FlatLineFlux, 'k-')
plt.grid()
k = k + 1

#Linear Flux Profile (y=x)
LinearFlux = np.zeros(steps)
LinearFlux[:] = z[:]
plt.figure(k)
plt.plot(z,LinearFlux, 'k-')
plt.grid()
k = k + 1

#Exponential Flux Profile
ExponentialFlux = np.zeros(steps)
ExponentialFlux[:] = np.exp(z)
plt.figure(k)
plt.plot(z,ExponentialFlux, 'k-')
plt.grid()
k = k + 1

#Cosine Flux Profile
CosineFlux = np.zeros(steps)
CosineFlux[:] = np.cos((np.pi/Hc)*z[:])
plt.figure(k)
plt.plot(z,CosineFlux, 'k-')
plt.grid()

#plt.show()
