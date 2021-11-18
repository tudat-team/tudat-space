# General imports
import matplotlib.pyplot as plt
import numpy as np
import os

# Tudat imports
from tudatpy.kernel import constants

# CDL imports
from code_with_MgaDsm_class.MgaDsmTrajectory import MgaDsmTrajectory

SAVE_PLOTS = True
PLOTS_DIRECTORY = '/mga_dsm_plots/'
PLOTS_TAG = 'Dsm_'

def main():

    ###########################################################################
    # Setup directory to save plots
    ###########################################################################
    if SAVE_PLOTS:
        current_dir = os.path.dirname(__file__)
        PLOTS_FILE = current_dir + PLOTS_DIRECTORY + PLOTS_TAG

        if not os.path.isdir(current_dir + PLOTS_DIRECTORY):
            os.makedirs(current_dir + PLOTS_DIRECTORY)

    ###########################################################################
    # Define transfer trajectory
    ###########################################################################
    # Define order of bodies (nodes)
    transfer_body_order = ['Earth', 'Earth', 'Venus', 'Venus',  'Mercury']
    # Select type of transfer
    leg_type = 'dsm_velocity_based_leg_type'

    # Define departure orbit
    departure_semi_major_axis = np.inf
    departure_eccentricity = 0
    # Define insertion orbit at Mercury
    arrival_semi_major_axis = np.inf
    arrival_eccentricity = 0

    # Create transfer_trajectory object
    transfer_trajectory = MgaDsmTrajectory(leg_type,transfer_body_order,departure_eccentricity,departure_semi_major_axis,
                                           arrival_eccentricity,arrival_semi_major_axis)

    ###########################################################################
    # Define trajectory parameters
    ###########################################################################
    julian_day = constants.JULIAN_DAY

    # Print parameter definitions
    transfer_trajectory.print_parameter_definitions()

    # Select trajectory parameters
    departure_date = [(1171.64503236 - 0.5) * julian_day]
    times_of_flight = [399.999999715 * julian_day, 178.372255301 * julian_day, 299.223139512 * julian_day,
                       180.510754824 * julian_day]
    node_free_parameters = [1408.99421278, 0.37992647165 * 2.0 * 3.14159265358979, np.arccos(2.0 * 0.498004040298 - 1.0) - 3.14159265358979 / 2.0,
                            1.80629232251 * 6.378e6, 1.35077257078, 0.0,
                            3.04129845698 * 6.052e6, 1.09554368115, 0.0,
                            1.10000000891 * 6.052e6, 1.34317576594, 0.0]
    leg_free_parameters = [0.234594654679,
                           0.0964769387134,
                           0.829948744508,
                           0.317174785637]
    trajectory_parameters = departure_date + times_of_flight + node_free_parameters + leg_free_parameters

    # Evaluate trajectory
    transfer_trajectory.evaluate(trajectory_parameters)

    ###########################################################################
    # Retrieve delta V's and time of flight
    ###########################################################################
    delta_v = transfer_trajectory.delta_v()
    time_of_flight = transfer_trajectory.time_of_flight()
    print('Delta V [m/s]: ',delta_v)
    print('TOF [day] : ',time_of_flight/julian_day)

    delta_v_per_node = transfer_trajectory.delta_v_per_node()
    delta_v_per_leg = transfer_trajectory.delta_v_per_leg()
    print('Delta V per leg [m/s]: ', delta_v_per_leg)
    print('Delta V per node [m/s]: ', delta_v_per_node)

    ###########################################################################
    # State history
    ###########################################################################
    state_history_wrt_sun,time_history_wrt_sun = transfer_trajectory.state_history()
    state_history_wrt_earth, time_history_wrt_earth = transfer_trajectory.state_history('Earth')

    plt.figure()
    plt.plot(state_history_wrt_sun[:, 0] / 1.5e11, state_history_wrt_sun[:, 1] / 1.5e11)
    plt.scatter([0],[0],color='red', label='Sun')
    plt.xlabel('x position wrt Sun [AU]')
    plt.ylabel('y position wrt Sun [AU]')
    plt.legend()
    if SAVE_PLOTS:
        plt.savefig(PLOTS_FILE+'x_y.pdf', bbox_inches='tight')
    plt.close()

    plt.figure()
    plt.plot(time_history_wrt_sun/julian_day, state_history_wrt_sun[:, 0] / 1.5e11)
    plt.xlabel('time [days]')
    plt.ylabel('x position wrt Sun [AU]')
    if SAVE_PLOTS:
        plt.savefig(PLOTS_FILE+'time_x.pdf', bbox_inches='tight')
    plt.close()


    ###########################################################################
    # Total and effective solar flux
    ###########################################################################
    total_solar_flux_history, time_history = transfer_trajectory.total_solar_flux()
    effective_solar_flux_history, time_history = transfer_trajectory.effective_solar_flux('Velocity')

    plt.figure()
    plt.plot(time_history / julian_day, total_solar_flux_history, label='total flux')
    plt.plot(time_history / julian_day, effective_solar_flux_history, label='effective flux')
    plt.legend()
    plt.xlabel('time [days]')
    plt.ylabel('solar flux [$W/m^2$]')
    plt.yscale('log')
    if SAVE_PLOTS:
        plt.savefig(PLOTS_FILE+'time_solarFlux.pdf', bbox_inches='tight')
    plt.close()

    ###########################################################################
    # Link budget
    ###########################################################################
    transmited_power = 27  # W
    transmiter_antenna_gain = 10
    receiver_antenna_gain = 1
    frequency = 1.57542e9  # HZ

    link_budget_history, time_history = transfer_trajectory.link_budget(frequency,transmited_power,
                                                                        transmiter_antenna_gain, receiver_antenna_gain)

    plt.figure()
    plt.plot(time_history / julian_day, link_budget_history)
    plt.xlabel('time [days]')
    plt.ylabel('received power [W]')
    plt.yscale('log')
    if SAVE_PLOTS:
        plt.savefig(PLOTS_FILE+'time_linkBudget.pdf', bbox_inches='tight')
    plt.close()

    ###########################################################################
    # Communications time per day
    ###########################################################################
    minimum_elevation = 10 * np.pi / 180
    station_name = 'Delft'
    gs_latitude = 52.0115769 * np.pi / 180
    gs_longitude = 4.3570677 * np.pi / 180

    transfer_trajectory.add_ground_station_simple(station_name,gs_latitude,gs_longitude)
    comms_time_per_day, time_history = transfer_trajectory.communications_time_per_day(station_name,minimum_elevation)

    plt.figure()
    plt.plot(time_history / julian_day, comms_time_per_day / 3600)
    plt.xlabel('time [days]')
    plt.ylabel('communications time per day [hours]')
    if SAVE_PLOTS:
        plt.savefig(PLOTS_FILE+'time_commsPerDay.pdf', bbox_inches='tight')
    plt.close()


    ###########################################################################
    return 0

if __name__ == "__main__":
    main()