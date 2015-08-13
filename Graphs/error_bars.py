def draw(data, name):
    scores = []
    import matplotlib.pyplot as plt
    import numpy as np
    for d in data:
        temp = []
        temp.append(d[0])
        temp.append(np.percentile(d[1], 50))
        temp.append(np.percentile(d[1], 75) - np.percentile(d[1], 25))
        temp.append(d[2])
        scores.append(temp)

    plt.figure()
    plt.errorbar([x[0] for x in scores], [x[1] for x in scores], xerr=0, yerr=[x[2] for x in scores])
    plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
    plt.show()





data = [[0.5, [1,2,3,4,5], "1"], [0.6, [3,4,5,3,4], "2"], [0.7, [4,3,2,5,3], "3"], [0.8, [5,4,5,3,2], "4"], [0.9, [3,4,5,3,4], "5"]]
draw(data, "problem1")