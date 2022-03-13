"""
Copyright (c) 2010-2022, Delft University of Technology
All rights reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

TUDATPY EXAMPLE APPLICATION: Mulitple Gravity Assist and Deep Space Maneuver transfers
FOCUS:                       Analysis of MGA-DSM transfer trajectories
"""

###############################################################################
# TUDATPY EXAMPLE APPLICATION: MGA-DSM transfers                   ############
###############################################################################

""" ABSTRACT.

This example demonstrates how Multiple Gravity Assist (MGA) transfer trajectories 
 with, or without, Deep Space Maneuvers (DSM) can be simulated. Both an example with 
 and an example without DSMs is provided. 
In addition, these example show how the result, such as Delta V and Time of Flight
 values can be retrieved from the transfer object.

"""


###############################################################################
# IMPORT STATEMENTS ###########################################################
###############################################################################
import numpy as np
import matplotlib.pyplot as plt
from tudatpy.kernel.trajectory_design import transfer_trajectory
from tudatpy.kernel.numerical_simulation import environment_setup
from tudatpy.util import result2array
from tudatpy.kernel import constants


def mga_without_dsm():

    ###########################################################################
    # DEFINE TRANSFER SETTINGS ################################################
    ###########################################################################

    # Simplified bodies
    bodies = environment_setup.create_simplified_system_of_bodies()
    central_body = 'Sun'

    # Define order of bodies (nodes) for gravity assists
    transfer_body_order = [
        'Earth', 'Venus', 'Venus', 'Earth',  'Jupiter',  'Saturn']

    # Define departure and insertion orbit
    departure_semi_major_axis = np.inf
    departure_eccentricity = 0.

    arrival_semi_major_axis = 1.0895e8 / 0.02
    arrival_eccentricity = 0.98

    # Define type of leg between bodies
    leg_type = transfer_trajectory.unpowered_unperturbed_leg_type

    ###########################################################################
    # CREATE TRANSFER SETTINGS AND OBJECT #####################################
    ###########################################################################

    # Define trajectory settings
    transfer_leg_settings, transfer_node_settings = transfer_trajectory.mga_transfer_settings(
        transfer_body_order,
        leg_type,
        departure_orbit=(departure_semi_major_axis, departure_eccentricity),
        arrival_orbit=(arrival_semi_major_axis, arrival_eccentricity))

    # Create transfer calculation object
    transfer_trajectory_object = transfer_trajectory.create_transfer_trajectory(
        bodies,
        transfer_leg_settings,
        transfer_node_settings,
        transfer_body_order,
        central_body)

    ###########################################################################
    # DEFINE TRANSFER PARAMETERS ##############################################
    ###########################################################################

    # Define times at each node
    julian_day = constants.JULIAN_DAY
    node_times = list()
    node_times.append((-789.8117 - 0.5) * julian_day)
    node_times.append(node_times[0] + 158.302027105278 * julian_day)
    node_times.append(node_times[1] + 449.385873819743 * julian_day)
    node_times.append(node_times[2] + 54.7489684339665 * julian_day)
    node_times.append(node_times[3] + 1024.36205846918 * julian_day)
    node_times.append(node_times[4] + 4552.30796805542 * julian_day)
    
    # Define free parameters per leg (now: none)
    leg_free_parameters = list()
    for i in range(len(transfer_body_order)-1):
        leg_free_parameters.append(np.zeros(0))

    # Define free parameters per node (now: none)
    node_free_parameters = list()
    for i in range(len(transfer_body_order)):
        node_free_parameters.append(np.zeros(0))

    ###########################################################################
    # EVALUATE TRANSFER #######################################################
    ###########################################################################

    # Evaluate transfer with given parameters
    transfer_trajectory_object.evaluate(node_times, leg_free_parameters, node_free_parameters)

    # Extract and print computed Delta V and time of flight
    print('Delta V [m/s]: ', transfer_trajectory_object.delta_v)
    print('Time of flight [day]: ', transfer_trajectory_object.time_of_flight / julian_day)
    print()
    print('Delta V per leg [m/s] : ', transfer_trajectory_object.delta_v_per_leg)
    print('Delta V per node [m/s] : ', transfer_trajectory_object.delta_v_per_node)

    transfer_trajectory.print_parameter_definitions(transfer_leg_settings, transfer_node_settings)

    # Extract and plot state history
    state_history = transfer_trajectory_object.states_along_trajectory(500)
    fly_by_states = np.array([state_history[node_times[i]] for i in range(len(node_times))])
    state_history = result2array(state_history)
    au = 1.5e11

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(state_history[:, 1] / au, state_history[:, 2] / au, state_history[:, 3] / au)
    ax.scatter(fly_by_states[0, 0] / au, fly_by_states[0, 1] / au, fly_by_states[0, 2] / au, color='blue', label='Earth departure')
    ax.scatter(fly_by_states[1, 0] / au, fly_by_states[1, 1] / au, fly_by_states[1, 2] / au, color='brown', label='Venus fly-by')
    ax.scatter(fly_by_states[2, 0] / au, fly_by_states[2, 1] / au, fly_by_states[2, 2] / au, color='brown', label='Venus fly-by')
    ax.scatter(fly_by_states[3, 0] / au, fly_by_states[3, 1] / au, fly_by_states[3, 2] / au, color='green', label='Earth fly-by')
    ax.scatter(fly_by_states[4, 0] / au, fly_by_states[4, 1] / au, fly_by_states[4, 2] / au, color='peru', label='Jupiter fly-by')
    ax.scatter(fly_by_states[5, 0] / au, fly_by_states[5, 1] / au, fly_by_states[5, 2] / au, color='red', label='Saturn arrival')
    ax.scatter([0], [0], [0], color='orange', label='Sun')
    ax.set_xlabel('x wrt Sun [AU]')
    ax.set_ylabel('y wrt Sun [AU]')
    ax.set_zlabel('z wrt Sun [AU]')
    ax.set_xlim([-10.5, 2.5])
    ax.set_ylim([-8.5, 4.5])
    ax.set_zlim([-6.5, 6.5])
    ax.legend(bbox_to_anchor=[1.15, 1])
    plt.show()

    return 0

