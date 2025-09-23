if __name__ == "__main__":

    plot = False
    simulation_type = 'normal' #bfe or normal

    #Monte Carlo parameters
    bounds = [[7000e3, 8000e3], [0.1, 0.6]] # Semi-major Axis and Eccentricity are tested here
    N = 2000
    n_cores = 4

    # Setup inputs for MC with BFE
    arg_dict = {}
    for it, bound in enumerate(bounds):
        arg_dict[it] = np.random.uniform(bound[0], bound[1], size=N)

    inputs = []
    for k in range(len(arg_dict[0])):
        inputs.append(tuple(arg_dict[p][k] for p in range(2)))

    # Run parallel MC analysis
    with mp.get_context("spawn").Pool(n_cores) as pool:
        outputs = pool.starmap(run_dynamics, inputs)
