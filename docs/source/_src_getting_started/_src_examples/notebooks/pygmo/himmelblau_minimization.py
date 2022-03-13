"""
Copyright (c) 2010-2021, Delft University of Technology
All rights reserved
This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

This tutorial is meant to illustrate the functionalities of PyGMO through the minimization problem of an analytical
function (Himmelblau function).

The PyGMO documentation is available here: https://esa.github.io/pygmo2/index.html. Be careful to read the correct
the documentation webpage (there is also a similar one for previous versions: https://esa.github.io/pygmo/index.html;
as you can see, they can easily be confused).

PyGMO is the Python counterpart of PAGMO: https://esa.github.io/pagmo2/index.html.
"""

# Import statements
import math
import pygmo
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import ticker as mtick
import numpy as np
from numpy import random

"""
Here, a Pygmo-compatible problem class is defined. This is usually known in Pygmo terminology as
User-Defined Problem (UDP). This class will be taken as input from the pygmo.problem() class to create the actual Pygmo
problem class. To be Pygmo-compatible, the UDP class must have two methods:

. get_bounds(): it takes no input and returns a tuple of two n-dimensional lists, containing respectively the lower and 
upper boundaries of each variable. The dimension of the problem (i.e. the value of n) is automatically inferred by the
return type of the this function;

. fitness(x): it takes a np.array as input (of size n) and returns a list with p values as output. In case of
single-objective optimization, p = 1, otherwise p will be equal to the number of objectives.

See also: https://esa.github.io/pygmo2/tutorials/coding_udp_simple.html
"""


##########################################################
# CREATE USER-DEFINED PROBLEM (UDP) ######################
##########################################################

def himmelblau_function(x: list) -> float:
    return math.pow(x[0] * x[0] + x[1] - 11.0, 2.0) + math.pow(x[0] + x[1] * x[1] - 7.0, 2.0)

class HimmelblauOptimization:
    """
    This class defines a PyGMO-compatible User-Defined Optimization Problem.

    Attributes
    ----------
    x_min : float
        Lower boundary for the first variable.
    x_max : float
        Upper boundary for the first variable.
    x_min : float
        Lower boundary for the second variable.
    y_max : float
        Upper boundary for the second variable.

    Methods
    -------
    get_bounds()
    fitness(x)
    """

    def __init__(self,
                 x_min: float,
                 x_max: float,
                 y_min: float,
                 y_max: float):
        """
        Constructor for the HimmelblauOptimization class.

        Parameters
        ----------
        x_min : float
            Lower boundary for the first variable.
        x_max : float
            Upper boundary for the first variable.
        x_min : float
            Lower boundary for the second variable.
        y_max : float
            Upper boundary for the second variable.

        Returns
        -------
        none
        """
        # Set input arguments as attributes
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def get_bounds(self):
        """
        Returns the boundaries of the search space.

        Parameters
        ----------
        none

        Returns
        -------
        tuple
            Two lists of size n (for this problem, n=2), containing respectively the lower and upper
            boundaries of each variable.
        """
        return ([self.x_min, self.y_min], [self.x_max, self.y_max])

    def fitness(self,
                x: list):
        """
        Computes the fitness value for the problem.

        Parameters
        ----------
        x : list
            Vector of decision variables of size n (for this problem, n = 2).

        Returns
        -------
        list
            List of size p with the values for each objective (for this single-objective optimization problem, p=1).
        """
        # Compute Himmelblau function value
        function_value = himmelblau_function(x)
        # Return list
        return [function_value]


