#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/20 12:09:59 (UT+8) daisuke>
#

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# target object name
target = "Sirius"

# name resolver
query_result = astroquery.simbad.Simbad.query_object (target)

# coordinate from Simbad
ra  = query_result['ra'][0]
dec = query_result['dec'][0]

# using skycoord of astropy
coord = astropy.coordinates.SkyCoord (ra, dec, frame='icrs', unit=u_deg)

# coordinate in decimal degree
ra_deg  = coord.ra.deg
dec_deg = coord.dec.deg

# coordinate in hms and dms format
ra_hms  = coord.ra.to_string (u_ha)
dec_dms = coord.dec.to_string (u_deg, alwayssign=True)

# printing result
print (f"target: {target}")
print (f" RA  = {ra_hms:>18s} = {ra_deg:10.6f} deg")
print (f" Dec = {dec_dms:>18s} = {dec_deg:+10.6f} deg")