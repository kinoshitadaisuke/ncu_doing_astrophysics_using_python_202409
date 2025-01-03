#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/13 08:14:33 (UT+8) daisuke>
#

# importing json module
import json

# file name
file_json = 'osc_0000_1989/SN1989V.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON data from file
    data = json.load (fh)

# printing data
for obj in data:
    print ("obj =", obj)
    for key in data[obj]:
        print ("  %-16s ==> %s" % (key, data[obj][key]) )
