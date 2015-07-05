
import math
heap = []

def swap(index1, index2):
    temp = heap[index1]
    heap[index1] = heap[index2]
    heap[index2] = temp

def heapify1(index):
    while index != 0:
        parent_index = find_parent(index)
        if heap[parent_index] < heap[index]:
            swap(parent_index, index)
        else:
            break
        index = parent_index

def max_child(index1, index2):
    # print "max_child: ", index1, index2, len(heap)
    if index2 >= len(heap):
        return index1

    if heap[index1] > heap[index2]:
        return index1
    else:
        return index2

def heapify2():
    index = 0
    # print heap
    child1, child2 = find_children(index)
    while child1 <= len(heap)-1 or child2 <= len(heap)-1:
        # print "ASd"
        # print "Child: ", child1, child2, index
        swap_index = max_child(child1, child2)
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



def insert(number):
    heap.append(number)
    if len(heap) != 1:
        heapify1(len(heap)-1)




def extract():
    # print heap
    return_value = heap[0]
    heap[0] = heap[-1]
    del(heap[-1])
    heapify2()
    return return_value



if __name__ == "__main__":
    from random import randint
    for x in xrange(100):
        insert(randint(1, 1000))

    sorted_array = []
    for _ in xrange(100):
         sorted_array.append(extract())

    for i, j in zip(sorted_array, sorted(sorted_array, reverse=True)):
        if i != j:
            print "fail"
            exit()
