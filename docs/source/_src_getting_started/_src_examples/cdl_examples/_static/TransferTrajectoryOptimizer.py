# General imports
import os
from typing import List, Tuple
import numpy as np
import pygmo as pg

# Tudat imports
import BuildDirectory
from tudatpy.kernel import constants
from tudatpy.kernel.astro import trajectory_design
from tudatpy.kernel.simulation import environment_setup, astro_setup
import tudatpy

# CDL imports
import TransferTrajectoryAnalysis
from TransferTrajectoryUtilities import get_all_pareto_info, select_results_directory
from constants import MINIMUM_TIME_OF_FLIGHT_DICT, MAXIMUM_TIME_OF_FLIGHT_DICT


###########################################################################
# CREATE PROBLEM CLASS ####################################################
###########################################################################

class TransferTrajectoryOptimizer:
    """
        Class to initialize, simulate and optimize the MultiGravityAssist-DeepSpaceManeuver transfer trajectory
        for the Collaborative Design Lab (CDL)

        Attributes
        ----------
        departure_date
        departure_date_margin
        maximum_delta_v
        number_of_evolutions
        population_size
        leg_type
        transfer_body_order
        departure_eccentricity
        departure_semi_major_axis
        arrival_eccentricity
        arrival_semi_major_axis
        seed

        Methods
        -------
        get_nobj()
        get_bounds()
        fitness()
        perform_optimization_or_load_data

        """
    def __init__(self,
                 number_of_evolutions: int,
                 population_size: int,
                 departure_date: float,
                 departure_date_margin: float,
                 maximum_delta_v: float,
                 leg_type: tudatpy.kernel.astro.trajectory_design.TransferLegTypes,
                 transfer_body_order: List[str],
                 departure_eccentricity: float = 0,
                 departure_semi_major_axis: float = np.inf,
                 arrival_eccentricity: float = 0,
                 arrival_semi_major_axis: float = np.inf,
                 seed: int = 4444):

        self.number_of_evolutions = number_of_evolutions
        self.population_size = population_size
        self.departure_date = departure_date
        self.departure_date_margin = departure_date_margin
        self.maximum_delta_v = maximum_delta_v
        self.leg_type = leg_type
        self.transfer_body_order = transfer_body_order
        self.departure_eccentricity = departure_eccentricity
        self.departure_semi_major_axis = departure_semi_major_axis
        self.arrival_eccentricity = arrival_eccentricity
        self.arrival_semi_major_axis = arrival_semi_major_axis
        self.seed = seed

        # Create system of bodies
        bodies = environment_setup.create_simplified_system_of_bodies()

        # Retrieve settings for nodes and legs of the transfer
        transfer_leg_settings, transfer_node_settings = trajectory_design.mga_transfer_settings(
            self.transfer_body_order,
            self.leg_type,
            departure_orbit=(self.departure_semi_major_axis, self.departure_eccentricity),
            arrival_orbit=(self.arrival_semi_major_axis, self.arrival_eccentricity))

        # Create transfer trajectory object
        transfer_trajectory = astro_setup.create_transfer_trajectory(bodies,
                                                                     transfer_leg_settings,
                                                                     transfer_node_settings,
                                                                     self.transfer_body_order,
                                                                     'Sun')

        self.transfer_trajectory_function = lambda: transfer_trajectory

    def get_nobj(self) -> int:
        """
        Returns the number of objectives (currently: double-objective -> delta V and time of flight)
        """
        return 2

    def get_bounds(self) -> tuple:
        """
        Returns the boundaries of the decision variables.
        """
        # Retrieve objects and variables
        transfer_trajectory = self.transfer_trajectory_function()
        number_of_nodes = transfer_trajectory.number_of_nodes
        number_of_legs = transfer_trajectory.number_of_legs
        transfer_body_order = self.transfer_body_order
        leg_type = self.leg_type

        number_of_parameters = self.get_number_of_parameters()

        lower_bound = list(np.empty(number_of_parameters))
        upper_bound = list(np.empty(number_of_parameters))

        # Define boundaries on departure date
        lower_bound[0] = self.departure_date - self.departure_date_margin
        upper_bound[0] = self.departure_date + self.departure_date_margin

        # Define boundaries on time of flight
        for i in range(number_of_legs):
            next_body = transfer_body_order[ i+1 ]
            minimum_time_of_flight = MINIMUM_TIME_OF_FLIGHT_DICT[next_body]
            maximum_time_of_flight = MAXIMUM_TIME_OF_FLIGHT_DICT[next_body]

            lower_bound[i + 1] = minimum_time_of_flight * constants.JULIAN_DAY
            upper_bound[i + 1] = maximum_time_of_flight * constants.JULIAN_DAY

        # Add bounds for DSM legs
        if leg_type == trajectory_design.dsm_velocity_based_leg_type:
            # Add excess velocity at departure node
            lower_bound[number_of_nodes] = 0. + 1e-4
            upper_bound[number_of_nodes] = 5000.

            # Add in-plane angle of excess velocity at departure node
            lower_bound[number_of_nodes + 1] = 0. * 2. * np.pi + 1e-4
            upper_bound[number_of_nodes + 1] = 1. * 2. * np.pi - 1e-4

            # Add out-of-plane angle of excess velocity at departure node
            lower_bound[number_of_nodes + 2] = -1. * np.pi / 2. + 1e-4
            upper_bound[number_of_nodes + 2] = 1. * np.pi / 2. - 1e-4

            # Add periapsis radius, orbit orientation rotation and swingby delta V at node 1 through n-1
            for i in range(number_of_nodes - 2):
                current_body = transfer_body_order[i + 1]
                minimum_pericenter_dict = trajectory_design.DEFAULT_MINIMUM_PERICENTERS

                minimum_pericenter = minimum_pericenter_dict[current_body]
                maximum_pericenter = 10. * minimum_pericenter

                lower_bound[number_of_nodes + 3 + 3*i] = minimum_pericenter
                upper_bound[number_of_nodes + 3 + 3*i] = maximum_pericenter

                #Add orbit-orientation angle
                lower_bound[number_of_nodes + 4 + 3*i] = - 1. * np.pi + 1e-4
                upper_bound[number_of_nodes + 4 + 3*i] = 1. * np.pi - 1e-4

                #Add delta_v at periapsis
                lower_bound[number_of_nodes + 5 + 3*i] = 0.
                upper_bound[number_of_nodes + 5 + 3*i] = 5000.

            # Add time of flight fraction for DSM moment per leg
            for i in range(number_of_legs):
                lower_bound[number_of_nodes + number_of_legs * 3 + i] = 0.05
                upper_bound[number_of_nodes + number_of_legs * 3 + i] = 0.95

        bounds = (lower_bound, upper_bound)
        return bounds

    def get_number_of_parameters(self):
        """
        Returns number of parameters that will be optimized
        """

        transfer_trajectory = self.transfer_trajectory_function()
        number_of_nodes = transfer_trajectory.number_of_nodes
        number_of_legs = transfer_trajectory.number_of_legs
        leg_type = self.leg_type

        if leg_type == trajectory_design.unpowered_unperturbed_leg_type:
            number_of_parameters = number_of_nodes
        elif leg_type == trajectory_design.dsm_velocity_based_leg_type:
            number_of_parameters = number_of_nodes + 4 * number_of_legs

        return number_of_parameters

    def fitness(self, trajectory_parameters: List[float]) -> list:
        """
        Returns delta V and Time of Flight of the transfer trajectory object with the given set of trajectory parameters
        """

        # Retrieve transfer trajectory object
        transfer_trajectory = self.transfer_trajectory_function()
        leg_type = self.leg_type

        # Convert list of trajectory parameters to appropriate format
        node_times, leg_free_parameters, node_free_parameters = TransferTrajectoryAnalysis.convert_trajectory_parameters(
            transfer_trajectory,
            leg_type,
            trajectory_parameters)
        # Evaluate trajectory
        try:
            transfer_trajectory.evaluate(node_times, leg_free_parameters, node_free_parameters)

            # Calculate fitness
            delta_v = transfer_trajectory.delta_v
            time_of_flight = transfer_trajectory.time_of_flight

            if delta_v > self.maximum_delta_v:
                delta_v = 200e3
                time_of_flight = 2e10

        except:
            delta_v = 1e10
            time_of_flight = 1e15

        return [delta_v, time_of_flight]

    def perform_optimization(self) -> Tuple[np.ndarray, str]:
        """
        Runs optimization, saves results and finds Pareto front

        :return:
        fitness
        pareto_fitness
        plots_dir
        """
        ###########################################################################
        # Setup directory to save data and plots
        ###########################################################################

        print(self.transfer_body_order)

        results_dir = select_results_directory(self.transfer_body_order, self.leg_type) + 'optimization/'

        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)

        ###########################################################################
        # Run optimization
        ###########################################################################
        print('Running optimization...')

        generations_dir = results_dir + 'generations/'
        if not os.path.isdir(generations_dir):
            os.makedirs(generations_dir)

        # Create Pygmo problem, this is this class
        transfer_problem = self

        # Select algorithm from Pygmo with default settings
        algo = pg.algorithm(pg.nsga2(gen=100, cr=0.95, eta_c=10.0, m=0.01, eta_m=50.0, seed=self.seed))

        # Initialize population and save it
        pop = pg.population(transfer_problem, size=self.population_size, seed=self.seed)

        fitness = pop.get_f()
        trajectory_parameters = pop.get_x()

        np.savetxt(generations_dir + 'Gen0_fitness.dat', fitness)
        np.savetxt(generations_dir + 'Gen0_parameters.dat', trajectory_parameters)

        # Evolve the population 100 times and save final generation
        for i in range( int( np.ceil( self.number_of_evolutions / 100 ) ) ):
            pop = algo.evolve(pop)

            fitness = pop.get_f()
            trajectory_parameters = pop.get_x()

            np.savetxt(generations_dir + 'Gen' + str((i+1)*100) + '_fitness.dat', fitness)
            np.savetxt(generations_dir + 'Gen' + str((i+1)*100) + '_parameters.dat', trajectory_parameters)

        # Find Pareto front in final generation
        pareto_fitness, pareto_parameters = get_all_pareto_info(fitness, trajectory_parameters)

        # Save pareto
        np.savetxt(results_dir + 'Pareto_parameters.dat', pareto_parameters)
        np.savetxt(results_dir + 'Pareto_fitness.dat', pareto_fitness)

        # return fitness, pareto_fitness, results_dir
        return pareto_fitness, results_dir