def mga_with_dsm( ):

    ###########################################################################
    # DEFINE TRANSFER SETTINGS ################################################
    ###########################################################################

    # Simplified bodies
    bodies = environment_setup.create_simplified_system_of_bodies()

    # Define order of bodies (nodes)
    transfer_body_order = ['Earth', 'Earth', 'Venus', 'Venus',  'Mercury']

    # Define type of leg between bodies
    leg_type = transfer_trajectory.dsm_velocity_based_leg_type

    ###########################################################################
    # CREATE TRANSFER SETTINGS AND OBJECT #####################################
    ###########################################################################

    # Define type of leg between bodies
    transfer_leg_settings, transfer_node_settings = transfer_trajectory.mga_transfer_settings(
        transfer_body_order,
        leg_type,
        departure_orbit=(np.inf, 0.0),
        arrival_orbit=(np.inf, 0.0))

    # Create transfer calculation object
    transfer_trajectory_object = transfer_trajectory.create_transfer_trajectory(
        bodies,
        transfer_leg_settings,
        transfer_node_settings,
        transfer_body_order,
        'Sun')

    ###########################################################################
    # DEFINE TRANSFER PARAMETERS ##############################################
    ###########################################################################

    # Define times at each node
    julian_day = constants.JULIAN_DAY
    node_times = list()
    node_times.append((1171.64503236 - 0.5) * julian_day)
    node_times.append(node_times[0] + 399.999999715 * julian_day)
    node_times.append(node_times[1] + 178.372255301 * julian_day)
    node_times.append(node_times[2] + 299.223139512 * julian_day)
    node_times.append(node_times[3] + 180.510754824 * julian_day)

    # Define free parameters per leg
    leg_free_parameters = list()
    leg_free_parameters.append(np.array([0.234594654679]))
    leg_free_parameters.append(np.array([0.0964769387134]))
    leg_free_parameters.append(np.array([0.829948744508]))
    leg_free_parameters.append(np.array([0.317174785637]))

    # Define free parameters per node
    node_free_parameters = list()
    node_free_parameters.append(np.array([1408.99421278, 0.37992647165 * 2.0 * 3.14159265358979, np.arccos(2.0 * 0.498004040298 - 1.0) - 3.14159265358979 / 2.0]))
    node_free_parameters.append(np.array([1.80629232251 * 6.378e6, 1.35077257078, 0.0]))
    node_free_parameters.append(np.array([3.04129845698 * 6.052e6, 1.09554368115, 0.0]))
    node_free_parameters.append(np.array([1.10000000891 * 6.052e6, 1.34317576594, 0.0]))
    node_free_parameters.append(np.array([]))

    ###########################################################################
    # EVALUATE TRANSFER #######################################################
    ###########################################################################

    # Evaluate transfer with given parameters
    transfer_trajectory_object.evaluate( node_times, leg_free_parameters, node_free_parameters)

    # Extract and print computed Delta V and time of flight
    print('Delta V [m/s]: ', transfer_trajectory_object.delta_v)
    print('Time of flight [day]: ', transfer_trajectory_object.time_of_flight / julian_day)
    print()
    print('Delta V per leg [m/s] : ', transfer_trajectory_object.delta_v_per_leg)
    print('Delta V per node [m/s] : ', transfer_trajectory_object.delta_v_per_node)

    transfer_trajectory.print_parameter_definitions(transfer_leg_settings, transfer_node_settings)

    # Extract and plot state history
    state_history = transfer_trajectory_object.states_along_trajectory(500)
    fly_by_states = np.array([state_history[node_times[i]] for i in range(len(node_times))])
    state_history = result2array(state_history)
    au = 1.5e11

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(state_history[:, 1] / au, state_history[:, 2] / au)
    ax.scatter(fly_by_states[0, 0] / au, fly_by_states[0, 1] / au, color='blue', label='Earth departure')
    ax.scatter(fly_by_states[1, 0] / au, fly_by_states[1, 1] / au, color='green', label='Earth fly-by')
    ax.scatter(fly_by_states[2, 0] / au, fly_by_states[2, 1] / au, color='brown', label='Venus fly-by')
    ax.scatter(fly_by_states[3, 0] / au, fly_by_states[3, 1] / au, color='brown')
    ax.scatter(fly_by_states[4, 0] / au, fly_by_states[4, 1] / au, color='grey', label='Mercury arrival')
    ax.scatter([0], [0], color='orange', label='Sun')
    ax.set_xlabel('x wrt Sun [AU]')
    ax.set_ylabel('y wrt Sun [AU]')
    ax.set_aspect('equal')
    ax.legend(bbox_to_anchor=[1, 1])
    plt.show()

    return 0


if __name__ == "__main__":
    mga_without_dsm()
    mga_with_dsm()
