import random

distance_matrix = [[0, 2, 9, 10],
                   [1, 0, 6, 4],
                   [15, 7, 0, 8],
                   [6, 3, 12, 0]]

def initialize_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        tour = list(range(num_cities))
        random.shuffle(tour)
        population.append(tour)
    return population

def calculate_distance(tour):
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

def fitness(tour):
    return 1 / calculate_distance(tour)

def select_parents(population):
    fitness_values = [fitness(tour) for tour in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return random.choices(population, probabilities, k=2)

def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    fill_pos = end
    for gene in parent2:
        if gene not in child:
            if fill_pos == size:
                fill_pos = 0
            child[fill_pos] = gene
            fill_pos += 1
    return child

def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm_tsp(pop_size, num_generations):
    population = initialize_population(pop_size, len(distance_matrix))
    for _ in range(num_generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = ordered_crossover(parent1, parent2), ordered_crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_tour = min(population, key=calculate_distance)
    return best_tour, calculate_distance(best_tour)

best_tour, best_distance = genetic_algorithm_tsp(pop_size=10, num_generations=100)
print("Best tour:", best_tour)
print("Best distance:", best_distance)
