
import math
heap = []

def swap(index1, index2):
    temp = heap[index1]
    heap[index1] = heap[index2]
    heap[index2] = temp

def heapify1(index):
    print index
    while index != 0:
        parent_index = find_parent(index)
        if heap[parent_index] < heap[index]:
            swap(parent_index, index)
        else:
            break
        index = parent_index

def max_child(index1, index2, length = len(heap)):
    # print "max_child: ", index1, index2, len(heap)
    if index2 >= length:
        return index1

    if heap[index1] > heap[index2]:
        return index1
    else:
        return index2

def heapify2(length2):
    index = 0
    print length2
    # print heap
    child1, child2 = find_children(index)
    while child1 <= length2-1 or child2 <= length2-1:
        # print "ASd"
        # print "Child: ", child1, child2, index
        swap_index = max_child(child1, child2, length2)
        # print "swap: ", swap_index
        if heap[swap_index] > heap[index]:
            swap(swap_index, index)
        index = swap_index
        child1, child2 = find_children(index)
        # print heap



def find_parent(index):
    return (index - 1)/2

def find_children(i):
    return 2*i + 1, 2*i + 2


def insertN():
    def insert(number, size):
        heap[size] = number
        if len(heap) != 0:
            heapify1(size)
    for i, element in enumerate(heap):
        print i
        insert(element, i)
    print heap

def extractN():
    def extract(i):
        print -1 * (i+1)
        swap(-1 * (i+1), 0)
        print heap
        heapify2(len(heap) - (i+1))

    for i, element in enumerate(heap):
        print i
        extract(i)

    print heap



if __name__ == "__main__":
    from random import randint, seed
    seed(2)
    for x in xrange(10):
        heap.append(randint(1, 10))
    print heap
    insertN()
    extractN()

    # sorted_array = []
    # for _ in xrange(100):
    #      sorted_array.append(extract())
    #
    # for i, j in zip(sorted_array, sorted(sorted_array, reverse=True)):
    #     if i != j:
    #         print "fail"
    #         exit()



# 9 8 5 4 5 6 2 3 10
