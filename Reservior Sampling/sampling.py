from __future__ import division 
import sys, random
minR=1
maxR=10000
cache_size=64
cache=[0 for i in xrange(cache_size)]

def median(listL):
  listL = sorted(listL)
  length = len(listL)
  if(length%2 == 0):
    return((listL[int(length/2)]+listL[int(length/2)+1])/2)
  else:
    return(listL[int(length/2)+1])

def any(minR,maxR):
  return minR + random.random()*(maxR-minR)

def random_sampling():
  f = open("data.dat","r")
  index=0
  for line in f:
    num = int(line)
    if(index<len(cache)):
      cache[index] = num
    else:
      temp = int(any(minR,index))
      if(temp < cache_size):
        cache[temp] = num
    index+=1
  print "Median Sampling: ",median(cache)

def brute_force():
  f = open("data.dat","r")
  n = []
  for line in f:
    num = int(line)
    n.append(num)
  f.close()
  print "Median: ",median(n)

if __name__ == '__main__': 
  brute_force()
  random_sampling()
