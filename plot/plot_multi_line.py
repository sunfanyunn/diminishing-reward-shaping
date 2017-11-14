import numpy as np
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LW = 1.5
eLW = 0.8
nb = 450
num_players = 2
first = True

line_colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

def plot(data_dir, annotations):


    def process(arr):
        ln = len(arr)
        x, y, stderr = [], [], []
        for i in range(0, ln-10, 10):
            x.append(i+5)
            y.append(np.mean(arr[i:i+10]))
            stderr.append(np.std(arr[i:i+10]))

        return x, y, stderr



    line = []
    if os.path.exists(os.path.join(data_dir, 'ori_history.npz')):
        ori_history = np.load(os.path.join(data_dir, 'ori_history.npz'))['arr_0']
        for i in range(num_players):
            x, y, stderr = process(ori_history[i][:nb])
            line.append(plt.errorbar(x, y, yerr=stderr, color=line_colors[k], marker='.', lw=LW, elinewidth=eLW, errorevery=3, capsize=2, markersize=5))

    #plt.legend(line_colors[k], annotations)



tot = len(sys.argv) - 1

k = 0
plot(sys.argv[1], 'Original')
k += 1
plot(sys.argv[2], 'Step Function (τ=10)')
k += 1
plot(sys.argv[3], 'Step Function (τ=8)')
k += 1
plot(sys.argv[4], 'Step Function (τ=7)')
k += 1
plot(sys.argv[5], 'Step Function (τ=6)')

plt.title('Gathering Game')
plt.ylabel('Original reward received in a single game')
plt.xlabel('Episode')

plt.tight_layout()
plt.legend()
plt.savefig('result.png')
