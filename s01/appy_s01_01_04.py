#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/09 14:53:48 (UT+8) daisuke>
#

# two numbers
a, b = 23, 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a         = {a}')
print (f'b         = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
