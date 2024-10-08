import pandas as pd
import numpy as np
from time import sleep
from datetime import datetime
#import matplotlib.pyplot as plt

DF_SIZE = 40 # define size of square dataframe
SLEEP_TIME = 0 # define sleep time in seconds - don't bother sleeping because it's already slow

# count iterations
num_generations = 0

# figure out if game has "stabilized" - if the game has kept the same number of cells for MAX_STABILIZED generations, then end the game
# this might never happen, because sometimes cells can keep bouncing back and forth
MAX_STABILIZED = 10
cell_history = []

# create a dataframe with random 1s and 0s based on PD_SIZE
df = pd.DataFrame(np.random.randint(0, 2, size=(DF_SIZE, DF_SIZE)))

def update_cell(df, row, col):
    neighbors = df.iloc[max(0, row - 1):min(DF_SIZE, row + 2), max(0, col - 1):min(DF_SIZE, col + 2)].values.flatten()
    neighbors_sum = np.sum(neighbors)
    if df.iloc[row, col] == 1:
        if neighbors_sum < 2 or neighbors_sum > 3:
            return 0
    else:
        if neighbors_sum == 3:
            return 1
    return df.iloc[row, col]

def update(orig_df):
    updated_df = orig_df.copy()
    for row in range(DF_SIZE):
        for col in range(DF_SIZE):
            updated_df.iloc[row, col] = update_cell(orig_df, row, col)
    return updated_df

def render_df(df):
    rendered_df = df.copy()
    rendered_df = rendered_df.replace({1: 'X', 0: ' '})
    return rendered_df

while True:
    print(datetime.now())
    print(f"Generation {num_generations}")
    live_cells = np.sum(df.values)
    print(f"Number of live cells: {live_cells}")
    print(render_df(df).to_string(index=False, header=False))
    cell_history.append(live_cells)

    if len(cell_history) > MAX_STABILIZED:
        #print(cell_history)
        #print(len(cell_history))
        if len(set(cell_history[-MAX_STABILIZED:])) == 1:
            print(f"Game stabilized after {num_generations} generations.")
            break  # Exit the loop if stabilized  
        cell_history.pop(0) # remove first item to prevent from growing indefinitely
    #plt.imshow(df, cmap='binary')
    #plt.title(f"Generation {num_generations}")
    #plt.show()
    df = update(df)
    num_generations += 1
    sleep(SLEEP_TIME)