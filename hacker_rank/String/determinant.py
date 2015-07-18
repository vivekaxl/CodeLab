# Enter your code here. Read input from STDIN. Print output to STDOUT
from copy import deepcopy
from decimal import Decimal
def detval(matrix):
    return Decimal(matrix[0][0] * matrix[1][1]) - Decimal(matrix[0][1] * matrix[1][0])

def cominor(m, number):
    matrix = deepcopy(m)
    if len(matrix) == 2: return matrix
    else:
        for mt,_ in enumerate(matrix):
            del(matrix[mt][number])
        del(matrix[0])
    return matrix

def recdet(arr):
    if len(arr) <= 2:
        return detval(arr)
    else:
        first_line = arr[0]
        return sum([((-1)**fl) * recdet(cominor(arr, fl)) for fl, _ in enumerate(first_line)])


def create_matrix(X, Y):
    lenX = len(X)
    lenY = len(Y)
    matrix = [[0 for _ in xrange(lenX)] for _ in xrange(lenY)]
    for x in xrange(lenX):
        for y in xrange(lenY):
            matrix[x][y] = Decimal((X[x] + Y[y])) ** -1
    return matrix
            
p = 1000000007
for _ in xrange(int(input())):
    print "boom"
    bl = raw_input()
    X = [Decimal(x) for x in raw_input().split()]
    Y = [Decimal(x) for x in raw_input().split()]
    matrix = create_matrix(X, Y)
    import numpy
    print ">> ", numpy.linalg.det(matrix)
    det = recdet(matrix) 
    print det
    print pow(int(det ** -1), p-2, p)
    