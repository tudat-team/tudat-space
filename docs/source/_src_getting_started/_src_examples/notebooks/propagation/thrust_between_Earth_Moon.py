"""
Copyright (c) 2010-2022, Delft University of Technology
All rights reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

TUDATPY EXAMPLE APPLICATION: Thrust in Earth-Moon system
FOCUS:                       Implementing thrust acceleration / basic guidance
"""

###############################################################################
# TUDATPY EXAMPLE APPLICATION: Basic thrust guidance in Earth-Moon  ###########
###############################################################################

""" ABSTRACT.

This example demonstrates the a basic use of thrust in the Earth-Moon system.
Thrust is implemented to be of constant magnitude, and be co-linear with velocity,
pushing the simulated vehicle from behind.
In addition to the acceleration from the thrust, a basic model is setup, consisting
of the acceleration of the Earth, Moon, and Sun, only considering them as Point Masses.
The mass of the vehicle is also propagated, using a mass rate model made to be
consistent with the rocket thrust used.
How to setup dependent variables to save the mass and altitude of the vehicle 
over time is also demonstrated.
Termination settings based on the minimum mass of the vehicle and its maximum altitude
are also shown.
Finally, how to plot the trajectory of the vehicle and of the Moon in 3D is demonstrated.
For this, this example also shows how to extract the position of the Moon over time
from SPICE.

"""

################################################################################
# IMPORT STATEMENTS ############################################################
################################################################################

import numpy as np
from tudatpy.util import result2array
from tudatpy.kernel import constants, numerical_simulation
from tudatpy.kernel.interface import spice
from tudatpy.kernel.numerical_simulation import environment_setup
from tudatpy.kernel.numerical_simulation import propagation_setup
from matplotlib import pyplot as plt

################################################################################
# GENERAL SIMULATION SETUP #####################################################
################################################################################

# Load spice kernels.
spice.load_standard_kernels()

# Set simulation start and end epochs (total simulation time of 30 days).
simulation_start_epoch = 1.0e7
simulation_end_epoch = 1.0e7 + 30.0 * constants.JULIAN_DAY

# Set vehicle mass.
vehicle_mass = 5.0e3

# Set vehicle thrust magnitude (in Newton).
thrust_magnitude = 10.0

# Set engine specific impulse.
specific_impulse = 5.0e3

################################################################################
# SETUP ENVIRONMENT ############################################################
################################################################################

# Define bodies in simulation.
bodies_to_create = ["Sun", "Earth", "Moon"]

# Create bodies in simulation.
body_settings = environment_setup.get_default_body_settings(bodies_to_create)
system_of_bodies = environment_setup.create_system_of_bodies(body_settings)

# Create the vehicle body in the environment
system_of_bodies.create_empty_body("Vehicle")
system_of_bodies.get_body("Vehicle").set_constant_mass(vehicle_mass)

################################################################################
# SETUP PROPAGATION : DEFINE THRUST GUIDANCE SETTINGS ##########################
################################################################################

# Define the direction of the thrust as colinear with the velocity of the orbiting vehicle, pushing it from behind
thrust_direction_settings = (
    propagation_setup.thrust.thrust_direction_from_state_guidance(
        central_body="Earth",
        is_colinear_with_velocity=True,
        direction_is_opposite_to_vector=False ) )

# Define the thrust magnitude as constant
thrust_magnitude_settings = (
    propagation_setup.thrust.constant_thrust_magnitude(
        thrust_magnitude=thrust_magnitude, specific_impulse=specific_impulse ) )

################################################################################
# SETUP PROPAGATION : CREATE ACCELERATION MODELS ###############################
################################################################################

# Define the accelerations acting on the vehicle
acceleration_on_vehicle = dict(
    Vehicle=[
        # Define the thrust acceleration from its direction and magnitude
        propagation_setup.acceleration.thrust_from_direction_and_magnitude(
            thrust_direction_settings=thrust_direction_settings,
            thrust_magnitude_settings=thrust_magnitude_settings,
        )
    ],
    # Define the acceleration due to the Earth, Moon, and Sun as Point Mass
    Earth=[propagation_setup.acceleration.point_mass_gravity()],
    Moon=[propagation_setup.acceleration.point_mass_gravity()],
    Sun=[propagation_setup.acceleration.point_mass_gravity()]
)

