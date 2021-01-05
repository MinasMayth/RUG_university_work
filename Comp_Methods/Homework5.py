# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:52:19 2021

@author: samya
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import interpolate
import math

def linear_interpolation(x0,y0,x1,y1,xp):
    
    # Calculating interpolated value
    yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)
    
    # Displaying result
    print('Interpolated value at '+ str(xp) + " is",yp)
    
def quadratic_interpolation(x0,y0,x1,y1,x2,y2,xp):
    
    b0 = y0
    b1 = (y1-y0)/(x1-x0)
    b2 = (((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)
    
    a0 = b0 - b1*x0 + b2*x0*x1
    a1 = b1 - b2*x0 - b2*x1
    a2 = b2
    
    yp = a0 + a1*xp + a2*xp**2
    
    print('Interpolated value at '+ str(xp) + " is",yp)



x_1 = 2.5e-10
x_2 = 1.0e-10
x_3 = 3.0e-10

t=[]; I=[]

f = open('laser_pulse.txt')
for i in f:
  k = i.split()
  t.append(float(k[0]))
  I.append(float(k[1]))
  
f.close()

print("\n***LINEAR INTERPOLATION***\n")
linear_interpolation(t[0],I[0],t[4],I[4],x_1)
linear_interpolation(t[0],I[0],t[4],I[4],x_2)
linear_interpolation(t[0],I[0],t[4],I[4],x_3)

print("\n***QUADRATIC INTERPOLATION***\n")
quadratic_interpolation(t[0],I[0],t[4],I[4],t[7],I[7],x_1)
quadratic_interpolation(t[0],I[0],t[4],I[4],t[7],I[7],x_2)
quadratic_interpolation(t[0],I[0],t[4],I[4],t[7],I[7],x_3)

print("\n***SCIPY INTERPOLATION***\n")
Interpolate = interpolate.interp1d(t,I)
print('Interpolated value at '+ str(x_1) + " is",Interpolate(x_1))
print('Interpolated value at '+ str(x_2) + " is",Interpolate(x_2))
print('Interpolated value at '+ str(x_3) + " is",Interpolate(x_3))


plt.plot(t,I, marker=11)
plt.show()

    