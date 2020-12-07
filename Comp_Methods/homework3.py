# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:17:05 2020

@author: samya
"""

#Part 1 - Newton Raphson Implementation

import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return x**2-2 # The main function
def derivative(x):
    return 2*x # The derivative of the main function

def newton(function, derivative, x0, tolerance, number_of_max_iterations=100):
    x1 = 0

    if abs(x0-x1)<= tolerance and abs((x0-x1)/x0)<= tolerance:
        return x0

    print("k\t x0\t\t function(x0)")
    k = 1

    while k <= number_of_max_iterations:
        x1 = x0 - (function(x0)/derivative(x0))
        print("x%d\t%e\t%e"%(k,x1,function(x1)))

        if abs(x0-x1)<= tolerance and abs((x0-x1)/x0)<= tolerance:
            plt.plot(x0, function(x0), 'or')
            return x1

        x0 = x1
        k = k + 1
        plt.plot(x0, function(x0), 'or')

        # Stops the method if it hits the number of maximum iterations
        if k > number_of_max_iterations:
            print("ERROR: Exceeded max number of iterations")

    return x1 # Returns the value

sqrt = newton(function, derivative, 1.7, 0.0000001)
print("The approximate value of x is: "+str(sqrt))

# Plotting configuration
u = np.arange(1.0, 2.0, 0.0001) # Setting up values for x in the plot
w = u**2 - 2 # Define the main function again

plt.plot(u, w)
plt.axhline(y=0.0, color='black', linestyle='-')
plt.title('Newton-Raphson Graphics for' + ' y = x^2 - 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['Xn'], loc='upper left')
plt.show()



#Part 2

class Cramer():
    def det2x2(A, v=False):
        if v:  print ('compute 2 x 2 det of')
        if v:  print (A)
        assert A.shape == (2,2)
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    def det3x3(A):
        print ('compute 3 x 3 det of')
        print (A)
        assert A.shape == (3,3)
        a,b,c = A[0]
        c1 = a * Cramer.det2x2(A[1:3,[1,2]])
        c2 = b * Cramer.det2x2(A[1:3,[0,2]])
        c3 = c * Cramer.det2x2(A[1:3,[0,1]])
        return c1 - c2 + c3
             
    def solve(A):
        print ('solve')
        print (A, '\n')
        assert A.shape == (3,4)
        D = Cramer.det3x3(A[:,:3])
        print ('D = ', D, '\n')
        if D == 0:
            print ('no solution')
            return
        Dx = Cramer.det3x3(A[:,[3,1,2]])
        print ('Dx = ', Dx, '\n')
        Dy = Cramer.det3x3(A[:,[0,3,2]])
        print ('Dy = ', Dy, '\n')
        Dz = Cramer.det3x3(A[:,[0,1,3]])
        print ('Dz = ', Dz, '\n')
        return Dx*1.0/D, Dy*1.0/D, Dz*1.0/D
        
    def check(A,x,y,z):
        print ('check')
        for i,r in enumerate(A):
            print ('row', i, '=', r)
            pL = list()
            for coeff,var in zip(r[:3],(x,y,z)):
                c = str(round(coeff,2))
                v = str(round(var,2))
                pL.append(c + '*' + v)
            print (' + '.join(pL),)
            print (' =', r[0]*x + r[1]*y + r[2]*z, '\n')

def test_Cramer():
    L = [3, 4, -3, 5,
         3, -2, 4, 7,
         3, 2, -1, 3]   
    A = np.array(L)
    A.shape = (3,4)
    result = Cramer.solve(A)
    if result:
        x,y,z = result
        print ('solution')
        print ('x =', x)
        print ('y =', y)
        print ('z =', z, '\n')

test_Cramer()


#Part 3

# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
    
    
    
# According to the above code, in the main Gaussian elimination component there is:
# A loop from 0 to n (Line 153)
# A loop from i+1 to n (Line 157)
# A loop from 0 to n+1 (Line 161)
# In the back substitution component there are two loops:
# A loop going bacmwards from n-2 to -1 (line 166)
# A loop from i+1 to n (Line 169)