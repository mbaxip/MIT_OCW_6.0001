"""
Write a program that does the following in order:
1. Asks the user to enter a number “x” 
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”. 
4. Prints out the log (base 2) of “x”. 
"""

import numpy

x = input('Enter number x: ')
y = input('Enter number y: ')
print('x raised to power y is ', int(x)**int(y))
print('log(base 2) of x is ', int(numpy.log2(int(x))))

