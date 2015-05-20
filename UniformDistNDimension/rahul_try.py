"""
Algorithm for the Isotropic method for producing random points on a unit N-hypersphere
A Note on a Uniformly Method for Generating Points on N-Dimensional Spheres
"""
from __future__ import division
from random import normalvariate, random
import numpy, math

def generate_points(n, point, dimension):
    theta = (math.pi) / n
    print theta
    return [x * math.cos(theta) for x in point]

def normalize_point(point):
    mag = sum([x*x for x in point]) ** 0.5
    return [x/mag for x in point]

def euclidean_distance(pointa, pointb):
    def dist(x,y):
        return numpy.sqrt(numpy.sum((x-y)**2))

    return dist(numpy.array(pointa), numpy.array(pointb))

if __name__ == "__main__":
    dimension = 3
    import matplotlib.pyplot as plt
    points = []
    points.append(normalize_point([1, 1, 1]))
    for i in xrange(9):
        points.append(generate_points(i+1, points[0], dimension))
        print generate_points(i+1, points[0], dimension)


    from numpy import random, cos, sin, sqrt, pi
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([point[0] for point in points],[point[1] for point in points], [point[2] for point in points] )
    plt.show()