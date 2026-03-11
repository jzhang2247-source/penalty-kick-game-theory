import numpy as np
import random

payoff = np.array([
    [0.60,0.95,0.90],
    [0.85,0.55,0.85],
    [0.92,0.94,0.58]
])

kicker_strategy = [0.4,0.2,0.4]
goalkeeper_strategy = [0.35,0.3,0.35]


def simulate(n=10000):

    goals = 0

    for _ in range(n):

        kick = np.random.choice([0,1,2],p=kicker_strategy)
        dive = np.random.choice([0,1,2],p=goalkeeper_strategy)

        prob = payoff[kick][dive]

        if random.random() < prob:
            goals += 1

    return goals/n


if __name__ == "__main__":

    rate = simulate()

    print("Average scoring probability:",round(rate,3))
