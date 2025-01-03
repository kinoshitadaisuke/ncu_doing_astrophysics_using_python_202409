#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/13 07:35:57 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.ascii

# file
file_data = 'ned1d_new.csv'

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# printing astropy table summary information
print (rawdata.info ())
