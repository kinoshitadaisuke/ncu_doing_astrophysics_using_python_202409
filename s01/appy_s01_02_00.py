#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/09 15:41:21 (UT+8) daisuke>
#

# importing sys modulje
import sys

# reading an integer number from keyboard typing
a_str = input ('Type one integer number: ')

# converting a string into integer
try:
    a = int (a_str)
except:
    print (f'ERROR: failed to convert string "{a_str}" into integer!')
    sys.exit (1)

# if and else statements
if (a % 2 == 0):
    print ("The number you type is an even number.")
else:
    print ("The number you type is an odd number.")