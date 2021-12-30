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

- :ref:`environment_setup`: physical modeling of environment properties (for both celestial and artificial bodies)
- :ref:`propagation_setup`: formulation of the differential equations representing the problem
- :ref:`integrator_setup`: numerical integration settings used to solve such differential equations


.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   state_propagation/environment_setup
   state_propagation/propagation_setup
   state_propagation/integration_setup


Simulation & Output
===================

Once all the settings are in place, the solution can be generated. All the details
about this part, including the interpretation and availability of outputs, are explained in the page about
:ref:`running_simulation`.
For simulations in which the dynamics and associated variational equations are propagated, see the page on
:ref:`running_variational_simulation`.


.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   state_propagation/running_simulation
   state_propagation/running_variational_simulation
