import random

def initialize_population(pop_size, string_length):
    return [''.join(random.choice('01') for _ in range(string_length)) for _ in range(pop_size)]

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parent1 = random.choices(population, weights=probabilities, k=1)[0]
    parent2 = random.choices(population, weights=probabilities, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

def mutate(individual, mutation_rate):
    mutated = ''.join(
        char if random.random() > mutation_rate else '1' if char == '0' else '0'
        for char in individual
    )
    return mutated

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(individual) for individual in population]
        max_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(max_fitness)]
        print(f"Generation {generation}: Best Fitness = {max_fitness}, Best Individual = {best_individual}")

        if max_fitness == string_length:
            print("Optimal solution found!")
            return best_individual
        
        new_population = []
        while len(new_population) < pop_size:
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.append(mutate(offspring1, mutation_rate))
            if len(new_population) < pop_size:
                new_population.append(mutate(offspring2, mutation_rate))
        population = new_population
    fitness_scores = [calculate_fitness(individual) for individual in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    print("Maximum generations reached. Best solution found:")
    return best_individual

def main():
    string_length = 10
    pop_size = 20
    num_generations = 100
    mutation_rate = 0.05
    result = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print(f"Final Solution: {result}, Fitness: {result.count('1')}")
main()