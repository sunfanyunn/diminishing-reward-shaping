import numpy as np
import os, subprocess, time, signal
import copy

from envs.adjustment import *

# upper left is [0,0]
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
label2action = {'up': 0, 'down': 1, 'left': 2, 'right': 3, 'still': 4}
action2label = {0: 'up', 1: 'down', 2: 'left', 3: 'right',4: 'still'}

class MazeEnv():

    def __init__(self, X, Y,agents, tpe, window_size, thresh):
        self.window_size = window_size
        self.X, self.Y = X, Y
        self.agents = agents
        # initialize to no apple on the map
        self.eaten = True
        # this counts for round
        self.thresh = thresh
        self.cnt = 0
        ln = len(self.agents)
        self.move_per_round = ln * (ln + 1) / 2
        self.maze = np.zeros((len(agents)+1,X,Y))
        self.init_pos = [(0,0), (X-1, Y-1), (0,Y-1), (X-1, 0)]
        # this decides the type of the adjustment function
        self.adjustment = globals()[tpe]
        # this initialized state according to the parameters
        self._update_env()

    def step(self, action, agent_id):
        assert self.maze[len(self.agents)][self.ax][self.ay] == 1.

        self.cnt += 1
        # new round starts
        if self.cnt % self.move_per_round == 1:
            for i in range(len(self.agents)):
                assert len(self.agents[i].history)%(i+1)==0

        # Order goes like ==>
        tot = len(self.agents)
        all_pos = [agent.pos for agent in self.agents]

        x, y = self.agents[agent_id].pos

        nx = x+dx[action]
        ny = y+dy[action]

        if not self._out_of_bound(nx, ny) and (nx, ny) not in all_pos:
            self.agents[agent_id].move(action)
            reward = float(self.maze[tot][nx][ny] == 1)
            ori_reward = reward

            if reward == 0.:
                reward += float(1/(abs(self.ax-nx)+abs(self.ay-ny)) - \
                                1/(abs(self.ax- x)+abs(self.ay -y)))
            else:
                self.eaten = True

        else:
            reward = ori_reward = 0.

        if ori_reward == 1:
            tt = self.agents[agent_id].get_I(self.window_size, agent_id)
            reward = self.adjustment(tt, self.thresh)

        # apples respawn
        self._update_env()
        self.agents[agent_id].history.append(ori_reward)

        episode_over = False
        return self.get_state(agent_id), ori_reward, float(reward), episode_over, {}

    def reset(self):
        self.eaten = True
        self.maze = np.zeros((len(self.agents)+1, self.X, self.Y))
        for idx, agent in enumerate(self.agents):
            agent.pos = self.init_pos[idx]
            agent.history = []

        self._update_env()

    def render(self, mode='human', close=False):
        pass

    def _update_env(self):
        tot = len(self.agents)
        for idx, agent in enumerate(self.agents):
            self.maze[idx] = np.zeros((self.X, self.Y))
            x, y = agent.pos
            self.maze[idx][x][y] = 1

        while self.eaten:
            self.maze[tot] = np.zeros((self.X, self.Y))
            x = np.random.randint(0, self.X)
            y = np.random.randint(0, self.Y)
            if not any((x,y)==agent.pos for agent in self.agents):
                self.ax = x
                self.ay = y
                self.maze[tot][x][y] = 1
                self.eaten = False
        
        assert np.sum(self.maze.flatten()) == tot + 1

    def _out_of_bound(self, x, y):
        return x < 0 or y < 0 or x >= self.X or y >= self.Y

    def get_state(self, agent_id):
        ret = []
        x, y = self.agents[agent_id].pos
        for idx, agent in enumerate(self.agents):
            if idx == agent_id:
                ret = [self.ax - x, self.ay - y] + ret
            else:
                ret += [agent.pos[0] - x, agent.pos[1] - y]

        ret += [self.agents[agent_id].get_I(self.window_size, agent_id)]
        return copy.deepcopy(np.array(ret))

    def _print_maze(self):
        print(self.maze)

    def visualize(self):
        ret = np.zeros((self.X,self.Y))
        tot = len(self.agents)
        print("======================")

        for i in range(self.X):
            print('#', end='')
            for j in range(self.Y):
                ok = False
                for idx, agent in enumerate(self.agents):
                    if agent.pos == (i,j):
                        ret[i][j] = idx+1
                        ok = True
                        print(idx, end='')
                        break
                if ok: continue

                if self.maze[tot][i][j] == 1:
                    ret[i][j] = tot + 1
                    print('a', end='')
                else:
                    print(' ', end='')
            print('#')
        print("======================")
        return ret
