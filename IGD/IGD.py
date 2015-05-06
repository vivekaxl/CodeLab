def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance

def IGD(approximation_points, original_points):
    summ = 0
    for o in original_points:
        min_distance = 1e32
        for a in approximation_points:
            min_distance = min(min_distance, euclidean_distance(o, a))
        summ += min_distance
    return summ/len(original_points)

def read(filename):
    f = open(filename, "r")
    true_PF = []
    for line in f:
        temp = []
        line.replace("\n", "")
        for x in line.split():
            temp.append(float(x))
        true_PF.append(temp)
    return true_PF

def equlity(lista, listb):
    count = 0
    for a in lista:
        for b in listb:

            temp = 0
            for i, j in zip(a, b):
                if i == j or i == j + 0.01 or i == j - 0.01:
                    temp += 1
            if temp == 3:
                count += 1
                break
    print count
    if count != len(listb):
        print "failed"
    else:
        print "pass"

def main():
    true_pf = read("true_pf.txt")
    approx = read("approx.txt")
    equlity(true_pf, approx)
    print len(true_pf), len(approx)
    #  assert(len(true_pf) == len(approx)), "Length of the TruePF and Approx PF is not equal"
    print IGD(approx, true_pf)

if __name__ == "__main__":
    main()