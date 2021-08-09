#! /usr/bin/env python3

from paraview.simple import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 
from math import sqrt, pi, sin, cos
import numpy as np

golden = (1 + sqrt(5.0)) / 2

def main():
    fig, axes = prep_plots()
    fig.set_size_inches(5, 10)
    theta_step = float(input('Set angle:'))
    s1 = make_spiral(4.0, 50*pi, theta_step, 0.0)
    #s2 = make_spiral(2.7, 50*pi, golden, 0.5)
    plot_spiral(fig, axes[0], s1, 'red')
    #plot_spiral(fig, axes[0], s2, 'blue')
    sp3d = make_spiral_3d(2.2, 50*pi, golden, 5)
    plot_spiral_3d(fig, axes[1], sp3d, 'green')
    output_fname = 'fermat_2d_and_3d.png'
    plt.savefig(output_fname)
    plt.show()

    
def make_spiral(A, theta_max, theta_step, theta_offset):
    # FIXME: not sure how to work the offset into this
    theta = np.arange(0, theta_max, theta_step)
    r = np.empty(theta.size)
    r = A * np.sqrt(theta)
    print(theta)
    print(r)
    return (theta, r)

def prep_plots():
    fig = plt.figure(figsize=plt.figaspect(2.))
    fig.suptitle('Fermat spirals in 2D and 3D')
    ax = fig.add_subplot(2, 1, 1, projection='polar')
    ax.grid(True)
    ax.set_title("A 2D Fermat spiral", va='bottom')
    ax3d = fig.add_subplot(2, 1, 2, projection='3d')
    ax3d.set_title("A 3D Fermat spiral by", va='bottom')
    return fig, (ax, ax3d)

def plot_spiral(fig, ax, sp, color):
    r = sp[1]
    # ax.set_ylim(r.min(), r.max())
    theta, r = sp
    # ax.plot(theta, r, color=color)
    ax.scatter(theta, r, color=color)
    ax.set_rmax(r.max())
    # plt.scatter(theta, r)

def make_spiral_3d(A, theta_max, theta_step, zmax):
    theta, r = make_spiral(2.2, 20*pi, pi/120, 0.0)
    z = np.linspace(-zmax, zmax, theta.size)
    r = r * (1 - z*z/zmax**2)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    print(theta, r, z)
    return (theta, r, z)

def plot_spiral_3d(fig, ax3d, sp3d, color):
    (theta, r, z) = sp3d
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    print(theta, r, z)
    ax3d.scatter(x, y, z, c='red', marker='o')

main()
