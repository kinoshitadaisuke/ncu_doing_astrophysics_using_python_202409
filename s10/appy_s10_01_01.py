#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/12 09:26:33 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'honey-badger/examples/planets/planets.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing astropy table
print (table)
