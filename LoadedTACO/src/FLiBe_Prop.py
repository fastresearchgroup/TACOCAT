# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for FLiBe
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  



def rho(T):
	rho = 2413-0.488*(T); #kg/m^3, error +- 2%
	return rho


def Cp(T):
	Cp = 2386; #J/kg-K, error +- 3%
	return Cp


def k(T):
	k = 1.1; #W/m-K, error +- 10%
	return k

def nu(T):
	nu =(0.116*np.exp(3755/T))*0.001; #N/m^2/s, error +- 20%
	return nu 
