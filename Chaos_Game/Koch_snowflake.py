from __future__ import division
DIVIDE = 3
DIMENSION = 2

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance

def divide_line_segment(pointa, pointb, divide=DIVIDE):
    increment = [0 for _ in xrange(DIMENSION)]
    for i, item in enumerate(increment): increment[i] = abs(pointa[i] - pointb[i])/float(divide)
    return increment

def find_vertices(pointa, pointb, divide = DIVIDE):
    if pointa[0] > pointb[0]: pointa, pointb = pointb, pointa
    increment = divide_line_segment(pointa, pointb, divide)
    points = [[pointa[d] + (increment[d] * count) for d in xrange(DIMENSION)] for count in xrange(divide)][1:]
    return points


def find_third_point(pointa, pointb, center):
    print pointa, pointb,
    s = 2 / (3 ** 0.5)
    x31 = pointb[0] + s*(pointa[1] - pointb[1])
    y31 = pointb[1] + s*(pointb[0] - pointa[0])
    x32 = pointb[0] - s*(pointa[1] - pointb[1])
    y32 = pointb[1] - s*(pointb[0] - pointa[0])
    d1 = euclidean_distance([x31, y31], center)
    d2 = euclidean_distance([x32, y32], center)
    print "dist: ", d1, d2
    if d1 > d2:
        return [x31, y31]
    else:
        return [x32, y32]


def divide_line(line, center):
    pointa = line.start
    pointb = line.end
    points = find_vertices(pointa, pointb)
    third = find_third_point(points[0], points[1], center)
    return [Line(pointa, points[0]), Line(points[0], third), Line(third, points[1]), Line(points[1], pointb)]

def find_center(lines):
    points = []
    for line in lines:
        points.append(line.start)
        points.append(line.end)

    mini = []
    maxi = []
    for d in xrange(DIMENSION):
        temp = sorted(points, key=lambda x: x[0])
        mini.append(temp[-1][d])
        maxi.append(temp[-1][d])
    return [(mini[0] + maxi[0])/2, (mini[1]+maxi[1])/2]


if __name__ == "__main__":

    import pylab
    pylab.ion()       # Turn on interactive mode.
    lines = [Line([0,0], [10, 0]), Line([10, 0], [10, 5.773]), Line([10, 5.773], [0, 0])]
    center = find_center(lines)
    while True:
        new_lines = []
        for line in lines: new_lines.extend(divide_line(line, center))
        x = []
        y = []
        for line in lines:
            x.append(line.start[0])
            x.append(line.end[0])
            y.append(line.start[1])
            y.append(line.end[1])
        lines = new_lines[:]
        pylab.plot(x, y)
        pylab.draw()
        import time
        time.sleep(10)
        this is not working. The third point calculation is wrong