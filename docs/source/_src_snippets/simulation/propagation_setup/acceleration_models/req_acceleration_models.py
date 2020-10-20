from tudatpy.kernel import constants
from tudatpy.kernel.interface import spice_interface
from tudatpy.kernel.simulation import environment_setup
from tudatpy.kernel.simulation import propagation_setup

# Define simulation time and step size
simulation_start_epoch = 0.0
simulation_end_epoch = constants.JULIAN_DAY
fixed_step_size = 100.0


# Load spice kernels.
spice_interface.load_standard_kernels()

# Create body objects
bodies_to_create = ["Earth"]

body_settings = environment_setup.get_default_body_settings(bodies_to_create,
            simulation_start_epoch,
            simulation_end_epoch,
            fixed_step_size)

bodies = environment_setup.create_bodies(body_settings)

# Create vehicle object
bodies["Apollo"] = environment_setup.Body()

# Set mass of vehicle
bodies["Apollo"].set_constant_body_mass(2000.0)

global_frame_origin = "SSB"
global_frame_orientation = "ECLIPJ2000"
environment_setup.set_global_frame_body_ephemerides(bodies, global_frame_origin,
                                                       global_frame_orientation)

# Define bodies that are propagated.
bodies_to_propagate = ["Apollo"]

# Define central bodies.
central_bodies = ["Earth"]