#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:44:40 (UT+8) daisuke>
#

# importing astropy module
import astropy.units

# units
u_m        = astropy.units.m
u_mm       = astropy.units.mm
u_GHz      = astropy.units.GHz
u_spectral = astropy.units.spectral ()

# frequency
freq = 115 * u_GHz

# wavelength corresponding to EM wave of frequency 115 GHz
wl    = freq.to (u_m, equivalencies=u_spectral)
wl_mm = freq.to (u_mm, equivalencies=u_spectral)

# printing result
print (f'frequency = {freq:g}  ==>  wavelength = {wl:g} = {wl_mm}')
