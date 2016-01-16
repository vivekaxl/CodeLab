from __future__ import division
def get_data(filename):
    content = []
    for i, line in enumerate(open(filename, "r").readlines()):
        if i == 0: continue
        numbers = map(float, line.replace("Y", "1").replace("N", "0").strip().split(","))
        content.append(numbers)
    return content


def get_training_testing(data, length):
    total_length = len(data)
    indexes = [i for i in xrange(total_length)]
    from random import shuffle
    shuffle(indexes)
    training = [data[i] for i in indexes[:length]]
    testing = [data[i] for i in indexes[length:]]

    return training, testing


def seperate_indepedent_dependent(data):
    return [d[:-1] for d in data], [d[-1] for d in data]


def create_model(training_independent, training_dependent):
    from sklearn import tree
    CART = tree.DecisionTreeRegressor()
    CART = CART.fit(training_independent, training_dependent)
    return CART


def experiment(filename, N):
    data = get_data(filename)
    training, testing = get_training_testing(data, N)
    training_independent, training_dependent = seperate_indepedent_dependent(training)
    testing_independent, testing_dependent = seperate_indepedent_dependent(testing)

    model = create_model(training_independent, training_dependent)
    predict_data = [float(x) for x in model.predict(testing_independent)]

    mre = []
    for i, j in zip(testing_dependent, predict_data):
        mre.append(abs(i - j) / float(i))

    from numpy import mean, median
    return median(mre), mean(mre)


def wrapper_experiment(name="Apache", filename="./Data/Apache_AllMeasurements.csv", N=[9, 18, 27, 29]):
    print ">"* 30, name
    result = []

    for n in N:
        for i in xrange(6):
            result.append(experiment(filename, n))
        from numpy import mean
        print "N: ", n, " Median: ", round(mean([f[0] for f in result]), 4) * 100, " Mean: ", \
            round(mean([f[1] for f in result]), 4) * 100

import random
random.seed(138)
wrapper_experiment()
wrapper_experiment("LLVM", "./Data/LLVM_AllMeasurements.csv", N=[11, 22, 33, 62])
wrapper_experiment("X264", "./Data/X264_AllMeasurements.csv", N=[16, 32, 48, 81])
wrapper_experiment("BDBC", "./Data/BDBC_AllMeasurements.csv", N=[18, 36, 54, 139])
wrapper_experiment("BDBJ", "./Data/BDBJ_AllMeasurements.csv", N=[26, 52, 78, 48])
wrapper_experiment("SQLite", "./Data/SQL_AllMeasurements.csv", N=[39, 78, 117, 566])