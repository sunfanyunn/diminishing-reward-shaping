import numpy as np
import matplotlib.pyplot as plt

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    return asum ,ent

 # Original game
player0 = [561, 327.766, 267.821, 117.697  ]
player1 = [1386, 854.316,  533.883, 531.829]

# After adjustment with stepfunction and thresh = 6
player00 = [726, 370, 241.1, 124.8]
player11 = [806, 802.6, 512.2, 510.2]

N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.10       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind , player0, width, color='black')

rects2 = ax.bar(ind + width , player1, width, color='black')

rects3 = ax.bar(ind + width + width + 0.1, player00, width, fill=False, color='b')

rects4 = ax.bar(ind + width + width + width + 0.1, player11, width, fill=False, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Resources consumed in a single game')
#ax.set_title('Scores by group and gender')
ax.set_xticks(ind + (3*width+0.1)/2)
ax.set_xticklabels(('5', '10', '15', '20'))
ax.set_xlabel('Spawn time of apples')
ax.tick_params(axis='x', length=0)

#ax.legend((rects1[0], rects4[0]), ('Original', 'Step Function(τ=6)'))
ax.legend((rects1[0], rects4[0]), ('Original', 'Shaping applied'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)
plt.savefig('gathering_st')
plt.show()
