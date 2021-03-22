"""
Copyright (c) 2010-2021, Delft University of Technology
All rights reserved
This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

This aim of this tutorial is to illustrate the use of PyGMO to optimize an astrodynamics problem simulated with
tudatpy. The problem describes the orbit design around a small body (asteroid Itokawa). The design variables are
the initial values of semi-major axis, eccentricity, inclination, and longitude of node. The objectives are good
coverage (this is now quantified by maximizing the mean value of the absolute longitude w.r.t. Itokawa
over the full propagation) and being close to the asteroid (the mean value of the distance should be minimized).
The constraints are set on the altitude: all the sets of design variables leading to an orbit

It is assumed that the reader of this tutorial is already familiar with the content of this basic PyGMO tutorial:
https://tudat-space.readthedocs.io/en/latest/_src_intermediate/pygmo.html.

The full PyGMO documentation is available here: https://esa.github.io/pygmo2/index.html. Be careful to read the
correct the documentation webpage (there is also a similar one for previous yet now outdated versions:
https://esa.github.io/pygmo/index.html; as you can see, they can easily be confused).

PyGMO is the Python counterpart of PAGMO: https://esa.github.io/pagmo2/index.html.
"""

###############################################################################
# IMPORT STATEMENTS ###########################################################
###############################################################################

# General imports
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from typing import List, Dict, Tuple
import os

# Pygmo import
import pygmo as pg

# Tudatpy imports
import tudatpy
from tudatpy.io import save2txt
from tudatpy.kernel import constants
from tudatpy.kernel.interface import spice_interface
from tudatpy.kernel.simulation import environment_setup
from tudatpy.kernel.simulation import propagation_setup
from tudatpy.kernel.astro import conversion, frames


###############################################################################
# DEFINITION OF HELPER FUNCTIONS ##############################################
###############################################################################

def get_itokawa_rotation_settings(itokawa_body_frame_name) -> \
        tudatpy.kernel.simulation.environment_setup.rotation_model.RotationalModelSettings:
    """
    Defines the Itokawa rotation settings by using a constant angular velocity.

    To do this, the initial orientation in the inertial frame is needed. This is expressed through the orientation
    of the pole. The angular velocity is also needed.

    Parameters
    ----------
    itokawa_body_frame_name : str
        Name of the Itokawa body-fixed frame.

    Returns
    -------
    tudatpy.kernel.simulation.environment_setup.rotation_model.RotationalModelSettings
        Rotational model settings object for Itokawa.
    """

    # Definition of initial Itokawa orientation conditions through the pole orientation
    # Declination
    pole_declination = np.deg2rad(-66.30)
    # Right ascension
    pole_right_ascension = np.deg2rad(90.53)
    # Meridian
    meridian_at_epoch = 0.0

    # Define initial Itokawa orientation in inertial frame (equatorial plane)
    initial_orientation_j2000 = frames.inertial_to_body_fixed_rotation_matrix(
        pole_declination, pole_right_ascension, meridian_at_epoch)
    # Get initial Itokawa orientation in inertial frame but in the Ecliptic plane
    initial_orientation_eclipj2000 = np.matmul(spice_interface.compute_rotation_matrix_between_frames(
        "ECLIPJ2000", "J2000", 0.0), initial_orientation_j2000)

    # Manually check the results, if desired
    # np.set_printoptions(precision=100)
    # print(initial_orientation_j2000)
    # print(initial_orientation_eclipj2000)

    # Compute rotation rate
    rotation_rate = np.deg2rad(712.143) / constants.JULIAN_DAY

    # Set up rotational model for Itokawa with constant angular velocity
    return environment_setup.rotation_model.simple(
        "ECLIPJ2000", itokawa_body_frame_name, initial_orientation_eclipj2000, 0.0, rotation_rate)


