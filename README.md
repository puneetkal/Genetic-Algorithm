[![PyPI](https://img.shields.io/pypi/v/vrp-genetic-algo)](https://pypi.org/project/vrp-genetic-algo/)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/vrp-genetic-algo/vrp-genetic-algo)
[![GitHub Workflow Status](https://github.com/yourusername/vrp-genetic-algo/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/vrp-genetic-algo/actions/workflows/ci.yml)
[![readthedocs status](https://readthedocs.org/projects/vrp-genetic-algo/badge/?version=latest)](https://vrp-genetic-algo.readthedocs.io/en/latest/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/yourusername/vrp-genetic-algo/dev.svg)](https://results.pre-commit.ci/latest/github/yourusername/vrp-genetic-algo/dev)

# Vehicle Routing Problem (VRP) Genetic Algorithm

The Vehicle Routing Problem (VRP) Genetic Algorithm project is designed to find optimal routes for a vehicle to visit a set of locations, including a depot and several customers. This project leverages a Genetic Algorithm (GA) to solve the VRP and visualizes the best route using `matplotlib`.

![Example Route](https://github.com/yourusername/vrp-genetic-algo/blob/main/docs/example-route.png?raw=true)
![Image1](https://github.com/user-attachments/assets/97390b6c-ea63-41c5-b113-5c1559d659e1)

## Coding Explanation
1. Setup Locations
The first step in the project is to define the locations that need to be visited. These include a central depot and multiple customer locations. Each location is represented by its coordinates in a 2D space.

2. Distance Matrix Calculation
To evaluate the efficiency of different routes, we calculate the distance between each pair of locations. This is done by creating a distance matrix where each entry represents the Euclidean distance between two locations. This matrix helps in assessing the total distance of any given route.

3. Genetic Algorithm Functions
Generate and Create Population:
The genetic algorithm starts by generating an initial population of routes. Each route is a permutation of the locations, representing a possible sequence in which the vehicle might visit the locations. The population is created by randomly shuffling these routes.

Fitness Function:
The fitness function evaluates how good a route is by calculating its total distance using the previously computed distance matrix. A shorter total distance indicates a better (more optimal) route.

Mutation:
Mutation introduces randomness into the population by altering existing routes. Specifically, it involves swapping two locations within a route. This helps in exploring new routes that might lead to better solutions.

Crossover:
Crossover combines parts of two parent routes to create new routes. This process involves selecting a segment of one parent route and filling in the remaining parts from the second parent, preserving as many good traits from both parents as possible.

Genetic Algorithm Execution:
The main genetic algorithm function evolves the population of routes over several generations. It selects the best routes (based on fitness), applies crossover and mutation to generate new routes, and ensures that the best solutions are preserved (elitism). The process continues until the algorithm converges or reaches a predefined number of generations.

4. Visualization
The best route found by the genetic algorithm is visualized using a plotting library. The visualization displays the locations as points and draws lines between them to represent the route. This helps in understanding the route and verifying the solution.

5. Running the Algorithm
To find and visualize the best route, you can adjust parameters such as the size of the population, the number of generations, and the size of the elite group. The algorithm is run with these parameters, and the results are printed and visualized, showing the most efficient route and its total distance.
![Image2](https://github.com/user-attachments/assets/851e9858-3a34-48c3-a444-079d7ce19025)

## Related Papers

- [A Comprehensive Review of the Vehicle Routing Problem and Its Variants](https://arxiv.org/abs/2401.06379)
- [Genetic Algorithms for Solving the Vehicle Routing Problem](https://arxiv.org/abs/2402.01353)
