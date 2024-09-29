import pandas as pd
import numpy as np
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt

DF_SIZE = 30 # define size of square dataframe
SLEEP_TIME = 1 # define sleep time in seconds

# count iterations
num_generations = 0

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

while True:
    print(datetime.now())
    print(f"Generation {num_generations}")
    print(df)
    plt.imshow(df, cmap='binary')
    plt.title(f"Generation {num_generations}")
    plt.show()
    df = update(df)
    num_generations += 1
    sleep(SLEEP_TIME)