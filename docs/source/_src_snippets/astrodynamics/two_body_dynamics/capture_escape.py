# required external imports (for parameters)
import numpy as np
import spiceypy as spice
import os

# required internal imports
from tudatpy.kernel import io
from tudatpy.kernel.astro import two_body_dynamics
from tudatpy.kernel.interface import spice_interface

# future implementation
spice_kernel_paths = spice_interface.get_standard_kernels([])

# load standard spice kernels
spice.furnsh(spice_kernel_paths)

# --------------------------------------------------
#  get gravitational parameter of Earth using spice:
# --------------------------------------------------

# get GM of Earth using spice bodvrd routine
spice_bodvrd_result = spice.bodvrd("Earth", "GM", 1)

# extract value from result which is tuple of (dim, values)
spice_bodvrd_param = spice_bodvrd_result[1][0]  # km^3/s^2

# convert to m^3/s^2
EARTH_GM = spice_bodvrd_param * (10 ** 3) ** 3

# --------------------------------------------------
# get average radius of Earth using spice:
# --------------------------------------------------

# get GM of Earth using spice bodvrd routine
spice_bodvrd_RADII_result = spice.bodvrd("Earth", "RADII", 3)

# extract value from result which is tuple of (dim, values)
spice_bodvrd_RADII = spice_bodvrd_RADII_result[1]  # km

# average ellipsoid radii for single value and convert to m
EARTH_R = np.average(spice_bodvrd_RADII) * 10 ** 3

# compute delta V required for Earth escape/departure from/to 100 km LEO
# requiring/exhibiting 1 km/s excess velocity
ΔV = two_body_dynamics.compute_escape_or_capture_delta_v(
    gravitational_param=EARTH_GM,
    semi_major_axis=EARTH_R + 100E3,  # 100 km LEO
    eccentricity=0.0,  # circular parking orbit
    excess_velocity=1E3  # 1 km/s needed in heliocentric
)
