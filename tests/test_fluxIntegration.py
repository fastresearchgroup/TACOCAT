#Trevor Franklin

import pytest
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys
sys.path.insert(0,'..') #This adds the ability to pull modules from the main folder
import TACOCAT
import LoadedTACO.src.Flux_Profiles as Flux_Profiles
import LoadedTACO.src.Geometry_Value as Geometry

print(TACOCAT.Tbulk)

FluxPro = np.zeros(Geometry.steps)
FluxPro[:] = Flux_Profiles.LinearFlux[:]
x = TACOCAT.Tbulk

print(x)