#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 17:41:27 (UT+8) daisuke>
#

# importing uncertainties module
import uncertainties

# quantity "a": 8.0 +/- 0.8
a = uncertainties.ufloat (8.0, 0.8)

# quantity "b": 4.0 +/- 0.6
b = uncertainties.ufloat (4.0, 0.6)

# calculation of a / b
c = a / b

# printing value of "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = a / b = {a} / {b} = {c}')
