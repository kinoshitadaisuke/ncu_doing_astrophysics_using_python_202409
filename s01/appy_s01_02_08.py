#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/10 07:30:23 (UT+8) daisuke>
#

# printing odd number between 0 and 30
for i in range (30):
    # if number is divisible by 2, then skipping to next number
    if (i % 2 == 0):
        continue
    # if not, then it is an odd number
    print (f'{i} is an odd number.')
