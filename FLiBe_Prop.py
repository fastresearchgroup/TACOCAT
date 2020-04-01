# Lane Carasik and Sierra Tutwiler
# Last Modified: 4/1/2020
# Calculate fluid properties for FLiBe
# Reference: Romatoski 2017 - Fluoride salt coolant properties for nuclear reactor applications - A review
# Notes:


import numpy as np 
import matplotlib as mpl 


def rho(T):
	rho = (1/(10**-3))*(0.89660679 + 0.5161343*((T+273.15)*10**-3) - 1.8297218*((T+273.15)*10**-3)**2 + 2.2016247*((T+273.15)*10**-3)**3 - 1.3975634*((T+273.15)*10**-3)**4 + 0.4486694*((T+273.15)*10**-3)**5 - 0.057963628*(T*10**-3)**6) #kg/m^3
	return rho


def Cp(T):
	Cp = 2386 #J/kg-K, error +- 3%
	return Cp


def k(T):
	k = 1.1; #W/m-K
	return k

def nu(T):
	nu = (200.7657 - 0.734683*(T+273.15) + (1.12102*10**-3)*(T+273.15)**2 - (0.774427*10**-6)*(T+273.15)**3 + (0.200382*10**-9)*(T+273.15)**4)/10**8 #m^2/s
	return nu