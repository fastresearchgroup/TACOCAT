# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for Nafzirf
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  



def rho(T):
	rho = 3827-0.889*(T); #kg/m^3, error +- 5%
	return rho


def Cp(T):
	Cp = 0.001172; #J/kg-K, error +- 10%
	return Cp


def k(T):
	k = 0.49; #W/m-K, error +- 15%
	return k

def nu(T):
	nu =(0.0767*np.exp(3977/T))*0.001; #N/m^2/s, 59.5 mol% NaF, 40.5 mol% ZrF4, error +- 20%
	return nu 
