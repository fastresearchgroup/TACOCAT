#Trevor Franklin
#Unit Test for Hex Geometry

import pytest
import numpy as np
from TACOCAT import HexDhCal

def test_Ha():
	assert round(HexDhCal.Ha(1), 5) == 2.59808
	assert round(HexDhCal.Ha(5), 5) == 12.99038
	assert round(HexDhCal.Ha(10), 5) == 25.98076