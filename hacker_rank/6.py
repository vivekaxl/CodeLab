# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division

class line_segments:
    def __init__(self, start, end):
        self. start = start
        self.end = end
        self.distance = end - start

    def __str__(self):
        return str(self.start) + " " + str(self.end) + " " + str(self.distance)

def good_bad(line1, line2):
    count = 0
    if line1.start <= line2.start and line1.end >= line2.end: return False
    elif line1.start >= line2.start and line1.end <= line2.end: return False
    return True

def temp_remove(lines, line):
    return [l for l in lines if not (l.start == line.start and l.end == line.end)]

def subset_selection(lines, new_line):
    for line in lines:
        if good_bad(line, new_line) is False:
            return False, line
    return True, None


first_line = raw_input()

lines = []
for _ in xrange(int(first_line)):
    second_line = raw_input()
    start, end = [int(x) for x in second_line.split()]
    lines.append(line_segments(start, end))

subset = []
for line in lines:
    cond, odd_line = subset_selection(subset, line)
    if cond is True: subset.append(line)
    else:
        if subset_selection(temp_remove(subset, odd_line), line) and odd_line.distance < line.distance:
            subset.remove(odd_line)
            subset.append(line)
for l in subset: print l
print len(subset)

