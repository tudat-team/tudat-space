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