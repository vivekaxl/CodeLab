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
    """similar solutions together: based on euclidean distance"""
    similarity_matrix = build_similarity_matrix(data)




def method2(data):


if __name__ == "__main__":
    data = read_data()
    method1(data)