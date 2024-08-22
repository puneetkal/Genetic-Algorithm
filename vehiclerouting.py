import numpy as np
import matplotlib.pyplot as plt
import random

# More complex set of locations
locations = np.array([
    [0, 0],    # Depot
    [2, 3],    # Customer 1
    [5, 4],    # Customer 2
    [7, 2],    # Customer 3
    [6, 6],    # Customer 4
    [8, 8],    # Customer 5
    [1, 7],    # Customer 6
    [3, 1],    # Customer 7
    [4, 5],    # Customer 8
    [9, 3],    # Customer 9
    [10, 7],   # Customer 10
])

# Number of locations
num_locations = len(locations)

# Distance matrix calculation
def distance_matrix(locations):
    num_locations = len(locations)
    dist_matrix = np.zeros((num_locations, num_locations))
    for i in range(num_locations):
        for j in range(num_locations):
            dist_matrix[i, j] = np.linalg.norm(locations[i] - locations[j])
    return dist_matrix

# Generate a random individual (route)
def generate_route(num_locations):
    return list(range(num_locations))

def create_population(size, num_locations):
    population = []
    for _ in range(size):
        route = generate_route(num_locations)
        random.shuffle(route)
        population.append(route)
    return population

def fitness(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end] = parent1[start:end]
    current_pos = end
    for city in parent2:
        if city not in child:
            if current_pos >= size:
                current_pos = 0
            child[current_pos] = city
            current_pos += 1
    return child

def genetic_algorithm(locations, population_size, generations, elitism_size):
    dist_matrix = distance_matrix(locations)
    population = create_population(population_size, len(locations))
    best_route = min(population, key=lambda r: fitness(r, dist_matrix))
    best_distance = fitness(best_route, dist_matrix)

    for _ in range(generations):
        # Sort population by fitness
        population = sorted(population, key=lambda r: fitness(r, dist_matrix))
        
        # Elitism: preserve the top solutions
        new_population = population[:elitism_size]
        
        # Generate new individuals
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:population_size // 2], 2)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        
        population = new_population[:population_size]  # Trim to the population size
        current_best = min(population, key=lambda r: fitness(r, dist_matrix))
        current_distance = fitness(current_best, dist_matrix)
        if current_distance < best_distance:
            best_route, best_distance = current_best, current_distance

    return best_route, best_distance

def plot_route(route, locations):
    plt.figure(figsize=(10, 8))
    plt.scatter(locations[:, 0], locations[:, 1], color='blue')
    for i, (x, y) in enumerate(locations):
        plt.text(x, y, f' {i}', fontsize=12, ha='right')
    
    for i in range(len(route)):
        start = locations[route[i]]
        end = locations[route[(i + 1) % len(route)]]
        plt.plot([start[0], end[0]], [start[1], end[1]], 'r-')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Vehicle Routing Problem Solution')
    plt.grid(True)
    plt.show()

# Parameters
population_size = 200
generations = 1000
elitism_size = 10  # Number of top solutions to preserve

# Run GA
best_route, best_distance = genetic_algorithm(locations, population_size, generations, elitism_size)

# Plot results
print(f'Best route: {best_route}')
print(f'Best distance: {best_distance}')
plot_route(best_route, locations)
