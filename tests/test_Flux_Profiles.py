#Trevor Franklin
#Unit Test for Hex Geometry

import pytest
import numpy as np
import os
import sys
sys.path.insert(0,'..') #This adds the ability to pull Flux profiles from the main folder
sys.path.insert(0,'./TACOCAT/src') #Looking for data in a subfolder
from pathlib import Path
import Flux_Profiles

