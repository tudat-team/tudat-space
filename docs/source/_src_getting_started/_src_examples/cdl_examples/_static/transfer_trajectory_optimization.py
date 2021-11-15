# General imports
import matplotlib.pyplot as plt
import numpy as np

# Tudat imports
import BuildDirectory

# CDL imports
from TransferTrajectoryOptimizer import TransferTrajectoryOptimizer
from transfer_trajectory_inputs import transfer_body_orders, leg_type, departure_date, departure_date_margin, \
                                     departure_semi_major_axis, departure_eccentricity, arrival_semi_major_axis, \
                                     arrival_eccentricity , number_of_evolutions, population_size, optimization_seed, \
                                     maximum_delta_v, save_optimization_plots

def main():
    ###########################################################################
    # Define inputs
    ###########################################################################

    for transfer_body_order in transfer_body_orders:

        ###########################################################################
        # Run optimization or load data
        ###########################################################################
        # Initialize optimization class
        optimizer = TransferTrajectoryOptimizer(number_of_evolutions,
                                                population_size,
                                                departure_date,
                                                departure_date_margin,
                                                maximum_delta_v,
                                                leg_type,
                                                transfer_body_order,
                                                departure_eccentricity,
                                                departure_semi_major_axis,
                                                arrival_eccentricity,
                                                arrival_semi_major_axis,
                                                optimization_seed)

        # fitness, pareto_fitness, results_dir = optimization.perform_optimization_or_load_data()
        pareto_fitness, results_dir = optimizer.perform_optimization()

        ###########################################################################
        # Plot optimization results
        ###########################################################################

        # Plot pareto front
        if save_optimization_plots:
            plt.figure()
            plt.suptitle(str(transfer_body_order))
            plt.plot(pareto_fitness[:, 1] / 86400, pareto_fitness[:, 0] / 1000, c='red', label='Pareto')
            plt.xlabel('Time of flight [days]')
            plt.ylabel('\Delta V [km/s]')
            plt.ylim([0, 20])
            plt.legend()
            plt.savefig(results_dir + 'Pareto_front.pdf', bbox_inches='tight')
            plt.close()

    print('The optimization has finished and the data has been saved')

    return 0

if __name__ == "__main__":    main()