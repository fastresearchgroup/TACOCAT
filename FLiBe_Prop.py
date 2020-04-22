

# Sierra Tutwiler
# Last Modified: 4/22/2020
# Calculate fluid properties for FLiBe
# Reference: 
# Note: 

import numpy as np 
import matplotlib as mpl 

def rho(T):
	rho = 2413-0.488*(T+273.15); #kg/m^3
	return rho


def Cp(T):
	Cp = 2386; #J/kg-K, error +- 3%
	return Cp


def k(T):
	k = 1.1; #W/m-K
	return k

def nu(T):
	nu =(0.116*exp(3755/(T+273.15)))*100; #m^2/s
	return nu 






