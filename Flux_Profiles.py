import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import math
import TACOCAT_Read_In_File as TCinput
import TACOCAT

z = TACOCAT.z
steps = TACOCAT.steps
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
CosineFlux[:] = np.cos((np.pi/TCinput.Hc)*z[:])
plt.figure(k)
plt.plot(z,CosineFlux, 'k-')
plt.grid()

plt.show()
