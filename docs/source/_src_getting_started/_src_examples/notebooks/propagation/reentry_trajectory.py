"""
Copyright (c) 2010-2022, Delft University of Technology
All rights reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

TUDATPY EXAMPLE APPLICATION: Re-entry trajectory
"""

###############################################################################
# TUDATPY EXAMPLE APPLICATION: Re-entry trajectory with aerodynamic guidance  #
###############################################################################

""" ABSTRACT.

This examples focuses on the application of aerodynamic guidance in the context
of a re-entry trajectory of the Space Transportation System (STS).
The aerodynamic guidance updates the angle of attack and the bank angle of the
vehicle based on its flight conditions.
The angle of attack is set to 40deg for a Mach number above 12, to 10deg for a
Mach number below 6, and varies linearly between them.
The bank angle is computed such that the derivative of the flight path angle
over time equals 0, and the flight path angle is then constant.
To do so, this example also showcases how to extract and use the flight condition
and body properties during the simulation.
The initial state of the STS is most notably its initial altitude of 120km, velocity
of 7.5km/s, and its flight path angle of -0.6deg.
A high number of dependent variable are also propagated in this example. All of them
are then plotted at the end of this script.

"""

###############################################################################
# IMPORT STATEMENTS ###########################################################
###############################################################################

import numpy as np
from tudatpy.kernel.interface import spice_interface
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.numerical_simulation import environment_setup, environment
from tudatpy.kernel.numerical_simulation import propagation_setup, propagation
from tudatpy.kernel.astro import element_conversion
from tudatpy.util import result2array
from matplotlib import pyplot as plt


###############################################################################
# AERODYNAMIC GUIDANCE CLASS ##################################################
###############################################################################

# Create a class for the aerodynamic guidance of the STS, inheriting from 'propagation.AerodynamicGuidance'
class STSAerodynamicGuidance(propagation.AerodynamicGuidance):

    def __init__(self, bodies: environment.SystemOfBodies):
        # Call the base class constructor
        propagation.AerodynamicGuidance.__init__(self)

        # Extract the STS and Earth bodies
        self.vehicle = bodies.get_body("STS")
        self.earth = bodies.get_body("Earth")

        # Extract the STS flight conditions, angle calculator, and aerodynamic coefficient interface
        self.vehicle_flight_conditions = bodies.get_body("STS").flight_conditions
        self.aerodynamic_angle_calculator = self.vehicle_flight_conditions.aerodynamic_angle_calculator
        self.aerodynamic_coefficient_interface = self.vehicle_flight_conditions.aerodynamic_coefficient_interface

    # Function that is called at each simulation time step to update the ideal bank angle of the vehicle
    def updateGuidance(self, current_time: float):
        # Get the (constant) angular velocity of the Earth body
        earth_angular_velocity = np.linalg.norm(self.earth.body_fixed_angular_velocity)
        # Get the distance between the vehicle and the Earth bodies
        earth_distance = np.linalg.norm(self.vehicle.position)
        # Get the (constant) mass of the vehicle body
        body_mass = self.vehicle.mass

        # Extract the current Mach number, airspeed, and air density from the flight conditions
        mach_number = self.vehicle_flight_conditions.mach_number
        airspeed = self.vehicle_flight_conditions.airspeed
        density = self.vehicle_flight_conditions.density

        # Set the current Angle of Attack (AoA). The following line enforces the followings:
        # * the AoA is constant at 40deg when the Mach number is above 12
        # * the AoA is constant at 10deg when the Mach number is below 6
        # * the AoA varies close to linearly when the Mach number is between 12 and 6
        # * a Logistic relation is used so that the transition in AoA between M=12 and M=6 is smoother
        self.angle_of_attack = np.deg2rad(30 / (1 + np.exp(-2*(mach_number-9))) + 10)

        # Update the variables on which the aerodynamic coefficients are based (AoA and Mach)
        current_aerodynamics_independent_variables = [self.angle_of_attack, mach_number]
        # Update the aerodynamic coefficients
        self.aerodynamic_coefficient_interface.update_coefficients(
            current_aerodynamics_independent_variables, current_time)

        # Extract the current force coefficients (in order: C_D, C_S, C_L)
        current_force_coefficients = self.aerodynamic_coefficient_interface.current_force_coefficients
        # Extract the (constant) reference area of the vehicle
        aerodynamic_reference_area = self.aerodynamic_coefficient_interface.reference_area

        # Get the heading, flight path, and latitude angles from the aerodynamic angle calculator
        heading = self.aerodynamic_angle_calculator.get_angle(environment.heading_angle)
        flight_path_angle = self.aerodynamic_angle_calculator.get_angle(environment.flight_path_angle)
        latitude = self.aerodynamic_angle_calculator.get_angle(environment.latitude_angle)

        # Compute the acceleration caused by Lift
        lift_acceleration = 0.5 * density * airspeed ** 2 * aerodynamic_reference_area * current_force_coefficients[2] / body_mass
        # Compute the gravitational acceleration
        downward_gravitational_acceleration = self.earth.gravitational_parameter / (earth_distance ** 2)
        # Compute the centrifugal acceleration
        spacecraft_centrifugal_acceleration = airspeed ** 2 / earth_distance
        # Compute the Coriolis acceleration
        coriolis_acceleration = 2 * earth_angular_velocity * airspeed * np.cos(latitude) * np.sin(heading)
        # Compute the centrifugal acceleration from the Earth
        earth_centrifugal_acceleration = earth_angular_velocity ** 2 * earth_distance * np.cos(latitude) * \
            (np.cos(latitude) * np.cos(flight_path_angle) + np.sin(flight_path_angle) * np.sin(latitude) * np.cos(heading))
        
        # Compute the cosine of the ideal bank angle
        cosine_of_bank_angle = ((downward_gravitational_acceleration - spacecraft_centrifugal_acceleration) * np.cos(flight_path_angle) - coriolis_acceleration - earth_centrifugal_acceleration) / lift_acceleration
        # If the cosine lead to a value out of the [-1, 1] range, set to bank angle to 0deg or 180deg
        if (cosine_of_bank_angle < -1):
            self.bank_angle = np.pi
        elif (cosine_of_bank_angle > 1):
            self.bank_angle = 0.0
        else:
            # If the cos is in the correct range, return the computed bank angle
            self.bank_angle = np.arccos(cosine_of_bank_angle)


