#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 6
gale = (840,0.3536,2960,199.6833,244.23,12.6091)
nsga2 = (840,0.3536,2960,199.6833,244.23,12.6091)
de = (840,0.3536,2960,199.6833,244.23,12.5129)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, gale, width, color='r')
rects2 = ax.bar(ind+width, nsga2, width, color='y')
rects3 = ax.bar(ind+2*width, de, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels( ("Apache", "Berkeley DB C", "Berkeley DB Java", "LLVM", "SQL", "X264") )

ax.legend((rects1[0], rects2[0], rects3[0]), ('Gale', 'NSGA2', "DE"))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()