def get_itokawa_ephemeris_settings(itokawa_gravitational_parameter) -> \
        tudatpy.kernel.simulation.environment_setup.ephemeris.KeplerEphemerisSettings:
    """
    Sets the Itokawa ephemeris.

    The ephemeris for Itokawa are set using a Keplerian orbit around the Sun. To do this, the initial position at a
    certain epoch is needed. The asteroid's gravitational parameter is also needed.

    Parameters
    ----------
    itokawa_gravitational_parameter : float
        Itokawa gravitational parameter.

    Returns
    -------
    tudatpy.kernel.simulation.environment_setup.ephemeris.KeplerEphemerisSettings
        The ephemeris settings object for Itokawa.
    """
    # Define Itokawa initial Kepler elements
    itokawa_kepler_elements = np.array([
        1.324118017407799 * constants.ASTRONOMICAL_UNIT,
        0.2801166461882852,
        np.deg2rad(1.621303507642802),
        np.deg2rad(162.8147699851312),
        np.deg2rad(69.0803904880264),
        np.deg2rad(187.6327516838828)])
    # Convert mean anomaly to true anomaly
    itokawa_kepler_elements[5] = conversion.mean_to_true_anomaly(
        eccentricity=itokawa_kepler_elements[1],
        mean_anomaly=itokawa_kepler_elements[5])
    # Get epoch of initial Kepler elements (in Julian Days)
    kepler_elements_reference_julian_day = 2459000.5
    # Sets new reference epoch for Itokawa ephemerides (different from J2000)
    kepler_elements_reference_epoch = (kepler_elements_reference_julian_day - constants.JULIAN_DAY_ON_J2000) \
                                      * constants.JULIAN_DAY
    # Sets the ephemeris model
    return environment_setup.ephemeris.keplerian(
        itokawa_kepler_elements,
        kepler_elements_reference_epoch,
        itokawa_gravitational_parameter,
        "Sun",
        "ECLIPJ2000")


def get_itokawa_gravity_field_settings(itokawa_body_fixed_frame: str,
                                       itokawa_radius: float) -> \
        tudatpy.kernel.simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings:
    """
    Defines the Itokawa gravity field model.

    It creates a Spherical Harmonics gravity field model expanded up to order 4 and degree 4. Normalized coefficients
    are hardcoded, as well as the gravitational parameter and the reference radius.

    Parameters
    ----------
    itokawa_body_fixed_frame : str
        Name of the body-fixed reference frame.
    itokawa_radius : float
        Reference radius of the asteroid.

    Returns
    -------
    tudatpy.kernel.simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings
        The gravity field settings object for Itokawa.
    """
    itokawa_gravitational_parameter = 2.36
    normalized_cosine_coefficients = np.array([
        [1.0, 0.0, 0.0, 0.0, 0.0],
        [-0.145216, 0.0, 0.219420, 0.0, 0.0],
        [0.036115, -0.028139, -0.046894, 0.069022, 0.0],
        [0.087852, 0.034069, -0.123263, -0.030673, 0.150282]])
    normalized_sine_coefficients = np.array([
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, -0.006137, -0.046894, 0.033976, 0.0],
        [0.0, 0.004870, 0.000098, -0.015026, 0.011627]])
    return environment_setup.gravity_field.spherical_harmonic(
        gravitational_parameter=itokawa_gravitational_parameter,
        reference_radius=itokawa_radius,
        normalized_cosine_coefficients=normalized_cosine_coefficients,
        normalized_sine_coefficients=normalized_sine_coefficients,
        associated_reference_frame=itokawa_body_fixed_frame)


def get_itokawa_shape_settings(itokawa_radius: float) -> \
        tudatpy.kernel.simulation.environment_setup.shape.SphericalBodyShapeSettings:
    """
    Defines the shape settings object for Itokawa.

    It uses a spherical model.

    Parameters
    ----------
    itokawa_radius : float
        Reference radius of the asteroid.

    Returns
    -------
    tudatpy.kernel.simulation.environment_setup.shape.SphericalBodyShapeSettings
        The spherical shape settings object for Itokawa.
    """
    # Creates spherical shape settings
    return environment_setup.shape.spherical(itokawa_radius)


