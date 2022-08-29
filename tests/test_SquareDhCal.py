#Trevor Franklin
#Unit Test for square geometry

import pytest
import numpy as np
import os
import sys
sys.path.insert(0,'..') #This adds the ability to geometry calculations from the main folder
sys.path.insert(0,'./TACOCAT/src') #Looking for data in a subfolder
from pathlib import Path
import SquareDhCal

def test_Sa():
	assert SquareDhCal.Sa(1,1,1) == 1
	assert SquareDhCal.Sa(2,3,4) == 576
	assert SquareDhCal.Sa(10,10,10) == 1000000

def test_Saf():
	assert round(SquareDhCal.SaF(1,1,1), 5) == 0.21460
	assert round(SquareDhCal.SaF(2,3,4), 5) == -35.69911
	assert round(SquareDhCal.SaF(10,10,10), 5) == -775.39816

def test_A1():
	assert round(SquareDhCal.A1(1,1), 5) == 0.21460
	assert round(SquareDhCal.A1(2,3), 5) == 28.93142
	assert round(SquareDhCal.A1(10,10), 5) == 9921.46018

def test_P1():
	assert round(SquareDhCal.P1(1), 5) == 3.14159 
	assert round(SquareDhCal.P1(2), 5) == 6.28319
	assert round(SquareDhCal.P1(10), 5) == 31.41593

def test_DH1():
	assert SquareDhCal.DH1(1,1) == 4
	assert SquareDhCal.DH1(2,3) == 8/3
	assert SquareDhCal.DH1(10,10) == 4