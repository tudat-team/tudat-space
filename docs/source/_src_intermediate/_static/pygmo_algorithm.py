# Define number of generations
number_of_generations = 1
# Create Differential Evolution object by passing the number of generations as input
de_algo = pygmo.de(gen=number_of_generations)
# Create pygmo algorithm object
algo = pygmo.algorithm(de_algo)