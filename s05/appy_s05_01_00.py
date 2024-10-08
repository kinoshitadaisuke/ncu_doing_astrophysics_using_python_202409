#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/07 14:53:18 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'generating random numbers of uniform distribution between 0 and 1'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n = args.number

# generating a set of random numbers of uniform distribution between 0.0 and 1.0
ru = scipy.stats.uniform.rvs (size=n)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{ru}')
