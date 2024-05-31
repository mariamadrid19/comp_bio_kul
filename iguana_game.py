from asyncore import read
import numpy as np
import os

# The random_seed is set to 0 to always have the same result
np.random.seed(0)


# This makes sure that the files are generated in the same folder as the script
os.chdir(os.path.dirname(os.path.realpath("Assignment_2(1).py")))


# Write a function that generates a random integer between - 2 and 2 a certain amount of times (8 times)
# the function should return each time a .txt file with the array of dives e.g. [ -1, 2, -2, -1, 0, 1 ]
# and with file name iguana_dives_day_1.txt, iguana_dives_day_2.txt, ...
# Write your generate_dive_arrays function here below

def generate_dive_arrays(n_trial, n_files):
    for i in range(1, n_files + 1):
        dives = np.random.randint(-2, 2, n_trial)
        file_name = F"iguana_dives_day_{i}.txt"
        with open(file_name, "w") as f:
            f.write(",".join(dives.astype(str)))

# This function should return True if there is never three consecutive dives below the surface and False if there is
def diving_mini_game(array):
    breath = 3

    for i in array:
        if i < 0:
            breath -= 1
        else:
            breath = 3

        if breath <= 0:
            return False
    return True

# The code below should store the data of day 7 in a variable and print if the iguana will survive or not (TRUE or FALSE) on that day
# Optional: Instead of True and False print that the iguana survived on that day etc.

def read_iguana_dive(day_dive_x):
    # read the file and convert the string to an array
    with open(day_dive_x, "r") as f:
        dives = f.read().split(",")
        dives = [int(i) for i in dives if i != ""]
    # check if the iguana survives
    return dives

# Once you have written the function to generate the files you can uncomment the code below
generate_dive_arrays(8,10)

# Here below you should call the function read_iguana_dive() and store the output in a variable called day_7
day_7 = read_iguana_dive("iguana_dives_day_7.txt")
diving_mini_game(day_7)

day_1 = read_iguana_dive("iguana_dives_day_1.txt")
day_2 = read_iguana_dive("iguana_dives_day_2.txt")
day_3 = read_iguana_dive("iguana_dives_day_3.txt")
day_4 = read_iguana_dive("iguana_dives_day_4.txt")
day_5 = read_iguana_dive("iguana_dives_day_5.txt")
day_6 = read_iguana_dive("iguana_dives_day_6.txt")
day_8 = read_iguana_dive("iguana_dives_day_8.txt")
day_9 = read_iguana_dive("iguana_dives_day_9.txt")
day_10 = read_iguana_dive("iguana_dives_day_10.txt")

# Here you can remove the comment below and check if the iguana survives on day 7
def iguana_lives_or_dies(day):
    array_of_days = [day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9, day_10]
    if diving_mini_game(day) == True:
        print("The iguana survived on day " + str(array_of_days.index(day) + 1))
    else:
        print("The iguana died on day " + str(array_of_days.index(day) + 1))

# Check if the iguana survives on other days as well and make a statement like the one above if the iguana dies
iguana_lives_or_dies(day_1)
iguana_lives_or_dies(day_2)
iguana_lives_or_dies(day_3)
iguana_lives_or_dies(day_4)
iguana_lives_or_dies(day_5)
iguana_lives_or_dies(day_6)
iguana_lives_or_dies(day_7)
iguana_lives_or_dies(day_8)
iguana_lives_or_dies(day_9)
iguana_lives_or_dies(day_10)
