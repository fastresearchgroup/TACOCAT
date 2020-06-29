#Thermal physical properties for UPu-Zr10
#Reference: L. B. CARASIK, P. O’NEAL, M. KENNINGTON, T. HUGHES, H. HONANG, N, GOTH, A 3 MW NaK Cooled Fast Reactor for Use as the First Lunar Base Fission Power Unit, Technical Report, 2015.

import numpy as np 

def kfuel(T):
	kfuel = 22 #Thermal Conductivity of Fuel - W/m-K @ 1000 C
	return kfuel

Tmelt = 1160.00 #Melting temperature of UPu-Zr10 - C