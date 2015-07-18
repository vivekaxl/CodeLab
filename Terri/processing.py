file_name = "Risk_Indicators_Only.csv"
f = open(file_name, "r")
data = []
# Read data from the file into an array called data
for line in f: data.append([l for l in line.split()])
f.close()

# Extract the unique entities from the data
entities = set()
for line in data:
    for l in line:
        entities.add(l)

print "Total number of unique entities is : ", len(entities)

# Create a map
matrix = {}
for entity in entities:
    matrix[entity] = {}
    for another in entities:
        matrix[entity][another] = 0

for d in data:
    for count, element in enumerate(d[:-1]):
         matrix[element][d[count+1]] += 1

str4csv = ""
str4csv += " ," + ','.join([m for m in matrix.keys()]) + "\n"
for m in matrix.keys():
    str4csv += m + "," + ','.join([str(matrix[m][key]) for key in matrix[m].keys()]) + "\n"

destination_file = file_name.split('.')[0] + "_matrix.csv"
f = open(destination_file, "w")
f.write(str4csv)
f.close()



