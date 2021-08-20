#! /usr/bin/env python3

#Luna Matti 08/2021

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 
from math import sqrt, pi, sin, cos
import numpy as np

golden = (1 + sqrt(5.0)) / 2
MAXTHETA=4500.02*pi

def main():
    fig, axes = prep_plots()
    fig.set_size_inches(5, 10)
    #asks for input regarding seed angle
    d = float(input('Set angle in degrees:'))
    theta_step = d* np.pi/180
    #s1 = make_spiral(2.0, MAXTHETA,theta_step, 0.0)
    #plot_spiral(fig, axes[0], s1, 'red')
    sp3d = make_spiral_3d(2.0, MAXTHETA, theta_step, 5)
    plot_spiral_3d(fig, axes, sp3d, 'green')
    output_fname = 'fermat_2d_and_3d.png'
    plt.savefig(output_fname)
    plt.show()
    
def make_spiral(A, theta_max, theta_step, theta_offset):
    #creates the negative and positive reflections in 2d
    thetaBottom = np.arange(0, theta_max/2, theta_step)
    thetaTop = np.arange(theta_max/2, theta_max, theta_step)
    rBottom = np.empty(thetaBottom.size)
    rBottom = A * np.sqrt(thetaBottom)
    rTop = np.flip(rBottom)
    theta=np.concatenate((thetaBottom,thetaTop),axis=0)
    r=np.concatenate((rBottom,rTop),axis=0)
    print(theta)
    print(r)
    return (theta, r)
    
def prep_plots():
    #sets up the plot
    fig = plt.figure(figsize=plt.figaspect(2.))
    fig.suptitle('Fermat spirals in 2D and 3D')
    '''
    ax = fig.add_subplot(2, 1, 1, projection='polar')
    ax.grid(True)
    ax.set_title("A 2D Fermat spiral", va='bottom')
    '''   
    ax3d = fig.add_subplot(1, 1, 1, projection='3d')
    ax3d.set_title("A 3D Fermat spiral", va='bottom')
    return fig, (ax3d)


def make_spiral_3d(A, theta_max, theta_step, zmax):
    #establishes z axis
    global MAXTHETA
    theta, r = make_spiral(2.0, MAXTHETA, theta_step, 0.0)
    z = np.linspace(-zmax,zmax , theta.size)
    #r = r * np.sqrt (1 + sqrt(5.0)) / )
    x = r*np.cos(-1*theta)
    y = r*np.sin(-1*theta)
    '''
else:
     theta, r = make_spiral(2.0, MAXTHETA, theta_step, 0.0)
     z = np.linspace(zmax, 0, theta.size)
        #r = r * np.sqrt (1 + sqrt(5.0)) / )
        x = r*np.cos(-1*theta)
        y = r*np.sin(-1*theta)
        '''
    return (theta, r, z)

def plot_spiral_3d(fig, ax3d, sp3d, color):
    #converts from polar to cartesian coordinates and plots points along spiral
    (theta, r, z) = sp3d
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    print(theta, r, z)
    ax3d.scatter(x, y, z, c='green', marker='.')

    
if __name__ == '__main__':
    main()
