import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x**2

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
l1, = plt.plot(x,y2,label='up')
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best')

plt.xlim(-1,2)
plt.ylim(-2,3)
plt.xlabel('I am X')
plt.ylabel('I am Y')
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
plt.annotate(f"$2x+1={y0}$",xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.text(-0.7,3,r'$This\ is\ the\ some\ text.\ \mu \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='blue',edgecolor='None',alpha=0.7))

plt.show()