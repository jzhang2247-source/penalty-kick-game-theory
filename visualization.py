import matplotlib.pyplot as plt

actions = ["Left","Center","Right"]

kicker_strategy = [0.4,0.2,0.4]

plt.bar(actions,kicker_strategy)

plt.title("Optimal Penalty Kick Strategy")
plt.ylabel("Probability")

plt.show()
