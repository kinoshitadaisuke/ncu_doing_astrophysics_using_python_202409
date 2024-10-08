#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 20:48:54 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = sympy.sin (x)

# integration of f(x)
I = sympy.integrate (f, x)

# printing result
print (f'f(x)  = {f}')
print (f'integration of f(x) = {I}')
