import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# EXERCISE 2:
# Here below there is a toy dataset 'x' that only includes the motion_mode colums (-1 for reversing, 0 for stationary, 1 for moving forward)
x = np.array([0, 1, -1, -1, -1, 0, 0, -1, -1, 0])
print(x)

#create two new arrays: one that saves all the indices where the worm starts reversing, and one that saves the indices where it stops reversing
#print the values of these two new arrays and inspect if your algorithm identified the starts and the stops correctly

#find the indices where the worm starts reversing
reversing = np.where(x == -1)
print(reversing)

#find the indices where the worm stops reversing (either because it starts moving forward or because it is stationary)
starting = np.where(x >= 0)
print(starting)

# Now let's do the same thing, but for one of the actual worms. Read the data in again.
# Start with creating a new 'trimmed' dataframe that contains only the frames right before, during, and after the stimulus.
# The stimulus occurs from 610 to 660 frames - in your trimmed dataframe, include up to 50 frames before and after the stimulus.
# Also include only the data for the worm with the unique_worm_id equal to 5

os.chdir(os.path.dirname(os.path.realpath("Dataset.csv")))
df = pd.read_csv("Dataset.csv")
print(df.head())
df_worm_5 = df[df["unique_worm_id"] == 5]
print(df_worm_5)
df_trimmed_worm_5 = df_worm_5[(df_worm_5["timestamp"] >= 560) & (df_worm_5["timestamp"] <= 710)]
print(df_trimmed_worm_5)

# now, using the code you made above for the toy example, extract all the start time and stop times of the reversals for this worm.
# also save the x and y coordinates of these moments 
stop = df_trimmed_worm_5.query("motion_mode == 0")
print(stop)
stop_times_coordinates = stop.filter(['timestamp', 'coord_x', 'coord_y'])
print(stop_times_coordinates)

start = df_trimmed_worm_5.query("motion_mode == -1" or "motion_mode == 1")
print(start)
start_times_coordinates = start.filter(['timestamp', 'coord_x', 'coord_y'])
print(start_times_coordinates)

#########################################################################################################################################

# EXERCISE 3:
# How many reversal bouts were there for worm 5?
reversal = start.query("motion_mode == -1")
print(reversal)
reversal_bouts = reversal.count()
print(reversal_bouts)

# How long were the reversal bouts of worm 5?
# Hint: you can use the function np.diff() to calculate the difference between two consecutive values in an array
#The reversal bouts of worm 5 were 0.7 seconds long


# How far did the worm move (euclidean distance) during each of its reversal bouts?
# Googling should help with finding out how to do this
def calculate_euc_distance(df, start, end):
    #print(f"start: {start}, end: {end}")
    timestamp_1 = df.query("timestamp == " + str(start))
    timestamp_2 = df.query("timestamp == " + str(end))

    x_timestamp_1 = timestamp_1.iloc[0]["coord_x"]
    y_timestamp_1 = timestamp_1.iloc[0]['coord_y']

    x_timestamp_2 = timestamp_2.iloc[0]["coord_x"]
    y_timestamp_2 = timestamp_2.iloc[0]['coord_y']

    x_distance = abs(x_timestamp_2 - x_timestamp_1)
    y_distance = abs(y_timestamp_2 - y_timestamp_1)
    distance = np.sqrt(x_distance**2 + y_distance**2)

    return distance

# print(calculate_euc_distance(reversal, 607, 613))
# print(calculate_euc_distance(reversal, 662, 667))

def swap(arr1, arr2):
    temp = arr1[:]
    arr1[1] = arr2[1]
    arr2[1] = temp[1] 

    return arr1, arr2


def calculate_start_end(df):
    start_end = []
    final = []
    # consecutive timestamps
    for i in range(0, len(df)):
        if df['timestamp'].iloc[i] - df['timestamp'].iloc[i-1] != 1:
            start_end.append([df['timestamp'].iloc[i], df['timestamp'].iloc[i-1]])

    if len(start_end) > 1:
        for i in range(0, len(start_end)-1):
            final.append(swap(start_end[i], start_end[i+1]))
    else:
        final = start_end

    return final

print(calculate_start_end(reversal))

def calculate_reversal_events(df):
    events_dict = {}
    reversal_events = []
    unique_values = (df['unique_worm_id'].unique())
    print("worm ids: " + str(unique_values))

    for worm in unique_values:
        worm_i = df[(df["unique_worm_id"] == worm) & ((df["timestamp"] >= 560) & (df["timestamp"] <= 710))]
        reversal = worm_i.query("motion_mode == -1")
        reversal_bouts = reversal.shape[0] #This gives the number of rows for the the dataframe generated before
        len_reversal_bouts = []
        start_and_end = calculate_start_end(reversal)
        distances = []

        for pair in start_and_end:
            shp = np.array(pair).shape
            # print(f"shape of pair: {shp}")
            # print(f"worm: {worm}, pair: {pair}")

            if len(shp) < 2:
                distances.append(calculate_euc_distance(reversal, pair[0], pair[1]))
                len_reversal_bouts.append(((pair[1] - pair[0]) + 1) / 10) # +1 because the difference between the timestamps is 1 less than the number of frames
            else:
                distances.append(calculate_euc_distance(reversal, pair[0][0], pair[0][1]))
                len_reversal_bouts.append(((pair[0][1] - pair[0][0]) + 1) / 10)
                distances.append(calculate_euc_distance(reversal, pair[1][0], pair[1][1]))
                len_reversal_bouts.append(((pair[1][1] - pair[1][0]) + 1) / 10)

        
        reversal_events.append([reversal_bouts] + [len_reversal_bouts] + [distances])

    for key, value in zip(unique_values, reversal_events):
        events_dict[f"Worm {key}"] = value
        
    return events_dict

print(calculate_reversal_events(df))
