from tudatpy.kernel.interface import spice_interface

# load tudat standard spice kernels
spice_interface.load_standard_kernels()

# --------------------------------------------------
#  get gravitational parameter of Earth using spice:
# --------------------------------------------------

# get GM of Earth using spice bodvrd routine
EARTH_GM = spice_interface.get_body_gravitational_parameter("Earth")

EARTH_GM = spice_interface.get_body_properties("Earth", "GM", 1)

EARTH_RADII = spice_interface.get_body_properties("Earth", "RADII", 3)

print(EARTH_RADII)

# --------------------------------------------------
# get cartesian state of Earth using spice:
# --------------------------------------------------
EARTH_STATE = spice_interface.get_body_cartesian_state_at_epoch(
    target_body_name="Earth",
    observer_body_name="SSB",
    reference_frame_name="ECLIPJ2000",
    aberration_corrections="None",
    ephemeris_time=0)

print(EARTH_STATE)
