import numpy as np
import os
import sys
import LoadedTACO.src.Geometry_Value as geometry
sys.path.insert(0,'../..') #This adds the ability to pull Flux profiles from the main folder
from pathlib import Path
import TACOCAT_Read_In_File as TCinput

steps = geometry.steps
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)
k = 1

#Flat Line Flux Profile (x = 1)
FlatLineFlux = np.zeros(steps)
FlatLineFlux[:] = 1

#Linear Flux Profile (y=x)
LinearFlux = np.zeros(steps)
LinearFlux[:] = z[:]

#Exponential Flux Profile
ExponentialFlux = np.zeros(steps)
ExponentialFlux[:] = np.exp(z)


#Chopped Cosine Flux Profile
CosineFlux = np.zeros(steps)
CosineFlux[:] = np.cos((np.pi/Hc)*z[:])

#--------------------------------------------------------------------#
#Dictionary

Flatline = {"Profile" : FlatLineFlux[:]}
Linear = {"Profile" : LinearFlux[:]}
Exponential = {"Profile" : ExponentialFlux[:]}
Cosine = {"Profile" : CosineFlux[:]}

Fluxes = {
	"Flatline" : Flatline,
	"Linear" : Linear,
	"Exponential" : Exponential,
	"Chopped_Cosine" : Cosine, 
}