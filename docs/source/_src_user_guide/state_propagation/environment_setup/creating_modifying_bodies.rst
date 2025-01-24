
.. _create_modifying_bodies:

====================
Modifying the bodies
====================

Once all settings for the bodies are defined as described in :ref:`creation_celestial_body_settings`, the bodies are
created and linked together, so that all required interdependencies are automatically satisfied.  

.. _create_empty_body:

Adding bodies to an existing :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`
==============================================================================================

After creating a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` from body settings, any number of additional
custom bodies may be added to the simulation. Such an approach can be useful when:

* Wanting to create a body that has a custom environment model that depends on the other bodies (such as aerodynamic guidance, thrust guidance, etc.), see :ref:`custom_models` for a detailed set of options.
* Wanting to add bodies to an existing system of bodies in a simulation loop

One crucial downside of adding bodies to an existing :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` is that the dependencies between the bodies can only go in 'one direction':
the newly added body may depend on the existing bodies, but the existing bodies can not always be (easily) updated to depend on the newly added body.

.. warning::
   The (semi-)manual creation of bodies, or the modification of environment models of existing bodies, is *not* the recommended approach to take.
   Unless you have a good reason to take this approach (such as those listed above), we recommend the creation of bodies using
   :ref:`creation of body settings <creation_celestial_body_settings>`


The first step is to add an empty :class:`~tudatpy.numerical_simulation.environment.Body` object to the existing
:class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object through its
:meth:`~tudatpy.numerical_simulation.environment.SystemOfBodies.create_empty_body` method:

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
            :language: python
         .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
            :language: python
         .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
            :language: python

      .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
         :language: python


which adds a body with no properties to the system.


.. _decorate_empty_body:

Addition of properties to a body
=================================

Properties can be added to an existing body after the body's creation (with the limitations mentioned above). For an artificial body, typical properties are:

* Rigid body model (mass, center of mass, inertia tensor), using the :func:`~tudatpy.numerical_simulation.environment_setup.add_rigid_body_properties` function
* Aerodynamic coefficients, using the :func:`~tudatpy.numerical_simulation.environment_setup.add_aerodynamic_coefficient_interface` function
* Radiation pressure target model, using the :func:`~tudatpy.numerical_simulation.environment_setup.add_radiation_pressure_target_model` function
* Engine model, using the :func:`~tudatpy.numerical_simulation.environment_setup.add_engine_model` or :func:`~tudatpy.numerical_simulation.environment_setup.add_variable_direction_engine_model` function
* Rotation model, using the :func:`~tudatpy.numerical_simulation.environment_setup.add_rotation_model` function

.. use manually synchronized tabs instead of tabbed code to allow dropdowns
.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
            :language: python
         .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
            :language: python
         .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
            :language: python
         .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
            :language: python

      .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body_properties.py
         :language: python

.. note::

  For the addition of the mass, we use the shorthand ``mass`` attribute of the :class:`~tudatpy.numerical_simulation.environment.Body` class.
  Modifying this attribute is equivalent to the second (commented) method to add a mass to a vehicle using the
  :func:`~tudatpy.numerical_simulation.environment_setup.add_rigid_body_properties` function.  The mass
  is an atypical property, for which we support the direct setting through the Body class, without
  going through a constituent environment model. We stress that this is *merely an interface of convenience*, and
  the (commented) interface in the above code snippet represents the 'formal' way of doing things.

In this example, the settings for the aerodynamic coefficients and radiation pressure are defined as the most
simple models available (constant drag-only aerodynamic coefficients, and cannonball radiation pressure).
The above approach uses the settings for environment models, just as the :ref:`creation of bodies from settings<creation_celestial_body_settings>`
(which is the preferred and recommended approach in most cases). However, instead of storing these environment settings
in a larger object defining the settings for the full bodies, and for all bodies together,
here we use the environment model settings *one at a time*. For each supported environment model, an ``add....``
function is provided in the :doc:`environment_setup` module.

Note that a similar approach is typically taken to add ground stations to a body (see :ref:`groundStationCreation`)
