# Set number of evolutions
number_of_evolutions = 100
# Evolve population multiple times
for i in range(number_of_evolutions):
    pop = algo.evolve(pop)
# Print its fitness value
print('Fitness (= function) value: ', pop.champion_f)
# Print its decision variable vector
print('Decision variable vector: ', pop.champion_x)
### OUTPUT ###
# Fitness (= function) value:  [1.29214202e-11]
# Decision variable vector:  [2.99999936 2.00000024]