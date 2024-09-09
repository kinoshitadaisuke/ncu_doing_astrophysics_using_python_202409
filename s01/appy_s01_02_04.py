#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/09 15:56:38 (UT+8) daisuke>
#

# initialisation of a variable "total"
total = 0

# data
list_data = range (1, 11, 1)

# calculating 1 + 2 + 3 + ... + 10 using "for" statement
for i in list_data:
    # adding "i" to "total"
    total = total + i

# printing result of calculation
print (f'1 + 2 + 3 + ... + 8 + 9 + 10 = {total}')
