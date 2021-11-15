# General imports
import matplotlib.pyplot as plt
import numpy as np
import os

# Tudat imports
import BuildDirectory
from tudatpy.kernel import constants
from tudatpy.kernel.simulation import environment_setup, astro_setup

# CDL imports
import TransferTrajectoryAnalysis
from TransferTrajectoryUtilities import get_user_input_for_analysis, select_results_directory, get_trajectory_parameters_of_desired_solutions
from transfer_trajectory_inputs import transfer_body_orders, leg_type, \
                                     departure_semi_major_axis, departure_eccentricity, arrival_semi_major_axis, \
                                     arrival_eccentricity, transmited_power, transmiter_antenna_gain, receiver_antenna_gain, \
                                     frequency, minimum_elevation, gs_latitude, gs_longitude, station_name, \
                                     save_analysis_plots

def main():
    PLOTS_DIR = 'trajectory_analysis_plots/'
    DATA_DIR = 'trajectory_analysis_data/'

    ###########################################################################
    # Choose desired results and load corresponding data
    ###########################################################################

    desired_body_order_index, desired_type, desired_values = get_user_input_for_analysis(transfer_body_orders)
    transfer_body_order = transfer_body_orders[desired_body_order_index]
    trajectory_parameters_list = get_trajectory_parameters_of_desired_solutions(
        leg_type,
        transfer_body_order,
        desired_type,
        desired_values)

    ###########################################################################
    # Loop over the selected trajectories
    ###########################################################################
    for trajectory_parameters in trajectory_parameters_list:

        ###########################################################################
        # Create and evaluate transfer trajectory
        ###########################################################################
        # Create system of bodies
        bodies = environment_setup.create_simplified_system_of_bodies()

        # Create transfer trajectory and evaluate it
        transfer_trajectory = TransferTrajectoryAnalysis.create_and_evaluate_transfer_trajectory(bodies,
                                                                                                 leg_type,
                                                                                                 transfer_body_order,
                                                                                                 trajectory_parameters,
                                                                                                 departure_semi_major_axis,
                                                                                                 departure_eccentricity,
                                                                                                 arrival_semi_major_axis,
                                                                                                 arrival_eccentricity)

        ###########################################################################
        # Retrieve delta V's and time of flight
        ###########################################################################
        delta_v = transfer_trajectory.delta_v
        time_of_flight = transfer_trajectory.time_of_flight
        print('Delta V [m/s]: ', delta_v)
        print('TOF [day] : ', time_of_flight / constants.JULIAN_DAY)

        delta_v_per_node = transfer_trajectory.delta_v_per_node
        delta_v_per_leg = transfer_trajectory.delta_v_per_leg
        print('Delta V per leg [m/s]: ', delta_v_per_leg)
        print('Delta V per node [m/s]: ', delta_v_per_node)

        ###########################################################################
        # Retrieve different data
        ###########################################################################

        # Retrieve state history with respect to the Sun
        state_history_wrt_sun, stateSun_time_history = TransferTrajectoryAnalysis.get_state_history(
            transfer_trajectory,
            bodies)

        # Retrieve state history with respect to Earth
        state_history_wrt_earth, stateEarth_time_history = TransferTrajectoryAnalysis.get_state_history(
            transfer_trajectory,
            bodies,
            'Earth')

        # Retrieve total solar flux
        total_solar_flux_history, solar_flux_time_history = TransferTrajectoryAnalysis.total_solar_flux(
            transfer_trajectory,
            bodies)

        # Retrieve link budget
        link_budget_history, link_budget_time_history = TransferTrajectoryAnalysis.link_budget(
            transfer_trajectory,
            bodies,
            frequency,
            transmited_power,
            transmiter_antenna_gain,
            receiver_antenna_gain)

        # Retrieve communications time per day
        TransferTrajectoryAnalysis.add_ground_station_simple(
            bodies,
            station_name,
            gs_latitude,
            gs_longitude)
        comms_time_per_day, comms_time_history = TransferTrajectoryAnalysis.communications_time_per_day(
            transfer_trajectory,
            bodies,
            station_name,
            minimum_elevation)

        ###########################################################################
        # Setup directories to save data and/or plots
        ###########################################################################
        current_dir = os.path.dirname(__file__) + '/'

        results_dir = select_results_directory(transfer_body_order,leg_type)

        trajectory_path = results_dir + str( round( delta_v / 1000, 2 ) ) + 'kmS_' + \
                         str( int( time_of_flight / 86400 ) ) + 'days/'
        if not os.path.isdir(trajectory_path):
            os.makedirs(trajectory_path)

        data_path = trajectory_path + DATA_DIR
        if not os.path.isdir(data_path):
            os.makedirs(data_path)

        if save_analysis_plots:
            plots_path = trajectory_path + PLOTS_DIR
            if not os.path.isdir(plots_path):
                os.makedirs(plots_path)


        ###########################################################################
        # Save data
        ###########################################################################
        with open(trajectory_path + 'trajectory_info.txt', 'w') as fp:
            fp.write(f'Trajectory parameters: {str(trajectory_parameters)}\n')
            fp.write(f'TOF [day]: {time_of_flight / constants.JULIAN_DAY}\n')
            fp.write(f'Delta V [m/s]: {delta_v}\n')
            fp.write(f'Delta V per leg [m/s]: {str(delta_v_per_leg)}\n')
            fp.write(f'Delta V per node [m/s]: {str(delta_v_per_node)}\n')

        np.savetxt(data_path + 'state_wrt_sun.txt',
                   np.column_stack([stateSun_time_history,state_history_wrt_sun]),
                   header = 'time[s] \t x[m] \t y[m] \t z[m] \t vx[m/s] \t vy[m/s] \t vz[m/s]')
        np.savetxt(data_path + 'state_wrt_earth.txt',
                   np.column_stack([stateEarth_time_history, state_history_wrt_earth]),
                   header='time[s] \t x[m] \t y[m] \t z[m] \t vx[m/s] \t vy[m/s] \t vz[m/s]')
        np.savetxt(data_path + 'solar_flux.txt',
                   np.column_stack([solar_flux_time_history, total_solar_flux_history]),
                   header='time[s] \t solar_flux [W/m^2]')
        np.savetxt(data_path + 'link_budget.txt',
                   np.column_stack([link_budget_time_history, link_budget_history]),
                   header='time[s] \t link_budget [W]')
        np.savetxt(data_path + 'comms_time.txt',
                   np.column_stack([comms_time_history, comms_time_per_day]),
                   header='time[s] \t comms_time_per_day [s]')

        ###########################################################################
        # Do and save plots
        ###########################################################################
        if save_analysis_plots:
            # Trajectory: x and y coordinates
            plt.figure()
            plt.plot(state_history_wrt_sun[:, 0] / 1.5e11, state_history_wrt_sun[:, 1] / 1.5e11)
            plt.scatter([0],[0],color='red', label='Sun')
            plt.xlabel('x [AU]')
            plt.ylabel('y [AU]')
            plt.axis('equal')
            plt.legend()
            plt.savefig(plots_path + 'x_y.pdf', bbox_inches='tight')
            plt.close()

            # Total solar flux
            plt.figure()
            plt.plot(solar_flux_time_history / constants.JULIAN_DAY, total_solar_flux_history)
            plt.xlabel('time [days]')
            plt.ylabel('total solar flux [$W/m^2$]')
            plt.yscale('log')
            plt.savefig(plots_path + 'time_solarFlux.pdf', bbox_inches='tight')
            plt.close()

            # Link budget
            plt.figure()
            plt.plot(link_budget_time_history / constants.JULIAN_DAY, link_budget_history)
            plt.xlabel('time [days]')
            plt.ylabel('received power [W]')
            plt.yscale('log')
            plt.savefig(plots_path+'time_linkBudget.pdf', bbox_inches='tight')
            plt.close()

            # Comms time per day
            plt.figure()
            plt.plot(comms_time_history / constants.JULIAN_DAY, comms_time_per_day / 3600)
            plt.xlabel('time [days]')
            plt.ylabel('communications time per day [hours]')
            plt.savefig(plots_path + 'time_commsPerDay.pdf', bbox_inches='tight')
            plt.close()

    ###########################################################################
    return 0

if __name__ == "__main__":
    main()