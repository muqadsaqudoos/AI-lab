import random

items = [(2, 10), (5, 20), (10, 30), (5, 25)]
weight_limit = 15

def initialize_knapsack_population(pop_size, num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(pop_size)]

def knapsack_fitness(chromosome):
    total_weight = sum(items[i][0] for i in range(len(chromosome)) if chromosome[i] == 1)
    total_value = sum(items[i][1] for i in range(len(chromosome)) if chromosome[i] == 1)
    return total_value if total_weight <= weight_limit else 0

def select_knapsack_parents(population):
    fitness_values = [knapsack_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, probabilities, k=2)

def single_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def bit_flip_mutate(chromosome):
    index = random.randint(0, len(chromosome) - 1)
    chromosome[index] = 1 - chromosome[index]

def genetic_algorithm_knapsack(pop_size, num_generations):
    population = initialize_knapsack_population(pop_size, len(items))
    for _ in range(num_generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_knapsack_parents(population)
            child1, child2 = single_point_crossover(parent1, parent2)
            bit_flip_mutate(child1)
            bit_flip_mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_solution = max(population, key=knapsack_fitness)
    return best_solution, knapsack_fitness(best_solution)

best_solution, best_value = genetic_algorithm_knapsack(pop_size=10, num_generations=100)
print("Best knapsack solution:", best_solution)
print("Best total value:", best_value)
