import numpy as np
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

f, ax = plt.subplots(2,2, sharex=True, sharey=True)

def plot(ax, function):

    ax.set_title(function)
    #ax.set_ylabel('Original reward received in a single game')
    #ax.set_xlabel('Episode')

    x = np.arange(0, 10, 0.001)
    if function == 'step function (τ=5)':
        y = (x<5).astype(np.int)
    elif function == 'negative step function (τ=5)':
        y = [-1 if xx > 5 else 1 for  xx in x]
    elif function == 'exponential':
        y = np.exp(-x)
    else:
        y = [1]*len(x)

    line = ax.plot(x, y, 'g')
    #ax.legend(line, annotations)


plot(ax[0][0], 'original')
plt.margins(x=0)

plot(ax[0][1], 'exponential (τ=1)')
plt.margins(x=0)

plot(ax[1][0], 'step function (τ=5)')
plt.margins(x=0)

plot(ax[1][1], 'negative step function (τ=5)')
plt.margins(x=0)

plt.tight_layout()
plt.savefig('fuck.png')
