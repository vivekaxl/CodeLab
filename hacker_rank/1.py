from __future__ import division
import itertools

class frame:
    newid = itertools.count().next
    def __init__(self, a):
        self.id = frame.newid() + 1
        self.a = float(a)
        self.sum = 0

first_line = raw_input()
N,P,X = first_line.split()
second_line = raw_input()
A = [float(x) for x in second_line.split()]
frames = []
for a in A: frames.append(frame(a))

for count, f in enumerate(frames):
    f.sum = (float(P) - (count * float(X))) * f.a

sorted_result = sorted(frames, key=lambda f: f.sum)

print sorted_result[-1].id
