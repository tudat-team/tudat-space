.. _state_propagation_intro:

******************
State Propagation
******************

In this section, the different stages of a typical simulation setup are described.
TudatPy is organized as shown in the figure below.


 .. figure:: _static/tudatpy_high_level.png
    :width: 600


Inputs
=======

There are three separate input types necessary to create a simulation:

- **Environment setup**: physical modeling of environment properties (for both celestial and artificial bodies)
- **Propagation setup**: formulation of the differential equations representing the problem
- **Integration setup**: numerical integration settings used to solve such differential equations

Each part is presented in detail in the pages linked below.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   state_propagation/environment_modeling
   state_propagation/dynamical_modeling
   state_propagation/numerical_modeling


Simulation & Output
===================

Once all the settings are in place, the solution can be generated. All the details
about this part, including the interpretation and availability of outptuts, are explained in the page *Running
simulations* (see below).
For simulations in which the dynamics and associated variational equations are propagated, see the page on *Running
variation simulations*.


.. toctree::
   :maxdepth: 1

   state_propagation/running_simulation
   state_propagation/running_variational_simulation
