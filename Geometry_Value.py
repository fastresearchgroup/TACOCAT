#Trevor Franklin
#Geometry Values

import SquareDhCal
import TACOCAT.src.HexDhCal
import numpy as np

#---------------------------------------------------------------------------------------#
# Geometry - Core
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

Square = {
	"FaceArea" : SquareDhCal.Sa(PtoD,FoCD,NFRA),
	"CoolantFlowArea" : SquareDhCal.SaF(Sa,NFuel,FoCD),
	"InnerHydraulicDiameter" : SquareDhCal.DH1(SquareDhCal.A1(PtoD,FoCD),SquareDhCal.P1(FoCD)),
}

Core_Geometry = {
	"Hexagonal" : Hexagonal,
	"Square" : Square,
}