def main():
    # Load spice kernels
    spice_interface.load_standard_kernels()

    # Set simulation start epoch
    simulation_start_epoch = 0.0

    # Set the maximum simulation time (avoid very long skipping re-entry)
    max_simulation_time = 3*24*3600

    ###########################################################################
    # CREATE ENVIRONMENT BODIES ###############################################
    ###########################################################################

    # Create default body settings for "Earth"
    bodies_to_create = ["Earth"]

    # Create default body settings for bodies_to_create, with "Earth"/"J2000" as the global frame origin and orientation
    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create, "Earth", "J2000"
    )

    # Create the system of bodies for the simulation
    bodies = environment_setup.create_system_of_bodies(body_settings)

    # Define central bodies
    central_bodies = ["Earth"]

    ###########################################################################
    # CREATE VEHICLE ##########################################################
    ###########################################################################

    # Create vehicle object and set its constant mass
    bodies.create_empty_body("STS")
    bodies.get_body( "STS" ).set_constant_mass(5.0e3)

    # Define the aerodynamic coefficient files (leave C_S empty)
    aero_coefficients_files = {0: "input/STS_CD.dat", 2:"input/STS_CL.dat"}

    # Setup the aerodynamic coefficients settings tabulated from the files
    coefficient_settings = environment_setup.aerodynamic_coefficients.tabulated_force_only_from_files(
        force_coefficient_files=aero_coefficients_files,
        reference_area=2690.0*0.3048*0.3048,
        independent_variable_names=[environment.angle_of_attack_dependent, environment.mach_number_dependent],
        are_coefficients_in_aerodynamic_frame=True,
        are_coefficients_in_negative_axis_direction=True
    )

    # Add predefined aerodynamic coefficients database to the body
    environment_setup.add_aerodynamic_coefficient_interface(bodies, "STS", coefficient_settings)

    # Define the STS as the body to propagate
    bodies_to_propagate = ["STS"]

    ###########################################################################
    # CREATE ACCELERATIONS ####################################################
    ###########################################################################

    # Define the accelerations acting on the STS (Earth as a Point Mass, and Earth's atmosphere)
    accelerations_settings_STS = dict(
        Earth=[
            propagation_setup.acceleration.point_mass_gravity(),
            propagation_setup.acceleration.aerodynamic(),
        ]
    )
    acceleration_settings = {"STS": accelerations_settings_STS}

    # Create the acceleration models
    acceleration_models = propagation_setup.create_acceleration_models(
        bodies, acceleration_settings, bodies_to_propagate, central_bodies
    )

    ###########################################################################
    # CREATE PROPAGATION SETTINGS #############################################
    ###########################################################################

    # Create the aerodynamic guidance object
    guidance_object = STSAerodynamicGuidance(bodies)

    # Set aerodynamic guidance (this line links the STSAerodynamicGuidance settings with the propagation)
    environment_setup.set_aerodynamic_guidance(guidance_object, bodies.get_body("STS"))

    # Set the initial state of the STS as spherical elements, and convert them to a cartesian state
    initial_radial_distance = bodies.get_body("Earth").shape_model.average_radius + 120e3
    # Convert the initial state
    initial_earth_fixed_state = element_conversion.spherical_to_cartesian_elementwise(
        radial_distance=initial_radial_distance,
        latitude=np.deg2rad(20),
        longitude=np.deg2rad(140),
        speed=7.5e3,
        flight_path_angle=np.deg2rad(-0.6),
        heading_angle=np.deg2rad(15),
    )

    # Convert the state from the Earth-fixed frame to the inertial frame
    earth_rotation_model = bodies.get_body("Earth").rotation_model
    initial_state = environment.transform_to_inertial_orientation(
        initial_earth_fixed_state, simulation_start_epoch, earth_rotation_model
    )

    # Define the list of dependent variables to save during the propagation
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.flight_path_angle("STS", "Earth"),
        propagation_setup.dependent_variable.altitude("STS", "Earth"),
        propagation_setup.dependent_variable.bank_angle("STS", "Earth"),
        propagation_setup.dependent_variable.angle_of_attack("STS", "Earth"),
        propagation_setup.dependent_variable.aerodynamic_force_coefficients("STS"),
        propagation_setup.dependent_variable.airspeed("STS", "Earth"),
        propagation_setup.dependent_variable.total_acceleration_norm("STS"),
        propagation_setup.dependent_variable.mach_number("STS", "Earth")
    ]

    # Define a termination conditions to stop once altitude goes below 25 km
    termination_altitude_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings=propagation_setup.dependent_variable.altitude("STS", "Earth"),
        limit_value=25.0e3,
        use_as_lower_limit=True)
    # Define a termination condition to stop after a given time (to avoid an endless skipping re-entry)
    termination_time_settings = propagation_setup.propagator.time_termination(simulation_start_epoch + max_simulation_time)
    # Combine the termination settings to stop when one of them is fulfilled
    combined_termination_settings = propagation_setup.propagator.hybrid_termination(
        [termination_altitude_settings, termination_time_settings], fulfill_single_condition=True )

    # Create the propagation settings
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        combined_termination_settings,
        output_variables=dependent_variables_to_save,
    )

    # Create numerical integrator settings (RK4 integrator with a step size fixed at 0.5s)
    fixed_step_size = 0.5
    integrator_settings = propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch, fixed_step_size
    )

    ###########################################################################
    # PROPAGATE TRAJECTORY ####################################################
    ###########################################################################

    # Create the simulation objects and propagate the dynamics
    dynamics_simulator = numerical_simulation.SingleArcSimulator(
        bodies, integrator_settings, propagator_settings
    )
    
    # Extract the resulting simulation dependent variables
    dependent_variables = dynamics_simulator.dependent_variable_history

    # Convert the dependent variables from a dictionary to a numpy array
    dependent_variables_array = result2array(dependent_variables)

    # Extract the time from the dependent variables array (and convert from seconds to minutes)
    time_min = dependent_variables_array[:,0] / 60
    # Extract all the other dependent variables from the multi-dimensional array
    flight_path_angle = dependent_variables_array[:,1]
    altitude = dependent_variables_array[:,2]
    bank_angle = dependent_variables_array[:,3]
    angle_of_attack = dependent_variables_array[:,4]
    drag_coefficient = dependent_variables_array[:,5]
    lift_coefficient = dependent_variables_array[:,7]
    airspeed = dependent_variables_array[:,8]
    total_acceleration = dependent_variables_array[:,9]
    mach_number = dependent_variables_array[:,10]

    ################################################################################
    # VISUALISATION / OUTPUT / PRELIMINARY ANALYSIS ################################
    ################################################################################

    # Define a matplotlib.pyplot figure
    plt.figure(figsize=(10, 6))
    # Plot the altitude over time
    plt.plot(time_min, altitude/1e3)
    # Add label to the axis
    plt.xlabel("Time [min]"), plt.ylabel("Altitude [km]")
    # Add a grid, and use a tight layout to save space
    plt.grid(), plt.tight_layout()

    # Plot the airspeed vs altitude
    plt.figure(figsize=(10, 6))
    plt.plot(airspeed, altitude/1e3)
    plt.xlabel("Airspeed [m/s]"), plt.ylabel("Altitude [km]")
    plt.grid(), plt.tight_layout()

    # Plot the g-load over time
    plt.figure(figsize=(10, 6))
    plt.plot(time_min, total_acceleration/9.81)
    plt.xlabel("Time [min]"), plt.ylabel("Total g-load [-]")
    plt.grid(), plt.tight_layout()

    # Plot C_D, C_L, and L/D over time
    plt.figure(figsize=(10, 6))
    plt.plot(time_min, drag_coefficient, label="Drag")
    plt.plot(time_min, lift_coefficient, label="Lift")
    plt.plot(time_min, lift_coefficient/drag_coefficient, label="Lift/Drag")
    plt.xlabel("Time [min]"), plt.ylabel("Aerodynamic coefficient [-]")
    # Also add a legend
    plt.legend()
    plt.grid(), plt.tight_layout()

    # Plot various angles over time (bank angle, angle of attack, and flight-path angle)
    plt.figure(figsize=(10, 6))
    plt.plot(time_min, np.rad2deg(bank_angle), label="Bank angle")
    plt.plot(time_min, np.rad2deg(angle_of_attack), label="Angle of attack")
    plt.plot(time_min, np.rad2deg(flight_path_angle), label="Flight-path angle")
    plt.xlabel("Time [min]"), plt.ylabel("Angle [deg]"), plt.legend()
    plt.grid(), plt.tight_layout()

    # Plot the AoA over Mach number
    plt.figure(figsize=(10, 6))
    plt.plot(mach_number, np.rad2deg(angle_of_attack))
    plt.xlabel("Mach number [-]"), plt.ylabel("Angle of attack [deg]")
    # Set the x-axis ticks spacing to 1
    plt.xticks(np.arange(0, 28.1, 1))
    plt.grid(), plt.tight_layout()

    # Compute the derivative of the flight path angle over time (dot(gamma) = Delta gamma / Delta t)
    flight_path_angle_derivative = np.fabs(( flight_path_angle[1:flight_path_angle.size] - flight_path_angle[0:-1])/fixed_step_size)
    # Plot the derivative of the flight path angle over time
    plt.figure(figsize=(10, 6))
    plt.plot(time_min[0:-1], np.rad2deg(flight_path_angle_derivative))
    plt.xlabel("Time [min]"), plt.ylabel("Absolute flight-path angle rate [deg/s]")
    plt.yscale("log")
    plt.yticks(10**np.arange(-12, 0.1, 1))
    plt.grid(), plt.tight_layout()

    # Show all the plots
    plt.show()

    # Final statement (not required, though good practice in a __main__)
    return 0


if __name__ == "__main__":
    main()