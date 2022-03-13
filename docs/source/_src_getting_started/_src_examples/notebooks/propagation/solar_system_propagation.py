"""
Copyright (c) 2010-2021, Delft University of Technology
All rights reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.

TUDATPY EXAMPLE APPLICATION: Solar System Propagation
FOCUS:                       Multi-body propagation and propagation variations
"""

###############################################################################
# TUDATPY EXAMPLE APPLICATION: Solar System Propagation            ############
###############################################################################

""" ABSTRACT.

This example script demonstrates a multi-body propagation of simplified inner
 solar system model. Multi-body propagations become necessary when one or more 
 propagated bodies cannot be treated as quasi-massless. Through their 
 non-negligible mass, the bodies mutually exert accelerations on each other and 
 thereby affecting each others' future states. In order to consistently simulate
 the evolution of such a system, the equations of motion of all massive bodies 
 have to be propagated concurrently in a multi-body propagation.
The example showcases the versatility with which the propagation_setup module 
 allows for advanced multi-body acceleration models and propagators.
 Via the selected_acceleration_per_body argument of the 
 propagation_setup.create_acceleration_models() function, acceleration model 
 settings can be defined for an arbitrary amount of bodies in the system. 
 The central_bodies argument gives the option specify the centre of propagation
 for each propagated body individually. In this script, this feature is used to
 implement a hierarchical propagation scheme. 

"""

################################################################################
# IMPORT STATEMENTS ############################################################
################################################################################
from tudatpy.util import result2array
from tudatpy.kernel import constants
from tudatpy.kernel import numerical_simulation
from tudatpy.kernel.interface import spice
from tudatpy.kernel.numerical_simulation import environment_setup
from tudatpy.kernel.numerical_simulation import propagation_setup, propagation

################################################################################
# GENERAL SIMULATION SETUP #####################################################
################################################################################

# Load spice kernels.
spice.load_standard_kernels()

# Set simulation start epoch.
simulation_start_epoch = 1.0e7

# Set simulation end epoch.
simulation_end_epoch = 1.0e7 + 5.0 * constants.JULIAN_YEAR

################################################################################
# SETUP ENVIRONMENT ############################################################
################################################################################

# Define bodies in simulation.
bodies_to_create = bodies_to_propagate = [
    "Moon",
    "Earth",
    "Mars",
    "Venus",
    "Mercury",
    "Sun",
]

# Create bodies in simulation.
body_settings = environment_setup.get_default_body_settings(bodies_to_create)
body_system = environment_setup.create_system_of_bodies(body_settings)

################################################################################
# SETUP PROPAGATION ############################################################
################################################################################

results = {}
for propagation_variant in ["barycentric", "hierarchical"]:

    ############################################################################
    # SETUP PROPAGATION : CREATE ACCELERATION MODELS ###########################
    ############################################################################

    # Create barycentric body settings
    acceleration_dict = {}
    for body_i in bodies_to_create:
        current_accelerations = {}
        for body_j in bodies_to_create:
            if body_i != body_j:
                current_accelerations[body_j] = [
                    propagation_setup.acceleration.point_mass_gravity()
                ]
        acceleration_dict[body_i] = current_accelerations

    # Barycentric propagation.
    if propagation_variant == "barycentric":
        central_bodies = ["SSB"] * len(bodies_to_create)

    # Hierarchical parent body propagation.
    elif propagation_variant == "hierarchical":
        central_bodies = []
        for body_name in bodies_to_create:
            if body_name == "Moon":
                central_bodies.append("Earth")
            elif body_name == "Sun":
                central_bodies.append("SSB")
            else:
                central_bodies.append("Sun")

    # Convert acceleration mappings into acceleration models.
    acceleration_models = propagation_setup.create_acceleration_models(
        body_system=body_system,
        selected_acceleration_per_body=acceleration_dict,
        bodies_to_propagate=bodies_to_propagate,
        central_bodies=central_bodies
    )

    ############################################################################
    # SETUP PROPAGATION : PROPAGATION SETTINGS #################################
    ############################################################################

    # Get system initial state.
    system_initial_state = propagation.get_initial_state_of_bodies(
        bodies_to_propagate=bodies_to_propagate,
        central_bodies=central_bodies,
        body_system=body_system,
        initial_time=simulation_start_epoch,
    )
    # Create termination settings.
    termination_condition = propagation_setup.propagator.time_termination(simulation_end_epoch)

    # Create propagation settings.
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        system_initial_state,
        termination_condition,
    )
    # Create numerical integrator settings.
    fixed_step_size = 3600.0
    integrator_settings = propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch, fixed_step_size
    )

    ############################################################################
    # PROPAGATE ################################################################
    ############################################################################

    # Instantiate the dynamics simulator.
    dynamics_simulator = numerical_simulation.SingleArcSimulator(
        body_system, integrator_settings, propagator_settings)

    # Propagate and store results to outer loop results dictionary.
    results[propagation_variant] = dynamics_simulator.state_history



