#Trevor Franklin
#Unit Test for Flux

import pytest
import numpy as np
import LoadedTACO.src.Flux_Profiles as fluxpro
import TACOCAT_Read_In_File as TCinput

steps = 36
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)

def test_FlatLineFlux():
    y = 1
    z_values = np.repeat(y,steps)
    assert list(z_values)==list(fluxpro.FlatLineFlux[:])
    
def test_LinearFlux():
    z_values = z
    assert list(z_values)==list(fluxpro.LinearFlux[:])

def test_ExponentialFlux():
    z_values = np.exp(z)
    assert list(z_values)==list(fluxpro.ExponentialFlux[:])

def test_CosineFlux():
    z_values = np.cos((np.pi/Hc)*z)
    assert list(z_values)==list(fluxpro.CosineFlux[:])