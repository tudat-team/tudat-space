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

Simulation & Output
===================

Once all the settings are in place, the solution can be generated. All the details
about this part, including the interpretation and availability of outptuts, are explained in the page on :ref:`running_simulation`.
For simulations in which the dynamics and associated variational equations are propagated, see the page on :ref:`running_variatitonal_simulation`.


