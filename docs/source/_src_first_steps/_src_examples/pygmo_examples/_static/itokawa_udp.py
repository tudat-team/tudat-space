from typing import Tuple, List
import numpy as np
import tudatpy
from tudatpy.kernel.numerical_simulation import propagation_setup
from tudatpy.kernel.astro import frame_conversion
from tudatpy.kernel.astro import element_conversion


class AsteroidOrbitProblem:
    """
    This class creates a PyGMO-compatible User Defined Problem (UDP).

    Attributes
    ----------


    Methods
    -------
    """

    def __init__(self,
                 bodies: tudatpy.kernel.numerical_simulation.environment.SystemOfBodies,
                 integrator_settings,
                 propagator_settings,
                 mission_initial_time: float,
                 mission_duration: float,
                 design_variable_lower_boundaries: Tuple[float],
                 design_variable_upper_boundaries: Tuple[float]):
        """
        Constructor for the AsteroidOrbitProblem class.

        Parameters
        ----------
        bodies : tudatpy.kernel.numerical_simulation.environment.SystemOfBodies:
            System of bodies.
        integrator_settings :
            Integrator settings object.
        propagator_settings :
            Propagator settings object.
        """
        # Sets input arguments as lambda function attributes
        # NOTE: this is done so that the class is "pickable", i.e., can be serialized by pygmo
        # TODO Dominic: add here, if needed
        self.bodies_function = lambda: bodies
        self.integrator_settings_function = lambda: integrator_settings
        self.propagator_settings_function = lambda: propagator_settings
        # Initialize empty dynamics simulator
        self.dynamics_simulator_function = lambda: None
        # Set other input arguments as regular attributes
        self.mission_initial_time = mission_initial_time
        self.mission_duration = mission_duration
        self.mission_final_time = mission_initial_time + mission_duration
        self.design_variable_lower_boundaries = design_variable_lower_boundaries
        self.design_variable_upper_boundaries = design_variable_upper_boundaries

    def get_bounds(self) -> Tuple[List[float], List[float]]:
        """
        Returns the search space.

        Parameters
        ----------
        none

        Returns
        -------
        Tuple[List[float], List[float]]
            Two lists of size n (for this problem, n=4), containing respectively the lower and upper
            boundaries of each variable.
        """
        return (list(self.design_variable_lower_boundaries), list(self.design_variable_upper_boundaries))

    def get_nobj(self) -> int:
        """
        Returns the number of objectives p (for this problem, p = 2).
        """
        return 2

    def fitness(self,
                orbit_parameters: List[float]) -> List[float]:
        """
        Computes the fitness value for the problem.

        Parameters
        ----------
        orbit_parameters : List[float]
            Vector of decision variables of size n (for this problem, n = 4).

        Returns
        -------
        List[float]
            List of size p with the values for each objective (for this multi-objective optimization problem, p=2).
        """
        # Retrieves system of bodies
        current_bodies = self.bodies_function()
        # Retrieves Itokawa gravitational parameter
        itokawa_gravitational_parameter = current_bodies.get("Itokawa").gravitational_parameter
        # Reset the initial state from the decision variable vector
        new_initial_state = conversion.keplerian_to_cartesian(
            gravitational_parameter=itokawa_gravitational_parameter,
            semi_major_axis=orbit_parameters[0],
            eccentricity=orbit_parameters[1],
            inclination=np.deg2rad(orbit_parameters[2]),
            argument_of_periapsis=np.deg2rad(235.7),
            longitude_of_ascending_node=np.deg2rad(orbit_parameters[3]),
            true_anomaly=np.deg2rad(139.87))
        # Retrieves propagator settings object
        propagator_settings = self.propagator_settings_function()
        # Retrieves integrator settings object
        integrator_settings = self.integrator_settings_function()
        # Reset the initial state
        propagator_settings.reset_initial_states(new_initial_state)

        # Propagate orbit
        dynamics_simulator = propagation_setup.SingleArcSimulator(current_bodies,
                                                                          integrator_settings,
                                                                          propagator_settings,
                                                                          print_dependent_variable_data=False)
        # Update dynamics simulator function
        self.dynamics_simulator_function = lambda: dynamics_simulator

        # Retrieve dependent variable history
        dependent_variables = dynamics_simulator.dependent_variable_history
        dependent_variables_list = np.vstack(list(dependent_variables.values()))
        # Retrieve distance
        distance = dependent_variables_list[:, 0]
        # Retrieve latitude
        latitudes = dependent_variables_list[:, 1]
        # Compute mean latitude
        mean_latitude = np.mean(np.absolute(latitudes))
        # Computes fitness as mean latitude
        current_fitness = 1.0 / mean_latitude

        # Exaggerate fitness value if the spacecraft has broken out of the selected distance range
        current_penalty = 0.0
        if (max(dynamics_simulator.dependent_variable_history.keys()) < self.mission_final_time):
            current_penalty += 1.0E4

        return [current_fitness + current_penalty, np.mean(distance) + current_penalty * 1.0E3]

    def get_last_run_dynamics_simulator(self):
        """
        Returns the dynamics simulator lambda function.
        """
        return self.dynamics_simulator_function()


