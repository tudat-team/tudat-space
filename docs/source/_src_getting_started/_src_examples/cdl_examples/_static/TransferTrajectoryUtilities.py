# General imports
from typing import List, Tuple
import numpy as np
from scipy.interpolate import interp1d
import os

# Tudat imports
import BuildDirectory
from tudatpy.kernel import constants
from tudatpy.kernel.simulation import environment_setup
from tudatpy.util import result2array
from tudatpy.kernel.math import interpolators
from tudatpy.kernel.astro import trajectory_design
import tudatpy

# CDL imports
from constants import SOLAR_LUMINOSITY

###########################################################################
def norm_history (vector_history: np.ndarray) -> np.ndarray:
    """
    Calculate the norm history of a vector history
    """

    num_cols = np.size(vector_history,axis=1)
    if num_cols == 0:
        return np.array([])
    else:
        for i in range(num_cols):
            if i == 0:
                sum_square = vector_history[:,i]**2
            else:
                sum_square = sum_square + vector_history[:, i] ** 2

        norm = np.sqrt(sum_square)

        return norm

###########################################################################
def total_solar_flux (state_history_wrt_sun: np.ndarray) -> np.ndarray:
    """
    Calculates total incident solar flux history
    State history given as argument should be with respect to Sun!
    """
    position_history = state_history_wrt_sun[:,0:3]
    distance_to_sun = norm_history(position_history)

    solar_flux_history = SOLAR_LUMINOSITY / (4 * np.pi * distance_to_sun**2)

    return solar_flux_history

###########################################################################
def angle_wrt_normal_vector (incident_radiation_vector: np.ndarray,
                             normal_vector:  np.ndarray) -> float:
    """
    Calculates the angle between an incident_radiation_vector and a normal vector, assuming both sides of the solar
    array can receive radiation. I.e. function calculates the minimum angle between incident_radiation_vector and
    normal_vector or -normal_vector. \n
    incident_radiation_vector - assumed to start on the spacecraft (although I don't think that makes a difference)
    """

    # Calculate normalized vectors - reduces numerical errors (?)
    incident_radiation_vector = incident_radiation_vector / np.linalg.norm(incident_radiation_vector)
    normal_vector = normal_vector / np.linalg.norm(normal_vector)

    # Calculate arccos
    angle_arccos = np.dot(incident_radiation_vector,normal_vector) / \
                   (np.linalg.norm(incident_radiation_vector) * np.linalg.norm(normal_vector) )
    # Calculate angle. Manually select value for boundary cases to deal with numerical errors
    if angle_arccos > 1:
        angle_of_incidence = 0
    elif angle_arccos < -1:
        angle_of_incidence = np.pi
    else:
        angle_of_incidence = np.arccos(angle_arccos)

    # If angle of incidence > pi/2, the sun is hitting the other side of the solar array
    if angle_of_incidence > np.pi/2:
        angle_of_incidence = np.pi - angle_of_incidence

    return angle_of_incidence

###########################################################################
def angle_wrt_normal_vector_history (state_history_wrt_sun: np.ndarray,
                                     normal_vector: np.ndarray) -> np.ndarray:
    """
    Calculates history of angle between incident radiation and normal vector
    """
    position_history = state_history_wrt_sun[:, 0:3]

    num_lines = np.size(position_history, axis=0)
    angle_of_incidence_history = np.ndarray((num_lines,1))

    for i in range(num_lines):
        angle_of_incidence_history[i] = angle_wrt_normal_vector(-position_history[i,:],normal_vector[i,:])

    return angle_of_incidence_history

###########################################################################
def effective_solar_flux (solar_flux_history: np.ndarray,
                          angle_of_incidence_history: np.ndarray) -> np.ndarray:
    """
    Calculates the effective solar flux, i.e. the solar flux perpendicular to the solar array
    """

    effective_solar_flux_history = np.ndarray((np.size(solar_flux_history), 1))

    for i in range(np.size(solar_flux_history)):
        effective_solar_flux_history[i] = solar_flux_history[i] * np.cos(angle_of_incidence_history[i])

    return effective_solar_flux_history

