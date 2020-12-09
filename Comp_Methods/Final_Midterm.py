# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:02:24 2020

@author: samya
"""

#Parts 1 and 2

import math

def secant_method(f, x0, x1):
    print("\n******SECANT-METHOD******")
    for i in range(0,3):
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
    return (x2)
 
f = lambda x: math.exp(-x)-x  #The Main Function  
 
root = secant_method(f, 0, 1)
print ("root is:", root)



def function(x):
    return math.exp(-x)-x # The main function
def derivative(x):
    return -math.exp(-x)-1 # The derivative of the main function

def NewtonsMethod(f, d, x, tolerance=0.000001):
    print("\n******NEWTON-RAPHSON******")
    for i in range (0,3):
        x1 = x - f(x) / d(x)
        print("x1-value:",x1)
        t = abs(x1 - x)
        print("t-value:",t)
        x = x1
    return x

x = 0

x0 = NewtonsMethod(function, derivative, x)

print('x: ', x)
print('root is: ', x0)
print('f(root):',round(function(x0),4))

# Part 3

def function(x):
    answer = x**2 
    return answer

def first_derivative(x):
    answer = 2*x
    return answer

def second_derivative(x):
    answer = 2
    return answer

def second_order_taylor(f1,f2,f3,x,h):
    print("\n******TAYLOR-APPROXIMATION******\n")
    approximation = (f1(x)) +  (f2(x)* h) + ((f3(x)*h**2)/math.factorial(2))
    return approximation

ans = second_order_taylor(function,first_derivative,second_derivative,0,1)

print("Taylor Approximation:",ans)