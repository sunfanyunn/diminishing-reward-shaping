import numpy as np
import os
import sys

data_dir = sys.argv[1]
num_players = int(sys.argv[1].split('_', 1)[0])
nb = int(sys.argv[2])

history = np.load(os.path.join(data_dir, 'history.npz'))['arr_0']
print(len(history))
print(len(history[0]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.title('learning curve')
# for i in range(num_players):
#     plt.plot(history[i][:nb], label = 'player_' + str(i))

if os.path.exists(os.path.join(data_dir, 'ori_history.npz')):
    ori_history = np.load(os.path.join(data_dir, 'ori_history.npz'))['arr_0']
    for i in range(num_players):
        plt.plot(ori_history[i][:nb], label = 'ori_' + str(i))
plt.legend()

plt.savefig(data_dir + '.png')
