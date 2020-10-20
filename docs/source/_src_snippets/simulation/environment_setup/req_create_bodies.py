# import statements required
from tudatpy.kernel.simulation import environment_setup
from tudatpy.kernel.interface import spice_interface

# load spice kernels
spice_interface.load_standard_kernels()
