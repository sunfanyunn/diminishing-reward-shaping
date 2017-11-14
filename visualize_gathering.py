import numpy as np
import os
import sys

from core.dqn import DQNAgent
from envs.gathering import MazeEnv
from config.gathering import *
#from plot_grid import plot

history = [ [] for _ in range(num_agents)]
ori_history = [ [] for _ in range(num_agents)]

if __name__ == "__main__":
    if not os.path.exists(data_dir):
         os.mkdir(data_dir)

    pic_dir = os.path.join(data_dir, 'pic')
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)

    agents, env = init()

    for idx, agent in enumerate(agents):
        agent.load(os.path.join(data_dir, '_'.join([
                'model',
                str(idx),
                str(args.load_trained_epoch)]) + '.h5')
            )

    done = False
    turn = [i for i in range(1, num_agents+1)]
    tot_turn = sum(turn)

    cnt = 0
    env.reset()

    for rnd in range(round_per_game):

        for idx, agent in enumerate(agents):
            for _ in range(turn[idx]):
                cnt += 1

                state = env.get_state(idx)
                action = agent.model.predict_classes(
                    np.reshape(state, (1,) + state.shape),
                    verbose=0)[0]

                print('agent', idx, action2label[action])
                print('get_I', agent.get_I(window_size, idx))
                next_state, ori_reward, reward, done, _ = env.step(action, idx)
                print(ori_reward, reward)
                env.visualize()
                input()
