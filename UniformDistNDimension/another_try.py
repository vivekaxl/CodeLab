from numpy import random, cos, sin, sqrt, pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def rand_sphere(n):
  """n points distributed evenly on the surface of a unit sphere"""
  z = 2 * random.rand(n) - 1   # uniform in -1, 1
  t = 2 * pi * random.rand(n)   # uniform in 0, 2*pi
  x = sqrt(1 - z**2) * cos(t)
  y = sqrt(1 - z**2) * sin(t)

  return x, y, z

x, y, z = rand_sphere(10)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print x
ax.scatter(x, y, z)
plt.show()