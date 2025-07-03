def batch_fitness(self,
            design_parameter_vectors: np.ndarray) -> List[float]:
    """
    Function to evaluate the fitness. A single-objective optimization is used, in which the objective is the deltaV
    necessary to execute the transfer.
    """

    # Compute the final index of each type of parameters
    time_of_flight_index = 3 + self.no_of_legs
    incoming_velocity_index = time_of_flight_index + self.no_of_swingbys
    swingby_periapsis_index = incoming_velocity_index + self.no_of_swingbys
    shaping_free_coefficient_index = swingby_periapsis_index + self.total_no_shaping_free_coefficients
    revolution_index = shaping_free_coefficient_index + self.no_of_legs

    len_single_dpv = revolution_index
    dpvs = design_parameter_vectors.reshape(len(design_parameter_vectors)//len_single_dpv, len_single_dpv)

    inputs, fitnesses = [], []
    for dpv in dpvs:
        inputs.append([list(dpv)])

    # cpu_count = len(os.sched_getaffinity(0))
    cpu_count = mp.cpu_count()
    with mp.get_context("spawn").Pool(processes=int(cpu_count-4)) as pool:
        outputs = pool.map(self.fitness, inputs)

    for output in outputs:
        fitnesses.append(output)

    return fitnesses

