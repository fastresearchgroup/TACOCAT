# Lane Carasik
# Last Modified: 12/15/2015

import numpy as np


#Geometric Calculations
def Ha(Ac):
	Ha = Ac*3*(3**.5)/2  #Area of Hexagonal Face - m^2
	return Ha

def HaF(Ha,NFuel,FoCD,WoD):
	HaF = Ha - NFuel*(np.pi*(FoCD/2)**2 + np.pi*(WoD/2)**2) #Flow Area of the Coolant m^2
	return HaF

#Wire Wrap
def LeadW(FoCD,WoD):
	LeadW = (FoCD + WoD)*np.pi
	return LeadW

#For Inner Subchannel
def A1(PtoD,FoCD,WoD):
	A1 = ((3**0.5)*(PtoD*FoCD)**2)/4 - (np.pi*FoCD**2)/8 - (np.pi*WoD**2)/8 # Area of inner flow channel
	return A1

def P1(FoCD,WoD):
	P1 = np.pi*FoCD/2 + np.pi*WoD/2 # Wetted Perimeter of the inner flow channel
	return P1

def Dh1(A1,P1):
	Dh1 = 4*A1/P1 # Hydraulic Diameter of the inner flow channel
	return Dh1

# For Edge Subchannel
def A2(PtoD,FoCD,WoD):
	A2 = PtoD*FoCD*(FoCD/2 + WoD) - (np.pi*FoCD**2)/8 - (np.pi*WoD**2)/8 # Area of edge flow channel
	return A2

def P2(PtoD,FoCD,WoD):
	P2 = PtoD*FoCD + np.pi*FoCD/2 + np.pi*WoD/2 # Wetter Perimeter of edge flow channel
	return P2

def Dh2(A2,P2):
	Dh2 = 4*A2/P2 # Hydraulic Diameter of the edge flow channel
	return Dh2

# For Corner Subchannel
def A3(FoCD,WoD):
	A3 = (1/(3**0.5))*(FoCD/2 + WoD)**2 - (np.pi*FoCD**2)/24 - (np.pi*WoD**2)/24 # Area of corner flow channel
	return A3

def P3(FoCD,WoD):
	P3 = (FoCD + 2*WoD)/(3**0.5) + np.pi*FoCD/6 + np.pi*WoD/6 # Wetter Perimeter of corner flow channel
	return P3

def Dh3(A3,P3):
	Dh3 = 4*A3/P3 # Hydraulic Diameter of the corner flow channel
	return Dh3