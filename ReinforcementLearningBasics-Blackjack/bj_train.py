## BLACK JACK TRAIN

# import libraries
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray


def main():
    # set env
    env = gym.make('Blackjack-v1', natural=False, sab=False) # setup doesn't pay extra per natural BJ 
    env.reset()
    done = False

