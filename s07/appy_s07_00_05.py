#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:11:04 (UT+8) daisuke>
#

# importing astropy module
import astropy.constants

# astronomical unit
au = astropy.constants.au

# printing au
print (au)
print ()

# parsec
pc = astropy.constants.pc

# km/s
unit_km = astropy.units.km

# printing pc
print (pc)
print ()

# 1 au
print (f'1 au = {au:g}')
print (f'     = {au.to (unit_km):g}')

# 1 pc
print (f'1 pc = {pc:g}')
print (f'     = {pc / au} au')
