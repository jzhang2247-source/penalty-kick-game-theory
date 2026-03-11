import numpy as np
from scipy.optimize import linprog

# Payoff matrix
# rows = kicker actions
# cols = goalkeeper actions

payoff = np.array([
    [0.60, 0.95, 0.90],  # Kick Left
    [0.85, 0.55, 0.85],  # Kick Center
    [0.92, 0.94, 0.58]   # Kick Right
])


def solve_nash_equilibrium(matrix):

    n = matrix.shape[0]

    # Linear programming formulation
    c = [-1] + [0]*n

    A_ub = []
    b_ub = []

    for j in range(n):
        constraint = [1] + [-matrix[i][j] for i in range(n)]
        A_ub.append(constraint)
        b_ub.append(0)

    A_eq = [[0] + [1]*n]
    b_eq = [1]

    bounds = [(None, None)] + [(0,1)]*n

    result = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds
    )

    strategy = result.x[1:]

    return strategy


if __name__ == "__main__":

    strategy = solve_nash_equilibrium(payoff)

    actions = ["Left","Center","Right"]

    print("Optimal Kicker Strategy")
    print("-----------------------")

    for a,p in zip(actions,strategy):
        print(f"{a}: {p:.3f}")
