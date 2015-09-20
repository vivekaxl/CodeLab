"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt




# data for apache
x_apache = [0.5, 0.6, 0.7, 0.8, 0.9]
plt.rcParams.update({'font.size': 8})


y_apache_exemplar =[22.060123417899998, 20.2320565948, 20.2645862085, 21.8135875453, 11.0532971428]
y_apache_baseline =[6.10386062048, 6.292535089579999, 5.36989804829, 4.9171974702100005, 3.9906587038300003]
y_apache_east_west_where =[8.69467174713, 8.31589462084, 9.03264040919, 7.382067856710001, 8.52448613233]



# data for bdbc
x_bdbc = [0.5, 0.6, 0.7, 0.8, 0.9]

y_bdbc_exemplar = [1.79029943266, 2.35988536574, 1.66914761715, 2.9478839729299997, 6.74296661236]
y_bdbc_baseline = [0.00500088027432, 0.0077303885296000005, 0.00650401839482, 0.0044510349638, 0.0063435076864799995]
y_bdbc_east_west_where = [0.23320416261, 0.12007414510799999, 0.17222717851, 0.25979064840800004, 0.26492887207000004]


# data for bdbj
x_bdbj = [0.5, 0.6, 0.7, 0.8, 0.9]
y_bdbj_exemplar 	= [14.4229058533, 14.969079643399999, 15.9929483683, 3.50262215385, 4.26545296952]
y_bdbj_baseline 	= [2.18989886393, 2.14213469845, 2.73014950345, 2.43351057868, 3.33023316225]
y_bdbj_east_west_where = [2.60398627922, 2.6926559448200003, 2.61382293484, 3.0216723384399997, 1.7746186756]

# data for llvm
x_llvm = [0.5, 0.6, 0.7, 0.8, 0.9]
y_llvm_exemplar 	= [3.03686178162, 2.3048862632000002, 2.0843237954, 2.73172174425, 2.3891251053800002]
y_llvm_baseline 	= [1.52564630468, 1.61127594373, 1.74312935723, 1.59637841964, 1.3999568439599999]
y_llvm_east_west_where = [2.44434224864, 2.04837203191, 2.10728923284, 1.97511965599, 1.9697401384200002]


# data for sql
x_sql = [0.5, 0.6, 0.7, 0.8, 0.9]
y_sql_exemplar	= [7.27029210357, 7.72392852193, 7.93863657574, 8.107963259669999, 8.34285400315]
y_sql_baseline 	= [4.53293018549, 4.5459692276400006, 4.7044621198700005, 4.8781525627, 5.22226692691]
y_sql_east_west_where = [6.29511156704, 6.51821155728, 6.6694600384300005, 6.76907594504, 6.696223387939999]

# data for x264
x_x264 = [0.5, 0.6, 0.7, 0.8, 0.9]
y_x264_exemplar 	= [14.0354432453, 7.91502796296, 10.3730377204, 9.49545687567, 10.8432886288]
y_x264_baseline 	= [0.0932951238409, 0.0887436786793, 0.0683612195665, 0.0538348916926, 0.0552243694221]
y_x264_east_west_where = [2.71919238179, 1.30660143866, 1.35034233642, 1.3666437972299998, 1.4983491500700001]

f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, sharex='col')
# plt.subplot(3, 2, 1)
ax1.plot(x_apache, y_apache_exemplar, 'ko-', color='r')
ax1.plot(x_apache, y_apache_baseline, 'kv-', color='b')
ax1.plot(x_apache, y_apache_east_west_where, 'kx-', color='g')
ax1.set_title('Apache')
ax1.set_xlim(0.45, 0.95)
ax1.set_xlabel("Training Data (% of data)")
ax1.set_ylabel("MRE")

# plt.subplot(3, 2, 2)
ax2.plot(x_bdbc, y_bdbc_exemplar, 'ko-', color='r')
ax2.plot(x_bdbc, y_bdbc_baseline, 'kv-', color='b')
ax2.plot(x_bdbc, y_bdbc_east_west_where, 'kx-', color='g')
ax2.set_title('Berkeley DB C')
ax2.set_xlim(0.45, 0.95)
ax2.set_ylim(-1, 7)
ax2.set_xlabel("Training Data (% of data)")
ax2.set_ylabel("MRE")

# plt.subplot(3, 2, 3)
ax3.plot(x_bdbj, y_bdbj_exemplar, 'ko-', color='r')
ax3.plot(x_bdbj, y_bdbj_baseline, 'kv-', color='b')
ax3.plot(x_bdbj, y_bdbj_east_west_where, 'kx-', color='g')
ax3.set_ylim([0,18])
ax3.set_title('Berkeley DB Java')
ax3.set_xlim(0.45, 0.95)
ax3.set_xlabel("Training Data (% of data)")
ax3.set_ylabel("MRE")

# plt.subplot(3, 2, 4)
ax4.plot(x_llvm, y_llvm_exemplar, 'ko-', color='r')
ax4.plot(x_llvm, y_llvm_baseline, 'kv-', color='b')
ax4.plot(x_llvm, y_llvm_east_west_where, 'kx-', color='g')
ax4.set_title('LLVM')
ax4.set_xticks(np.arange((min(x_llvm)-0.05), (max(x_llvm)+0.06), 0.1))
ax4.set_xlabel("Training Data (% of data)")
ax4.set_ylabel("MRE")

# plt.subplot(3, 2, 5)
ax5.plot(x_sql, y_sql_exemplar, 'ko-', color='r')
ax5.plot(x_sql, y_sql_baseline, 'kv-', color='b')
ax5.plot(x_sql, y_sql_east_west_where, 'kx-', color='g')
ax5.set_title('SQL')
ax5.set_yticks(np.arange(int(min(y_sql_baseline)- 1), int(max(y_sql_exemplar)+1), 1))
ax5.set_xticks(np.arange((min(x_sql)-0.05), (max(x_sql)+0.06), 0.1))
ax5.set_xlabel("Training Data (% of data)")
ax5.set_ylabel("MRE")

# plt.subplot(3, 2, 6)
ax6.plot(x_x264, y_x264_exemplar, 'ko-', color='r')
ax6.plot(x_x264, y_x264_baseline, 'kv-', color='b')
ax6.plot(x_x264, y_x264_east_west_where, 'kx-', color='g')
ax6.set_ylim([-1,16])
ax6.set_title('X264')
ax6.set_xticks(np.arange((min(x_x264)-0.05), (max(x_x264)+0.06), 0.1))
ax6.set_xlabel("Training Data (% of data)")
ax6.set_ylabel("MRE")

plt.subplots_adjust(left=0.35, bottom=0.04, right=0.90, top=0.97, wspace=0.10, hspace=0.10)
plt.figlegend([ax1.lines[0], ax1.lines[1], ax1.lines[2]], ["Where Exemplar", "BaseLine", "Where East West"], frameon=False, loc='lower center', bbox_to_anchor=(0.5, -0.005), fancybox=True, ncol=3)
f.tight_layout()
f.set_size_inches(5, 8)
plt.subplot_tool()
# plt.savefig('destination_path.eps', format='eps')
plt.show()