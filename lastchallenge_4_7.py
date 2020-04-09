#!/usr/bin/env python3
def calculator (x, y, z):
    product = x*y*z
  # if x = int and y = int and z = int # this is testing for integers
    return product
 #  else print('The input provided is not valid.')
def calculator2():
    productsum = calculator (1, 2, 3) + calculator (4, 5, 6)
    print(productsum)
calculator2()
