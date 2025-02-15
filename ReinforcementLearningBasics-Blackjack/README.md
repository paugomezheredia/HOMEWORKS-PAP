# Reinforcement Learning Basics
First Homework _Reinforcement Learning Basics - Blackjack_ Folder contains the implementation of a Deep Q-Learning (DQL) agent trained to play Blackjack. The project works with fundamental concepts of Reinforcement Learning (RL), including environment interaction, experience replay, and neural network-based Q-value approximation.

The DQL agent learns to play Blackjack using:

- Environment: The agent interacts with the OpenAI Gym Blackjack environment.
- State Representation: Encodes game state, including player’s hand, dealer’s visible card, and use of an ace.
- Action Space: The agent can choose to hit (draw a card) or stand (end turn).
- Reward System: Positive reward for winning, negative for losing, and zero for draws.
- Deep Q-Network (DQN): A neural network approximates the Q-values for state-action pairs.
- Experience Replay: Stores experiences to improve learning stability.
- Exploration vs Exploitation: Uses an epsilon-greedy policy to balance exploration and exploitation.

## Results: 
Initial State: (state details)
Action: Hit, Next State: (next state details), Reward: 0, Done: False
Action: Stick, Next State: (next state details), Reward: 1, Done: True
Episode finished with total reward: 1

- **Game 1**:
Initial State: (16, 7, 0)
Action: Stick, Next State: (16, 7, 0), Reward: -1.0, Done: True
Episode finished with total reward: -1.0
![image](imagenes\result-1-figure.png)

- **Game 2**:
Initial State: (20, 10, 0)
Action: Hit, Next State: (30, 10, 0), Reward: -1.0, Done: True
Episode finished with total reward: -1.0
![image](imagenes\result-2-figure.png)

- **Game 3**:
Initial State: (17, 10, 0)
Action: Hit, Next State: (19, 10, 0), Reward: 0.0, Done: False
Action: Stick, Next State: (19, 10, 0), Reward: 1.0, Done: True
Episode finished with total reward: 1
![image](imagenes\result-3-figure.png)