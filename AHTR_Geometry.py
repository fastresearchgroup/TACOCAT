import numpy as np 
#Notes: 324 fuel assemblies

Hc = 7.9 #Active height of core - m
Ar = 1.48 #Active radius of core - m
NFuel = 216*324 #Number of fuel rods
Cr = (0.9525/100)/2 #Radius of coolant channel holes - m
CVol = 1260 #Volume of the core - m^3

def A(Cr):
	A = np.pi*(Cr**2) #Cross sectional area of coolant hole - m^2
	return A

def HaF(A):
	HaF = A*108*324 #Flow Area of the Coolant - m^2
	return HaF

def P(Cr):
	P = 2*np.pi*Cr #Wetted perimeter - m
	return P

def Dh(A,P):
	Dh = (4*A)/P #Hydraulic Diameter
	return Dh

