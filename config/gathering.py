import argparse
def parse_arguments():
    argparser = argparse.ArgumentParser(description='RL Gathering Game')
    argparser.add_argument('-agents', '--agents', type=int, default=2)
    argparser.add_argument('-adjustment', '--adjustment', type=str, default='default')
    argparser.add_argument('-lte', '--load_trained_epoch', type=int, default=200)
    argparser.add_argument('-to', '--train_episodes', type=int, default=500)
    argparser.add_argument('-st', '--spawn_time', type=int, default=5)
    argparser.add_argument('-ms', '--map_size', type=int, default=5)
    argparser.add_argument('-bs', '--batch_size', type=int, default=1000)
    argparser.add_argument('-ie', '--info_epoch', type=int, default=50)
    argparser.add_argument('-thresh', '--thresh', type=float, default=1)
    return argparser.parse_args()

args = parse_arguments()
print(args)
#####
# action
#####
label2action = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
action2label = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}

####
# global parameters 
####
num_agents = args.agents
tpe = args.adjustment
batch_size = args.batch_size
EPISODES = args.train_episodes
info_epoch = args.info_epoch
data_dir = '_'.join([str(num_agents), tpe, str(args.thresh)])

window_size = 5
thresh = args.thresh

######
# game parameters
######
spawn_time = args.spawn_time
round_per_game = 1000
action_size = 4
X = Y = args.map_size
init_pos = [(0,0), (X-1, Y-1), (0,Y-1), (X-1, 0)]

input_dim = (num_agents+1)*X*Y +  1
def init():
    from core.dqn import DQNAgent
    agents = [DQNAgent(action_size, init_pos[i][0], init_pos[i][1], input_dim) for i in range(num_agents)]
    from envs.gathering import MazeEnv
    env = MazeEnv(X, Y, spawn_time, agents, tpe, window_size, thresh)
    return agents, env
