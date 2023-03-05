if __name__ == "__main__":
    seed = 42
    pop_size = 1000
    number_of_islands = 4

# Create Pygmo problem
    transfer_optimization_problem = MGAHodographicShapingTrajectoryOptimizationProblem(
        central_body, transfer_body_order, bounds, departure_semi_major_axis, departure_eccentricity,
        arrival_semi_major_axis, arrival_eccentricity)
    problem = pg.problem(transfer_optimization_problem)

# Create algorithm and define its seed
    algorithm = pg.algorithm(pg.sga(gen=1))
    algorithm.set_seed(seed)

# Create island
    archi = pg.archipelago(n=number_of_islands, algo=algorithm, prob=transfer_optimization_problem, pop_size=pop_size)

    num_gen = 40

# Initialize lists with the best individual per generation
    list_of_champion_f = []
    list_of_champion_x = []

# mp.freeze_support() needs to be called when using multiprocessing on windows
# mp.freeze_support()

    for i in range(num_gen):
        print('Evolution: %i / %i' % (i+1, num_gen))

        archi.evolve() # Evolve archi
        archi.wait_check() # Wait until all evolution tasks in the archi finish

        # Save current champion
        list_of_champion_x.append(archi.get_champion_x())
        list_of_champion_f.append(archi.get_champion_f())

    print('Evolution finished')

