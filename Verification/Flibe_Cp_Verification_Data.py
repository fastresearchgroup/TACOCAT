# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for FLiBe
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  



def Cp1(T):
	Cp1 = 2343; #J/kg-K, Liquid, Measurement, Cantor (1968), Douglas and Payne (1969)
	return Cp1


def Cp2(T):
	Cp2 = 2347; #J/kg-K, 745.2–900 K, Measurement, Douglas and Payne (1969)
	return Cp2


def Cp3(T):
	Cp3 = 2369; #J/kg-K, Liquid, Predicted, Williams et al. (2006), Holcomb and Cetiner (2010), Samuel (2009)
	return Cp3

def Cp4(T):
	Cp4 = 2380; #J/kg-K, 600–1200 K, 20% Uncertainity, Reported, Gierszewski et al. (1980)
	return Cp4

def Cp5(T):
	Cp5 = 2386; #J/kg-K, Liquid, 3% Uncertainity, Reported, Cantor (1965), Cantor (1968), Davis (2005), Dewan (2013), Serrano-Lopez et al. (2013)
	return Cp5

def Cp6(T):
	Cp6 = 2390; #J/kg-K, Liquid, Benes and Konings (2009)
	return Cp6

def Cp7(T):
	Cp7 = 2414; #J/kg-K, Liquid, Measurement, Cantor (1968), Rosenthal et al. (1968), Williams et al. (2006), Benes andKonings (2009), Samuel (2009), Holcomb and Cetiner (2010), Sohal et al. (2010)
	return Cp7