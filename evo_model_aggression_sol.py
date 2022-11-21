import numpy as np
import matplotlib.pyplot as plt


###############
### GLOBALS ###
###############

popsize = 1000      # population size
gen_number = 50         # number of generations that the code is run for
mutprob = 0.01      # the probability that a mutation occurs
freq_aggressivness = 0.01 # initial frequency of aggresive individuals

# create a class called 'individual'
class Individual:
    def __init__(self, mybehaviour):
        self.behaviour = mybehaviour
        self.fitness = 2
    def calculate_fitness(self, behaviour_partner):
        if(self.behaviour == 0):
            if(behaviour_partner == 0):
                self.fitness += 1
            else:
                self.fitness += 0
        else:
            if(behaviour_partner == 0):
                self.fitness += 2
            else:
                self.fitness -= 2
    def calculate_relative_fitness(self, totalFitness):
        self.relativeFitness = self.fitness/totalFitness

# create an array that we will use to save the average length over evolutionary time
data = np.empty(gen_number)

# create an empty population
pop = np.empty(popsize, dtype=object)


#############################
### INITIALIZE POPULATION ###
#############################

# add individuals to the population according to the initial frequency of aggressivness
for i in range(popsize):
    if i < popsize * freq_aggressivness:
        pop[i] =  Individual(1)
    else:
        pop[i] = Individual(0)


######################
### RUN SIMULATION ###
######################

# run our evolutionary simulation for 'numgen' generations
for j in range(gen_number):
    
    # record the average length in this generation in the array 'data' (for plotting at the end)
    data[j] = np.mean([ind.length for ind in pop])

    [ind.calculate_fitness(pop[np.random.randint(popsize)].behaviour) for ind in pop]

    # calculate the relative fitnesses of each individual (so they all add up to 1)
    [ind.calculate_relative_fitness(np.sum([ind.fitness for ind in pop])) for ind in pop]

    # draw all parents by drawing popsize numbers from 0 to popsize with probabilities given by the relative fitnesses
    parents = np.random.choice(popsize, popsize, p=[ind.relativeFitness for ind in pop])

    # create an empty array to store the next generation
    newpop = np.empty(popsize, dtype=object)

    for i in range(popsize):
        # with probability 'mut_prob', a mutation occurs.
        # otherwise the individual simply inherits the length of the parent
        if(np.random.uniform() < mutprob):
            newpop[i] = Individual(pop[parents[i]].length + np.random.normal(scale=0.1))
        else:
            newpop[i] = Individual(pop[parents[i]].length)

        #copy the new population into the old one
        pop[i] = newpop[i] 


###################
### PLOT OUTPUT ###
###################

plt.plot(range(gen_number), data)
plt.show()