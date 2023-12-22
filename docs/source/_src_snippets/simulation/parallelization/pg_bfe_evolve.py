if __name__ == "__main__":
    bfe = True

    seed = 42
    pop_size = 500

# Create Pygmo problem
    transfer_optimization_problem = MGAHodographicShapingTrajectoryOptimizationProblem(
        central_body, transfer_body_order, bounds, departure_semi_major_axis, departure_eccentricity,
        arrival_semi_major_axis, arrival_eccentricity)
    prob= pg.problem(transfer_optimization_problem)

# Create algorithm and define its seed
    algo = pg.gaco()
    if bfe:
        algo.set_bfe(pg.bfe())
    algo = pg.algorithm(algo)

    bfe_pop = pg.default_bfe() if bfe else None
    pop = pg.population(prob=prob, size=pop_size, seed=seed)

    num_gen = 150

# Initialize lists with the best individual per generation
    list_of_champion_f = [pop.champion_f]
    list_of_champion_x = [pop.champion_x]

# mp.freeze_support() needs to be called when using multiprocessing on windows
# mp.freeze_support()

    for i in range(num_gen):
        print(f'Evolution: {i+1} / {num_gen}', end='\r')
        pop =algo.evolve(pop)

        # Save current champion
        list_of_champion_x.append(pop.champion_x)
        list_of_champion_f.append(pop.champion_f)
    print('Evolution finished')

