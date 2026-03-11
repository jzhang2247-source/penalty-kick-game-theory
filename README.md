# Penalty Kick Strategy with Game Theory

This project demonstrates how game theory can be used to
derive optimal strategies for penalty kicks in football.

The model treats the penalty kick as a zero-sum game between:

- Kicker
- Goalkeeper

Using mixed strategy Nash equilibrium, the optimal probability
distribution for each action is computed.

## Features

- Game theory payoff matrix
- Nash equilibrium solver
- Monte Carlo simulation
- Strategy visualization

## Run

Install dependencies:

pip install -r requirements.txt

Solve equilibrium:

python penalty_game.py

Run simulation:

python simulation.py
