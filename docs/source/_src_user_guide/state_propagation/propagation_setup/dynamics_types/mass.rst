.. _mass_dynamics:

=============
Mass Dynamics
=============

Settings to propagate numerically the mass of a body can be created through the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass` factory function, described in
detail in the API documentation. In this page, only the Tudat-specific aspects of the input will be briefly described.

The mass is typically propagated numerically to account for the influence of thrust on a vehicle's mass. Unlike other
types of dynamics, there are no alternative representations (propagators) for the mass.

Inputs
======

In addition to the settings described :ref:`here <propagation_inputs>`, the definition of rotatitonal dynamics settings requires:

- A set of mass models (created via the :func:`~tudatpy.numerical_simulation.propagation_setup.create_mass_rate_models` factory function; see below)
- The initial conditions for the propagation (initial mass and time)


Mass-rate models
================

The setup of a mass rate model in Tudat is substantially simpler than for the :ref:`accelerations <acceleration_model_setup>` and :ref:`torques <torque_model_setup>`.
This is, in part, due to the very limited set of options for computing mass rates.

Typically (but not necessarilly), a mass rate is directly related to a body's thrust. An example of this is shown below,
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

For a full description of available functions, see associated pages of `mass-rate models <https://tudatpy.readthedocs.io/en/latest/mass_rate.html>`_ and `thrust models <https://tudatpy.readthedocs.io/en/latest/thrust.html>`_ in the API documentation.

.. _mass_example:

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
