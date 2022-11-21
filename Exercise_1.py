#import required packages - pandas, numpy, matplotlib.pyplot, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#this line of code makes sure that you read the file from the same folder that this python file is located in
os.chdir(os.path.dirname(os.path.realpath('Dataset.csv')))

#load the .csv data file as a pandas dataframe 
data = pd.read_csv('Dataset.csv')

#inspect the data (print the first few lines): do you understand what is in all the columns?
print(data.head())

#how many unique worms are in the data? 
#hint: there is a function built in pandas for this - google it
print(len(data['unique_worm_id'].unique()))
unique_values = (data['unique_worm_id'].unique())
print(unique_values)
worm_4 = data[data['unique_worm_id'] == 4]
print(worm_4)

#get a first impression of the data: plot the data with timestamp on x-axis and speed on y-axis
plt.plot(data["timestamp"], data["speed"])
plt.xlabel("Timestamp (s)")
plt.ylabel("Speed (mm/s)")
plt.show()

#EXTRA: try to plot the data as a line for each worm separately in a single graph
#also plot vertical lines in the plot at the time of the start and the end of the stimulus (see slides)
for worm in unique_values:
    worm_i = data[data['unique_worm_id'] == worm]
    plt.plot(worm_i['timestamp'], worm_i['speed'], label = worm)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (mm/s)')
    plt.title('Speed over time for each worm')
plt.show()

