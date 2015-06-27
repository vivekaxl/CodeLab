from __future__ import division

class substring:
    def __init__(self, str):
        self.str = str


def func(str):
    return 0 if str[0] != str[-1] else 1

def substring(str):
    substr = []
    for i in xrange(len(str)):
        for j in xrange(i+1, len(str)):
            if i == j : substr.append(str[i])
            else: substr.append(str[i:j])
    return substr

N = raw_input()
N = int(N)
str = raw_input()
score = 0
substr = substring(str)
for s in substr:
    print s
    score += func(s)

print score