def create_simulation_bodies(itokawa_radius: float) -> tudatpy.kernel.simulation.environment_setup.SystemOfBodies:
    """
    It creates all the body settings and body objects required by the simulation.

    Parameters
    ----------
    itokawa_radius : float
        Radius of Itokawa, assuming a spherical shape.

    Returns
    -------
    tudatpy.kernel.simulation.environment_setup.SystemOfBodies
        System of bodies to be used in the simulation.
    """
    ### CELESTIAL BODIES ###
    # Define Itokawa body frame name
    itokawa_body_frame_name = "Itokawa_Frame"

    # Create default body settings for selected celestial bodies
    bodies_to_create = ["Sun", "Earth", "Jupiter", "Saturn", "Mars"]

    # Create default body settings for bodies_to_create, with "Earth"/"J2000" as
    # global frame origin and orientation. This environment will only be valid
    # in the indicated time range [simulation_start_epoch --- simulation_end_epoch]
    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create,
        "SSB",
        "ECLIPJ2000")

    # Add Itokawa body
    body_settings.add_empty_settings("Itokawa")
    # Gravity field definition
    itokawa_gravity_field_settings = get_itokawa_gravity_field_settings(itokawa_body_frame_name,
                                                                        itokawa_radius)
    # Adds Itokawa settings
    # Gravity field
    body_settings.get("Itokawa").gravity_field_settings = itokawa_gravity_field_settings
    # Rotational model
    body_settings.get("Itokawa").rotation_model_settings = get_itokawa_rotation_settings(itokawa_body_frame_name)
    # Ephemeris
    body_settings.get("Itokawa").ephemeris_settings = get_itokawa_ephemeris_settings(
        itokawa_gravity_field_settings.gravitational_parameter)
    # Shape (spherical)
    body_settings.get("Itokawa").shape_settings = get_itokawa_shape_settings(itokawa_radius)
    # Create system of selected bodies
    bodies = environment_setup.create_system_of_bodies(body_settings)

    ### VEHICLE BODY ###
    # Create vehicle object
    bodies.create_empty_body("Spacecraft")
    bodies.get_body("Spacecraft").set_constant_mass(400.0)

    # Create radiation pressure settings, and add to vehicle
    reference_area_radiation = 4.0
    radiation_pressure_coefficient = 1.2
    radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
        "Sun",
        reference_area_radiation,
        radiation_pressure_coefficient)
    environment_setup.add_radiation_pressure_interface(
        bodies,
        "Spacecraft",
        radiation_pressure_settings)

    return bodies


def get_acceleration_models(bodies_to_propagate: List[str],
                            central_bodies: List[str],
                            bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies) -> \
        Dict[str, Dict[str, List[tudatpy.kernel.astro.fundamentals.AccelerationModel]]]:
    """
    Creates the acceleration models for the simulation.

    The accelerations acting on the Spacecraft currently considered are the spherical harmonic gravity of Itokawa,
    the point mass gravity of the Sun, Jupiter, Saturn, Mars, the Earth, and the solar radiation pressure.

    Parameters
    ----------
    bodies_to_propagate : List[str]
        List of bodies to be numerically propagated.
    central_bodies: List[str]
        List of central bodies related to the propagated bodies.
    bodies : bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies
        System of bodies object

    Returns
    -------
    Dict[str, Dict[str, List[tudatpy.kernel.astro.fundamentals.AccelerationModel]]]
        Acceleration settings object.
    """
    # Define accelerations acting on Spacecraft
    accelerations_settings_spacecraft = dict(
        Sun=
        [
            propagation_setup.acceleration.cannonball_radiation_pressure(),
            propagation_setup.acceleration.point_mass_gravity()
        ],
        Itokawa=
        [
            propagation_setup.acceleration.spherical_harmonic_gravity(4, 4)
        ],
        Jupiter=
        [
            propagation_setup.acceleration.point_mass_gravity()
        ],
        Saturn=
        [
            propagation_setup.acceleration.point_mass_gravity()
        ],
        Mars=
        [
            propagation_setup.acceleration.point_mass_gravity()
        ],
        Earth=
        [
            propagation_setup.acceleration.point_mass_gravity()
        ]
    )

    # Create global accelerations settings dictionary
    acceleration_settings = {"Spacecraft": accelerations_settings_spacecraft}

    # Create acceleration models
    return propagation_setup.create_acceleration_models(
        bodies,
        acceleration_settings,
        bodies_to_propagate,
        central_bodies)


