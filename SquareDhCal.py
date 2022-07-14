#Trevor Franklin
#Geometry

import numpy as np 

#Geometric Calculations
def Sa(PtoD,FoCD,NFRA):
	Sa = (NFRA*PtoD*FoCD)**2 #Area of Square Array Face m^2
	return Sa

def SaF(Sa,NFuel,FoCD):
	SaF = Sa - NFuel*np.pi*(FoCD/2)**2 #Flow Area of the Coolant m^2
	return SaF

#Inner SubChannel
def A1(PtoD,FoCD):
	A1 = (PtoD*FoCD)**2 - (1/4)*np.pi*(FoCD**2) #Area of Inner Flow Channel
	return A1

def P1(FoCD):
	P1 = 2*np.pi*(FoCD/2) #Wetted Perimeter of the Inner Flow Channel
	return P1

def DH1(A1,P1):
	DH1 = 4*A1/P1 #Hydrualic diamter of the Inner SubChannel
	return DH1

