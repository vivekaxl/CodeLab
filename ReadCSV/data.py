#__author__ = 'FuWei'
from __future__ import  division
import sys
import pdb
from os import listdir
from os.path import isfile, join
# from table import *

class o(object):
 def __init__(i, **filed):
   i.__dict__.update(filed)
   return i

class Row(object):
  def __init__(i,data):
    i.x = data[:-1]
    i.y = data[-1]
    i.w = 0
  def __len__(i): return len(i.x)+1
  def weights(i,l,m):
    if i.y == 1:
      i.w = 1/(2*l) # Y, crater
    else:
      i.w = 1/(2*m) # N, non-crater



def read(files):
  Y, N = 0,0
  rows = []
  path = "../data/features"
  # datafiles = [ join(path,f) for f in listdir(path) if isfile(join(path,f))]
  for data in [join(path,f) for f in files]:
    print(data)
    with open(data,"r") as f:
      line = f.readline() #header, ski\
      for line in f.readlines():
        line = map(float, line.split(","))
        if line[-1] == 1:
          Y +=1
        else:
          N +=1
        rows.append(Row(line))
      map(lambda x:x.weights(Y,N),rows)
  return rows

def changeHeader(f = "./data"):
  all_files = [ (join(f,path)) for path in listdir(f) if isfile(join(f, path))]
  for one in all_files:
    content = ""
    f = open(one,"r")
    count = 0
    while True:
      line = f.readline()
      if not line:
        break
      else:
        if count == 0:
          newheader = []
          pdb.set_trace()
          header = line.split(",")
          for item in header[:-1]:
            newheader +=["$"+item]
          newheader +=["$<"+header[-1]]
          content +=",".join(newheader)
        if count !=0:
          content += ",".join(line.split("\r\n")[0].split(","))
      count +=1

    print(len(content))
    f = open(one+".csv", "w")
    f.write(content)
    f.close()
      # print (content)









    #
    #
    # content = f.readlines()
    # header = content[0].split(",")
    # newheader = []
    # for item in header[:-1]:
    #   if "$" in item:
    #     newheader +=[item]
    #   else:
    #     newheader +=["$"+item]
    # newheader += ["$<"+header[-1]]
    # content[0] = ",".join(newheader)
    # # pdb.set_trace()
    #
    # for row in content:
    #   with open(one+".csv","a") as f:
    #     f.write(row)
    # pdb.set_trace()

# def addn(f = "./data/treat"):
#   all_files = [ (join(f,path)) for path in listdir(f) if isfile(join(f,path))]
#   for one in all_files:
#     content = []
#     with open(one,"r") as f:
#       # pdb.set_trace()
#       content = f.readlines()
#       for j in content:
#       content[0]+=[j+"\n"]
#
#
#     for row in content:
#       with open(one+".csv","a") as f:
#         f.write(row)


def new_header(f = "./data"):
    import csv
    import sys

    all_files = [ (join(f,path)) for path in listdir(f) if isfile(join(f, path))]
    for filename in all_files:
        f = open(filename, 'rb')
        mod_file = []
        try:
            reader = csv.reader(f)
            for i,row in enumerate(reader):
                if i == 0:
                    mod_file.append(row)
                    continue # first row is the header
                print(i, len(row))
                new_row = []
                for e in row:

                    try:
                        one, two = e.split("-") # Values are ranges
                    except ValueError: # last column is a experience column
                        new_row.append(float(e))
                        continue
                    if one.replace(" ", "") == "ninf": one = -1 # ninf represents -infinity
                    else: one = float(one)
                    two = float(two)
                    new_row.append((one-two)/2)
                mod_file.append(new_row)
            print "Number of rows in the file: ", len(mod_file)
            fp = open(filename+"_mod", 'w')
            a = csv.writer(fp, delimiter=',')
            a.writerows(mod_file)
            fp.close()
        finally:
            f.close()



if __name__ == "__main__":
  new_header()
  # addn()