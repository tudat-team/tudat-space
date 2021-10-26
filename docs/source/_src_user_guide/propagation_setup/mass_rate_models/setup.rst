.. _mass_rate_model_setup:

=====================
Mass Rate Model Setup
=====================

The setup of a mass rate model in Tudat is substantially simpler than for the :ref:`accelerations <acceleration_model_setup>` and :ref:`torques <torque_model_setup>`. This is, in part, due to the very limited set of options for computing mass rates. Typically, a mass rate should be directly related to a body's thrust. An example of this is shown below:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/mass_models/from_thrust_mass_rate.py
             :language: python

         .. tab:: C++

             :language: cpp

Here, all thrust accelerations acting on a vehicle (which include a definition of specific impulse) are used to compute the mass rate. Note that the acceleration models, created as discussed :ref:`here <acceleration_model_setup>`, are required as input, to link the  thrust acceleration to the mass rate.              