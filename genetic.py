import random
import math
# Size of initial population filled with some permutation of 0s and 1s
POPULATION_SIZE = 50

# Maximum number of generations the algorithm will run
MAX_GENERATION_SIZE = 200

# Start initial population with only zeros? If not, random permutation of 0s and 1s will be given
# Starting with 0s and 1s will generally make you find a good solution faster
START_POP_WITH_ZEROES = False


def fitness(target,capacity,weight_value):
    """
    fitness(target) will return the fitness value of permutation named "target".
    Higher scores are better and are equal to the total value of items in the permutation.
    If total_weight is higher than the capacity, return 0 because the permutation cannot be used.
    """
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:
        if index >= len(weight_value):
            break
        if (i == 1):
            total_value += weight_value[index][1]
            total_weight += weight_value[index][0]
        index += 1

    if total_weight > capacity:
        return 0,0
    else:
        return total_value, total_weight

def spawn_starting_population(length,size):
    return [spawn_individual(length) for x in range(0, size)]


def spawn_individual(length):
    if START_POP_WITH_ZEROES:
        return [random.randint(0, 0) for x in range(0, length)]
    else:
        return [random.randint(0, 1) for x in range(0, length)]


def mutate(target):
    r = random.randint(0, len(target) - 1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1


def evolve_population(pop):
    parent_eligibility = 0.2
    mutation_chance = 0.08
    parent_lottery = 0.05

    parent_length = int(parent_eligibility * len(pop))
    parents = pop[:parent_length]
    nonparents = pop[parent_length:]

    for np in nonparents:
        if parent_lottery > random.random():
            parents.append(np)

    for p in parents:
        if mutation_chance > random.random():
            mutate(p)

    children = []
    desired_length = len(pop) - len(parents)
    while len(children) < desired_length:
        male = pop[random.randint(0, len(parents) - 1)]
        female = pop[random.randint(0, len(parents) - 1)]
        half = math.floor(len(male) / 2)
        child = male[:half] + female[half:]
        if mutation_chance > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents


def genetic_algorithm(number,capacity, weight_value):
    generation = 1
    population = spawn_starting_population(len(weight_value), POPULATION_SIZE)
    best_value=0
    best_combination = []
    for g in range(0, MAX_GENERATION_SIZE):
        #print("Generation %d with %d" % (generation, len(population)))
        population = sorted(population, key=lambda x: x[1], reverse=True)
        for i in population:
            value, weight =fitness(i, capacity, weight_value)
            if (best_value<value):
                best_combination = i
                best_value = value
        population = evolve_population(population)
        generation += 1
    return best_value, best_combination


