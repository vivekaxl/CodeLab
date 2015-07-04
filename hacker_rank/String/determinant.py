from copy import deepcopy
def det(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

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
        return det(arr)
    else:
        first_line = arr[0]
        return sum([(-1)**fl * recdet(cominor(arr, fl)) for fl, _ in enumerate(first_line)])

def getx(number):
    need to optimize this
    x = 1
    while number ** x % (10**9 + 7) != 1:
        x += 1
    print number ** x
    return x

count = 1
dimension = 3
arr = [[(dimension * i) + (j+1) for j in xrange(dimension)] for i in xrange(dimension)]
# print recdet(arr)

print getx(600**-1)