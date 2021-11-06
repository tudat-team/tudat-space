******************
State Propagation
******************

In this section, the different stages of a typical simulation setup are described.
TudatPy is organized as shown in the figure below.


 .. figure:: _static/tudatpy_high_level.png
    :width: 1000


Inputs
=======

There are three separate input types necessary to create a simulation:

- :ref:`environment_setup`: physical modeling of environment properties (for both celestial and artificial bodies)
- :ref:`simulation_propagator_setup`: formulation of the differential equations representing the problem
- :ref:`integrator_setup`: numerical integration settings used to solve such differential equations

Each part is presented in detail in the pages linked above.

Simulator
=========

Once all the settings are in place, the simulation must be run by creating a `Simulator` object. All the details
about this part are explained in :ref:`running_simulation`.

Output
=======

All the output of the simulation is stored as different attributes of the `Simulator` object. For more information
about the output, please refer to :ref:`single_arc_propagation`.