# Compile the accelerations acting on the vehicle
acceleration_dict = dict(Vehicle=acceleration_on_vehicle)

# Set which body to propagate
bodies_to_propagate = ["Vehicle"]

# Set the central body
central_bodies = ["Earth"]

# Create the acceleration models from the acceleration mapping dictionary
acceleration_models = propagation_setup.create_acceleration_models(
    body_system=system_of_bodies,
    selected_acceleration_per_body=acceleration_dict,
    bodies_to_propagate=bodies_to_propagate,
    central_bodies=central_bodies
)

################################################################################
# SETUP PROPAGATION : DEPENDENT VARIABLE SETTINGS ##############################
################################################################################

# Create a dependent variable to save the altitude of the vehicle w.r.t. Earth over time
vehicle_altitude_dep_var = propagation_setup.dependent_variable.altitude( "Vehicle", "Earth" )

# Create a dependent variable to save the mass of the vehicle over time
vehicle_mass_dep_var = propagation_setup.dependent_variable.body_mass( "Vehicle" )

################################################################################
# SETUP PROPAGATION : TERMINATION SETTINGS #####################################
################################################################################

# Get system initial state (in cartesian coordinates)
system_initial_state = np.array([8.0e6, 0, 0, 0, 7.5e3, 0])

# Create a termination setting to stop when altitude of the vehicle is above 100e3 km
termination_distance_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings = vehicle_altitude_dep_var,
        limit_value = 100E6,
        use_as_lower_limit = False)

# Create a termination setting to stop when the vehicle has a mass below 4e3 kg
termination_mass_settings = propagation_setup.propagator.dependent_variable_termination(
        dependent_variable_settings = vehicle_mass_dep_var,
        limit_value = 4000.0,
        use_as_lower_limit = True)

# Create a termination setting to stop at the specified simulation end epoch
termination_time_settings = propagation_setup.propagator.time_termination(simulation_end_epoch)

# Setup a hybrid termination setting to stop the simulation when one of the aforementionned termination setting is reached
termination_settings_list = [termination_distance_settings, termination_mass_settings, termination_time_settings ]
termination_condition = propagation_setup.propagator.hybrid_termination( termination_settings_list, fulfill_single_condition = True )

################################################################################
# SETUP PROPAGATION : PROPAGATION SETTINGS #####################################
################################################################################

# Create the translational propagation settings (use a Cowell propagator)
translational_propagator_settings = propagation_setup.propagator.translational(
    central_bodies,
    acceleration_models,
    bodies_to_propagate,
    system_initial_state,
    termination_condition,
    propagation_setup.propagator.cowell,
    output_variables=[vehicle_altitude_dep_var, vehicle_mass_dep_var]
)

# Create a mass rate model so that the vehicle looses mass according to how much thrust acts on it
mass_rate_settings = dict(Vehicle=[propagation_setup.mass_rate.from_thrust()])
mass_rate_models = propagation_setup.create_mass_rate_models(
    system_of_bodies,
    mass_rate_settings,
    acceleration_models
)
# Create the mass propagation settings
mass_propagator_settings = propagation_setup.propagator.mass(
    bodies_to_propagate, mass_rate_models, [vehicle_mass], termination_condition )

# Combine the translational and mass propagator settings
propagator_settings = propagation_setup.propagator.multitype(
    [translational_propagator_settings, mass_propagator_settings],
    termination_condition,
    [vehicle_altitude_dep_var, vehicle_mass_dep_var])

################################################################################
# SETUP PROPAGATION : INTEGRATOR SETTINGS ######################################
################################################################################

# Setup the variable step integrator time step sizes
initial_time_step = 10.0
minimum_time_step = 0.01
maximum_time_step = 86400
# Setup the tolerance of the variable step integrator
tolerance = 1e-10

