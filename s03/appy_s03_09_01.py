#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 21:00:54 (UT+8) daisuke>
#

# importing numpy module
import numpy

# explicitly specify PCG64 for random number generator
rng = numpy.random.Generator (numpy.random.PCG64 ())

# generating a random number of uniform distribution between 0 and 1
array_x = rng.random ()

# printing generated random numbers
print (f'{array_x}')
