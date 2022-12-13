import random
import pandas as pd

data = {}
data['B1'] = [random.randint(0,1) for x in range(200)]
data['B2'] = [random.randint(0,1) for x in range(200)]
data['B3'] = [random.randint(0,1) for x in range(200)]
data['B4'] = [random.randint(0,1) for x in range(200)]
data['B5'] = [random.randint(0,1) for x in range(200)]
data = pd.DataFrame(data)
observations = 200
machines = 5
machine_selected = []
rewards = [0] * machines
penalties = [0] * machines
total_reward = 0
for n in range(0, observations):
    bandit = 0
    beta_max = 0
    for i in range(0, machines):
        beta_d = random.betavariate(rewards[i] + 1, penalties[i] + 1)
        if beta_d > beta_max:
            beta_max = beta_d
            bandit = i
    machine_selected.append(bandit)
    reward = data.values[n, bandit]
    if reward == 1:
        rewards[bandit] = rewards[bandit] + 1
    else:
        penalties[bandit] = penalties[bandit] + 1
    total_reward = total_reward + reward
print("\n\nRewards By Machine = ", rewards)
print("\nTotal Rewards = ", total_reward)
print("\nMachine Selected At Each Round By Thompson Sampling : \n", machine_selected)