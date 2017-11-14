import numpy as np
import os, subprocess, time, signal
import copy

from envs.adjustment import *

# upper left is [0,0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

label2action = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
action2label = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}



class MazeEnv():

    def __init__(self, X, Y, spawn_time, agents, tpe, window_size, thresh):
        self.window_size = window_size
        self.X, self.Y = X, Y
        self.spawn_time = spawn_time
        self.time = np.random.randint(0, spawn_time, size=(self.X, self.Y))
        self.agents = agents
        ln = len(self.agents)
        # this counts for round
        self.thresh = thresh
        self.cnt = 0
        self.move_per_round = ln * (ln + 1) / 2
        self.maze = np.zeros((len(agents)+1,X,Y))
        self.init_pos = [(0,0), (X-1, Y-1), (0,Y-1), (X-1, 0)]
        # this decides the type of the adjustment function
        self.adjustment = globals()[tpe]
        # this initialized state according to the parameters
        self._update_env()

    def step(self, action, agent_id):
        self.cnt += 1
        # new round starts
        if self.cnt % self.move_per_round == 1:
            for i in range(len(self.agents)):
                assert len(self.agents[i].history)%(i+1)==0

        # Order goes like ==>
        # agent takes action to consume apples -> apples respawn
        # Apple will not respawn if the agent is on the grid
        tot = len(self.agents)
        all_pos = [agent.pos for agent in self.agents]

        x, y = self.agents[agent_id].pos

        nx = x+dx[action]
        ny = y+dy[action]

        if not self._out_of_bound(nx, ny) and (nx, ny) not in all_pos:
            self.agents[agent_id].move(action)
            reward = (self.maze[tot][nx][ny] == 1)
        else:
            reward = 0


        ori_reward = float(reward)
        if ori_reward == 1.:
            tt = self.agents[agent_id].get_I(self.window_size, agent_id)
            reward = self.adjustment(tt, self.thresh)
            self.agents[agent_id].hunger_time = 0

        # apples respawn
        self._update_env()

        self.agents[agent_id].history.append(ori_reward)
        episode_over = False
        return self.get_state(agent_id), ori_reward, float(reward), episode_over, {}

    def reset(self):
        self.time = np.random.randint(0, self.spawn_time, size=(self.X, self.Y))
        self.maze = np.zeros((len(self.agents)+1, self.X, self.Y))
        for idx, agent in enumerate(self.agents):
            agent.pos = self.init_pos[idx]
            agent.hunger_time = 0
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

        for i in range(self.X):
            for j in range(self.Y):
                # agent on top of this position
                if self._producible(i,j):
                    self.time[i][j] = (self.time[i][j]+1)%self.spawn_time
                    if self.time[i][j] == 0:
                        self.maze[tot][i][j] = 1

        # if there is agent, the fruit will be dead
        for agent in self.agents:
            x, y = agent.pos
            self.maze[tot][x][y] = 0

    def _producible(self, x, y):
        return abs(x-self.X//2) + abs(y-self.Y//2) < self.X//2

    def _out_of_bound(self, x, y):
        return x < 0 or y < 0 or x >= self.X or y >= self.Y

    def get_state(self, agent_id):
        # ret = np.concatenate([self.maze.flatten(),
        #     [self.agents[agent_id].hunger_time]])
        ret = np.concatenate([self.maze.flatten(), 
            [self.agents[agent_id].get_I(self.window_size, agent_id)]])
        return copy.deepcopy(ret)

    def _print_maze(self):
        print(self.maze)

    def visualize(self):
        ret = np.zeros((self.X,self.Y))
        tot = len(self.agents)
        print("=======")

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
        print("=======")
        return ret
