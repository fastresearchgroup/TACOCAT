#Trevor Franklin
#Geometry Values

import TACOCAT.src.SquareDhCal
import TACOCAT.src.HexDhCal
import numpy as np
import os
import sys
sys.path.insert(0,'../..') #This adds the ability to geometry calculations from the main folder
import TACOCAT_Read_In_File as TCinput

#---------------------------------------------------------------------------------------#
# Geometry - Core
steps = 36
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps) #this needs to be a numpy array of position along the core in - m
Ar = 33.8/100 #Active Radius of the core - m
Ac = (2*(Ar**2)*np.pi/(3*3**0.5))**0.5 #Length of Hexagonal Size - m

# Geometry - Fuel
FoD = 0.58/100 #Fuel Outer Diameter - m
FoCD = 0.64/100 #Cladding Outer Diameter - m
WoD = 0.1/100 #Wire Wrap Diamerer - m
PtoD = 1.18 #Pitch to Diameter Ratio
NFuel = 1951 #Number of Fuel Rods
NFRA = 45 #PlaceHolder for number of rodes in an array

Sa = (NFRA*PtoD*FoCD)**2

#---------------------------------------------------------------------------------------#

Hexagonal = {
	"FaceArea" : TACOCAT.src.HexDhCal.Ha(Ac),
	"CoolantFlowArea" : TACOCAT.src.HexDhCal.HaF(TACOCAT.src.HexDhCal.Ha(Ac),NFuel,FoCD,WoD),
	"InnerHydraulicDiameter" : TACOCAT.src.HexDhCal.Dh1(TACOCAT.src.HexDhCal.A1(PtoD,FoCD,WoD),TACOCAT.src.HexDhCal.P1(FoCD,WoD)),
	}

Wire_Wrapped_Hexagonal = {
	"FaceArea" : TACOCAT.src.HexDhCal.Ha(Ac),
	"CoolantFlowArea" : TACOCAT.src.HexDhCal.HaF(TACOCAT.src.HexDhCal.Ha(Ac),NFuel,FoCD,WoD),
	"InnerHydraulicDiameter" : TACOCAT.src.HexDhCal.Dh1(TACOCAT.src.HexDhCal.A1(PtoD,FoCD,WoD),TACOCAT.src.HexDhCal.P1(FoCD,WoD)),
	}

Square = {
	"FaceArea" : TACOCAT.src.SquareDhCal.Sa(PtoD,FoCD,NFRA),
	"CoolantFlowArea" : TACOCAT.src.SquareDhCal.SaF(Sa,NFuel,FoCD),
	"InnerHydraulicDiameter" : TACOCAT.src.SquareDhCal.DH1(TACOCAT.src.SquareDhCal.A1(PtoD,FoCD),TACOCAT.src.SquareDhCal.P1(FoCD)),
	}

Core_Geometry = {
	"Hexagonal" : Hexagonal,
	"Square" : Square,
	"Wire_Wrapped_Hexagonal" : Wire_Wrapped_Hexagonal,
	}
