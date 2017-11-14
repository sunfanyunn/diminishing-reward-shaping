import numpy as np
import os
import sys

from core.dqn import DQNAgent
from envs.hunter_prey import MazeEnv
from config import *

history = [ [] for _ in range(num_agents)]
ori_history = [ [] for _ in range(num_agents)]

if __name__ == "__main__":
    if not os.path.exists(data_dir):
         os.mkdir(data_dir)

    agents, env = init()
    done = False

    turn = [i for i in range(1, num_agents+1)]
    tot_turn = sum(turn)

    for e in range(EPISODES):

        env.reset()
        reward_sum = [0]*num_agents
        ori_reward_sum = [0]*num_agents

        for rnd in range(round_per_game):

            for idx, agent in enumerate(agents):
                for _ in range(turn[idx]):
                    state = env.get_state(idx)

                    action = agent.act(state)
                    next_state, ori_reward, reward, done, _ = env.step(action, idx)
                    agent.remember(state, action, reward, next_state, done)
                    reward_sum[idx] += reward
                    ori_reward_sum[idx] += ori_reward

        print("reward_sum", reward_sum)
        print("ori_reward_sum", ori_reward_sum)

        for i in range(num_agents):
            history[i].append(reward_sum[i])
            ori_history[i].append(ori_reward_sum[i])


        for agent in agents:
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        if e % info_epoch == 0:
            print('save model')
            for idx, agent in enumerate(agents):
                agent.save(os.path.join(data_dir, '_'.join(['model', str(idx), str(e)]) + '.h5'))
                np.savez(os.path.join(data_dir, 'history'), np.array(history))
                np.savez(os.path.join(data_dir, 'ori_history'), np.array(ori_history))
