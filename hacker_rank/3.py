from __future__ import division

dance_pairs = []
temp_dance_pairs = []
class frame:
    def __init__(self, hboy, hgirl):
        self.hboy = hboy
        self.hgirl = hgirl
        self.diff = abs(hboy - hgirl)
    def __str__(self):
        return str(self.hboy) + " " + str(self.hgirl)

def add_dance_pairs(hboy, hgirl):
    dance_pairs.append(frame(hboy, hgirl))

def add_temp_dance_pairs(hboy, hgirl):
    temp_dance_pairs.append(frame(hboy, hgirl))



first_line = raw_input()
N, K = first_line.split()

second_line = raw_input()
heights_boys = second_line.split()
heights_boys = sorted([int(s) for s in heights_boys])

third_line = raw_input()
heights_girls = third_line.split()
heights_girls = sorted([int(s) for s in heights_girls], reverse=True)


count = 0
for bcount, hb in enumerate(heights_boys):
    for gcount, hg in enumerate(heights_girls):
        if abs(hb - hg) < int(K):
            add_dance_pairs(hb, hg)
            heights_girls.remove(hg)
            continue


print len(dance_pairs)


