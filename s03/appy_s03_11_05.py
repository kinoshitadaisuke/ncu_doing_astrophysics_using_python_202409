#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 21:18:36 (UT+8) daisuke>
#

# importing numpy module
import numpy
import numpy.ma

# data
data = numpy.array ([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, \
                     5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5])

# printing data
print ("data:")
print (data)

# making a mask using an operator ">"
mask = data > 7.0

# printing mask
print ("mask:")
print (mask)

# making a masked array
masked_data = numpy.ma.array (data, mask=mask)

# printing a masked array
print ("masked_data:")
print (masked_data)
