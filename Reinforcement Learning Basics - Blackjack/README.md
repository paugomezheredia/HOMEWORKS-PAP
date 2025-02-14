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

![image](https://github.com/user-attachments/assets/6409ef88-6510-492b-9e5b-8b6f5f15304f)
