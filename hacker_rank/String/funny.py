
def return_number(lists):

    for list in lists:
        print list
        items = []
        for l in list:
            a = l[0]
            b = l[-1]
            items.append(abs(ord(a) - ord(b)))
        if all(items[0] == item for item in items) is False:
            return False
    return True



arr = "acxz"


arr1 = [[arr[i], arr[i+1]] for i in xrange(0, len(arr)-1)]

arr2 = [[arr1[i], arr1[-1 * (i+1)]] for i in xrange(len(arr1))]



print arr
print arr1
print arr2
print return_number(arr2)