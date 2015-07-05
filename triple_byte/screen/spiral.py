
n, = map(int, raw_input().split())

# left to right
def direction1(startx, starty, length):
    for i in xrange(length):
        spiral[startx][starty+i] = "*"
    return startx + 1, starty+length-1

# top to bottom
def direction2(startx, starty, length):
    for i in xrange(length):
        spiral[startx + i][starty] = "*"
    return startx+length-1, starty-1

# right to left
def direction3(startx, starty, length):
    for i in xrange(length):
        spiral[startx][starty-i] = "*"
    return startx -1, starty-length + 1

# bottom to top
def direction4(startx, starty, length):
    for i in xrange(length):
        spiral[startx-i][starty] = "*"
    return startx-length + 1, starty + 1


def print_spiral():
    for s in spiral:
        print ''.join(s)
    raw_input()

spiral = [[" " for _ in xrange(n)] for _ in xrange(n)]

len = n
startx = 0
starty = 0
while len > 1:
    startx, starty = direction1(startx, starty, len)
    len -= 1
    startx, starty = direction2(startx, starty, len)
    len -= 1
    startx, starty = direction3(startx, starty, len)
    len -= 1
    startx, starty = direction4(startx, starty, len)
    len -= 1

print_spiral()

# direction1(0, 0, 5)
# direction2(0, 9, 5)
# direction3(9, 9, 5)
# direction4(9, 0, 5)
#
# for s in spiral:
#     print  s







