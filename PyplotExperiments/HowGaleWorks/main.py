import csv
import matplotlib.pyplot as plt
from textwrap import wrap
from matplotlib import rc

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 7}

rc('font', **font)

def transform(filename):
    return "../" + filename

def read_csv(filename, header=False):
    data = []
    f = open(filename, 'rb')
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        if i == 0 and header is False: continue  # Header
        elif i ==0 and header is True:
            H = row
            continue

        data.append([i-1]+[1 if x == "Y" else 0 for x in row[:-1]] + [float(row[-1])]) # TODO: DecisionTree regressor returns int values. As a work around I multiply all the class values by 10**4
    f.close()
    if header is True: return H, data
    return data

def get_data(filename):
    header, data = read_csv(filename, header=True)
    data0 = [d[-1] for d in data]
    data0.sort()
    return [[i, d] for i, d in enumerate(data0)]

def get_answer_points(data, answer_found):
    return_answer = []
    for af in answer_found:
        for d in data:
            # print round(d[-1], 4), round(af, 4)
            if int(d[-1]*10**4) == int(af*10**4):
                return_answer.append(d)
                continue
    return return_answer

def draw_graph_apache(name="Apache", answer_25=[870], answer_50=[900], answer_75=[930]):
    data = get_data("./data/Apache_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]

def draw_graph_bdbc(name="BDBC", answer_25=[0.3595], answer_50=[0.3617], answer_75=[0.36292]):
    data = get_data("./data/BDBC_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]


def draw_graph_bdbj(name="BDBJ", answer_25=[3085], answer_50=[3139], answer_75=[3155]):
    data = get_data("./data/BDBJ_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]
    # print y_d

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]

def draw_graph_llvm(name="LLVM", answer_25=[200.9233], answer_50=[201.7033], answer_75=[202.23333]):
    data = get_data("./data/LLVM_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]

    print [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]

def draw_graph_sql(name="SQL", answer_25=[870], answer_50=[900], answer_75=[930]):
    data = get_data("./data/SQL_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]

def draw_graph_x264(name="x264", answer_25=[244.35], answer_50=[246.273], answer_75=[246.58]):
    data = get_data("./data/X264_AllMeasurements.csv")
    x_d = [d[0] for d in data]
    y_d = [d[-1] for d in data]

    answer_point_25 = get_answer_points(data, answer_25)
    x_a_25 = [d[0] for d in answer_point_25]
    y_a_25 = [d[-1] for d in answer_point_25]

    answer_point_50 = get_answer_points(data, answer_50)
    x_a_50 = [d[0] for d in answer_point_50]
    y_a_50 = [d[-1] for d in answer_point_50]

    answer_point_75 = get_answer_points(data, answer_75)
    x_a_75 = [d[0] for d in answer_point_75]
    y_a_75 = [d[-1] for d in answer_point_75]


    return [x_d, y_d], [x_a_25, y_a_25], [x_a_50, y_a_50], [x_a_75, y_a_75]


import numpy as np

left, width = .55, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1)
# plt.subplot(3, 2, 1)
results = draw_graph_apache()
x_d, y_d = results[0][0], results[0][1]
import matplotlib.pyplot as plt
ax1.plot(x_d, y_d, color='r')
ax1.scatter(results[1][0], results[1][1], color='b', s=10)
ax1.scatter(results[2][0], results[2][1], color='r', s=20)
ax1.scatter(results[3][0], results[3][1], color='y', s=10)
ax1.set_yticks(np.arange(500, 3000, 500))
ax1.text(right, 0.5*(bottom+top), 'Apache',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax1.transAxes)

results = draw_graph_bdbc()
x_d, y_d = results[0][0], results[0][1]
x_a, y_a = results[-1][0], results[-1][1]
# print x_a, y_a

ax2.plot(x_d, y_d, color='r')
ax2.scatter(results[1][0], results[1][1], color='b', s=10)
ax2.scatter(results[2][0], results[2][1], color='r', s=20)
ax2.scatter(results[3][0], results[3][1], color='y', s=10)
ax2.set_yticks(np.arange(0, 50, 10))
ax2.text(right, 0.5*(bottom+top), 'BDBC',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax2.transAxes)


results = draw_graph_bdbj()
x_d, y_d = results[0][0], results[0][1]
x_a, y_a = results[-1][0], results[-1][1]
import matplotlib.pyplot as plt
ax3.plot(x_d, y_d, color='r')
ax3.scatter(results[1][0], results[1][1], color='b', s=10)
ax3.scatter(results[2][0], results[2][1], color='r', s=20)
ax3.scatter(results[3][0], results[3][1], color='y', s=10)
ax3.set_yticks(np.arange(2000, 20000, 4000))
ax3.text(right, 0.5*(bottom+top), 'BDBJ',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax3.transAxes)


results = draw_graph_llvm()
x_d, y_d = results[0][0], results[0][1]
x_a, y_a = results[-1][0], results[-1][1]
# print x_a, y_a
import matplotlib.pyplot as plt
ax4.plot(x_d, y_d, color='r')
ax4.scatter(results[1][0], results[1][1], color='b', s=10)
ax4.scatter(results[2][0], results[2][1], color='r', s=20)
ax4.scatter(results[3][0], results[3][1], color='y', s=10)
ax4.set_ylim(190, 300)
ax4.set_yticks(np.arange(190, 300, 30))
ax4.text(right, 0.5*(bottom+top), 'LLVM',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax4.transAxes)


results = draw_graph_sql()
x_d, y_d = results[0][0], results[0][1]
x_a, y_a = results[-1][0], results[-1][1]
ax5.plot(x_d, y_d, color='r')
ax5.scatter(0, 12.5129, color='b', s=10)
ax5.scatter(0, 12.569, color='r', s=20)
ax5.scatter(1, 12.6091, color='y', s=10)
ax5.set_ylim(12, 18)
ax5.set_yticks(np.arange(12, 18, 1))
ax5.text(right, 0.5*(bottom+top), 'SQL',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax5.transAxes)


results = draw_graph_x264()
x_d, y_d = results[0][0], results[0][1]
x_a, y_a = results[-1][0], results[-1][1]
# print x_a, y_a
import matplotlib.pyplot as plt
ax6.plot(x_d, y_d, color='r')
ax6.scatter(results[1][0], results[1][1], color='b', s=10)
ax6.scatter(results[2][0], results[2][1], color='r', s=20)
ax6.scatter(results[3][0], results[3][1], color='y', s=10)
ax6.set_yticks(np.arange(200, 950, 150))
ax6.text(right, 0.5*(bottom+top), 'X264',
        horizontalalignment='center',
        verticalalignment='center',
        rotation=270,
        fontsize=11,
        transform=ax6.transAxes)

plt.setp( ax1.get_xticklabels(), visible=False)
plt.setp( ax2.get_xticklabels(), visible=False)
plt.setp( ax3.get_xticklabels(), visible=False)
plt.setp( ax4.get_xticklabels(), visible=False)
plt.setp( ax5.get_xticklabels(), visible=False)
plt.setp( ax6.get_xticklabels(), visible=False)

plt.subplots_adjust(left=0.20, bottom=0.04, right=0.90, top=0.97, wspace=0.25, hspace=0.28)
f.set_size_inches(4, 6)
f.subplots_adjust(wspace=0, hspace=0)
# plt.subplot_tool()
# plt.figlegend([ax1.lines[0], ax1.lines[1], ax1.lines[2]], ["Where Exemplar", "BaseLine", "Where East West"], frameon=False, loc='lower center', bbox_to_anchor=(0.5, -0.023), fancybox=True, ncol=3)
# f.tight_layout()
plt.savefig('optimizer_result.eps', format='eps')
# plt.show()
