def draw(raw_data, name):
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.array(raw_data)
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    fig.colorbar(heatmap)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    plt.savefig("./Chart/" + name + ".png")


def read_data(filename="./Data/DTLZ2_14_5.csv"):
    data = [map(float, d.replace("\n", "").split(",")) for d in open(filename, "r").readlines()]
    ndata = normalization(data)
    return ndata


def normalization(data):
    """data: is a list of list"""
    number_of_objectives = len(data[0])
    number_of_lines = len(data)
    normalized_content = [[0 for _ in xrange(number_of_objectives)] for _ in xrange(number_of_lines)]

    for obj in xrange(number_of_objectives):
        one_column = [line[obj] for line in data]
        maximum = max(one_column)
        minimum = min(one_column)
        l_normalization = lambda x: (x - minimum)/(maximum - minimum)
        normalized_one_column = map(l_normalization, one_column)
        assert(len(normalized_one_column) == number_of_lines), "Something is wrong"
        for line in xrange(number_of_lines):
            normalized_content[line][obj] = normalized_one_column[line]

    return normalized_content


def method1(data):
    """as presentd in the data: strawman"""
    draw(data, "method1")


def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


def build_similarity_matrix(data):
    """
    higher the value more different the points are
    so, the diagonal would be 0
    """
    dimension = len(data)
    similarity_matrix = [[euclidean_distance(data[i], data[j]) if i!= j else 0 for j in xrange(dimension)] for i in xrange(dimension)]
    return similarity_matrix


def method2(data):
    # Generate random features and distance matrix.
    import scipy
    import pylab
    import scipy.cluster.hierarchy as sch
    x = scipy.array(xrange(len(data)))
    D = scipy.array(build_similarity_matrix(data))

    # Compute and plot first dendrogram.
    fig = pylab.figure(figsize=(15,15))
    ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
    Y = sch.linkage(D, method='centroid')
    Z1 = sch.dendrogram(Y, orientation='right')
    ax1.set_xticks([])
    ax1.set_yticks([])

    # Compute and plot second dendrogram.
    ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
    Y = sch.linkage(D, method='single')
    Z2 = sch.dendrogram(Y)
    ax2.set_xticks([])
    ax2.set_yticks([])

    # Plot distance matrix.
    axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
    idx1 = Z1['leaves']
    idx2 = Z2['leaves']
    D = D[idx1,:]
    D = D[:,idx2]
    im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)
    axmatrix.set_xticks([])
    axmatrix.set_yticks([])

    axmatrix.set_xticks(range(len(data)))
    axmatrix.set_xticklabels(idx1, minor=False)
    axmatrix.xaxis.set_label_position('bottom')
    axmatrix.xaxis.tick_bottom()

    pylab.xticks(rotation=-90, fontsize=8)

    axmatrix.set_yticks(range(len(data)))
    axmatrix.set_yticklabels(idx2, minor=False)
    axmatrix.yaxis.set_label_position('right')
    axmatrix.yaxis.tick_right()
    pylab.yticks( fontsize=8)

    axcolor = fig.add_axes([0.94,0.1,0.02,0.6])
    pylab.colorbar(im, cax=axcolor)
    fig.show()
    fig.savefig('./Chart/dendrogram.png')

    # This is not working completely. But you can draw inspiration




if __name__ == "__main__":
    data = read_data()
    method1(data)
    # method2(data)