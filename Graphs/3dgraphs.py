import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111)

# gale
list_nsga2 = [[float(x) for x in l.split(",")[-2:]] for l in open("./Data/nsgaii_zdt1.csv").readlines() ]
list_spea2 = [[float(x) for x in l.split(",")[-2:]] for l in open("./Data/spea2_zdt1.csv").readlines()]
list_gale = [[float(x) for x in l.split(",")[-2:]] for l in open("./Data/gale_zdt1.csv").readlines()]


xs = [l[0] for l in list_nsga2]
ys = [l[1] for l in list_nsga2]
ax.scatter(xs, ys, c='r', marker='o')

xs = [l[0] for l in list_spea2]
ys = [l[1] for l in list_spea2]
ax.scatter(xs, ys, c='b', marker='^')

xs = [l[0] for l in list_gale]
ys = [l[1] for l in list_gale]
ax.scatter(xs, ys, c='g', marker='x')

ax.set_xlabel('First Objective')
ax.set_ylabel('Second Objective')

plt.title("ZDT1")

# plt.show()
plt.savefig("zdt1.png")