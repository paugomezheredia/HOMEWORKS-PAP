import gymnasium as gym

def blackjack_env():
    env = gym.make('Blackjack-v1', natural=False, sab=False)
    return env
