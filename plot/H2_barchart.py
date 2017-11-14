import numpy as np
import matplotlib.pyplot as plt

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    return asum ,ent

 # Original game
player0 = [561,595, 601, 726]
player1 = [1386, 1309,  1269, 806]

# After adjustment with stepfunction and thresh = 6
#player00 = [726, 370, 241.1, 124.8]
#player11 = [806, 802.6, 512.2, 510.2]

N = 4

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind , player0, width, fill=False, color='black')
rects2 = ax.bar(ind + width , player1, width, color='black')

# add some text for labels, title and axes ticks
ax.set_ylabel('Resources consumed in a single game')
ax.set_ylim([0, 1600])
ax.set_title('Step function (2-player Gathering Game)')
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('Original', 'τ=10', 'τ=8', 'τ=6'))
ax.set_xlabel('')
ax.tick_params(axis='x', length=0)

#ax.legend((rects1[0], rects4[0]), ('Original', 'Step Function(τ=6)'))
ax.legend((rects1[0], rects2[0]), ('agent0', 'agent1'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() - rect.get_width()/4., 1.05*height,
                '{:.4f}'.format(calc([player0[i], player1[i]])[1]),
                ha='center', va='bottom')

#autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('g2_step')
plt.show()