def main():
    ##########################################################
    # CREATE PROBLEM #########################################
    ##########################################################

    """
    First, we define the Pygmo problem by using the UDP class defined above. Note that an instance of the UDP class
    must be passed as input to pygmo.problem() and NOT the class itself. It is also possible to use a PyGMO UDP, i.e.
    a problem that is already defined in PyGMO, but it will not be shown in this tutorial.
    See also: https://esa.github.io/pygmo2/tutorials/using_problem.html.
    """
    # Instantiation of the UDP problem
    udp = HimmelblauOptimization(-5.0, 5.0, -5.0, 5.0)
    # Creation of the pygmo problem object
    prob = pygmo.problem(udp)
    # Print the problem's information
    print('\n########### PRINTING PROBLEM INFORMATION ###########\n')
    print(prob)

    ##########################################################
    # CREATE ALGORITHM #######################################
    ##########################################################

    """
    As a second step, we have to create an algorithm to solve the problem. Many different algorithms are available
    through PyGMO, including heuristic methods and local optimizers. In this example, we will use the Differential
    Evolution (DE). Similarly to the UDP, it is also possible to create a User-Defined Algorithm (UDA), but in this
    tutorial we will use an algorithm readily available in PyGMO.
    See also: https://esa.github.io/pygmo2/tutorials/using_algorithm.html.
    """
    # Define number of generations
    number_of_generations = 1
    # Fix seed
    current_seed = 171015
    # Create Differential Evolution object by passing the number of generations as input
    # NOTE: specific inputs for different pygmo algorithms may vary, check each algorithm's documentation
    # See also https://esa.github.io/pygmo2/overview.html#list-of-algorithms
    de_algo = pygmo.de(gen=number_of_generations, seed=current_seed)
    # Create pygmo algorithm object
    algo = pygmo.algorithm(de_algo)
    # Print the algorithm's information
    print('\n########### PRINTING ALGORITHM INFORMATION ###########\n')
    print(algo)

    ##########################################################
    # INITIALIZE POPULATION ##################################
    ##########################################################

    """
    A population in PyGMO is essentially a container for multiple individuals. Each individual has an associated 
    decision vector which can change (evolution), the resulting fitness vector, and an unique ID to allow their
    tracking. The population is initialized starting from a specific problem to ensure that all individuals are 
    compatible with the UDP. The default population size is 0.
    """
    # Set population size
    pop_size = 1000
    # Set seed
    current_seed = 171015
    # Create population
    pop = pygmo.population(prob, size=pop_size, seed=current_seed)
    # Inspect population (this is going to be long, uncomment if desired)
    # print('\n########### PRINTING POPULATION INFORMATION ###########\n')
    # print(pop)

    ##########################################################
    # EVOLVE POPULATION ######################################
    ##########################################################

    # Set number of evolutions
    number_of_evolutions = 100
    # Initialize empty containers
    individuals_list = []
    fitness_list = []
    # Evolve population multiple times
    for i in range(number_of_evolutions):
        pop = algo.evolve(pop)
        individuals_list.append(pop.get_x()[pop.best_idx()])
        fitness_list.append(pop.get_f()[pop.best_idx()])

    # At the end of the evolution(s), we extract the best individual
    print('\n########### PRINTING CHAMPION INDIVIDUALS ###########\n')
    # Print its fitness value
    print('Fitness (= function) value: ', pop.champion_f)
    # Print its decision variable vector
    print('Decision variable vector: ', pop.champion_x)
    # Print the number of function evaluations (calls to the fitness function)
    print('Number of function evaluations: ', pop.problem.get_fevals())
    # Print the difference wrt to the minimum location
    print('Difference wrt the minimum: ', pop.champion_x - np.array([3,2]))

    ##########################################################
    # VISUALIZE OPTIMIZATION #################################
    ##########################################################

    # Set font size for plots
    font = {'size': 18}
    matplotlib.rc('font', **font)
    # Extract best individuals for each generation
    best_x = [ind[0] for ind in individuals_list]
    best_y = [ind[1] for ind in individuals_list]
    # Extract problem bounds
    (x_min, y_min), (x_max, y_max) = udp.get_bounds()

    # Plot fitness over generations
    fig, ax = plt.subplots(figsize=(16, 4))
    ax.plot(np.arange(0, number_of_evolutions), fitness_list, label='Function value')
    # Plot champion
    champion_n = np.argmin(np.array(fitness_list))
    ax.scatter(champion_n, np.min(fitness_list), marker='x', color='r', label='All-time champion')
    # Prettify
    ax.set_xlim((0, number_of_evolutions))
    ax.grid('major')
    ax.set_title('Best individual of each generation', fontweight='bold')
    ax.set_xlabel('Number of generation')
    ax.set_ylabel(r'Himmelblau function value $f(x,y)$')
    ax.legend(loc='upper right')
    plt.savefig('fitness_himmelblau.png', bbox_inches='tight')

    # Plot Himmelblau function
    grid_points = 100
    x_vector = np.linspace(x_min, x_max, grid_points)
    y_vector = np.linspace(y_min, y_max, grid_points)
    x_grid, y_grid = np.meshgrid(x_vector, y_vector)
    z_grid = np.zeros((grid_points, grid_points))
    for i in range(x_grid.shape[1]):
        for j in range(x_grid.shape[0]):
            z_grid[i, j] = himmelblau_function([x_grid[i, j], y_grid[i, j]])
    # Create figure
    fig, ax = plt.subplots(figsize=(16, 10))
    cs = ax.contour(x_grid, y_grid, z_grid, 50)
    # Plot best individuals of each generation
    ax.scatter(best_x, best_y, marker='x', color='r')
    # Prettify
    ax.set_xlim((x_min, x_max))
    ax.set_ylim((y_min, y_max))
    ax.set_title('Himmelblau function', fontweight='bold')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    cbar = fig.colorbar(cs)
    cbar.ax.set_ylabel(r'Himmelblau function value $f(x,y)$')
    plt.savefig('contour_himmelblau.png', bbox_inches='tight')

    # Visualize only one minimum
    eps = 1E-3
    x_min, x_max = (3 - eps, 3 + eps)
    y_min, y_max = (2 - eps, 2 + eps)
    grid_points = 100
    x_vector = np.linspace(x_min, x_max, grid_points)
    y_vector = np.linspace(y_min, y_max, grid_points)
    x_grid, y_grid = np.meshgrid(x_vector, y_vector)
    z_grid = np.zeros((grid_points, grid_points))
    for i in range(x_grid.shape[1]):
        for j in range(x_grid.shape[0]):
            z_grid[i, j] = himmelblau_function([x_grid[i, j], y_grid[i, j]])
    fig, ax = plt.subplots(figsize=(16, 10))
    cs = ax.contour(x_grid, y_grid, z_grid, 50)
    # Plot best individuals of each generation
    ax.scatter(best_x, best_y, marker='x', color='r', label='Best individual of each generation')
    ax.scatter(pop.champion_x[0], pop.champion_x[1], marker='x', color='k', label='Champion')
    # Prettify
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.5f'))
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.5f'))
    plt.xticks(rotation=45)
    ax.set_xlim((x_min, x_max))
    ax.set_ylim((y_min, y_max))
    ax.set_title('Vicinity of (3,2)', fontweight='bold')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    cbar = fig.colorbar(cs)
    cbar.ax.set_ylabel(r'Himmelblau function value $f(x,y)$')
    ax.legend(loc='lower right')
    ax.grid('major')
    plt.savefig('one_minimum_himmelblau.png', bbox_inches='tight')


    ##########################################################
    # GRID SEARCH ############################################
    ##########################################################

    # Set number of points
    number_of_nodes = 1000
    # Extract problem bounds
    (x_min, y_min), (x_max, y_max) = udp.get_bounds()
    x_vector = np.linspace(x_min, x_max, number_of_nodes)
    y_vector = np.linspace(y_min, y_max, number_of_nodes)
    x_grid, y_grid = np.meshgrid(x_vector, y_vector)
    z_grid = np.zeros((number_of_nodes, number_of_nodes))
    for i in range(x_grid.shape[1]):
        for j in range(x_grid.shape[0]):
            z_grid[i, j] = himmelblau_function([x_grid[i, j], y_grid[i, j]])
    best_f = np.min(z_grid)
    best_ind = np.argmin(z_grid)
    best_x = (x_grid.flatten()[best_ind], y_grid.flatten()[best_ind])
    print('\n########### RESULTS OF GRID SEARCH (' + str(number_of_nodes) + ' nodes per variable) ########### ')
    print('Best fitness with grid search (' + str(number_of_nodes) + ' points):', best_f)
    print('Decision variable vector: ', best_x)
    print('Number of function evaluations: ', number_of_nodes**2)
    print('Difference wrt the minimum: ', best_x - np.array([3, 2]))
    del number_of_nodes

    ##########################################################
    # MONTE-CARLO SEARCH #####################################
    ##########################################################

    # Fix seed (for reproducibility)
    random.seed(current_seed)
    # Size of random number vector
    number_of_points = 1000
    x_vector = random.random(number_of_points)
    x_vector *= (x_max - x_min)
    x_vector += x_min
    y_vector = random.random(number_of_points)
    y_vector *= (y_max - y_min)
    y_vector += y_min
    x_grid, y_grid = np.meshgrid(x_vector, y_vector)
    z_grid = np.zeros((number_of_points, number_of_points))
    for i in range(x_grid.shape[1]):
        for j in range(x_grid.shape[0]):
            z_grid[i, j] = himmelblau_function([x_grid[i, j], y_grid[i, j]])
    best_f = np.min(z_grid)
    best_ind = np.argmin(z_grid)
    best_x = (x_grid.flatten()[best_ind], y_grid.flatten()[best_ind])
    print('\n########### RESULTS OF MONTE-CARLO SEARCH (' + str(number_of_points) + ' points per variable) ' +
                                                                                    '########### ')
    print('Best fitness with grid search (' + str(number_of_points) + ' points):', best_f)
    print('Decision variable vector: ', best_x)
    print('Number of function evaluations: ', number_of_points**2)
    print('Difference wrt the minimum: ', best_x - np.array([3, 2]))
    del number_of_points

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()

