## BLACK JACK TRAIN

# import libraries
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from IPython import display
import time

# define function train
def train():
    # set env
    env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode='rgb_array') # setup doesn't pay extra per natural BJ 
    state, info = env.reset()  # reset env get the initial state
    done = False
    reward = 0

    print("Initial State:", state)

    while not done:
        # Render the current state as an image
        img = env.render()
        display.display(display.Image(img))
        display.clear_output(wait=True)  # Clear the previous image
        time.sleep(1)  # Add a delay to make the game visible

        # Sample a random action (0 or 1)
        action = env.action_space.sample()

        # Take the action and observe the result
        next_state, reward, done, truncated, info = env.step(action)

        # Print the step details
        print(f"Action: {'Hit' if action == 1 else 'Stick'}, Next State: {next_state}, Reward: {reward}, Done: {done}")

        # Update the state
        state = next_state

    print(f"Episode finished with total reward: {reward}")

    # Close the environment
    env.close()

# Run the TRAIN function
if __name__ == "__train__":
    train()