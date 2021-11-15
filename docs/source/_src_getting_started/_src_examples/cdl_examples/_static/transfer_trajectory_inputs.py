# Tudat imports
import BuildDirectory
from tudatpy.kernel.astro import trajectory_design
from tudatpy.kernel import constants

# General imports
import numpy as np

###########################################################################
# Define transfer trajectory properties
###########################################################################

# Define order of bodies (nodes)
transfer_body_orders = [['Earth', 'Venus', 'Venus', 'Earth', 'Jupiter', 'Saturn'],
                        ['Earth', 'Jupiter', 'Saturn']]

# Select type of transfer
# Valid options: - trajectory_design.unpowered_unperturbed_leg_type
#                - trajectory_design.dsm_velocity_based_leg_type
leg_type = trajectory_design.unpowered_unperturbed_leg_type

# Set departure date its margin
departure_date = (-789.8117 - 0.5) * constants.JULIAN_DAY
departure_date_margin = 180.0 * constants.JULIAN_DAY

# Define departure orbit
departure_semi_major_axis = np.inf              # Optional
departure_eccentricity = 0                      # Optional

# Define insertion orbit
arrival_semi_major_axis = 1.0895e8 / 0.02       # Optional
arrival_eccentricity = 0.98                     # Optional

###########################################################################
# Define variables used in the optimization
###########################################################################
# Set optimization parameters - see guidelines on Tudat website
number_of_evolutions = 3000
population_size = 500
optimization_seed = 4444                        # Optional

# Set maximum Delta V acceptable during the optimization
maximum_delta_v = 2e8 # [m/s]

# Set whether optimization plots are saved
save_optimization_plots = True

###########################################################################
# Define variables used for analysis of the transfer trajectories
###########################################################################
# Select properties for calculation of link budget
transmited_power = 27  # W
transmiter_antenna_gain = 10
receiver_antenna_gain = 1
frequency = 1.57542e9  # HZ

# Select ground station used
minimum_elevation = 10 * np.pi / 180
gs_latitude = 52.0115769 * np.pi / 180
gs_longitude = 4.3570677 * np.pi / 180
station_name = 'Delft'

# Set whether analysis plots are saved
save_analysis_plots = True