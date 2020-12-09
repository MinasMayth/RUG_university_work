import math

def function(x):
    return math.exp(-x**2)-1 # The main function
def derivative(x):
    return -2*x*math.exp(-x**2) # The derivative of the main function

def NewtonsMethod(f, d, x, tolerance=0.000001):
    print("******NEWTON-RAPHSON******\n")
    while True:
        x1 = x - f(x) / d(x)
        print("x1-value:",round(x1,4))
        t = abs(x1 - x)
        print("t-value:",round(t,4))
        if t < tolerance:
            print("Reached t-value below tolerance!")
            break
        x = x1
    return x


x = 0.5

x0 = NewtonsMethod(function, derivative, x)

print('x: ', x)
print('x0: ', round(x0, 4))
print('f(x0):',round(function(x0),4))



"""
Question 3 - If you are unable to analytically calculate the derivate to 
do newton-raphson then there are a variety of other methods that you can use
to find the roots of an equation. For example, you could use bisection or false-position,
however these require their own conditions (Bisection, for example, has to have the
two chosen endpoints on opposite sides of the x-axis). Practically, you can also use
certain libraries available in python that can calculate the derivative for you
(i.e. sympy.Derivative(), or sympy.diff())


"""

#Part 4

def function(x):
    answer = math.cos(x) #cos(x) has been used as a placeholder, you may replace it- and the derivatives- with what you want
    return answer

def first_derivative(x):
    answer = -math.sin(x)
    return answer

def second_derivative(x):
    answer = -math.cos(x)
    return answer

def third_derivative(x):
    answer = math.sin(x)
    return answer

def third_order_taylor(f1,f2,f3,f4,x0, a):
    print("\n******TAYLOR-APPROXIMATION******\n")
    approximation = ((f1(a)/math.factorial(0)) * (x0-a)**0) +  ((f2(a)/math.factorial(1)) * (x0-a)**1) +  ((f3(a)/math.factorial(2)) * (x0-a)**2) + ((f4(a)/math.factorial(3)) * (x0-a)**3)
    return approximation

ans = third_order_taylor(function,first_derivative,second_derivative,third_derivative,0,0)

print("Taylor Approximation:",ans)