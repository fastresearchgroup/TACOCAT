# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for Flinak
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  

def rho(T):
	rho = 2579-(0.624*(T)); #kg/m^3, error +- 2%
	return rho


def Cp(T):
	Cp = 1884; #J/kg-K, error +- 10%
	return Cp


def k(T):
	k = 0.36+0.00056*T; #W/m-K, error +- 10%
	return k

def nu(T):
	nu =(0.04*np.exp(4170/T))*0.001; #N/m^2/s, error +- 10%
	return nu 
