from __future__ import division
from os import listdir


def get_data(filename):
    content = open(filename, "r").readlines()
    content = [map(float, line.strip().split(",")) for line in content]
    return content

def generate_graph(filename, content):
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = [l[0] for l in content]
    ys = [l[1] for l in content]
    zs = [l[2] for l in content]

    ax.scatter(xs, ys, zs, c="r", marker="^")

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    print filename
    plt.show()
    # plt.savefig("./charts/"+filename+".png", dpi=100)

files = listdir("./Data/")
files = ["./Data/" + file for file in files]

for file in files:
    content = get_data(file)
    graph_name = file.split("/")[-1].split(".")[0]
    generate_graph(graph_name, content)
