import numpy as np
import matplotlib.pyplot as plt

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    return asum ,ent

 #[ 167.11  509.96]
 #[ 185.202  477.143]
 #[ 198.224  482.934]
 #[ 214.7  458.1]    # Original game
player0 = [180, 192, 194, 225, 211, 188, 200, 222, 144, 167, 185, 198, 215]
player1 = [506, 496, 493, 444, 479, 487, 478, 322, 177, 510, 477, 483, 458]

# After adjustment with stepfunction and thresh = 6
#player00 = [726, 370, 241.1, 124.8]
#player11 = [806, 802.6, 512.2, 510.2]

fig, ax = plt.subplots(figsize=(11,6))

def plot(player0, player1, ax, labels, color='black'):
    N = len(player0)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars

    global rects1, rects2
    rects1 = ax.bar(ind , player0, width, fill=False, color=color)
    rects2 = ax.bar(ind + width , player1, width, color=color)

# add some text for labels, title and axes ticks
    ax.set_ylabel('Resources consumed in a single game')
    ax.set_ylim([0, 650])
    ax.set_title('2 player Hunter Prey')
    ax.set_xticks(ind + width/2)
    ax.set_xticklabels(labels)
    ax.set_xlabel('')
    ax.tick_params(axis='x', length=0)


labels = ['Original', 'τ=8', 'τ=6', 'τ=4','τ=2',
          'τ=8', 'τ=6', 'τ=4', 'τ=2',
          'τ=5', 'τ=10', 'τ=25', 'τ=50']
plot(player0, player1, ax, labels, color='black')
for i in range(1, len(labels)):
    if i <= 4:
        rects1[i].set_color('r')
        rects2[i].set_color('r')
    elif i <= 8:
        rects1[i].set_color('g')
        rects2[i].set_color('g')
    else:
        rects1[i].set_color('b')
        rects2[i].set_color('b')

ax.legend((rects2[0], rects2[3], rects2[6], rects2[10]), ('Original', 'Step Function', 'Negative step function', 'Exponential'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        s, ent = calc([player0[i], player1[i]])
        ax.text(rect.get_x() - rect.get_width()/4., 1.01*height,
                '{}\n{:.4f}'.format(s, ent),
                ha='center', va='bottom')

#autolabel(rects1)
autolabel(rects2)
#ax.legend((rects1[0], rects2[0]), ('agent0', 'agent1'))
plt.tight_layout()
plt.savefig('h2')
plt.show()
