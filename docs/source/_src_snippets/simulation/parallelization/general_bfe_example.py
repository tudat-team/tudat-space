def run_simulation(arg_1, arg_2):
    # Do some tudat things...
    return 1, arg_1 + arg_2

# Main script
if __name__ == "__main__":
    # Number of simulations to run
    N = 500
    arg_1_list = np.random.normal(-100, 50, size=N)
    arg_2_list = np.random.normal(1e6, 2e5, size=N)

    # Combine list of inputs
    inputs = []
    for i in range(N):
        inputs.append((arg_1_list[i], arg_2_list[i]))

    # Run simulations in parallel, using half the available cores
    n_cores = mp.cpu_count()//2
    with mp.get_context("spawn").Pool(n_cores) as pool:
        outputs = pool.starmap(run_simulation, inputs)

