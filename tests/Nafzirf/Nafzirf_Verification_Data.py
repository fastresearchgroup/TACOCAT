# Sierra Tutwiler
# Last Modified: 5/22/2020
# Calculate fluid properties for Nafzirf
# Reference: "Annals of Nuclear Energy", Romatoski and Hu
# Note: 
	#Temperature is in Kelvin

import numpy as np 
import matplotlib.pyplot as plt  



def rho1(T):
	rho1 =  (3.86-0.00092*(T-273.15))*1000; #kg/m^3, 42.2% NaF 58.8% ZrF4, error +- 5%, Cohen et al. (1956), Cohen and Jones (1954), Powers et al. (1963)
	return rho1


def rho2(T):
	rho2 =  (3.79-0.00090*(T-273.15))*1000; #kg/m^3, 48% NaF 52% ZrF4, error +- 5%, Cohen et al. (1956), Cohen and Jones (1954), Powers et al. (1963)
	return rho2


def rho3(T):
	rho3 =  (3.75-0.00090*(T-273.15))*1000; #kg/m^3, 50% NaF 50% ZrF4, Cohen and Jones (1954)
	return rho3

def rho4(T):
	rho4 =  (3.79-0.00093*(T-273.15))*1000; #kg/m^3, 50% NaF 50% ZrF4, error +- 5%, Cohen et al. (1956), Lane (1958), Powers et al. (1963), Davis (2005)
	return rho4

def rho5(T):
	rho5 =  (3.72-0.00089*(T-273.15))*1000; #kg/m^3, 52% NaF 48% ZrF4, error +- 5%, Cohen et al. (1956), Cohen and Jones (1954), Powers et al. (1963)
	return rho5

def rho6(T):
	rho6 =  (3.71-0.00089*(T-273.15))*1000; #kg/m^3, 53% NaF 47% ZrF4, error +- 5%, Cohen et al. (1956), Cohen and Jones (1954), Powers et al. (1963)
	return rho6

def rho7(T):
	rho7 =  (3.70-0.00089*(T-273.15))*1000; #kg/m^3, 54.1% NaF 45.9% ZrF4, Cohen et al. (1956)
	return rho7

def rho8(T):
	rho8 =  (3.65-0.00088*(T-273.15))*1000; #kg/m^3, 57% NaF 43% ZrF4, error +- 5%, Cohen et al. (1956), Cohen and Jones (1954), Powers et al. (1963), Williams et al. (2006)
	return rho8

def rho9(T):
	rho9 =  (3.935-0.000918*(T-273.15))*1000; #kg/m^3, 57% NaF 43% ZrF4, Salanne et al. (2009)
	return rho9

def rho10(T):
	rho10 =  (3.584-0.000889*(T-273.15))*1000; #kg/m^3, 59.5% NaF 40.5% ZrF4, Williams (2006)
	return rho10

def rho11(T):
	rho11 =  (3.65-0.00088*(T-273.15))*1000; #kg/m^3, 59.5% NaF 40.5% ZrF4, Williams (2006), Samuel(2009)
	return rho11

def rho12(T):
	rho12 =  (3.49-0.00086*(T-273.15))*1000; #kg/m^3, 66.7% NaF 33.3% ZrF4, Cohen et al. (1956), Cohen and Jones (1954)
	return rho12

def rho13(T):
	rho13 =  (3.22-0.00081*(T-273.15))*1000; #kg/m^3, 81% NaF 19% ZrF4, error +- 5%, Cohen et al. (1956), Powers et al. (1963)
	return rho13

def k1(T):
	k1 = 0.43; #W/m-K, 42.2% NaF 58.8% ZrF4, Khokhlov et al. (2009)
	return k1

def k2(T):
	k2 = 0.45; #W/m-K, 48% NaF 52% ZrF4, Khokhlov et al. (2009)
	return k2

def k3(T):
	k3 = 0.45; #W/m-K, 50% NaF 50% ZrF4, Khokhlov et al. (2009)
	return k3

def k4(T):
	k4 = 0.46; #W/m-K, 52% NaF 48% ZrF4, Khokhlov et al. (2009)
	return k4

def k5(T):
	k5 = 0.46; #W/m-K, 53% NaF 47% ZrF4, Khokhlov et al. (2009)
	return k5

def k6(T):
	k6 = 0.47; #W/m-K, 54.1% NaF 45.9% ZrF4, Khokhlov et al. (2009)
	return k6

def k7(T):
	k7 = 0.48; #W/m-K, 57% NaF 43% ZrF4, Khokhlov et al. (2009)
	return k7

def k8(T):
	k8 = 0.49; #W/m-K, 59.5% NaF 40.5% ZrF4, Khokhlov et al. (2009)
	return k8

def k9(T):
	k9 = 0.53; #W/m-K, 66.7% NaF 33.3% ZrF4, Khokhlov et al. (2009)
	return k9

def k10(T):
	k10 = 0.63; #W/m-K, 81% NaF 19% ZrF4, Khokhlov et al. (2009)
	return k10

def Cp1(T):
	Cp1 = 1.151*0.001; #J/kg-K, error +- 15%, 50% NaF 50% ZrF4, Cohen et al. (1956), Powers and Blalock (1956), Powers et al. (1963), Davis (2005)
	return Cp1

def Cp2(T):
	Cp2 = 1.130*0.001; #J/kg-K, error +- 10%, 53% NaF 47% ZrF4, Cohen et al. (1956), Powers and Blalock (1956), Powers et al. (1963), Davis (2005)
	return Cp2

def Cp3(T):
	Cp3 = 1.172*0.001; #J/kg-K, error +- 10%, 57% NaF 43% ZrF4, Cohen et al. (1956), Powers and Blalock (1956), Williams et al. (2006)
	return Cp3

def Cp4(T):
	Cp4 = 1.172*0.001; #J/kg-K, error +- 10%, 59.5% NaF 40.5% ZrF4, Cohen et al. (1956), Powers and Blalock (1956)
	return Cp4