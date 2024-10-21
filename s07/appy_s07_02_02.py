#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:58:43 (UT+8) daisuke>
#

# importing astropy module
import astropy.table
import astropy.units

# units
u_mag    = astropy.units.mag
u_arcsec = astropy.units.arcsec

# data for making Astropy Table
hr       = [2491, 2326, 5340, 5459, 7001, \
            1708, 1713, 2943, 472, 2061]
name     = ['Sirius', 'Canopus', 'Arcturus', 'Alpha Centauri', 'Vega', \
            'Capella', 'Rigel', 'Procyon', 'Achernar', 'Betelgeuse']
vmag     = [-1.46, -0.72, -0.04, -0.01, 0.03, \
            0.08, 0.12, 0.38, 0.46, 0.50] * u_mag
bv       = [0.00, 0.15, 1.23, 0.71, 0.00, \
            0.80, -0.03, 0.42, -0.16, 1.85]
parallax = [0.375, 0.028, 0.090, 0.751, 0.123, \
            0.073, 0.013, 0.288, 0.026, 0.005] * u_arcsec
sptype   = ['A1V', 'F0II', 'K1.5III', 'G2V', 'A0V', \
            'G5III', 'B8I', 'F5IV', 'B3V', 'M2I']

# making Astropy Table
stars = astropy.table.QTable ([hr, name, vmag, bv, parallax, sptype], \
                              names=('HR number', 'Name', 'V-band mag', \
                                     'B-V colour index', 'Parallax', \
                                     'Spectral Type'), \
                              meta={'hr': 'HR number of star', \
                                    'name': 'name of star', \
                                    'vmag': 'V-band apparent magnitude', \
                                    'bv': '(B-V) colour index', \
                                    'parallax': 'parallax in arcsec', \
                                    'sptype': 'spectral type'} )

# getting column names
colnames = stars.colnames

# the other way to get column names
columns = stars.columns

# printing table and column names
print (f'{stars}')
print ()
print (f'stars.colnames = {colnames}')
print ()
print (f'stars.columns  = {columns}')
