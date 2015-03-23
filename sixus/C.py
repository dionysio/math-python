import matplotlib.pyplot as plt
import numpy as np

def logistic(r,x):
    return 4*r * x* (1 - x)

'''discard - basically how many of values to use from the end
iterations - how many iterations of logistic func
low_x, high_x - limit the x axis (values of r)
low_y, high_y - limit the y axis (actual values of logistic func)
'''
def draw_f(iterations=2000, discard=100, low_x=0, high_x=1, low_y=0, high_y=1):
    x = 0.235 * np.ones(iterations) #numpy array of 0.235s - I do not think the number itself is important
    r = np.linspace(0, 1, iterations) #numpy array of equally divided values between 0 and 1
    for i in range(iterations-discard): #calculate but do not draw
        x = logistic(r, x)
    for i in range(iterations-discard, iterations):
        x = logistic(r, x)
        plt.plot(r, x, ',k')
    plt.xlim(low_x, high_x)
    plt.ylim(low_y, high_y)
    plt.savefig('feigenbaum.png')