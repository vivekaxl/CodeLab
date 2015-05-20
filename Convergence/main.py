from __future__ import division
from individual import individual
from random import random, choice, uniform
from math import fabs


MIN = 1
MAX = 1000
def generate_population(number = 100):
    assert(number > 0), "Population needs to be greater than 0"
    population = {}
    for _ in xrange(number):
        pop = individual([uniform(1, MAX) for _ in xrange(2)])
        population[pop.id] = pop
    return population

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance


# approximation
def convex_hull(individual, population, radius = 0.05 * MAX):
    origin = individual.decision
    neighbourhood = []
    for key in population.keys():
        pop = population[key]
        pop.distance = euclidean_distance(origin, pop.decision)

    for key in population.keys():
        pop = population[key]
        if pop.distance <= radius and pop.id != individual.id:
            # print pop.distance, radius
            neighbourhood.append(pop)
    # print "Length: ", len(neighbourhood)
    return neighbourhood


def push_neighbor(pushed, pole, nudge_ratio = 0.05):
    assert(len(pushed.decision) == len(pole.decision)), "Something is wrong"
    # 10% push towards pole - neighbour
    # rand() push towards pole - center
    # print "B: ", pushed.decision
    for i, p in enumerate(pushed.decision):
        pushed.decision[i] = abs((pushed.decision[i] + pole.decision[i]) * (1 - nudge_ratio))%MAX
    # print "A: ", pushed.decision
    return pushed


import matplotlib.pyplot as plt
def main_loop():
    population = generate_population()
    import pylab
    pylab.ion()       # Turn on interactive mode.
    pylab.hold(False) # Clear the plot before adding new data.
    count = 0
    while True:
        count += 1
        for key in population.keys():
            pop = population[key]
            neighborhood = convex_hull(pop, population)
            neighborhood = [push_neighbor(neigh, pop) for neigh in neighborhood]
            if len(neighborhood) == 0: continue
            random_direction = choice(neighborhood)
            population[pop.id] = push_neighbor(pop, random_direction, 0.1 + random())
            for neigh in neighborhood:
                population[neigh.id] = (neigh)
        if count % 5 == 0:
            x = []
            y = []
            for key in population.keys():
                pop = population[key].decision
                x.append(pop[0])
                y.append(pop[1])
            pylab.scatter(x, y)
            pylab.draw()
            print "There"



if __name__ == "__main__":
    main_loop()









