import numpy as np
import matplotlib.pyplot as plt

n= 5

# m1 = (0.10,0.12,0.10,0.11,0.14,0.10)
# m2 = (0.21,0.21,0.20,0.22,0.20,0.21)
# m3 = (0.29,0.27,0.28,0.24,0.23,0.23)
# m4 = (0.41,0.39,0.35,0.37,0.41,0.40)
# x = [0.5, 0.6, 0.7, 0.8, 0.9]

apache_baseline = [137788.5,104640,78930,55248,26349]
apache_exemplar = [258108,258321,258324,248911.5,243237]
apache_east_west = [227490,226917,226852.5,201306,189255]
# x = [0.5, 0.6, 0.7, 0.8, 0.9]


bdbc_baseline = [10511.7769123,8435.63783231,6203.85023231,4039.88633231,2057.03919731]
bdbc_exemplar = [20956.9546223,20978.1694073,21019.9951123,20984.3909923,21000.3801923]
bdbc_east_west = [18688.5706823,18624.6701323,18598.1385023,18519.0945473,18521.3334223]

bdbj_baseline = [574495.3,462322,346561,203310.3,93529.45]
bdbj_exemplar = [1061677.9,1059829.9,1063038.6,1051029.9,982782.6]
bdbj_east_west = [913205.8,910559.25,895507.45,907351.85,740612.65]

llvm_baseline = [121157.381527,97335.4397117,72515.4648017,48062.9071667,23989.0442667]
llvm_exemplar = [230708.157252,226278.684457,224381.062432,224054.006872,224144.563387]
llvm_east_west = [217591.091812,207646.680032,203009.353062,203823.206437,203777.498912]

sql_baseline = [33759.002568,27053.834673,20277.338168,13526.470568,6760.65586798]
sql_exemplar = [66065.420423,65937.159138,65941.616833,65944.066688,65954.609288]
sql_east_west = [64291.693748,63977.951268,63993.933783,63997.356813,63992.287383]

x264_baseline = [264567.6846, 217141.711665, 158112.660925, 103372.429995, 51963.547165]
x264_exemplar = [515505.376645, 505347.78268, 506371.483135, 506529.32012, 506056.326785]
x264_east_west = [481032.437875, 454872.414625, 452258.38552, 452595.647675, 450948.96363]

# fig, ax = plt.subplots()
#
index = np.array([50, 60, 70, 80, 90])
bar_width = 2
#
opacity = 0.2
error_config = {'ecolor': '0.3'}
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size':9.5})
rc('text', usetex=True)

f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6,1, sharex='col')

ax1.set_title('Apache')
r1 = ax1.bar(index, apache_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax1.bar(index+bar_width, apache_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax1.bar(index + 2*bar_width, apache_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax1.set_xlim(45, 98)
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.yaxis.offsetText.set_visible(False)
ax1.set_xlabel("Training Data (\% of data)")
ax1.set_ylabel("Time saved \n(x$10^5$) secs", fontsize=11)

ax2.set_title('Berkeley DB C')
r1 = ax2.bar(index, bdbc_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax2.bar(index + bar_width, bdbc_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax2.bar(index + bar_width+ bar_width, bdbc_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax2.set_xlim(45, 98)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.yaxis.offsetText.set_visible(False)
ax2.set_xlabel("Training Data (\% of data)")
ax2.set_ylabel("Time saved \n(x$10^4$) secs", fontsize=11)

ax3.set_title('Berkeley DB Java')
r1 = ax3.bar(index, bdbj_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax3.bar(index + bar_width, bdbj_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax3.bar(index + bar_width+ bar_width, bdbj_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax3.set_xlim(45, 98)
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax3.yaxis.offsetText.set_visible(False)
ax3.set_xlabel("Training Data (\% of data)")
ax3.set_ylabel("Time saved \n(x$10^6$) secs", fontsize=11)

ax4.set_title('LLVM')
r1 = ax4.bar(index, llvm_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax4.bar(index + bar_width, llvm_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax4.bar(index + bar_width+ bar_width, llvm_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax4.set_xlim(45, 98)
ax4.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax4.yaxis.offsetText.set_visible(False)
ax4.set_xlabel("Training Data (\% of data)")
ax4.set_ylabel("Time saved \n(x$10^5$) secs", fontsize=11)

ax5.set_title('SQL')
r1 = ax5.bar(index, sql_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax5.bar(index + bar_width, sql_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax5.bar(index + bar_width+ bar_width, sql_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax5.set_xlim(45, 98)
ax5.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax5.yaxis.offsetText.set_visible(False)
ax5.set_xlabel("Training Data (\% of data)")
ax5.set_ylabel("Time saved \n(x$10^4$) secs", fontsize=11)

ax6.set_title('X264')
r1 = ax6.bar(index, x264_baseline, bar_width,alpha=opacity,color='b',error_kw=error_config)
r2 = ax6.bar(index + bar_width, x264_exemplar, bar_width,alpha=opacity,color='r',error_kw=error_config)
r3 = ax6.bar(index + bar_width+ bar_width, x264_east_west, bar_width,alpha=opacity,color='g',error_kw=error_config)
ax6.set_xlim(45, 98)
ax6.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax6.yaxis.offsetText.set_visible(False)
ax6.set_xlabel("Training Data (\% of data)")
ax6.set_ylabel("Time saved \n(x$10^5$) secs", fontsize=11)


plt.figlegend([r1, r2, r3], ["BaseLine", "Where Exemplar",  "Where East West"], frameon=False, loc='lower center', bbox_to_anchor=(0.5, -0.0145), fancybox=True, ncol=3)
# f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
#
# ax1.bar(x,m1, 0.2) # thickness=0.2
# ax2.bar(x,m2, 0.2)
# ax3.plot(x,m3)
# ax4.plot(x,m4)
f.set_size_inches(6.0, 8.5)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.tight_layout()
# plt.show()
plt.savefig('performance_graph.eps', format='eps')