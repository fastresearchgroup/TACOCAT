import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import math
import TACOCAT

z = TACOCAT.z
steps = TACOCAT.steps

#Flat Line Flux Profile (x = 1)
FlatLineFlux = np.zeros(steps)
FlatLineFlux[:] = 1
plt.plot(z,FlatLineFlux, 'k-')
plt.grid()
plt.show()

#Linear Flux Profile (y=x)
LinearFlux = np.zeros(steps)
LinearFlux[:] = z[:]
plt.plot(z,LinearFlux, 'k-')
plt.grid()
plt.show()

#Exponential Flux Profile
ExponentialFlux = np.zeros(steps)
ExponentialFlux[:] = np.exp(z)
plt.plot(z,ExponentialFlux, 'k-')
plt.grid()
plt.show()
