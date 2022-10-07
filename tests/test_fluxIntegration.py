#Trevor Franklin

import pytest
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys
sys.path.insert(0,'..') #This adds the ability to pull Flux profiles from the main folder
import TACOCAT

Test = TACOCAT.test(2,2)

print(Test)