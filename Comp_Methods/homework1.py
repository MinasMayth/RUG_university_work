# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:09:28 2020

@author: samya
"""

import math
from decimal import *

# Python program to calculate 
#1. e^x 
#2. sin x
#3. cos x 
  
# Functions to calculate value 
# using sum of first n terms of  
# Taylor Series 


def exponential(x, n): 
    p = 0
    getcontext().prec = n
    for i in range(n): 
        p += Decimal(x**i)/Decimal(math.factorial(i)) 
    return(p)  
  
    # This portion of the code was drawn from https://www.geeksforgeeks.org/program-to-efficiently-calculate-ex/, by Danish Raza 



# Both following functions are taken from https://stackoverflow.com/questions/45169675/python-calculate-sine-cosine-with-a-precision-of-up-to-1-million-digits

def sin_taylor(x, n):
    p = 0
    getcontext().prec = n
    for i in range(n):
        p += Decimal(((-1)**i)*(x**(2*i+1)))/(Decimal(math.factorial(2*i+1)))
    return (p)


def cos_taylor(x, n):
    p = 0
    getcontext().prec = n
    for i in range(n):
        p += Decimal(((-1)**i)*(x**(2*i)))/(Decimal(math.factorial(2*i)))
    return (p)

if __name__ == "__main__":
    # Driver program to test above functions
    x = float(input("Enter X Value: "))
    n = int(input("How many Sig. Figs?"))
    print ('e^x:', exponential(x, n))
    print ('sin:', sin_taylor(x, n))
    print ('cos:', cos_taylor(x, n))
    
    
    
    #Part 3
    x = .1 + .1 + .1
    print("\nQuestion 3")
    print("\nX:",x)
    print("Is .1 + .1 + .1 = .3?")
    if .1 + .1 + .1 == .3:
        print(True)
    else:
        print(False)
    