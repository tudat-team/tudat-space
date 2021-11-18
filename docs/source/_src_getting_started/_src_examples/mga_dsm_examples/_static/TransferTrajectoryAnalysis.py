# General imports
import os
from typing import List, Tuple
import numpy as np

# Tudat imports
import BuildDirectory
from tudatpy.kernel import constants
from tudatpy.kernel.astro import trajectory_design, conversion
from tudatpy.kernel.simulation import environment_setup, astro_setup
from tudatpy.util import result2array
import TransferTrajectoryUtilities
import tudatpy

# Definition of default number of states per leg and per day
STATES_PER_LEG = 500
STATES_PER_DAY = 96

###########################################################################
def create_and_evaluate_transfer_trajectory (
        bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
        leg_type: tudatpy.kernel.astro.trajectory_design.TransferLegTypes,
        transfer_body_order: List[str],
        trajectory_parameters: List[float],
        departure_semi_major_axis: float = np.inf,
        departure_eccentricity: float = 0,
        arrival_semi_major_axis: float = np.inf,
        arrival_eccentricity: float = 0) -> tudatpy.kernel.astro.trajectory_design.TransferTrajectory:
    """
    Creation of transfer calculation object \n
    Assumptions: \n
    - Spacecraft departs/arrives at/from the edge of sphere of influence \n
    - Simplified system of bodies
    """

    # Define type of leg between bodies
    transfer_leg_settings, transfer_node_settings = trajectory_design.mga_transfer_settings(
        transfer_body_order,
        leg_type,
        departure_orbit = (departure_semi_major_axis, departure_eccentricity),
        arrival_orbit = (arrival_semi_major_axis, arrival_eccentricity) )

    # Create transfer calculation object
    transfer_trajectory = astro_setup.create_transfer_trajectory(bodies,
                                                                 transfer_leg_settings,
                                                                 transfer_node_settings,
                                                                 transfer_body_order,
                                                                 'Sun')

    # Convert list of trajectory parameters to appropriate format
    node_times, leg_free_parameters, node_free_parameters = convert_trajectory_parameters(transfer_trajectory,
                                                                                          leg_type,
                                                                                          trajectory_parameters)

    # Evaluate trajectory
    transfer_trajectory.evaluate(node_times, leg_free_parameters, node_free_parameters)

    return transfer_trajectory

###########################################################################
def convert_trajectory_parameters (transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                                   leg_type: tudatpy.kernel.astro.trajectory_design.TransferLegTypes,
                                   trajectory_parameters: List[float],
                                   ) -> Tuple[ List[float], List[List[float]], List[List[float]] ]:
    """
    Gets inputs for transfer object from list of trajectory parameters \n
    Trajectory parameters specified according to the following order: \n
    - For unpowered_unperturbed_leg_type: trajectory_parameters = [node_times] \n
    - For dsm_velocity_based_leg_type: trajectory_parameters = [node_times,node_free_parameters,leg_free_parameters]
    """

    # Check type of leg
    if leg_type == trajectory_design.dsm_position_based_leg_type:
        raise RuntimeError('Parameters conversion for DSM position-based leg not yet supported')

    # Declare lists of transfer parameters
    node_times = list()
    leg_free_parameters = list()
    node_free_parameters = list()

    # Rename number of nodes and legs
    number_of_nodes = transfer_trajectory.number_of_nodes
    number_of_legs = transfer_trajectory.number_of_legs

    # Extract from trajectory parameters the lists with each type of parameters
    traj_parameters_node_times = trajectory_parameters[0:number_of_nodes]
    if leg_type == trajectory_design.dsm_velocity_based_leg_type:
        traj_parameters_node_free_parameters = trajectory_parameters[
                                               number_of_nodes:number_of_nodes + 3 * (number_of_nodes - 1)]
        traj_parameters_leg_free_parameters = trajectory_parameters[
                                              number_of_nodes + 3 * (number_of_nodes - 1):]

    # Get node times
    # 0th element of parameters_list: departure time
    node_times.append(traj_parameters_node_times[0])
    # Other elements of parameters_list: time of flight -> need to calculate gravity assist date
    accumulated_time = traj_parameters_node_times[0]
    for i in range(1, number_of_nodes):
        accumulated_time += traj_parameters_node_times[i]
        node_times.append(accumulated_time)

    # Get leg_free_parameters and node_free_parameters for the different types of trajectories
    if leg_type == trajectory_design.unpowered_unperturbed_leg_type:
        # One empty array for each leg
        for i in range(number_of_legs):
            leg_free_parameters.append( [] )
        # One empty array for each node
        for i in range(number_of_nodes):
            node_free_parameters.append( [] )
    elif leg_type == trajectory_design.dsm_velocity_based_leg_type:
        for i in range(number_of_legs):
            leg_free_parameters.append( [traj_parameters_leg_free_parameters[i]] )
        for i in range(number_of_nodes - 1):
            node_free_parameters.append( traj_parameters_node_free_parameters[3 * i:3 * i + 3] )
        # One empty array for the last node
        node_free_parameters.append( [] )

    return node_times, leg_free_parameters, node_free_parameters


