import numpy as np
import os
import sys

from core.dqn import DQNAgent
from envs.hunter_prey import MazeEnv
from config.hunter_prey import *

history = [ [] for _ in range(num_agents)]
ori_history = [ [] for _ in range(num_agents)]

if __name__ == "__main__":
    if not os.path.exists(data_dir):
         os.mkdir(data_dir)
    agents, env = init()

    for idx, agent in enumerate(agents):
        agent.load(os.path.join(data_dir, '_'.join(['model',
                                                    str(idx),
                                                    str(args.load_trained_epoch)]) + '.h5'))

    done = False
    turn = [i for i in range(1, num_agents+1)]

    tot_turn = sum(turn)

    for e in range(5):

        env.reset()
        reward_sum = [0]*num_agents
        ori_reward_sum = [0]*num_agents

        for rnd in range(round_per_game):

            for idx, agent in enumerate(agents):
                for _ in range(turn[idx]):
                    state = env.get_state(idx)

                    action = agent.model.predict_classes(
                        np.reshape(state, (1,) + state.shape),
                        verbose=0)[0]

                    next_state, ori_reward, reward, done, _ = env.step(action, idx)
                    agent.remember(state, action, reward, next_state, done)
                    reward_sum[idx] += reward
                    ori_reward_sum[idx] += ori_reward


        print("reward_sum", reward_sum)
        print("ori_reward_sum", ori_reward_sum)

        for i in range(num_agents):
            history[i].append(reward_sum[i])
            ori_history[i].append(ori_reward_sum[i])

    print("Average ori_reward_sum")
    print(np.sum(np.array(ori_history)/5, axis=1)/5)