################################################################################
# VISUALISATION / OUTPUT / PRELIMINARY ANALYSIS ################################
################################################################################

# After propagation, the state evolution is visualised by plotting the
#  trajectory of each body over the propagation time.
# Note that in the hierarchical case the raw output of the propagation cannot be
#  plotted in the one figure, since some bodies have their propagated state
#  defined w.r.t different bodies. The results of the hierarchical propagation
#  are therefore split over multiple figures.

from matplotlib import pyplot as plt


# auxiliary function for plotting multi-body state history and splitting hierarchical states
def plot_multi_body_system_state_history(system_state_history_array, propagated_bodies, hierarchical=False):

    if hierarchical:

        fig1 = plt.figure(figsize=(8, 24))  #figsize=plt.figaspect(3))
        ax1 = fig1.add_subplot(311, projection='3d')
        ax1.set_title(f'Trajectory of the Sun w.r.t SSB')
        ax1.scatter(0, 0, 0, marker='x', label="Sun")

        ax2 = fig1.add_subplot(312, projection='3d')
        ax2.set_title(f'System state evolution w.r.t Sun')
        ax2.scatter(0, 0, 0, marker='x', label="SSB")

        ax3 = fig1.add_subplot(313, projection='3d')
        ax3.set_title(f'Trajectory of the Moon w.r.t Earth')
        ax3.scatter(0, 0, 0, marker='x', label="Earth")



        for i, body in enumerate(propagated_bodies):

            if body == "Sun":
                ax1.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                         system_state_history_array[:, 6 * i + 3],
                         label=body)

            elif body != "Sun" and body != "Moon":
                ax2.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                         system_state_history_array[:, 6 * i + 3],
                         label=body)

            elif body == "Moon":
                ax3.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                         system_state_history_array[:, 6 * i + 3],
                         label=body)

        axs = [ax1, ax2, ax3]
        ax_lims = [[-2.0E9, 2.0E9], [-2.5E11, 2.5E11], [-4.0E8, 4.0E8]]  # equal axis limit per subplot, [m]

        for ax, ax_lim in zip(axs, ax_lims):
            ax.legend()
            ax.set_xlabel('x [m]')
            ax.set_xlim(ax_lim)
            ax.set_ylabel('y [m]')
            ax.set_ylim(ax_lim)
            ax.set_zlabel('z [m]')
            ax.set_zlim(ax_lim)



    else:

        fig1 = plt.figure(figsize=(8, 8))
        ax1 = fig1.add_subplot(111, projection='3d')
        ax1.set_title(f'System state evolution of all bodies w.r.t SSB.')


        for i, body in enumerate(propagated_bodies):
            ax1.plot(system_state_history_array[:, 6 * i + 1], system_state_history_array[:, 6 * i + 2],
                     system_state_history_array[:, 6 * i + 3],
                     label=body)
            ax1.scatter(system_state_history_array[0, 6 * i + 1], system_state_history_array[0, 6 * i + 2],
                        system_state_history_array[0, 6 * i + 3],
                        marker='x')

        ax1.scatter(0, 0, 0, marker='x', label="SSB", color='black')
        ax1.legend()
        ax1.set_xlabel('x [m]')
        ax1.set_xlim([-2.5E11, 2.5E11])
        ax1.set_ylabel('y [m]')
        ax1.set_ylim([-2.5E11, 2.5E11])
        ax1.set_zlabel('z [m]')
        ax1.set_zlim([-2.5E11, 2.5E11])

    return fig1

# convert state history dictionaries to arrays for easier processing
barycentric_system_state_array = result2array(results['barycentric'])
hierarchical_system_state_array = result2array(results['hierarchical'])

# plot system evolution
figA = plot_multi_body_system_state_history(barycentric_system_state_array, bodies_to_propagate)
figB = plot_multi_body_system_state_history(hierarchical_system_state_array, bodies_to_propagate, hierarchical=True)
plt.tight_layout()
plt.show()

figA.savefig('output/multi_body_barycentric', dpi=400)
figB.savefig('output/multi_body_hierarchical', dpi=400)
