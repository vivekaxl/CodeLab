solutions = [[0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1],
[0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
[0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0],
[0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0],
[0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1]]


def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


for i in xrange(len(solutions)):
    for j in xrange(len(solutions)):
        print i, j, euclidean_distance(solutions[i], solutions[j])