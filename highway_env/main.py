from highway_env.envs.nicola_custom_env import *
from highway_env.envs.racetrack_env import *
from stable_baselines3 import DQN
import matplotlib.pyplot as plt

# Environment
import gymnasium as gym
import highway_env

# Visualization utils
import sys

model = DQN('MlpPolicy', 'nicola_custom_env-v0',
            policy_kwargs=dict(net_arch=[256, 256]),
            learning_rate=5e-4,
            buffer_size=15000,
            learning_starts=200,
            batch_size=32,
            gamma=0.8,
            train_freq=1,
            target_update_interval=50,
            exploration_fraction=0.7,
            verbose=1)

model.learn(int(2e4))

print(gym.envs.registry)
print("trest")

rt_y = gym.make('nicola_custom_env-v0', render_mode="human")
obs, info = rt_y.reset()
print(rt_y.action_space)

for i in range(1000):
    obs, reward, terminated, truncated, info = rt_y.step([-1])

# %%