# Create numerical integrator settings (using a RKF7(8) coefficient set)
integrator_settings = propagation_setup.integrator.runge_kutta_variable_step_size(
    simulation_start_epoch,
    initial_time_step,
    propagation_setup.integrator.rkf_78,
    minimum_time_step,
    maximum_time_step,
    relative_error_tolerance=tolerance,
    absolute_error_tolerance=tolerance)

################################################################################
# PROPAGATE ####################################################################
################################################################################

# Instantiate the dynamics simulator and run the simulation
dynamics_simulator = numerical_simulation.SingleArcSimulator(
    system_of_bodies, integrator_settings, propagator_settings, print_dependent_variable_data=True
)

# Extract the state history
state_history = dynamics_simulator.state_history

# Extract the dependent variable history
dependent_variable_history = dynamics_simulator.dependent_variable_history

################################################################################
# VISUALISATION / OUTPUT / PRELIMINARY ANALYSIS ################################
################################################################################

# Retrieve the Moon trajectory over vehicle propagation epochs from spice
moon_states_from_spice = {
    epoch:spice.get_body_cartesian_state_at_epoch("Moon", "Earth", "J2000", "None", epoch)
    for epoch in list(state_history)
}

# Convert state dictionaries to multi-dimensional arrays
vehicle_array = result2array(state_history)
moon_array = result2array(moon_states_from_spice)

# Convert dependent variables dictionary to multi-dimensional arrays
dep_var_array = result2array(dependent_variable_history)

# Extract the time, altitude, and vehicle mass values to separate arrays
dep_var_epochs = dep_var_array[:,0]
altitude_array = dep_var_array[:,1]
mass_array = dep_var_array[:,2]

# Create a figure for the altitude of the vehicle above Earth
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111)
ax1.set_title(f"Vehicle altitude above Earth")

# Plot the altitude of the vehicle over time
ax1.plot((dep_var_epochs - dep_var_epochs[0])/constants.JULIAN_DAY, altitude_array/1e3)

# Add a grid and axis labels to the plot
ax1.grid(), ax1.set_xlabel("Simulation time [day]"), ax1.set_ylabel("Vehicle altitude [km]")

# Use a tight layout for the figure (do last to avoid trimming axis)
fig1.tight_layout()

# Create a figure for the altitude of the vehicle above Earth
fig2 = plt.figure(figsize=(10, 6))
ax2 = fig2.add_subplot(111)
ax2.set_title(f"Vehicle mass over time")

# Plot the mass of the vehicle over time
ax2.plot((dep_var_epochs - dep_var_epochs[0])/constants.JULIAN_DAY, mass_array)

# Add a grid and axis labels to the plot
ax2.grid(), ax2.set_xlabel("Simulation time [day]"), ax2.set_ylabel("Vehicle mass [kg]")

# Use a tight layout for the figure (do last to avoid trimming axis)
fig2.tight_layout()

# Create a figure with a 3D projection for the Moon and vehicle trajectory around Earth
fig3 = plt.figure(figsize=(7, 6))
ax3 = fig3.add_subplot(111, projection="3d")
ax3.set_title(f"System state evolution in 3D")

# Plot the vehicle and Moon positions as curve, and the Earth as a marker
ax3.plot(vehicle_array[:, 1], vehicle_array[:, 2], vehicle_array[:, 3], label="Vehicle", linestyle="-.", color="green")
ax3.plot(moon_array[:, 1], moon_array[:, 2], moon_array[:, 3], label="Moon", linestyle="-", color="grey")
ax3.scatter(0.0, 0.0, 0.0, label="Earth", marker="o", color="blue")

# Add a legend, set the plot limits, and add axis labels
ax3.legend()
ax3.set_xlim([-3E8, 3E8]), ax3.set_ylim([-3E8, 3E8]), ax3.set_zlim([-3E8, 3E8])
ax3.set_xlabel("x [m]"), ax3.set_ylabel("y [m]"), ax3.set_zlabel("z [m]")

# Use a tight layout for the figure (do last to avoid trimming axis)
fig3.tight_layout()

# Show all the plots
plt.show()