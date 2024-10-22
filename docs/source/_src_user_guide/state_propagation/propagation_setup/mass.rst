.. _mass_dynamics:

=============
Mass Dynamics
=============

Settings to propagate the mass of a body numerically can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass` factory function, described
in detail in the :doc:`API documentation <propagator>`. In the current page, only the
Tudat-specific aspects of the input will be briefly described.

The mass is typically propagated numerically to account for the influence of thrust on a vehicle's mass. Unlike other
types of dynamics, there are no alternative representations (propagators) for the mass.

Inputs
======

In addition to the general propagation settings described :ref:`here <propagation_inputs>`, the definition of rotational dynamics settings requires:

- A set of mass models (created via the :func:`~tudatpy.numerical_simulation.propagation_setup.create_mass_rate_models` factory function; see below)
- The initial conditions for the propagation (initial mass and time)


Mass-rate models
================

The setup of a mass rate model in Tudat is substantially simpler than for the :ref:`accelerations <acceleration_models_setup>` and :ref:`torques <torque_model_setup>`.
This is, in part, due to the very limited set of options for computing mass rates.

Typically, a mass rate is directly related to a body's thrust (a user may use thrust without mass propagation, although this will neglect part of the physics of the problem). 
An example of this is shown below,
where all thrust accelerations acting on a vehicle (which include a definition of specific impulse) are used to compute
the mass rate. Note that the acceleration models, created as discussed :ref:`here <acceleration_models_setup>`, are
required as input, to link the thrust acceleration to the mass rate.


.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
        :color: muted

        .. code-block:: python

            from tudatpy.kernel.numerical_simulation import propagation_setup

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/mass_models/from_thrust_mass_rate.py
         :language: python

For a full description of available functions, see associated pages of :doc:`mass-rate models <mass_rate>` and :doc:`thrust models <thrust>` in the API documentation. For mass rate models that are not internally associated with thrust (for whatever reason), the user is recommended to use the :func:`~tudatpy.numerical_simulation.propagation_setup.mass_rate.custom_mass_rate` function.

.. _mass_example:

Example
========

In the example below, the body "Spacecraft" will be propagated w.r.t. body "Earth", using given mass
rate models and a given initial mass. A Runge Kutta 4 integrator is defined with step-size of 2
seconds. The propagation will terminate once the ``simulation_end_epoch`` termination condition is
reached. Next to that, the propagator is asked to save the Keplerian state of the spacecraft as
dependent variable. The time and rotational state will be printed on the terminal once every 24
hours (simulation time).

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. dropdown:: Required
      :color: muted

      .. code-block:: python

          from tudatpy.kernel.numerical_simulation import propagation_setup

    .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
        :language: python