###########################################################################
def link_budget (state_history_wrt_reference_body: np.ndarray,
                 frequency: float,
                 transmited_power: float,
                 transmiter_antenna_gain: float,
                 receiver_antenna_gain: float) -> np.ndarray:
    """
    Calculates link budget
    """

    distance_to_antenna_body_history = norm_history(state_history_wrt_reference_body[:,0:3])

    wavelength = constants.SPEED_OF_LIGHT / frequency

    link_budget_history = transmited_power * transmiter_antenna_gain * receiver_antenna_gain * wavelength ** 2 / \
                          (4 * np.pi * distance_to_antenna_body_history) ** 2

    return link_budget_history

# ###########################################################################
# def add_ground_station(bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
#                        ground_station_body: str,
#                        station_name: str,
#                        position_type_name: str,
#                        ground_station_position: List[float]):
#     """
#     Adds ground station to the list of bodies. \n
#     See old documentation for description of ground_station_position parameters. \n
#     Old documentation: http://tudat.tudelft.nl/tutorials/tudatFeatures/estimationSetup/linkEndSetup.html?highlight=geodetic#ground-station-creation
#     """
#
#     if position_type_name == 'cartesian_position_type':
#         position_type = conversion.cartesian_position_type
#     elif position_type_name == 'spherical_position_type':
#         position_type = conversion.spherical_position_type
#     elif position_type_name == 'geodetic_position_type':
#         position_type = conversion.geodetic_position_type
#     else:
#         raise RuntimeError('Invalid position type')
#
#     ground_station_body = bodies.get_body(ground_station_body)
#     environment_setup.add_ground_station(ground_station_body, station_name, ground_station_position, position_type)
#
# ###########################################################################
# def add_ground_station_simple (bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
#                                station_name: str,
#                                station_latitude: float,
#                                station_longitude: float):
#     """
#     Adds ground station to the list of bodies; function with simplified inputs. Assumes: \n
#     - Ground station located on Earth
#     - Location of ground station specified by its latitude and longitude (in radians)
#     - Location of ground station specified with geocentric coordinates (spherical position)
#     """
#     ground_station_body = 'Earth'
#     position_type_name = 'spherical_position_type'
#     ground_station_position = [constants.EARTH_EQUATORIAL_RADIUS,station_latitude,station_longitude]
#
#     add_ground_station(bodies,ground_station_body,station_name,position_type_name,ground_station_position)

###########################################################################
def state_history_nparray2dict (state_history: np.ndarray,
                                time_history: np.ndarray) -> dict:
    """
    Converts the state_history and time_history (which are np.ndarray) to a single dict, with the time_history as keys
    """
    full_state_history_dict = dict()

    for i in range(np.size(time_history)):
        full_state_history_dict[time_history[i]] = state_history[i,:]

    return full_state_history_dict

###########################################################################
def add_vehicle(bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                state_history: np.ndarray,
                time_history: np.ndarray,
                spacecraft_name: str):
    """
    Adds vehicle to list of bodies defines its ephemeris
    Ephemeris interpolator uses a 6th order Lagrange interpolator (selected 6th order because that's what
    the interpolated spice ephemeris use)
    """

    # Create vehicle object
    bodies.create_empty_body(spacecraft_name)
    environment_setup.add_empty_tabulate_ephemeris(bodies, spacecraft_name)

    # Get full state history as dictionary
    full_state_history_dict = state_history_nparray2dict(state_history,time_history)

    # Create interpolator
    interpolator_settings = interpolators.lagrange_interpolation(6)
    interpolator = interpolators.create_one_dimensional_interpolator_Vector6d(full_state_history_dict,
                                                                              interpolator_settings)

    # Define interpolator used in ephemeris
    ephemeris_object = bodies.get_body("Vehicle").ephemeris
    ephemeris_object.reset_interpolator(interpolator)

