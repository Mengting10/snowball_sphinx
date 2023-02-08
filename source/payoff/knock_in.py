import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

plt.rcParams['font.sans-serif'] = ['Songti Sc']
plt.rcParams["axes.unicode_minus"] = False

def knockin_return(performance, retention, ki_participation, coupon):
    if performance < -(1-retention)/ki_participation:
        return -(1-retention)
    elif -(1-retention)/ki_participation <= performance <= 0:
        return ki_participation * performance
    else:
        return coupon

def no_knockin_return(performance, retention, coupon, bonus):
    if performance >= 0:
        return coupon
    elif 0 > performance >= -(1-retention):
        return bonus
    else:
        return -(1-retention)

n = 500
S = np.linspace(-0.5, 0.5, n)
retention = 0.8
ki_participation = 1.5
ko_participation = 0
coupon = 0.2
bonus = 0.2

y_ki = np.zeros(n)
y_noki = np.zeros(n)
for i in range(n):
    y_ki[i] = knockin_return(S[i], retention, ki_participation, coupon)
    y_noki[i] = no_knockin_return(S[i], retention, coupon, bonus)


plt.figure()
plt.xlabel('挂钩标的涨跌幅',loc='right')
plt.ylabel('Return',loc='top')  

ax = plt.gca()  

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')  

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left') 

ax.spines['bottom'].set_position(('data', 0))  
ax.annotate('', (0.54,0), xytext=(0.58,0), arrowprops={'arrowstyle':'<-'})
ax.spines['left'].set_position(('data', 0))
ax.annotate('', (0,0.2), xytext=(0,0.23), arrowprops={'arrowstyle':'<-'})

# plt.title('雪球已敲入到期损益', fontsize=15)
# plt.xticks([-0.4, -0.2, 0, 0.2, 0.4],['-40%', '-20%', '0', '20%', '40%'])
# plt.plot(S, y_ki)
# plt.savefig('雪球已敲入到期损益.png')
# plt.show()
plt.title('雪球未敲入到期损益', fontsize=15)
plt.xticks([-0.4, -0.2, 0, 0.2, 0.4],['-40%', '-20%', '0', '20%', '40%'])
plt.plot(S, y_noki)
plt.savefig('雪球未敲入到期损益.png')
# plt.show()

