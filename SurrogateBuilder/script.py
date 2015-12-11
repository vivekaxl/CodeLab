def WHEREDataTransformation(filename):
    from Utilities.where import where
    # The Data has to be access using this attribute table._rows.cells
    import pandas as pd
    df = pd.read_csv(filename)
    headers = [h for h in df.columns if '$<' not in h]
    data = df[headers]
    clusters = where(data)

    return clusters


def line_prepender(filename):
    with open(filename, 'r+') as f:
        content = f.readlines()
        total_number_of_elements = len(content[0].split(","))
        line = ",".join(
            ["$" + str(i) for i in xrange(total_number_of_elements - 3)] + ["$<" + str(i) for i in xrange(3)])

        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + "".join(content))


def modify_files():
    basename = "./Data/"
    from os import listdir
    problem_names = [basename + folder_name + "/" for folder_name in listdir(basename)]
    repeat_names = [problem_name + repeat_name + "/" for problem_name in problem_names for repeat_name in
                    listdir(problem_name)]
    from random import randint
    file_names = [repeat_name + filename for repeat_name in repeat_names for filename in listdir(repeat_name)]
    for file_name in file_names:
        line_prepender(file_name)


def random_point(clusters, filename):
    from random import choice
    import pandas as pd
    df = pd.read_csv(filename)
    decisions = len([h for h in df.columns if '$<' not in h])
    objectives = len([h for h in df.columns if '$<' in h])
    df = df.values.tolist()
    training_independent = [choice(c).tolist() for c in clusters]
    print decisions
    full_data = []
    for ti in training_independent:
        assert(len(ti) == decisions), "Something is wrong"
        for element in df:
            match = True
            for t, e in zip(ti, element[:decisions]):
                if t == e: pass
                else:
                    match = False
                    break

            if match is True:
                full_data.append(element)
                break

    return [fd[:decisions] for fd in full_data], [fd[decisions:] for fd in full_data]


def surrogate_generate(training_independent, training_dependent):
    from sklearn.tree import DecisionTreeRegressor
    number_of_objectives = len(training_dependent[0])
    cart_trees = []
    for objective in xrange(number_of_objectives):
        cart_trees.append(DecisionTreeRegressor())
        cart_trees[objective].fit(training_independent, [td[objective] for td in training_dependent])
    return cart_trees


def get_testing_data(training_independent, filename):
    decisions = len(training_independent[0])
    print filename
    import pandas as pd
    all_data = pd.read_csv(filename).values.tolist()
    testing_data =[]
    for i, data in enumerate(all_data):
        match = []
        for ti in training_independent:
            # if all the elements of data[:decisions] is equal to ti then skips
            equal = reduce(lambda x,y: x and y, [True if t == d else False for t, d in zip(ti, data[:decisions])])
            match.append(equal)
        matching = reduce(lambda x,y: x or y, match)
        #print matching, i#, data[:decisions]  this is a match
        if matching is False: testing_data.append(data)

    # assert(len(testing_data) + len(training_independent) == len(all_data)), "Something is wrong"
    return [t[:decisions] for t in testing_data], [t[decisions:] for t in testing_data]


def validate_data(surrogate, testing_independent, testing_dependent):
    objectives = len(testing_dependent[0])
    assert(len(surrogate) == objectives), "Something is wrong"
    results = []
    for o in xrange(objectives):
        prediction = [float(x) for x in surrogate[o].predict(testing_independent)]
        o_testing_dependent = [td[o] for td in testing_dependent]
        mre = []
        for i, j in zip(o_testing_dependent, prediction):
            mre.append(abs(i - j)/(float(i)+0.0001))
        results.append(sum(mre)/len(mre))
    print results


def get_filenames(policy):
    basename = "./Data/"
    from os import listdir
    problem_names = [basename + folder_name + "/" for folder_name in listdir(basename)]
    repeat_names = [problem_name + repeat_name + "/" for problem_name in problem_names for repeat_name in
                    listdir(problem_name)]
    from random import randint
    file_names = [repeat_name + listdir(repeat_name)[randint(0, len(listdir(repeat_name)) - 1)] for repeat_name in
                  repeat_names]

    for file_name in file_names:
        clusters = WHEREDataTransformation(file_name)
        training_independent, training_dependent = policy(clusters, file_name)
        testing_independent, testing_dependent = get_testing_data(training_independent, file_name)
        assert(len(testing_dependent) == len(testing_independent)), "Somethign is wrong"

        surogates = surrogate_generate(training_independent, training_dependent)
        validate_data(surogates, testing_independent, testing_dependent)

    import pdb
    pdb.set_trace()


get_filenames(random_point)
# modify_files()
