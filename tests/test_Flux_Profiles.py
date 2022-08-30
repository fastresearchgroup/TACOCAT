#Trevor Franklin
#Unit Test for Hex Geometry

import pytest
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys
sys.path.insert(0,'..') #This adds the ability to pull Flux profiles from the main folder
sys.path.insert(0,'./TACOCAT/src') #Looking for data in a subfolder
import Flux_Profiles
sys.path.insert(0,'..') #This adds the ability to pull Flux profiles from the main folder
import TACOCAT_Read_In_File as TCinput

steps = 36
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)

def test_FlatLineFlux():
    y = 1
    z_values = np.repeat(y,steps)
    np.testing.assert_array_equal(z_values, Flux_Profiles.FlatLineFlux[:])
    
def test_LinearFlux():
    z_values = z
    np.testing.assert_array_equal(z_values, Flux_Profiles.LinearFlux[:])

def test_ExponentialFlux():
    z_values = np.exp(z)
    np.testing.assert_array_equal(z_values, Flux_Profiles.ExponentialFlux[:])

def test_CosFlux():
    x, y = [-1, 0, 1], [1, 1, 1]
    x_plot, y_plot = ax.lines[0].get_xydata()
    plt.show()
    np.testing.assert_array_equal(y_plot, plt.plot(z,CosFlux[:]))