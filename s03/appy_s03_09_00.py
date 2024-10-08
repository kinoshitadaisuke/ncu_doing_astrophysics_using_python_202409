#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:59:15 (UT+8) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.default_rng ()

# generating a random number of uniform distribution between 0 and 1
array_x = rng.random ()

# printing generated random numbers
print (f'{array_x}')
