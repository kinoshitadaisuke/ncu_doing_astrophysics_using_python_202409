#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/30 07:23:26 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.pyplot

# constructing a parser object
descr  = 'A sample Matplotlib code using explicit axes interface'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--output', default='sample.png', \
                     help='output file name (default: sample.png)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output = args.output

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# data to be plotted
data_x = numpy.linspace (0.0, +5.0, 10000)
data_y = numpy.sin (data_x**data_x) / (data_x**data_x)

#
# for making a plot using object-oriented interface,
# we first construct "fig" and "axes" objects,
# and then use methods for these "fig" and "axes".
#

# making a "fig" object using a function "matplot.pyplot.figure ()"
fig = matplotlib.pyplot.figure ()

# constructing an axes object using object-oriented interface
ax = fig.add_subplot (111)

# plotting data using object-oriented interface
ax.plot (data_x, data_y, label='Sample data')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
