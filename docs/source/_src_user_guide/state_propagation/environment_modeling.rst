.. _environment_setup:

=================
Environment Setup
=================


General information
====================

In TudatPy, the physical environment is defined by a system of bodies, each encapsulated in a
:class:`~tudatpy.numerical_simulation.environment.Body` object. Each body contains a list of properties
(gravity field, ephemeris, *etc.*, see below for a comprehensive list), which may be interdependent.

.. note::
   The :class:`~tudatpy.numerical_simulation.environment.Body` object may represent a celestial body or a
   manmade vehicle. Tudat makes *no* a priori distinction between the two: the distinction is made by the user when
   creating the bodies.

The combination of all Body objects is stored in a
:class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object (typically named
simple ``bodies`` in the code). During the propagation, all the required properties of bodies are extracted and combined
to evaluated accelerations/torques/guidance/... and compute the state derivative of thee system.

Procedure
==================

The typical procedure to create the environment is represented in the figure and explained below.

1. **Create body settings**: create settings for bodies which have default settings (typically celestial bodies) and,
   if needed, customize these settings as desired (see :ref:`create_celestial_body_settings`).

2. **Create system of bodies**: use the settings above to create a system of body objects, automatically resolving any
   interdependencies (see :ref:`create_bodies_from_settings`).

In addition, if needed:

3. **Create and model empty bodies**: create any additional bodies which have no defaults (typically a vehicle) and
   assign properties to them (see :ref:`create_artificial_bodies`).

.. figure:: _static/tudatpy_environment.png
   :width: 600

Environment information during the propagation
===============================================

In some cases, you may need to interact with the simulation environment *during* the propagation.
You can find details on how to extract information (states, orientations, altitude, *etc.*) from the simulation
during the propagation in :ref:`environment_during_propagation`.

