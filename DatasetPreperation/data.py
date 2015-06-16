from __future__ import  division
from os import listdir
from os.path import isfile, join
import itertools

class Objects:
    def __init__(self, column_name):
        self.name = column_name
        self.fields = {}
        self.newid = itertools.count().next

    def add(self, instance_name):
        if instance_name not in self.fields.keys():
            self.fields[instance_name] = self.newid()
        return self.get(instance_name)

    def get(self, instance_name):
        return int(self.fields[instance_name])

class ObjectContainer:
    def __init__(self, fields):
        self.fields = {}
        for f in fields:
            self.fields[f] = Objects(f)

    def add(self, column_name, instance_name):
        self.fields[column_name].add(instance_name)
        return self.get(column_name, instance_name)

    def get(self, column_name, instance_name):
        return self.fields[column_name].get(instance_name)



def list_similarity(list1, list2):
    temp = sum([1 if x != y else 0 for x, y in zip(list1, list2)])
    return True if temp == 0 else False

def change_name(name):
    assert(name[-3:] == "csv"), "This converter is for csv files"
    return name[:-4] + "_mod.csv"

def write_csv(name, content):
    import csv
    fp = open(change_name(name), 'wb')
    a = csv.writer(fp, delimiter=',')
    a.writerows(content)
    fp.close()


def transform_csv_files(f="./Data"):
    import csv

    all_files = sorted([(join(f,path)) for path in listdir(f) if isfile(join(f, path))], reverse=True)

    assert(len(all_files) == 2), "Only files in the folder must be training and testing"
    assert(("train" in all_files[0]) is True), "Please name the training file as train"
    assert(("test" in all_files[1]) is True), "Please name the testing file as test"

    fd_train = open(all_files[0], 'r')
    fd_test = open(all_files[1], 'r')

    training_reader = csv.reader(fd_train)
    testing_reader = csv.reader(fd_test)

    header_train = training_reader.next()  # header of the training file
    header_test = testing_reader.next()  # header of the testing file

    assert(list_similarity(header_train, header_test) is True), "Training and Testing file should have the same header"

    assign_container = ObjectContainer(header_train)

    transformed_training_dataset = []
    for row_no, row in enumerate(training_reader):
        list_row = []
        assert(len(header_train) == len(row)), "Length of the header should be same as Length of the row"
        for feature_name, feature_instance in zip(header_train, row):
            list_row.append(assign_container.add(feature_name, feature_instance))
        transformed_training_dataset.append(list_row)

    write_csv(all_files[0], [header_train] + transformed_training_dataset)  # adding header to the csv file

    transformed_testing_dataset = []
    for row_no, row in enumerate(testing_reader):
        list_row = []
        assert(len(header_test) == len(row)), "Length of the header should be same as Length of the row"
        for feature_name, feature_instance in zip(header_test, row):
            list_row.append(assign_container.add(feature_name, feature_instance))
        transformed_testing_dataset.append(list_row)

    write_csv(all_files[1], [header_test] + transformed_testing_dataset)  # adding header to the csv file

    # for generating ECL file
    generate_dsecl_files(header_test, transformed_training_dataset, transformed_testing_dataset)


def generate_dsecl_files(header, training, testing):
    name = raw_input("Enter the name of the file: ")
    ecl_content = "EXPORT " + name +"DS " + ":= MODULE \n"

    # Constructing RECORD
    ecl_content += "\t SHARED " + name + "Record " + " := RECORD \n"
    for count, h in enumerate(header): ecl_content += "\t\t Types.t_FieldNumber " + h + ";\n"
    ecl_content += "\tEND;\n"

    # Constructing Training
    ecl_content += "\tEXPORT Train_Data := DATASET([ \n"
    for train in training: ecl_content += "\t\t{" + ",".join(repr(str(n)) for n in train).replace("'", "") + "},\n"
    ecl_content = ecl_content[:-2]  # last entry doesn't need a comma
    ecl_content += "],\n\t" + name + "Record);\n"

    # Constructing Testing
    ecl_content += "\tEXPORT Test_Data := DATASET([ \n"
    for test in testing: ecl_content += "\t\t{" + ",".join(repr(str(n)) for n in test).replace("'", "") + "},\n"
    ecl_content = ecl_content[:-2]  # last entry doesn't need a comma
    ecl_content += "],\n\t" + name + "Record);\n"

    ecl_content += "\tEND;\n"

    open(name + "DS.ecl", "w").write(ecl_content)









if __name__ == "__main__":
    transform_csv_files()

