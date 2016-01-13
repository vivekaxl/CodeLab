from __future__ import division
from os import listdir


def get_data(filename):
    content = open(filename, "r").readlines()
    content = [map(float, line.strip().split(",")) for line in content]
    return content


def get_data2(filename):
    content = open(filename, "r").readlines()
    content = [map(float, line.strip().split(",")[-3:]) for line in content]
    return content


def change_list(content):
    xs = [l[0] for l in content]
    ys = [l[1] for l in content]
    zs = [l[2] for l in content]

    return xs, ys, zs


def generate_graph(filename, final_frontier, nsga2, nsga3, vale8):
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for content, color, marker in [(final_frontier, "r", "^"), (nsga2, "g", "s"), (nsga3, "y", "^"), (vale8, "b", ".")]:
        xs, ys, zs = change_list(content)
        ax.scatter(xs, ys, zs, c=color, marker=marker)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(filename)

    print filename
    plt.show()
    # plt.savefig("./charts/"+filename+".png", dpi=100)


final_frontier = "./data/"
vale8 = "./vale8/"
nsga2 = "./nsga2/"
nsga3 = "./nsga3/"


files = listdir("./Data/")
files = [file for file in files]

for file in files:
    content = get_data(final_frontier + file)
    graph_name = file.split("/")[-1].split(".")[0]

    nsga2_content = get_data2(nsga2 + file)
    nsga3_content = get_data2(nsga3 + file)
    vale8_content = get_data2(vale8 + file)

    generate_graph(graph_name, content, nsga2_content, nsga3_content, vale8_content)

    # import pdb
    # pdb.set_trace()
