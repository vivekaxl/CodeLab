"""
Algorithm for the Isotropic method for producing random points on a unit N-hypersphere
A Note on a Uniformly Method for Generating Points on N-Dimensional Spheres
"""
from __future__ import division
from random import normalvariate
import numpy

def generate_points(dimension):
    points = [normalvariate(0,1) for _ in xrange(dimension)]
    r = sum([point**2 for point in points])**0.5
    temp = [point/r for point in points]
    return temp

def euclidean_distance(pointa, pointb):
    def dist(x,y):
        return numpy.sqrt(numpy.sum((x-y)**2))

    return dist(numpy.array(pointa), numpy.array(pointb))

if __name__ == "__main__":
    dimension = 3
    import matplotlib.pyplot as plt
    points = []
    for _ in xrange(10):
        # temp = euclidean_distance(generate_points(dimension), [0 for _ in xrange(dimension)])
        # print temp
        # assert(round(temp,1) == 1.0), "Something"
        points.append(generate_points(dimension))

    from numpy import random, cos, sin, sqrt, pi
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([point[0] for point in points],[point[1] for point in points], [point[2] for point in points] )
    plt.show()