#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/21 20:48:51 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# VOTable file name
file_votable = "m3.vot.gz"

# output file name
file_output = 'm3.list'

# reading VOTable
data_vot = astropy.io.votable.parse_single_table (file_votable)

# printing data type
print (f'data type of "data_vot" = {type (data_vot)}')

# converting VOTable data into Astropy table
table = data_vot.to_table ()

# printing data type
print (f'data type of "table"    = {type (table)}')

# printing column information of data read from VOTable file
print (f'columns of Gaia data:')
for column in table.columns:
    print (f'  {column}')
