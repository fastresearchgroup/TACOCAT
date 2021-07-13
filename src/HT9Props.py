'''% Lane Carasik
% Last Modified: 11/18/2015
% Calculate material properties for HT9 Steel 
% Reference: Thermal Conductivity and Thermal Expansion of Stainless Steels
% D9 and HT9
% Note: The temperature has to be calculated in K'''

def k(T):
	if T < 1030:
		k = 17.622 + (2.428*10**-2)*T - (1.696*10**-5)*T**2 #W/m-K
	else:
		k = 12.027 + (1.218*10**-2)*T
	return k 

