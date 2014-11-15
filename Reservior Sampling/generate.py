from __future__ import division 
import sys, random
minR=1
maxR=10000

def any():
  return minR+random.random()*(maxR-minR)

f = open("data.dat","w")
for i in xrange(500):
  f.write("%d\n"%any())
f.close()
