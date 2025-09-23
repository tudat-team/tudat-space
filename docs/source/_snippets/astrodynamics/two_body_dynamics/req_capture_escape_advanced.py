# required external imports (for parameters)
import numpy as np
import spiceypy as spice
import os

# required internal imports
from tudatpy import io
from tudatpy.astro import two_body_dynamics

# current implementation
tudat_spice_kernels = [
    "pck00010.tpc",
    "gm_de431.tpc",
    "tudat_merged_spk_kernel.bsp",
    "naif0012.tls"]

spice_kernel_paths = map(
    lambda x: os.path.join(io.get_spice_kernel_path(), x),
    tudat_spice_kernels)

# future implementation
# spice_kernel_paths = spice_interface.get_standard_kernels()

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