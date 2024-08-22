import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Problem setup
NUM_CITIES = 20
POPULATION_SIZE = 100
NUM_GENERATIONS = 200

# Create random city coordinates
cities = np.random.rand(NUM_CITIES, 2)

# Calculate distances between cities
def distance(city1, city2):
    return np.sqrt(np.sum((city1 - city2)**2))

distance_matrix = np.zeros((NUM_CITIES, NUM_CITIES))
for i in range(NUM_CITIES):
    for j in range(NUM_CITIES):
        distance_matrix[i][j] = distance(cities[i], cities[j])

# Fitness function
def evaluate_path(individual):
    return sum(distance_matrix[individual[i]][individual[i+1]] for i in range(len(individual)-1)) + distance_matrix[individual[-1]][individual[0]],

# Set up the genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", np.random.permutation, NUM_CITIES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate_path)

# Run the genetic algorithm
population = toolbox.population(n=POPULATION_SIZE)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)

final_pop, logbook = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, 
                                         ngen=NUM_GENERATIONS, stats=stats, verbose=True)

# Get the best solution
best_individual = tools.selBest(final_pop, k=1)[0]
best_path = best_individual
best_distance = best_individual.fitness.values[0]

# Visualization
plt.figure(figsize=(12, 6))

# Plot cities
plt.subplot(121)
plt.scatter(cities[:, 0], cities[:, 1], c='red', s=50)
for i, (x, y) in enumerate(cities):
    plt.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points')

# Plot the best path
for i in range(len(best_path)):
    start = cities[best_path[i]]
    end = cities[best_path[(i + 1) % len(best_path)]]
    plt.plot([start[0], end[0]], [start[1], end[1]], 'b-')

plt.title(f"Best Path (Distance: {best_distance:.2f})")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")

# Plot evolution progress
plt.subplot(122)
gen, avg, min_ = logbook.select("gen", "avg", "min")
plt.plot(gen, avg, label="Average")
plt.plot(gen, min_, label="Minimum")
plt.title("Evolution Progress")
plt.xlabel("Generation")
plt.ylabel("Distance")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Best path: {best_path}")
print(f"Best distance: {best_distance:.2f}")