###########################################################################
# I think the small jumps in the comms time per day happen because the period of the elevation is slightly different
# from 1 julian day. Therefore, in different dates slightly different parts of the elevation function are selected in
# each day, thus sometimes leading to the steps in the comms time.
def calculate_communications_time_per_day (elevation_angles: np.ndarray,
                                           time_history: np.ndarray,
                                           minimum_elevation: float) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculate time available for communications per day. Returns it as the tuple: \n
    - comms_time_per_day_history, time_history
    Time for communications calculated using linear interpolation
    """

    # Initialize dictionary that will keep the time available for communications per day
    comms_time_per_day = dict()
    time_history = time_history

    # Select beggining of first day
    day = time_history[0]
    next_day = day + constants.JULIAN_DAY

    # Loop through all states
    # Variables used:
    # i - last state before start of day
    # j - last state before end of day
    # k - auxiliar variable, that is incremented from i to j
    i = 0
    while i < np.size(time_history):

        # Initialize communications time in the day
        comms_time_per_day[day] = 0

        # Select j as being the last data point before the start of the next day
        j = i
        while time_history[j] < next_day and j < np.size(time_history) - 1:
            j += 1
        # If last day of time_history has been reached, comms time is not calculated
        if j == np.size(time_history) - 1:
            break
        j -= 1

        # Get communications time between i and i+1
        comms_time_per_day[day] += comms_leftBoundary_to_stateX(elevation_angles,time_history,minimum_elevation,i+1,day)

        # Loop trough the states in the day using auxiliary variable k. Do that to calculate the time available for
        # communications between i+1 and j
        k = i+1
        while k < j:
            comms_time_per_day[day] += comms_stateX_to_stateXPlus1(elevation_angles, time_history, minimum_elevation, k)
            k += 1

        # Get communications time between j and j+1
        comms_time_per_day[day] += comms_stateX_to_rightBoundary(elevation_angles,time_history,minimum_elevation,j,next_day)

        # Select variables for next day
        i = j
        day = next_day
        next_day += constants.JULIAN_DAY
    # End of while

    # Remove first element of dictionary (because it was initialized slightly different wrt the others)
    comms_time_per_day.pop(time_history[0],None)
    # Remove last element of dictionary, as it just has the value 0
    comms_time_per_day.pop(day,None)

    comms_per_day_and_time_history = result2array(comms_time_per_day)
    comms_time_history = comms_per_day_and_time_history[:,0]
    comms_time_per_day = comms_per_day_and_time_history[:,1]

    return comms_time_per_day, comms_time_history

###########################################################################
def linear_interpolation (x1: float,
                          x2: float,
                          y1: float,
                          y2: float,
                          x3: float) -> float:
    """
    Executes linear interpolation between (x1,y1) and (x2,y2), returning y3
    """

    f_linear = interp1d([x1, x2], [y1, y2])
    y3 = float(f_linear(x3))

    return y3

###########################################################################
def comms_leftBoundary_to_rightBoundary (left_elevation: float,
                                         left_time: float,
                                         right_elevation: float,
                                         right_time: float,
                                         minimum_elevation: float) -> float:
    """
    Calculates the time available for communications between a left (elevation, time) pair and a right (elevation, time)
    pair
    """

    if left_time > right_time:
        raise RuntimeError('left_time should be smaller than right_time')

    if left_time == right_time:
        comms_time = 0
    elif left_elevation < minimum_elevation and right_elevation < minimum_elevation:
        comms_time = 0
    elif left_elevation > minimum_elevation and right_elevation > minimum_elevation:
        comms_time = right_time - left_time
    else:
        comms_boundary_time = linear_interpolation(left_elevation, right_elevation, left_time, right_time,
                                                   minimum_elevation)

        if left_elevation > minimum_elevation and right_elevation < minimum_elevation:
            comms_time = comms_boundary_time - left_time
        else:
            comms_time = right_time - comms_boundary_time

    return comms_time

###########################################################################
def comms_stateX_to_stateXPlus1 (elevation_angles: np.ndarray,
                                 time_history: np.ndarray,
                                 minimum_elevation: float,
                                 x: int) -> float:
    """
    Calculates the time available for communications between state x and state x+1
    """

    left_elevation = elevation_angles[x]
    left_time = time_history[x]
    right_elevation = elevation_angles[x+1]
    right_time = time_history[x+1]

    comms_time = comms_leftBoundary_to_rightBoundary(left_elevation, left_time, right_elevation, right_time,
                                                     minimum_elevation)

    return comms_time

###########################################################################
def comms_leftBoundary_to_stateX (elevation_angles: np.ndarray,
                                  time_history: np.ndarray,
                                  minimum_elevation: float,
                                  x: int,
                                  left_time: float) -> float:
    """
    Calculates communications time between a left boundary and state x. The left boundary time is located between time
    x-1 and time x
    """

    left_elevation = linear_interpolation(time_history[x-1], time_history[x],
                                          elevation_angles[x-1], elevation_angles[x],
                                          left_time)
    right_time = time_history[x]
    right_elevation = elevation_angles[x]

    comms_time = comms_leftBoundary_to_rightBoundary(left_elevation, left_time, right_elevation, right_time,
                                                     minimum_elevation)

    return comms_time

###########################################################################
def comms_stateX_to_rightBoundary (elevation_angles: np.ndarray,
                                   time_history: np.ndarray,
                                   minimum_elevation: float,
                                   x: int,
                                   right_time: float) -> float:
    """
    Calculates communications time between a state x and a right boundary. The right boundary time is located between
    time x and time x+1
    """

    right_elevation = linear_interpolation(time_history[x], time_history[x+1],
                                           elevation_angles[x], elevation_angles[x+1],
                                           right_time)

    left_time = time_history[x]
    left_elevation = elevation_angles[x]

    comms_time = comms_leftBoundary_to_rightBoundary(left_elevation, left_time, right_elevation, right_time,
                                                     minimum_elevation)

    return comms_time

###########################################################################
def communications_time_per_day (bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
                                 state_history: np.ndarray,
                                 time_history: np.ndarray,
                                 elevation_time_history: np.ndarray,
                                 station_name: str,
                                 minimum_elevation: float) -> Tuple[np.ndarray,np.ndarray]:
    """
    Calculates and returns time available for communications per day. Returns it as the tuple: \n
    - comms_time_per_day_history, time_history
    Inputs: \n
    - state_history and time_history: used to create the interpolator necessary for calculating the elevation
    - elevation_time_history: time history of the retrieved elevations
    """

    # Create vehicle object
    spacecraft_name = "Vehicle"
    add_vehicle(bodies, state_history, time_history, spacecraft_name)

    # Retrieve elevation history
    elevation_history = environment_setup.get_target_elevation_angles(bodies.get_body("Earth"),
                                                                      bodies.get_body(spacecraft_name),
                                                                      station_name,
                                                                      elevation_time_history)
    elevation_history = np.array(elevation_history)

    # Calculate time available for communications
    comms_time_per_day, comms_time_history = calculate_communications_time_per_day(elevation_history,
                                                                                   elevation_time_history,
                                                                                   minimum_elevation)

    return comms_time_per_day, comms_time_history

###########################################################################
def elevation (bodies: tudatpy.kernel.simulation.environment_setup.SystemOfBodies,
               state_history: np.ndarray,
               time_history: np.ndarray,
               elevation_time_history: np.ndarray,
               station_name: str) -> np.ndarray:
    """
    Calculates and returns elevation history \n
    Inputs: \n
    - state_history and time_history: used to create the interpolator necessary for calculating the elevation
    - elevation_time_history: time history of the retrieved elevations
    """

    # Create vehicle object
    spacecraft_name = "Vehicle"
    add_vehicle(bodies, state_history, time_history, spacecraft_name)

    # Retrieve elevation history
    elevation_history = environment_setup.get_target_elevation_angles(bodies.get_body("Earth"),
                                                                      bodies.get_body(spacecraft_name),
                                                                      station_name,
                                                                      elevation_time_history)
    elevation_history = np.array(elevation_history)

    return elevation_history

###########################################################################
def get_all_pareto_info(costs: np.ndarray,
                        trajectory_parameters: np.ndarray):
    """
    Returns the individuals that form a Pareto front and returns the corresponding fitness values and trajectory parameters
    """
    is_efficient = np.ones(costs.shape[0], dtype=bool)

    pareto = []
    pareto_parameters = []

    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i] >= c, axis=1)) and np.all(np.any(costs[i + 1:] >= c, axis=1))
        if is_efficient[i] == 1:
            pareto.append(list(costs[i, :]))
            pareto_parameters.append(list(trajectory_parameters[i, :]))

    pareto = np.asarray(pareto)
    pareto_parameters = np.asarray(pareto_parameters)

    order = pareto[:, 1].argsort()

    pareto = pareto[order]
    pareto_parameters = pareto_parameters[order]

    return pareto, pareto_parameters


###########################################################################
def get_user_input_for_analysis(transfer_body_orders: List[str]):
    """
    Lets the user input info about the solutions (s)he wants to exploit further
    """
    input_correct = False
    while input_correct == False:
        print()
        print('------------------------------------------------------')
        if len(transfer_body_orders) == 1:
            desired_body_order = 0
        else:
            print()
            print('You have the following transfer body orders available: ')
            for i in range( len(transfer_body_orders) ):
                print(f'{i}: ',transfer_body_orders[i])
            print()
            desired_body_order = input('Provide the list index (0 to ' + str(
                len(transfer_body_orders) - 1) + ') of the transfer body order that you wish: ')

        try:
            desired_body_order = int(desired_body_order)
        except:
            print('Bad input, an integer is required, please specify again')
            continue

        if (desired_body_order > (len(transfer_body_orders) - 1)) or (desired_body_order < 0):
            print('There are ', len(transfer_body_orders),
                  ' transfer body orders, please choose a value from 0 to ', (len(transfer_body_orders) - 1))
            continue

        desired_type = input("Do you want to specify the desired delta v (dv) or time of flight (tof)? ")

        if desired_type == 'dv':
            print()
            desired_values = input('Provide your desired delta v (km/s) (you can specify multiple, to do so separate '
                                   'each with a comma: ')

            try:
                desired_values = [float(desired_value) * 1000 for desired_value in desired_values.split(',')]
                input_correct = True
            except:
                print('Bad input, please specify again')
                continue

        elif desired_type == 'tof':
            print()
            desired_values = input('Provide your desired time of flight (days) (you can specify multiple, to do so '
                                   'separate each with a comma: ')

            try:
                desired_values = [float(desired_value) * 86400 for desired_value in desired_values.split(',')]
                input_correct = True
            except:
                print('Bad input, please specify again')
                continue

        else:
            print('Bad input, please specify again')
            continue

    return desired_body_order, desired_type, desired_values


###########################################################################
def get_closest_pareto_solutions(desired_type: str,
                                 desired_value: float,
                                 pareto_fitness: np.ndarray,
                                 pareto_parameters: np.ndarray):
    """
        Searches for the solution that lies closest to the input value on the Pareto front \n
        Input: \n
        - desired_type: dv or tof \n
        - desired_value: float \n
        - pareto_fitness: list[float] \n
        - pareto_parameters: list[list[float]] \n
        Returns: \n
        - best_fitness
        - best_parameters

    """
    if desired_type == 'dv':
        abs_differences = abs(pareto_fitness[:, 0] - desired_value)
        best_index = np.argmin(abs_differences)
        best_fitness = pareto_fitness[best_index]
        best_parameters = pareto_parameters[best_index]
    elif desired_type == 'tof':
        abs_differences = abs(pareto_fitness[:, 1] - desired_value)
        best_index = np.argmin(abs_differences)
        best_fitness = pareto_fitness[best_index]
        best_parameters = pareto_parameters[best_index]

    return best_fitness, best_parameters


###########################################################################
def get_transfer_body_order_abbreviation(transfer_body_order: List[str]) -> str:
    """
    Returns an abbreviation for a sequence of planets
    """
    abbrev = ''
    i = 0
    for planet in transfer_body_order:
        abbrev += planet[0]
        i += 1

    return abbrev

###########################################################################
def select_results_directory(transfer_body_order: List[str],
                             leg_type: tudatpy.kernel.astro.trajectory_design.TransferLegTypes) -> str:
    """
    Determines the path of the directory where the results are saved
    """
    transfer_body_order_abbreviation = get_transfer_body_order_abbreviation(transfer_body_order)

    current_dir = os.path.dirname(__file__)
    if leg_type == trajectory_design.unpowered_unperturbed_leg_type:
        results_dir = current_dir + '/MGA_noDSM_' + transfer_body_order_abbreviation + '/'
    elif leg_type == trajectory_design.dsm_velocity_based_leg_type:
        results_dir = current_dir + '/MGA_DSM_' + transfer_body_order_abbreviation + '/'

    return results_dir

###########################################################################
def get_trajectory_parameters_of_desired_solutions(leg_type,
                                                   transfer_body_order: List[str],
                                                   type: str,
                                                   values: List[float]):

    """"
    Loads data closest to the desired solutions and returns the transfer trajectory object, the trajectory parameters
    for these solutions and the repository names where the plots for these are to be stored.
    """

    results_dir = select_results_directory(transfer_body_order, leg_type) + 'optimization/'

    pareto_fitness = np.loadtxt(results_dir + 'Pareto_fitness.dat', dtype=float, unpack=False)
    pareto_parameters = np.loadtxt(results_dir + 'Pareto_parameters.dat', dtype=float, unpack=False)

    trajectory_parameters_list = []

    for value in values:
        # Obtain solution on the Pareto front that is closed to the desired value
        best_fitness, best_trajectory_parameters = get_closest_pareto_solutions(type,
                                                                                value,
                                                                                pareto_fitness,
                                                                                pareto_parameters)
        trajectory_parameters_list.append(best_trajectory_parameters)

    return trajectory_parameters_list

###########################################################################
def get_user_input_for_saving(transfer_body_orders: List[str],
                              current_dir: str,
                              leg_type: tudatpy.kernel.astro.trajectory_design.TransferLegTypes):
    """
       Lets the user input info about the solutions (s)he wants to save to Excel
    """

    input_correct = False
    while input_correct == False:
        if len(transfer_body_orders) == 1:
            desired_index = 0
            input_correct = True
        else:
            print('You have the following transfer body orders available: ')
            for i in range(len(transfer_body_orders)):
                print(f'{i}: ', transfer_body_orders[i])
            print()

            desired_index = input('Provide the transfer body order index  (0 to ' + str(
                        len(transfer_body_orders) - 1) + ') that you want to save: ')

            try:
                desired_index = int(desired_index)

            except:
                print('Bad input, an integer is required, please specify again')
                continue

            if (desired_index > (len(transfer_body_orders) - 1)) or (desired_index < 0):
                print('There are ', len(transfer_body_orders),
                      ' transfer body orders, please choose a value from 0 to ', (len(transfer_body_orders) - 1))
                continue

            input_correct = True

    transfer_body_order_desired = transfer_body_orders[desired_index]
    transfer_body_order_desired_abbrev = get_transfer_body_order_abbreviation(transfer_body_order_desired)

    if leg_type == trajectory_design.unpowered_unperturbed_leg_type:
        case_dir = current_dir + '/MGA_noDSM_' + transfer_body_order_desired_abbrev + '/'
    else:
        case_dir = current_dir + '/MGA_DSM_' + transfer_body_order_desired_abbrev + '/'

    available_dirs = os.listdir(case_dir)


    input_correct = False
    while input_correct == False:
        if len(available_dirs) == 2:
            desired_index = 0
            input_correct = True
        else:
            print()
            print('You have the following cases available: ')
            for i in range(len(available_dirs) - 1):
                print(f'{i}: ', available_dirs[i])
            print()

            desired_index = input('Provide the case index  (0 to ' + str(
                len(available_dirs) - 2) + ') that you want to save: ')

            try:
                desired_index = int(desired_index)

            except:
                print('Bad input, an integer is required, please specify again')
                continue

            if (desired_index > (len(available_dirs) - 2)) or (desired_index < 0):
                print()
                print('There are ', len(available_dirs) - 1,
                      ' available cases, please choose a value from 0 to ', (len(available_dirs) - 2))
                continue

            input_correct = True

    desired_dir_to_save = case_dir + available_dirs[desired_index]

    return desired_dir_to_save