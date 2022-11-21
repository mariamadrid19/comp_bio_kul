import numpy as np
import matplotlib.pyplot as plt
import random

popsize = 1000
sigma = 2

def calculate_fitness(length):
    return np.exp(-((length - 10)**2)/(2*sigma**2))

#create an empty population
pop = np.empty((popsize,2))
print(pop)

#add 10 individuals to the population with random length and calculate their fitness
for i in range(popsize):
    pop[i,0] = np.random.normal(loc=7.0, scale=1.0)
    pop[i,1] = calculate_fitness(pop[i,0])

np.set_printoptions(suppress=True) #this is to make sure that the print of the array doesn't use scientific notation
print(pop)

fitness = pop[:,1]
print(fitness)

cumulative_fitness = np.empty((0,10))
cumulfit = 0

for i, fit in enumerate(fitness):
    cumulfit += fit
    cumulative_fitness = np.append(cumulative_fitness, cumulfit)

pick = np.random.uniform(high=cumulfit)

parent = 0
while pick > cumulative_fitness[parent]:
    parent += 1

print("inidividual " + str(parent) + " will reproduce (fitness: " + str(fitness[parent]) + ")")


#Create a loop to build the new generation. 
#It should have the same size as the parent generation. 
#For each new individual, first select a parent proportional to fitness (the model is asexual)
new_generation=np.empty((popsize,2))
print(new_generation)

for i in range(popsize):
    pick = np.random.uniform(high=cumulfit)
    parent = 0
    while pick > cumulative_fitness[parent]:
        parent += 1
    new_generation[i,0] = pop[parent,0] + np.random.normal(loc=0.0, scale=0.1)
    new_generation[i,1] = calculate_fitness(new_generation[i,0])
print(pop)
print(new_generation)

#Implement sexual reproduction. 
#Select two parents for each individual, with the offspring length the average of their parents, plus some variation.for i in range(popsize):
#for i in range(popsize):
#    parent1 = 0
#    parent2 = 0
#    while pick > cumulative_fitness[parent1, parent2]:
#        parent1 += 1
#        parent2 += 1
#    new_generation[i,0] = pop[parent,0] + np.random.normal(loc=0.0, scale=0.1)
#    new_generation[i,1] = calculate_fitness(new_generation[parent,1])
#    print(new_generation)

#Write a loop that repeats this process for many generations. 
#Use the new population after selection as the starting point for the next generation

# population = new_generation
population_1 = new_generation
print(population_1)
max_gen = 100
gen = 0
data = np.empty((max_gen,2))
print("--")
print(data)

for j in range(max_gen):
    population_0 = population_1

    fitness = population_0[:,1]

    cumulative_fitness = np.empty((0,10))
    cumulfit = 0

    for i, fit in enumerate(fitness):
        cumulfit += fit
        cumulative_fitness = np.append(cumulative_fitness, cumulfit)

    for i in range(popsize):
        pick = np.random.uniform(high=cumulfit)
        parent = 0
        while pick > cumulative_fitness[parent]:
            parent += 1
        # population[i,0] = pop[parent,0] + np.random.normal(loc=0.0, scale=0.1)
        # population[i,1] = calculate_fitness(population[i,0])
        population_1[i,0] = population_0[parent,0] + np.random.normal(loc=0.0, scale=0.1)
        population_1[i,1] = calculate_fitness(population_1[i,0])
    gen = gen + 1
    data[j,0] = np.mean(population_1[:,0])
    data[j,1] = gen

print(population_1)
print(data)

plt.scatter(data[:,1], data[:,0])
plt.show()
