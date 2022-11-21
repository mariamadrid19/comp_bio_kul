generation = 0
popSize = 1
maxGenerations = 150
growthRate = 1
mass_bacterium = 10E-12
population_mass = popSize * mass_bacterium
mass_earth = 6E27

#Alter the code to output after how many generations the population is heavier than the earth
while population_mass < mass_earth:
  print(population_mass)
  popSize += popSize * growthRate
  population_mass = popSize * mass_bacterium
  generation = generation + 1

print("It took", generation, "generations for the population to reach the mass of the Earth.")


import matplotlib.pyplot as plt
import numpy as np

generation_2 = 0
popSize_2 = 1
maxGenerations_2 = 150
growthRate_2 = 1

initial_gen_size = np.array([[generation_2],[popSize_2]])

while generation_2 < maxGenerations_2:
  print(popSize_2)
  popSize_2 += growthRate_2 * popSize_2
  generation_2 = generation_2 + 1
  initial_gen_size = np.append(initial_gen_size, [[generation_2],[popSize_2]], axis=0)

plt.plot(initial_gen_size[:,0], initial_gen_size[:,1])
plt.xlabel("Generation")
plt.ylabel("Population Size")
plt.show()

#Implement a carrying capacity of 1,000 individuals. How long does it take for the population to reach this carrying capacity?
import numpy as np
import matplotlib.pyplot as plt

generation = 0
popSize = 10
maxGenerations = 50
growthRate = 0.1
carrying_capacity = 1000
data = np.array([[generation, popSize]])

while generation < maxGenerations:
  print(popSize)
  popSize += growthRate * popSize * (1 - popSize / carrying_capacity)
  generation = generation + 1
  data = np.append(data, [[generation, popSize]], axis=0)

plt.plot(data[:,0], data[:,1])
plt.xlabel("generation")
plt.ylabel("population size")
plt.show()

#Implement a carrying capacity and modify growth rate. 
#Create a function that allows to input a specific growth rate and outputs a plot of the population size over generations.
def plot_population(growth_rate):
  import numpy as np
  import matplotlib.pyplot as plt
  generation = 0
  popSize = 10
  maxGenerations = 50
  carrying_capacity = 1000
  initial_pop_size = np.array([[generation, popSize]])

  while generation < maxGenerations:
    popSize += round(growth_rate * popSize * (1 - popSize / carrying_capacity))
    generation = generation + 1
    initial_pop_size = np.append(initial_pop_size, [[generation, popSize]], axis=0)

  plt.plot(initial_pop_size[:,0], initial_pop_size[:,1])
  plt.xlabel("Generation")
  plt.ylabel("Population size")
  plt.show()

plot_population(0.1)
plot_population(0.5)
plot_population(1.0)
plot_population(1.5)
plot_population(1.8)
plot_population(2.0)
plot_population(2.5)

#subplot function, matplotlib.pyplot

#Stochastic model of population growth where every individual randomly has either 0 or 1 offspring
import random
import numpy as np
import matplotlib.pyplot as plt
generation = 0
popSize = 10
maxGenerations = 50
carrying_capacity = 100
initial_pop_size = np.array([[generation, popSize]])

while generation < maxGenerations:
    random_growth_rate = random.randint(0,1)
    print(random_growth_rate)
    for i in range(popSize):
        total_offspring = popSize * random_growth_rate
    popSize += round(total_offspring * (1 - popSize / carrying_capacity))
    generation = generation + 1
    initial_pop_size = np.append(initial_pop_size, [[generation, popSize]], axis=0)

plt.plot(initial_pop_size[:,0], initial_pop_size[:,1])
plt.xlabel("Generation")
plt.ylabel("Population size")
plt.show()