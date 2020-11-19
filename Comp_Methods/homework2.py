import numpy as np
import matplotlib.pyplot as plt


def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a #Lower Limit
    b_n = b #Upper Limit
    last_m_n = 0 #arbitrary value?
    for n in range(1,N+1): #In the range of num of iterations
        m_n = (a_n + b_n)/2 #m_n is xr from the book, this is the midpoint
        f_m_n = f(m_n) #Function applied to m_n
        if f(a_n)*f_m_n < 0: #the root lies in the lower subinterval, set b_n = m_n and try again
            a_n = a_n
            b_n = m_n
        elif f(a_n)*f_m_n > 0: #the root lies in the upper subinterval, set a_n = m_n and try again
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0: #Solution has been found
            print("Found exact solution.")
            return m_n
        else: #How can it fail here? Maybe if an invalid input?
            print("Bisection method fails.")
            return None
        
        try:
            approx_error = ((m_n - last_m_n)/m_n) * 100
            #print("error", approx_error)
            if abs(approx_error) < 0.05:
                print("Iterations:",n)
                return m_n
        except ZeroDivisionError:
            pass
        
        
        
        last_m_n = m_n
        
    
    return (a_n + b_n)/2


def plotter(f): #Quick function to plot the graphs of the equation
    # 100 linearly spaced numbers
    x = np.linspace(-5,5,100)
      
    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    # plot the function
    plt.plot(x,f(x), 'r')
    
    # show the plot
    plt.show()


if __name__ == "__main__":
    f1 = lambda x: (x**5) + (3*x**3) + 1
    f2 = lambda x: np.sin(x) + x**3 - 2
    f3 = lambda x: (x**5) + (4*np.exp(2*x)) + 5
    
    #All endpoint values have been chosen graphically
    plotter(f1)
    print(bisection(f1,-8,8,50))
    
    plotter(f2)
    print(bisection(f2,-4,4,50))
    
    plotter(f3)
    print(bisection(f3,-6,6,50))





