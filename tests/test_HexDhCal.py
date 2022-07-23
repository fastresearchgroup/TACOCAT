#Trevor Franklin
#Unit Test for Hex Geometry

import pytest
import numpy as np
from TACOCAT import HexDhCal

def test_Ha():
	assert round(HexDhCal.Ha(1), 5) == 2.59808
	assert round(HexDhCal.Ha(5), 5) == 12.99038
	assert round(HexDhCal.Ha(10), 5) == 25.98076

def test_HaF():
	assert round(HexDhCal.HaF(1,1,1,1), 5) == -0.57080
	assert round(HexDhCal.HaF(2,3,4,5), 5) == -94.60397
	assert round(HexDhCal.HaF(10,10,10,10), 5) == -1560.79633

def test_LeadW():
	assert round(HexDhCal.LeadW(1,1), 5) == 6.28319
	assert round(HexDhCal.LeadW(2,3), 5) == 15.70796
	assert round(HexDhCal.LeadW(10,10), 5) == 62.83185

def test_A1():
	assert round(HexDhCal.A1(1,1,1), 5) == -0.35239
	assert round(HexDhCal.A1(2,3,4), 5) == 5.77098
	assert round(HexDhCal.A1(10,10,10), 5) == 4251.58720

def test_P1():
	assert round(HexDhCal.P1(1,1), 5) == 3.14159
	assert round(HexDhCal.P1(2,3), 5) == 7.85398
	assert round(HexDhCal.P1(10,10), 5) == 31.41593

def test_Dh1():
	assert round(HexDhCal.Dh1(1,1), 5) == 4
	assert round(HexDhCal.Dh1(2,3), 5) == 2.66667
	assert round(HexDhCal.Dh1(10,10), 5) == 4

def test_A2():
	assert round(HexDhCal.A2(1,1,1), 5) == 0.71460
	assert round(HexDhCal.A2(2,3,4), 5) == 23.18252
	assert round(HexDhCal.A2(10,10,10), 5) == 1421.46018

def test_P2():
	assert round(HexDhCal.P2(1,1,1), 5) == 4.14159
	assert round(HexDhCal.P2(2,3,4), 5) == 16.99557
	assert round(HexDhCal.P2(10,10,10), 5) == 131.41593

def test_Dh2():
	assert round(HexDhCal.Dh2(1,1), 5) == 4
	assert round(HexDhCal.Dh2(2,3), 5) == 2.66667
	assert round(HexDhCal.Dh2(10,10), 5) == 4

def test_A3():
	assert round(HexDhCal.A3(1,1), 5) == 1.03724
	assert round(HexDhCal.A3(2,3), 5) == 7.53591
	assert round(HexDhCal.A3(10,10), 5) == 103.72387

def test_P3():
	assert round(HexDhCal.P3(1,1), 5) == 2.77925
	assert round(HexDhCal.P3(2,3), 5) == 7.23680
	assert round(HexDhCal.P3(10,10), 5) == 27.79248

def test_Dh3():
	assert round(HexDhCal.Dh3(1,1), 5) == 4
	assert round(HexDhCal.Dh3(2,3), 5) == 2.66667
	assert round(HexDhCal.Dh3(10,10), 5) == 4