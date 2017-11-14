import numpy as np
import matplotlib.pyplot as plt

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    return asum ,ent

#exponential
#[  441.9  1101.3  1652.5]
#[  515.9   910.3  1721. ]
#[  540.5  1142.1  1569.9]
#[  515.1  1161.   1578.9]
 # Original game
player0 = [502, 569, 654, 780, 529, 653, 752, 442, 516, 541, 515]
player1 = [1160, 1214, 1202, 879, 1220, 1129, 950, 1101, 910, 1142, 1161]
player2 = [1659, 1465, 1312, 928, 1555, 1193, 959, 1653, 1721, 1570, 1679]

# After adjustment with stepfunction and thresh = 6
#player00 = [726, 370, 241.1, 124.8]
#player11 = [806, 802.6, 512.2, 510.2]

fig, ax = plt.subplots(figsize=(11,6.5))

def plot(labels, color='black'):
    N = len(player0)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.15       # the width of the bars

    global rects1, rects2, rects3
    rects1 = ax.bar(ind , player0, width, fill=False, color=color)
    rects2 = ax.bar(ind + width , player1, width, fill=False, hatch='//', color=color)
    rects3 = ax.bar(ind+width*2, player2, width, color=color)

# add some text for labels, title and axes ticks
    ax.set_ylabel('Resources consumed in a single game')
    ax.set_ylim([0, 1900])
    ax.set_title('3 player Gathering Game')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(labels)
    ax.set_xlabel('')
    ax.tick_params(axis='x', length=0)



labels = ['Original', 'τ=10', 'τ=8', 'τ=6',
          'τ=10', 'τ=8', 'τ=6',
          'τ=5', 'τ=10', 'τ=25', 'τ=50']
plot(labels, color='black')
for i in range(1, len(labels)):
    if i <= 3:
        rects1[i].set_color('r')
        rects2[i].set_color('r')
        rects3[i].set_color('r')
    elif i <= 6:
        rects1[i].set_color('g')
        rects2[i].set_color('g')
        rects3[i].set_color('g')
    else:
        rects1[i].set_color('b')
        rects2[i].set_color('b')
        rects3[i].set_color('b')

ax.legend((rects3[0], rects3[3], rects3[6], rects3[10]), ('Original', 'Step Function', 'Negative step function', 'Exponential'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for i, rect in enumerate(rects):
        height = rect.get_height()
        s, ent = calc([player0[i], player1[i], player2[i]])
        if i == 4:
            ax.text(rect.get_x() - 2*rect.get_width(), 0.9*height,
                    '{}\n{:.4f}'.format(s, ent),
                    ha='center', va='bottom')
        else:
            ax.text(rect.get_x() - rect.get_width()/4., 1.01*height,
                    '{}\n{:.4f}'.format(s, ent),
                    ha='center', va='bottom')

#autolabel(rects1)
autolabel(rects3)
#ax.legend((rects1[0], rects2[0]), ('agent0', 'agent1'))
plt.tight_layout()
plt.savefig('g3')
plt.show()
