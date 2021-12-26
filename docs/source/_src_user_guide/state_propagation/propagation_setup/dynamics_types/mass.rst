.. _mass_dynamics:

=============
Mass Dynamics
=============


Settings to propagate numerically the translational state of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass` factory function, described in
detail in the API reference, which creates an object of type
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.MassPropagatorSettings` (see below
an :ref:`example`).

.. tip::
  Propagating the mass of a body is typically (but not exclusively) coupled with the use of a
  thrust model.

.. todo::
    Add page and link to thrust guidance.

In this page, only the Tudat-native objects necessary as input will be described. For all the other inputs, please
refer to the related API entry (:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass`).

.. note::
  Settings to define the propagation of rotational dynamics reflect those specified in :ref:`translational_dynamics`
  and :ref:`rotational_dynamics`.
  Besides the obvious differences, an important one is that no 'central body' and no propagator type are given.

Inputs
=======

The Tudatpy-native inputs to create the settings for a translational propagator are the following:

- a set of mass models (created via the :func:`~tudatpy.numerical_simulation.propagation_setup.create_mass_rate_models` factory function);
- settings to terminate the propagation (see :ref:`termination_settings`);
- dependent variables that should be saved (see :ref:`dependent_variables`).

.. _example:

Example
========

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth", using given mass rate models (not
provided) and a given initial mass.
The propagation will terminate once the ``simulation_end_epoch`` epoch is reached.
Next to that, the propagator is asked to save the total acceleration, Keplerian state, latitude, and longitude of the
spacecraft as
dependent variables. The time and state will be printed on the terminal once every 24 hours (simulation time), while
the state will be propagated through the Encke formulation.
dependent variable. The time and rotational state will be printed on the terminal once every 24 hours (simulation
time).

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup


          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

.. note::
    The setup of a mass rate model in Tudat is substantially simpler than for the
    :ref:`accelerations <acceleration_model_setup>` and :ref:`torques <torque_model_setup>`.
    This is, in part, due to the very limited set of options for computing mass rates.

Typically, a mass rate should be directly related to a body's thrust. An example of this is shown below,
where all thrust accelerations acting on a vehicle (which include a definition of specific impulse) are used to compute
the mass rate. Note that the acceleration models, created as discussed :ref:`here <acceleration_model_setup>`, are
required as input, to link the thrust acceleration to the mass rate.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/mass_models/from_thrust_mass_rate.py
             :language: python

         .. tab:: C++

             :language: cpp

.. seealso::
    For a full description of available functions, see associated pages of `mass-rate models <https://tudatpy.readthedocs.io/en/latest/mass_rate.html>`_ and `thrust models <https://tudatpy.readthedocs.io/en/latest/thrust.html>`_ in the API documentation.
