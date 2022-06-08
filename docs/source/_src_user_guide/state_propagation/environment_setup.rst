.. _environment_setup:

=================
Environment Setup
=================

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   environment_setup/create_bodies/create_body_settings
   environment_setup/create_bodies/create_bodies_from_settings
   environment_setup/create_bodies/available
   environment_setup/create_bodies/default_settings
   environment_setup/architecture/custom_settings
   environment_setup/architecture/specific_environment_considerations
   environment_setup/architecture/environment_during_propagation
   environment_setup/architecture/use_of_reference_frames
   environment_setup/architecture/environment_architecture


General information
========================

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
to evaluated accelerations/torques/guidance/... and compute the state derivative of the system.

Procedure
========================

The typical procedure to create the environment is represented in the figure and explained below.

1. **Create body settings**: create settings for bodies which have default settings (typically celestial bodies) and,
   if needed, customize these settings as desired, and/or manually add settings for bodies without defaults (see :ref:`create_celestial_body_settings`).

2. **Create system of bodies**: use the settings above to create a system of body objects, automatically resolving any
   interdependencies (see :ref:`create_bodies_from_settings`).

In addition, if needed:

3. **Create and model additional bodies**: create any additional bodies which, and add them to the existing set of bodies (see :ref:`adding new bodies<create_empty_body>`).

.. figure:: _static/tudatpy_environment.png
   :width: 600

Environment information during the propagation
=================================================


In some cases, you may need to interact with the simulation environment *during* the propagation.
You can find details on how to extract information (states, orientations, altitude, *etc.*) from the simulation
during the propagation in :ref:`environment_during_propagation`.

