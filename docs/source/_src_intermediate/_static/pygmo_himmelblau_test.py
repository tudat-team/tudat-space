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

"""
Here, a Pygmo-compatible problem class is defined. This is usually known in Pygmo terminology as
User-Defined Problem (UDP). This class will be taken as input from the pygmo.problem() class to create the actual Pygmo
problem class. To be Pygmo-compatible, the UDP class must have two methods:

. get_bounds(): it takes no input and returns a tuple of two n-dimensional lists, defining respectively the lower and 
upper boundaries of each variable. The dimension of the problem (i.e. the value of n) is automatically inferred by the
return type of the this function;

. fitness(x): it takes a np.array as input (of size n) and returns a list with p values as output. In case of
single-objective optimization, p = 1, otherwise p will be equal to the number of objectives.

See also: https://esa.github.io/pygmo2/tutorials/coding_udp_simple.html
"""


##########################################################
# CREATE USER-DEFINED PROBLEM (UDP) ######################
##########################################################

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
        # Set input arguments as attributs
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def get_bounds(self):
        """
        Defines the boundaries of the search space.

        Parameters
        ----------
        none

        Returns
        -------
        tuple
            Two lists of size n (for this problem, n=2), defining respectively the lower and upper
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
        function_value = math.pow(x[0] * x[0] + x[1] - 11.0, 2.0) + math.pow(x[0] + x[1] * x[1] - 7.0, 2.0)
        # Return list
        return [function_value]


def main():
    ##########################################################
    # CREATE PROBLEM #########################################
    ##########################################################

    """
    First, we define the Pygmo problem by using the UDP class defined above. Note that an instantiation of the UDP class
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
    # Evolve population multiple times
    for i in range(number_of_evolutions):
        pop = algo.evolve(pop)
    # At the end of the evolution(s), we extract the best individual
    print('\n########### PRINTING CHAMPION INDIVIDUALS ###########\n')
    # Print its fitness value
    print('Fitness (= function) value: ', pop.champion_f)
    # Print its decision variable vector
    print('Decision variable vector: ', pop.champion_x)


if __name__ == "__main__":
    main()
