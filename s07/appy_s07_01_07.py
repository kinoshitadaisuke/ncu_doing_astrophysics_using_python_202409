#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:43:28 (UT+8) daisuke>
#

# importing astropy module
import astropy.units

# units
u_micron   = astropy.units.micron
u_Hz       = astropy.units.Hz
u_GHz      = astropy.units.GHz
u_spectral = astropy.units.spectral ()

# wavelength
wl = 850 * u_micron

# frequency corresponding to EM wave of wavelength 850 micron
freq     = wl.to (u_Hz, equivalencies=u_spectral)
freq_GHz = wl.to (u_GHz, equivalencies=u_spectral)

# printing result
print (f'wavelength = {wl:g}  ==>  frequency = {freq:g} = {freq_GHz:g}')
