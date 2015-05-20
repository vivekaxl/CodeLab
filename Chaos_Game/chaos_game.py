def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance

def midpoint(pointa, pointb):
    # print "->> ", pointa, pointb,
    distance = euclidean_distance(pointa, pointb)
    mid_point = []
    for x in xrange(len(pointa)):
        mid_point.append((pointa[x] + pointb[x])/2.0)
    # print mid_point
    return mid_point

def main():
    points = [[0,0], [0,4], [4,0]]
    import random
    start = [random.randrange(1, 6), random.randrange(1, 6)]

    import pylab
    pylab.ion()       # Turn on interactive mode.
    # pylab.hold(False) # Clear the plot before adding new data.

    while True:

        random_no = random.randrange(1, 6)
        selected_pole = points[random_no/2]
        #print selected_pole
        start = midpoint(selected_pole, start)
        pylab.scatter(start[0], start[1])
        pylab.draw()



if __name__ == "__main__":
    main()