###########################################################################
def get_state_history(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                      bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                      reference_body: str = 'Sun',
                      states_per_leg: float = STATES_PER_LEG) -> Tuple[np.ndarray,np.ndarray]:
    """
    Returns the state history (and corresponding time history) with respect to the specified body as the tuple: \n
    - state_history, time_history
    Default values: \n
    - Reference body is the Sun
    - Number of states per leg
    """

    # Retrieve state and time history with respect to the Sun
    full_state_history_wrt_sun = result2array( transfer_trajectory.states_along_trajectory( states_per_leg ) )
    time_history_wrt_sun = full_state_history_wrt_sun[:,0]
    state_history_wrt_sun = full_state_history_wrt_sun[:, 1:]

    if reference_body == 'Sun':     # Return state history with respect to the Sun
        return state_history_wrt_sun,time_history_wrt_sun

    else:                            # Retrieve and return state history with respect to other body
        central_body = 'Sun'
        reference_body_state = np.zeros(np.shape(state_history_wrt_sun))
        central_body_state = np.zeros(np.shape(state_history_wrt_sun))

        # Retrieve state history of reference body and central body
        for i in range(np.size(time_history_wrt_sun)):
            reference_body_state[i, :] = \
                bodies.get_body(reference_body).get_state_in_based_frame_from_ephemeris(time_history_wrt_sun[i])
            central_body_state[i, :] = \
                bodies.get_body(central_body).get_state_in_based_frame_from_ephemeris(time_history_wrt_sun[i])

        state_history_wrt_reference_body = state_history_wrt_sun + central_body_state - reference_body_state

        return state_history_wrt_reference_body, time_history_wrt_sun

