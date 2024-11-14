#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/13 08:18:51 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc   = 'making Hubble diagram using SNIa from Open Supernova Catalog'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution in DPI (default: 150)')

# command-line arguments analysis
args = parser.parse_args ()

# input parameters
file_data      = args.input
file_fig       = args.output
resolution_dpi = args.resolution

# numpy arrays to store data
data_d = numpy.array ([])
data_v = numpy.array ([])
data_z = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading data
    for line in fh:
        # skip the line, if it starts with '#'
        if (line[0] == '#'):
            continue
        # splitting the line
        data  = line.split ()
        # extracting data
        d1 = float (data[0])
        d2 = float (data[1])
        z  = float (data[2])
        v  = float (data[3])
        # checking distance
        diff = numpy.absolute (d1 - d2)
        diff_rel = diff / d2
        if (diff_rel > 0.1):
            continue
        # appending data to numpy arrays
        data_d = numpy.append (data_d, d2)
        data_v = numpy.append (data_v, v)
        data_z = numpy.append (data_z, z)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
ax.plot (data_d, data_v, \
         linestyle='None', marker='o', markersize=2, color='blue', \
         label='type-Ia supernovae fro Open Supernova Catalogue')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=resolution_dpi, bbox_inches="tight")