def get_termination_settings(mission_initial_time: float,
                             mission_duration: float,
                             minimum_distance_from_com: float,
                             maximum_distance_from_com: float):
    """
    Defines the termination settings for the simulation.

    Nominally, the simulation terminates when a final epoch is reached. However, this can happen in advance if the
    spacecraft breaks out of the predefined altitude range.

    Parameters
    ----------
    mission_initial_time : float
        Initial time from the reference epoch when initial kepler elements are defined.
    mission_duration : float
        Length of the simulation.
    minimum_distance_from_com : float
        Minimum distance Itokawa's center of mass.
    maximum_distance_from_com : float
        Maximum distance Itokawa's center of mass.

    Returns
    -------
    tudatpy.kernel.simulation.propagation_setup.propagator.PropagationTerminationSettings
        Termination settings object.
    """
    time_termination_settings = propagation_setup.propagator.time_termination(
        mission_initial_time + mission_duration,
        terminate_exactly_on_final_condition=False
    )
    # Altitude
    upper_altitude_termination_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings=propagation_setup.dependent_variable.relative_distance('Spacecraft', 'Itokawa'),
        limit_value=maximum_distance_from_com,
        use_as_lower_limit=False,
        terminate_exactly_on_final_condition=False
    )
    lower_altitude_termination_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings=propagation_setup.dependent_variable.altitude('Spacecraft', 'Itokawa'),
        limit_value=minimum_distance_from_com,
        use_as_lower_limit=True,
        terminate_exactly_on_final_condition=False
    )

    # Define list of termination settings
    termination_settings_list = [time_termination_settings,
                                 upper_altitude_termination_settings,
                                 lower_altitude_termination_settings]

    return propagation_setup.propagator.hybrid_termination(termination_settings_list,
                                                           fulfill_single_condition=True)


def get_dependent_variables_to_save():
    """
    Selects the dependent variables to be saved.

    Currently, these are the relative distance from Itokawa and the position of the spacecraft with respect to the
    asteroid expressed in spherical coordinates.

    Parameters
    ----------
    none

    Returns
    -------
    List[tudatpy.kernel.simulation.propagation_setup.dependent_variable.tp::SingleDependentVariableSaveSettings
    """
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.central_body_fixed_spherical_position(
            "Spacecraft", "Itokawa"
        )
    ]
    return dependent_variables_to_save


###########################################################################
# CREATE PYGMO-COMPATIBLE USER-DEFINED PROBLEM CLASS ######################
###########################################################################

