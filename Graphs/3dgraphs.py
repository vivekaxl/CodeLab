import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111)

# gale
list_gale = [[float(x) for x in l.split(",")[-2:]] for l in open("./Data/gale4_dtlz1_7_3.csv").readlines() ]
list_nsga2 = [[float(x) for x in l.split(",")[-2:]] for l in open("./Data/nsga2_dtlz1_7_3.csv").readlines()]

print list_gale[0]
xs = [l[0] for l in list_gale]
ys = [l[1] for l in list_gale]
# zs = [l[2] for l in list_gale]
ax.scatter(xs, ys, c='r', marker='o')

xs = [l[0] for l in list_nsga2]
ys = [l[1] for l in list_nsga2]
# zs = [l[2] for l in list_nsga2]
ax.scatter(xs, ys, c='b', marker='^')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()
plt.savefig("zdt1.png")