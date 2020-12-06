from scipy.integrate import ode
import numpy as np
from math import sin
import matplotlib.pyplot as plt

#Part 1
    

def rk2a( f, x0, t ):
    """
        This version is based on the algorithm presented in "Numerical
        Analysis", 6th Edition, by Burden and Faires, Brooks-Cole, 1997.
    """
    global acceleration_list
    acceleration_list = []
    
    
    n = len( t )
    x = np.array( [ x0 ] * n )
    for i in range( n - 1 ):
        h = t[i+1] - t[i]
        k1 = h * f( t[i], x[i] ) / 2.0
        x[i+1] = x[i] + h * f( t[i] + h / 2.0 , x[i] + k1)

    return x

def derivative(t, p_and_v): #Function to define the derivative
    a = sin(t)
    
    #Retrieving the acceleration to be used in graphing from here
    global acceleration_list
    acceleration_list.append(a)
    v = p_and_v[1]
    
    return np.array([v,a])



x0 = np.array([0.,0.])
t = np.array([i for i in np.linspace(0,20,num=41)])

x = rk2a(derivative, x0, t)

time=t[1:];velocity=x[1:,1];position=x[1:,0];acceleration=[i for i in acceleration_list if i not in acceleration_list[::2]]

for i in range(len(time)):
    print("\nTime: "+ str(t[i])+",Velocity: "+ str(velocity[i])+",Position: "+ str(position[i])+",Acceleration: "+ str(acceleration[i]))

fig, ax = plt.subplots(3)
ax[0].set_title("RK2A on Newton's equations of motion")
ax[0].plot(time, acceleration)
ax[1].plot(time, velocity)
ax[2].plot(time, position)
plt.tight_layout()


#Scipy integrator for comparison/confirmation of results

time=[];velocity=[];position=[];acceleration=[] # for plotting
dt = 0.5

integral = ode( derivative )
integral.set_integrator('dopri5')
integral.set_initial_value(np.array([0.,0.]))
while integral.successful() and integral.t <=20:
    integral.integrate(integral.t + dt)
    time.append(integral.t)
    acceleration.append(sin(integral.t))
    velocity.append(integral.y[1]) # solution for the differential equation dv/dt=a(t)
    position.append(integral.y[0]) # dx/dt = v(t)
    

fig, ax = plt.subplots(3)
ax[0].set_title("Scipy Integrator on Newton's equations of motion")
ax[0].plot(time, acceleration)
ax[1].plot(time, velocity)
ax[2].plot(time, position)
plt.tight_layout()





# Part 2 and 3


def forward_euler_expanded(x,y,h, x_final):
    # x = x initial condition
    # y = y initial condition
    # h = step size
    # x_final = x final value
    
    
    
    approx_y = []
    exact_y = []
    
    def trueS(x):
        return -0.5*x**4 + 4*x**3 -10*x**2+8.5*x+1
    
    def phi(x):
        dy_dx = -2*x**3 + 12*x**2 - 20*x + 8.5
        return dy_dx
    
    
    print("\nForward Euler for x =",x,", y =",y,",h =",h," and x_final = ",x_final)
    while x <= x_final:
        y = y + phi(x)*h
        x = x + h
        print('approx.',y,'exact', trueS(x))
         
        approx_y.append(y)
        exact_y.append(trueS(x))
        
    return(approx_y,exact_y)
    
   
        
step_05 = forward_euler_expanded(0,1,0.5,4)
step_025 = forward_euler_expanded(0,1,0.25,4)
step_0025 = forward_euler_expanded(0,1,0.025,4)

x_values_05 = np.arange(0,4.5,0.5)
x_values_025 = np.arange(0,4.25,0.25)
x_values_0025 = np.arange(0, 4.025, 0.025)

fig, ax = plt.subplots(3)
ax[0].set_title("Step Size 0.5")
ax[0].plot(x_values_05, step_05[0], label ="y_approx")
ax[0].plot(x_values_05, step_05[1], label ="y_exact")
ax[0].legend(loc="upper left")
ax[1].set_title("Step Size 0.25")
ax[1].plot(x_values_025, step_025[0], label ="y_approx")
ax[1].plot(x_values_025, step_025[1], label ="y_exact")
ax[2].set_title("Step Size 0.025")
ax[2].plot(x_values_0025, step_0025[0], label ="y_approx")
ax[2].plot(x_values_0025, step_0025[1], label ="y_exact")

plt.tight_layout()

#Decreasing the step size will lead to much more accurate predictions!
