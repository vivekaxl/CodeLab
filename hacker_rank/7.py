from __future__ import division
modulo_no = 10 ** 9 + 7

count_arr = [(count + 1) * (count + 2) for count in xrange(10 ** 3)]

def first_query(arr, x, y):
    temp_count = count_arr[:(y-x)]
    for cnt, (_, t_count) in enumerate(zip(arr[x:y+1], temp_count)):
        arr[x+cnt] += t_count
    return arr

def second_query(arr, x, y):
    return sum(arr[x:y+1]) % modulo_no



first_line = raw_input()
N, Q = first_line.split()

arr = [0 for _ in xrange(int(N))]

for _ in xrange(int(Q)):
    second_line = raw_input()
    a, x, y = [int(x) for x in second_line.split()]
    if a == 1:
        arr = first_query(arr, x-1, y-1)
    if a == 2:
        print second_query(arr, x-1, y-1)

