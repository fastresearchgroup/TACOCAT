# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for Flinak
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  


def Cp1(T):
	Cp1 = 1674.8; #J/kg-K, error +- 4%, Janz and Tomkins (1981)
	return Cp1

def Cp2(T):
	Cp2 = 1880.0; #J/kg-K, Ambrosek et al. (2009), Serrano-Lopez et al. (2013)
	return Cp2

def Cp3(T):
	Cp3 = 1882.8; #J/kg-K, Sohal et al. (2010)
	return Cp3

def Cp4(T):
	Cp4 = 1884; #J/kg-K, error +- 10%, Davis (2005)
	return Cp4

def Cp5(T):
	Cp5 = 1884.15; #J/kg-K, Grimes et al. (1958)
	return Cp5

def Cp6(T):
	Cp6 = 1890.0; #J/kg-K, error +- 5%, Hoffman et al. (1955), Vriesema (1979)
	return Cp6

def Cp7(T):
	Cp7 = 1905.97; #J/kg-K, Allen (2010)
	return Cp7

def Cp8(T):
	Cp8 = 2010.0; #J/kg-K, Holcomb and Cetiner (2010), Yoder (2014)
	return Cp8

def Cp9(T):
	Cp9 = 2090.0; #J/kg-K, Grele and Gedeon (1954)



def k1(T):
	k1 = 0.435+0.0005*T; #W/m-K, Khokhlov et al.
	return k1