###########################################################################
def total_solar_flux(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                     bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                     states_per_leg: float = STATES_PER_LEG) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates total incident solar flux history. Returns it as the tuple: \n
    - total_solar_flux_history, time_history
    Default values: \n
    - Number of states per leg
    """

    state_history, time_history = get_state_history(transfer_trajectory, bodies, 'Sun',states_per_leg)
    total_solar_flux_history = TransferTrajectoryUtilities.total_solar_flux(state_history)

    return total_solar_flux_history, time_history

###########################################################################
def _angle_of_incidence(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                        bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                        solar_array_orientation_reference: str,
                        states_per_leg: float = STATES_PER_LEG) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates the angle of the incident solar radiation with respect to a direction normal to the solar arrays.
    Returns it as the tuple: \n
    - angle_incidence_history, time_history
    Inputs: \n
    - solar_array_orientation_reference: direction perpendicular to solar array. Possibilities: Velocity, Sun,
    planets of solar system
    Default values: \n
    - Number of states per leg (see documentation for value)
    """

    state_history, time_history = get_state_history(transfer_trajectory, bodies, 'Sun', states_per_leg)

    if solar_array_orientation_reference == 'Velocity':
        normal_vector = state_history[:, 3:]
    elif solar_array_orientation_reference == 'Sun':
        normal_vector = -state_history[:, 0:3]
    elif solar_array_orientation_reference in {'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                                               'Neptune', 'Pluto'}:
        state_history_wrt_planet = get_state_history(transfer_trajectory, bodies, solar_array_orientation_reference,
                                                     states_per_leg)[0]
        normal_vector = -state_history_wrt_planet[:, 0:3]
    else:
        raise RuntimeError('Invalid reference for solar array orientation')

    angle_of_incidence_history = TransferTrajectoryUtilities.angle_wrt_normal_vector_history(state_history,
                                                                                             normal_vector)

    return angle_of_incidence_history, time_history

###########################################################################
def effective_solar_flux(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                         bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                         solar_array_orientation_reference: str,
                         states_per_leg: float = STATES_PER_LEG) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates the effective solar flux, i.e. the solar flux perpendicular to the solar array.
    Returns it as the tuple: \n
    - effective_solar_flux_history, time_history
    Inputs: \n
    - solar_array_orientation_reference: direction perpendicular to solar array. Possibilities: Velocity, Sun,
    planets of solar system
    Default values: \n
    - Number of states per leg
    """

    time_history = get_state_history(transfer_trajectory, bodies, 'Sun', states_per_leg)[1]

    angle_of_incidence_history = _angle_of_incidence(transfer_trajectory, bodies, solar_array_orientation_reference,
                                                     states_per_leg)[0]

    solar_flux_history = total_solar_flux(transfer_trajectory, bodies, states_per_leg)[0]

    effective_solar_flux_history = TransferTrajectoryUtilities.effective_solar_flux(solar_flux_history,
                                                                                    angle_of_incidence_history)

    return effective_solar_flux_history, time_history

###########################################################################
def link_budget(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                frequency: float,
                transmited_power: float,
                transmiter_antenna_gain: float,
                receiver_antenna_gain: float,
                reference_body: str = 'Earth',
                states_per_leg: float = STATES_PER_LEG) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates link budget with respect to the specified reference body. Returns it as the tuple: \n
    - link_budget_history, time_history
    Default values: \n
    - Earth as reference body
    - Number of states per leg (see documentation for value)
    """
    state_history_wrt_reference_body, time_history = get_state_history(transfer_trajectory, bodies,
                                                                       reference_body, states_per_leg)

    link_budget_history = TransferTrajectoryUtilities.link_budget(state_history_wrt_reference_body, frequency,
                                                                  transmited_power, transmiter_antenna_gain,
                                                                  receiver_antenna_gain)

    return link_budget_history, time_history

###########################################################################
def add_ground_station_simple(bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                              station_name: str,
                              ground_station_latitude: float,
                              ground_station_longitude: float):
    """
    Adds ground station to the list of bodies; function with simplified inputs. Assumes: \n
    - Ground station located on Earth
    - Location of ground station specified by its latitude and longitude (in radians)
    - Location of ground station specified with geocentric coordinates (spherical position)
    """

    ground_station_body = 'Earth'
    position_type = conversion.spherical_position_type
    ground_station_position = [constants.EARTH_EQUATORIAL_RADIUS, ground_station_latitude, ground_station_longitude]

    ground_station_body = bodies.get_body(ground_station_body)
    environment_setup.add_ground_station(ground_station_body, station_name, ground_station_position, position_type)

###########################################################################
def communications_time_per_day(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
                                bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                                station_name: str,
                                minimum_elevation: float) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates the time available for communications per day. Returns it as the tuple: \n
    - comms_time_per_day_history, time_history
    """

    state_history, time_history = get_state_history(transfer_trajectory, bodies)

    # Determine elevation time history (for the calculation of the elevations)
    # Recommended value of states per day: at least 4 per hour (96 per day)
    elevation_time_history = np.arange(time_history[0],time_history[-1],constants.JULIAN_DAY/STATES_PER_DAY)

    comms_time_per_day_history, comms_time_history = TransferTrajectoryUtilities.communications_time_per_day(
        bodies, state_history, time_history, elevation_time_history, station_name, minimum_elevation)

    return comms_time_per_day_history, comms_time_history

###########################################################################
def elevation(transfer_trajectory: tudatpy.kernel.astro.trajectory_design.TransferTrajectory,
              bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
              station_name: str) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates elevation. Returns it as the tuple: \n
    - elevation_history, time_history
    """

    state_history, time_history = get_state_history(transfer_trajectory, bodies)

    # Determine elevation time history (for the calculation of the elevations)
    elevation_time_history = np.arange(time_history[0], time_history[-1], constants.JULIAN_DAY / STATES_PER_DAY)

    elevation_history = TransferTrajectoryUtilities.elevation(bodies, state_history, time_history,
                                                              elevation_time_history, station_name)

    return elevation_history, elevation_time_history