class AsteroidOrbitProblem:
    """
    This class creates a PyGMO-compatible User Defined Problem (UDP).

    Attributes
    ----------


    Methods
    -------
    """

    def __init__(self,
                 bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
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
        bodies : tudatpy.kernel.simulation.environment_setup.SystemOfBodies:
            System of bodies.
        integrator_settings :
            Integrator settings object.
        propagator_settings :
            Propagator settings object.
        """
        # Sets input arguments as lambda function attributes
        # NOTE: this is done so that the class is "pickable", i.e., can be serialized by pygmo
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
        Defines the search space.

        Parameters
        ----------
        none

        Returns
        -------
        Tuple[List[float], List[float]]
            Two lists of size n (for this problem, n=4), defining respectively the lower and upper
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
        itokawa_gravitational_parameter = current_bodies.get_body("Itokawa").gravitational_parameter
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
        dynamics_simulator = propagation_setup.SingleArcDynamicsSimulator(current_bodies,
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


def main():
    """
    The problem describes the orbit design around a small body (asteroid Itokawa).

    DYNAMICAL MODEL
    Itokawa spherical harmonics, cannonball radiation pressure from Sun, point-mass third-body
    from Sun, Jupiter, Saturn, Earth, Mars

    PROPAGATION TIME
    5 days

    INTEGRATOR
    RKF7(8) with tolerances 1E-8

    TERMINATION CONDITIONS
    In addition to 5 day time, minimum distance from Itokaw's center of mass: 150 m (no crashing),
    maximum distance from center of mass: 5 km (no escaping)

    DESIGN VARIABLES
    Initial values of semi-major axis, eccentricity, inclination, and longitude of node

    OBJECTIVES
    1. good coverage: the mean value of the absolute longitude w.r.t. Itokawa over the full propagation should be
       maximized;
    2. close orbit: the mean value of the distance should be minimized.
    """
    ###########################################################################
    # CREATE SIMULATION SETTINGS ##############################################
    ###########################################################################

    # Load spice kernels
    spice_interface.load_standard_kernels()

    # Define Itokawa radius
    itokawa_radius = 161.915

    # Set simulation start and end epochs
    mission_initial_time = 0.0
    mission_duration = 5.0 * 86400.0

    # Set boundaries on the design variables
    design_variable_lb = (300, 0.0, 0.0, 0.0)
    design_variable_ub = (2000, 0.3, 180, 360)

    # Set termination conditions
    minimum_distance_from_com = 150.0 + itokawa_radius
    maximum_distance_from_com = 5.0E3 + itokawa_radius

    # Create simulation bodies
    bodies = create_simulation_bodies(itokawa_radius)

    ###########################################################################
    # CREATE ACCELERATIONS ####################################################
    ###########################################################################

    bodies_to_propagate = ["Spacecraft"]
    central_bodies = ["Itokawa"]

    # Create acceleration models.
    acceleration_models = get_acceleration_models(bodies_to_propagate, central_bodies, bodies)

    # Create numerical integrator settings.
    integrator_settings = propagation_setup.integrator.runge_kutta_variable_step_size(
        mission_initial_time, 1.0, propagation_setup.integrator.RKCoefficientSets.rkf_78,
        1.0E-6, 86400.0, 1.0E-8, 1.0E-8)

    ###########################################################################
    # CREATE PROPAGATION SETTINGS #############################################
    ###########################################################################

    # Define list of dependent variables to save
    dependent_variables_to_save = get_dependent_variables_to_save()

    # Create propagation settings
    termination_settings = get_termination_settings(
        mission_initial_time, mission_duration, minimum_distance_from_com, maximum_distance_from_com)

    # Define (Cowell) propagator settings with mock initial state
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        np.zeros(6),
        termination_settings,
        output_variables=dependent_variables_to_save
    )

    ###########################################################################
    # OPTIMIZE ORBIT WITH PYGMO ###############################################
    ###########################################################################

    # Fix seed for reproducibility
    fixed_seed = 17031861
    # Instantiate orbit problem
    orbitProblem = AsteroidOrbitProblem(bodies,
                                        integrator_settings,
                                        propagator_settings,
                                        mission_initial_time,
                                        mission_duration,
                                        design_variable_lb,
                                        design_variable_ub)

    # Select Moead algorithm from pygmo, with one generation
    algo = pg.algorithm(pg.nsga2(gen=1, seed=fixed_seed))
    # Create pygmo problem using the UDP instantiated above
    prob = pg.problem(orbitProblem)
    # Initialize pygmo population with 48 individuals
    population_size = 48
    pop = pg.population(prob, size=population_size, seed=fixed_seed)
    # Set the number of evolutions
    number_of_evolutions = 50
    # Initialize containers
    fitness_list = []
    population_list = []
    # Evolve the population recursively
    for gen in range(number_of_evolutions):
        print('Evolving population; at generation ' + str(gen))
        # Evolve the population
        pop = algo.evolve(pop)
        # Store the fitness values and design variables for all individuals
        fitness_list.append(pop.get_f())
        population_list.append(pop.get_x())

    ###########################################################################
    # ANALYZE FIRST AND LAST GENERATIONS ######################################
    ###########################################################################

    dump_results_to_file = False

    # Get output path
    output_path = os.getcwd() + '/PygmoExampleSimulationOutput/'

    # Retrieve first and last generations for further analysis
    pops_to_analyze = {0: 'initial',
                       number_of_evolutions - 1: 'final'}
    # Initialize containers
    simulation_output = dict()
    # Loop over first and last generations
    for population_index, population_name in pops_to_analyze.items():
        current_population = population_list[population_index]
        # Save fitness and population members
        if dump_results_to_file:
            # Create directory
            if not os.path.isdir(output_path):
                os.mkdir(output_path)
            np.savetxt(output_path + 'Fitness_' + population_name + '.dat', fitness_list[population_index])
            np.savetxt(output_path + 'Population_' + population_name + '.dat', population_list[population_index])
        # Current generation's dictionary
        generation_output = dict()
        # Loop over all individuals of the populations
        for individual in range(population_size):
            # Retrieve orbital parameters
            current_orbit_parameters = current_population[individual]
            # Propagate orbit and compute fitness
            orbitProblem.fitness(current_orbit_parameters)
            # Retrieve state and dependent variable history
            current_states = orbitProblem.get_last_run_dynamics_simulator().state_history
            current_dependent_variables = orbitProblem.get_last_run_dynamics_simulator().dependent_variable_history
            # Save results to dict
            generation_output[individual] = [current_states, current_dependent_variables]
            # Write data to files
            if dump_results_to_file:
                save2txt(current_dependent_variables,
                         population_name + '_dependent_variables' + str(individual) + '.dat',
                         output_path)
                save2txt(current_states,
                         population_name + '_states' + str(individual) + '.dat',
                         output_path)
        # Append to global dictionary
        simulation_output[population_index] = [generation_output,
                                               fitness_list[population_index],
                                               population_list[population_index]]

    ###########################################################################
    # ANALYZE RESULTS #########################################################
    ###########################################################################

    # Set font size for plots
    font = {'size': 12}
    matplotlib.rc('font', **font)

    # Create dictionaries
    decision_variable_names = {0: 'Semi-major axis [m]',
                               1: 'Eccentricity',
                               2: 'Inclination [deg]',
                               3: 'Longitude of the node [deg]'}
    decision_variable_range = {0: [800.0, 1300.0],
                               1: [0.10, 0.17],
                               2: [90.0, 95.0],
                               3: [250.0, 270.0]}
    decision_variable_symbols = {0: r'$a$',
                                 1: r'$e$',
                                 2: r'$i$',
                                 3: r'$\Omega$'}
    decision_variable_units = {0: r' m',
                               1: r' ',
                               2: r' deg',
                               3: r' deg'}
    # Loop over populations
    for population_index in simulation_output.keys():
        # Retrieve current population
        current_generation = simulation_output[population_index]
        # Plot Pareto fronts for all design variables
        fig, axs = plt.subplots(2, 2, figsize=(14, 8))
        fig.suptitle('Generation ' + str(population_index), fontweight='bold', y=0.95)
        current_fitness = current_generation[1]
        current_population = current_generation[2]
        for ax_index, ax in enumerate(axs.flatten()):
            cs = ax.scatter(np.deg2rad(current_fitness[:, 0]),
                            current_fitness[:, 1],
                            40,
                            current_population[:, ax_index],
                            marker='.')
            cbar = fig.colorbar(cs, ax=ax)
            cbar.ax.set_ylabel(decision_variable_names[ax_index])
            ax.grid('major')
            if ax_index > 1:
                ax.set_xlabel(r'Objective 1: coverage [$deg^{-1}$] ')
            if ax_index == 0 or ax_index == 2:
                ax.set_ylabel(r'Objective 2: proximity [$m$]')
        # Save figure
        fig.savefig('pareto_generation_' + str(population_index) + '.png', bbox_inches='tight')

    # Plot histogram for last generation, semi-major axis
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Final orbits by decision variable', fontweight='bold', y=0.95)
    last_pop = simulation_output[number_of_evolutions - 1][2]
    for ax_index, ax in enumerate(axs.flatten()):
        ax.hist(last_pop[:, ax_index], bins=30)
        # Prettify
        ax.set_xlabel(decision_variable_names[ax_index])
        if ax_index % 2 == 0:
            ax.set_ylabel('Occurrences in the population')
    # Save figure
    fig.savefig('histograms_final_generation.png', bbox_inches='tight')

    # Plot orbits of initial and final generation
    fig = plt.figure(figsize=(12, 6))
    fig.suptitle('Initial and final orbit bundle', fontweight='bold', y=0.95)
    title = {0: 'Initial orbit bundle',
             1: 'Final orbit bundle'}
    # Loop over populations
    for ax_index, population_index in enumerate(simulation_output.keys()):
        current_ax = fig.add_subplot(1, 2, 1 + ax_index, projection='3d')
        # Retrieve current population
        current_generation = simulation_output[population_index]
        current_population = current_generation[2]
        # Loop over individuals
        for ind_index, individual in enumerate(current_population):
            # Plot orbit
            state_history = list(current_generation[0][ind_index][0].values())
            state_history = np.vstack(state_history)
            current_ax.plot(state_history[:, 0],
                            state_history[:, 1],
                            state_history[:, 2],
                            linewidth=0.5)
        # Prettify
        current_ax.set_xlabel('X [m]')
        current_ax.set_ylabel('Y [m]')
        current_ax.set_zlabel('Z [m]')
        current_ax.set_title(title[ax_index], y=1.0, pad=15)
    # Save figure
    fig.savefig('orbit_bundles_initial_final_gen.png', bbox_inches='tight')

    # Plot orbits of final generation divided by parameters
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle('Final orbit bundle by decision variable', fontweight='bold', y=0.95)
    # Retrieve current population
    current_generation = simulation_output[number_of_evolutions - 1]
    # Plot Pareto fronts for all design variables
    current_population = current_generation[2]
    # Loop over decision variables
    for var in range(4):
        # Create axis
        current_ax = fig.add_subplot(2, 2, 1 + var, projection='3d')
        # Loop over individuals
        for ind_index, individual in enumerate(current_population):
            # Set plot color according to boundaries
            if individual[var] < decision_variable_range[var][0]:
                plt_color = 'r'
                label = decision_variable_symbols[var] + ' < ' + str(decision_variable_range[var][0]) + \
                        decision_variable_units[var]
            elif decision_variable_range[var][0] < individual[var] < decision_variable_range[var][1]:
                plt_color = 'b'
                label = str(decision_variable_range[var][0]) + ' < ' + \
                        decision_variable_symbols[var] + \
                        ' < ' + str(decision_variable_range[var][1]) + decision_variable_units[var]
            else:
                plt_color = 'g'
                label = decision_variable_symbols[var] + ' > ' + str(decision_variable_range[var][1]) + \
                        decision_variable_units[var]

            # Plot orbit
            state_history = list(current_generation[0][ind_index][0].values())
            state_history = np.vstack(state_history)
            current_ax.plot(state_history[:, 0],
                            state_history[:, 1],
                            state_history[:, 2],
                            color=plt_color,
                            linewidth=0.5,
                            label=label)
        # Prettify
        current_ax.set_xlabel('X [m]')
        current_ax.set_ylabel('Y [m]')
        current_ax.set_zlabel('Z [m]')
        current_ax.set_title(decision_variable_names[var], y=1.0, pad=10)
        handles, decision_variable_legend = current_ax.get_legend_handles_labels()
        decision_variable_legend, ids = np.unique(decision_variable_legend, return_index=True)
        handles = [handles[i] for i in ids]
        current_ax.legend(handles, decision_variable_legend, loc='lower right', bbox_to_anchor=(0.3, 0.6))
    # Save figure
    fig.savefig('orbit_bundle_final_gen_by_variable.png', bbox_inches='tight')

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
