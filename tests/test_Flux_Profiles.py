#Trevor Franklin
#Unit Test for Hex Geometry

import pytest
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys
sys.path.insert(0,'..') #This adds the ability to pull Flux profiles from the main folder
sys.path.insert(0,'./TACOCAT/src') #Looking for data in a subfolder
from pathlib import Path
import Flux_Profiles

def test_FlatLineFlux():
    x, y = [-1, 0, 1], [1, 1, 1]
    x_plot, y_plot = ax.lines[0].get_xydata()
    plt.show()
    #np.testing.assert_array_equal(y_plot, plt.plot(z,FlatLineFlux))