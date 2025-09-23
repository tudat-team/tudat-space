.. _termination_settings:

==============================
Termination Settings
==============================

The termination settings are a key parameter in the propagation of a body’s orbit, since these will determine the
computational time and the size of the output file. Depending on the application, the user may want to end the body
propagation according to different criteria. The
:class:`~tudatpy.dynamics.propagation_setup.propagator.PropagationTerminationSettings` object is a
mandatory input argument necessary to create propagation settings.

.. contents:: List of available termination settings
   :depth: 1
   :local:


Simulation time
================

The simulation stops once a certain simulation time has passed.

For more information, see the API reference entry:
:func:`~tudatpy.dynamics.propagation_setup.propagator.time_termination`.

.. note::
   The simulation time is expressed in seconds after a reference epoch (1st January 2000) and *not* after the initial
   time of the simulation.

CPU time
=========

The simulation stops once a certain CPU time has passed. This is useful to make sure that the propagation does not
exceed a certain computation time.

For more information, see the API reference entry:
:func:`~tudatpy.dynamics.propagation_setup.propagator.cpu_time_termination`.

Dependent variable
===================

The simulation stops once a dependent variable meets a given criterion. The termination variable can be any dependent
variable listed in :ref:`dependent_variables` (where the way to create those is also explained).
Such variable, together with the limit value, can be used as lower or upper boundary.

For more information, see the API reference entry:
:func:`~tudatpy.dynamics.propagation_setup.propagator.dependent_variable_termination`.

Custom function
================

The simulation stops once a user-defined function returns ``True``.

For more information, see the API reference entry:
:func:`~tudatpy.dynamics.propagation_setup.propagator.custom_termination`.

Hybrid
===================

The simulation stops once multiple criteria are met. It may be possible that the user desires to terminate a
propagation according several criteria, where such criteria may or may not be fulfilled simultaneously.

For more information, see the API reference entry:
:func:`~tudatpy.dynamics.propagation_setup.propagator.hybrid_termination`.

.. tip::
  When using a dependent variable as termination condition, it is advised to also include a (cpu) time termination
  condition to ensure that your simulation will terminate.






