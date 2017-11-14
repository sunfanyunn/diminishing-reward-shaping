# -*- coding: utf-8 -*-
import random
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.layers.convolutional import Conv2D
from keras.layers.core import Dense, Dropout, Activation, Flatten


dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
label2action = {'up': 0, 'down': 1, 'left': 2, 'right': 3, 'still': 4}
action2label = {0: 'up', 1: 'down', 2: 'left', 3: 'right',4: 'still'}

class DQNAgent:
    def __init__(self, action_size, x0, y0, input_dim):
        self._pos = (x0, y0)
        self.hunger_time = 0
        self.action_size = action_size
        self.history = []

        self.memory = deque(maxlen=20000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.99
        self.learning_rate = 0.001
        self.model = self._build_model(input_dim)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    def move(self, action):
        x, y = self.pos
        self.pos = (x + dx[action], y + dy[action])
        return self.pos

    def _build_model(self, input_dim):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(32, activation='relu', input_shape=(input_dim,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate, clipnorm=1))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = np.reshape(state, (1,)+state.shape)
        act_values = self.model.predict(state, verbose=0)
        return np.argmax(act_values[0]) # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:

            state = np.reshape(state, (1,)+state.shape)
            next_state = np.reshape(next_state, (1,)+next_state.shape)

            target = reward
            if not done:
                target = reward + self.gamma * \
                np.amax(np.clip(self.model.predict(next_state)[0], -1, 1))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def get_I(self, window_size, agent_id):
        t = len(self.history)%(agent_id+1)
        tt = window_size * (agent_id + 1)
        if t > 0:
            return sum(self.history[-tt-t:-t])
        else:
            return sum(self.history[-tt:])

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)
