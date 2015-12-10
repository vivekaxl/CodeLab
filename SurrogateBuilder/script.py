def WHEREDataTransformation(filename):
    from Utilities.RahulTool.methods1 import wrapper_createTbl
    # The Data has to be access using this attribute table._rows.cells
    transformed_table = [[int(z) for z in x.cells[:-1]] + x.cells[-1:] for x in wrapper_createTbl(filename)._rows]
    cluster_numbers = set(map(lambda x: x[-1], transformed_table))

    # separating clusters
    # the element looks like [clusterno, rows]
    cluster_table = []
    for number in cluster_numbers:
        cluster_table.append([number]+ [filter(lambda x: x[-1] == number, transformed_table)])
    return cluster_table


def line_prepender(filename):
    with open(filename, 'r+') as f:
        content = f.readlines()
        total_number_of_elements =  len(content[0].split(","))
        line = ",".join(["$"+str(i) for i in xrange(total_number_of_elements - 3)] + ["$<"+str(i) for i in xrange(3)])

        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + "".join(content))


def modify_files():
    basename = "./Data/"
    from os import listdir
    problem_names = [basename + folder_name + "/" for folder_name in listdir(basename)]
    repeat_names = [problem_name + repeat_name + "/" for problem_name in problem_names  for repeat_name in listdir(problem_name)]
    from random import randint
    file_names = [repeat_name + filename for repeat_name in repeat_names for filename in listdir(repeat_name)]
    for file_name in file_names:
        line_prepender(file_name)


def get_filesnames():
    basename = "./Data/"
    from os import listdir
    problem_names = [basename + folder_name + "/" for folder_name in listdir(basename)]
    repeat_names = [problem_name + repeat_name + "/" for problem_name in problem_names  for repeat_name in listdir(problem_name)]
    from random import randint
    file_names = [repeat_name + listdir(repeat_name)[randint(0, len(listdir(repeat_name))-1)] for repeat_name in repeat_names]

    for file_name in file_names:
        WHEREDataTransformation(file_name)
    import pdb
    pdb.set_trace()


get_filesnames()
# modify_files()