#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/12/22 17:53:19 (UT+8) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'star_planet.bin'

# constructing a simulation object
sim = rebound.Simulation ()

# adding one solar mass star
sim.add (m=1.0)

# adding a planet of m=0.001, a=1, and e=0.3
sim.add (m=10**-3, a=1.0, e=0.3)

# printing simulation object
print (sim)

# saving simulation into a file
sim.save_to_file (file_sim)
