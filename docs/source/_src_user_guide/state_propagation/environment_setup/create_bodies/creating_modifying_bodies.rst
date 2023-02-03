
.. _create_modifying_bodies:

=================================
Creating and modifying the bodies
=================================

Once all settings for the bodies are defined as described in :ref:`creation_celestial_body_settings`, the bodies are
created and linked together, so that all required interdependencies are automatically satisfied.  

.. _create_bodies_from_settings_first:

Creation of system of bodies from settings
===========================================

The example below shows how to create a set of bodies, using the :func:`~tudatpy.numerical_simulation.environment_setup.create_system_of_bodies` function:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp


The :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` class (the type of the ``bodies`` variable in the above simulation) is at the heart of many Tudat simulations. It contains all
properties of your celestial and manmade bodies, and is used to retieve properties of your accelerations, state derivative models, output
variables, etc. A more detailed discussion of the architecture of the :class:`~tudatpy.numerical_simulation.environment.Body` and :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` classes, as well as their constituent environment models and possible interdependencies, are discussed :ref:`here <environment_architecture>`

It is crucial to understand the distinction between ``body_settings`` (of type :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings`) and ``bodies`` (of type :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`). The former is merely a list of
settings for the models in the environment and is the main *input* to the body creation. It does not provide any functionality to perform any specific
calculations: it describes what the models *should* do when rhet are created. The latter (``bodies``) is the object which is actually used
during the propagation, and performs all required calculations (updating an ephemeris to the current time, calculating
body orientations, determining atmospheric properties at a given location, *etc*). Since the creation of the ``bodies``
requires many steps, links with other packages, links between bodies, links between environment objects, frame
transformations, `etc.`, we have chose to not require a manual definition of its contents by the user, although such an apporoach is possible. 


.. _create_empty_body:

Adding bodies to an existing ``SystemOfBodies``
===============================================

After creating a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` from body settings, any number of additional
custom bodies may be added to the simulation. Such an approach can be useful when:

* Wanting to add bodies to an existing system of bodies (for instance: first running a simulation with N bodies, and then one with N+1 bodies)
* Wanting to create a body that has a custom environment model that depends on the other bodies (such as aerodynamic guidance, thrust guidance, etc.), see :ref:`custom_models` for a detailed set of options.

One crucial downside of adding bodies to an existing ``SystemOfBodies`` is that the dependencies between the bodies can only go in 'one direction': the newly added body may depend on the existing bodies, but the existing bodies can typically not be updated to depend on the newly added body. 

.. warning::
   The (semi-)manual creation of bodies, or the modification of environment models of existing bodies, is *not* the recommended approach to take. Unless you have a good reason to take this approach (such as those listed above), we recommend the creation of bodies using :ref:`creation of body settings <creation_celestial_body_settings>`


The first step is to add an empty :class:`~tudatpy.numerical_simulation.environment.Body` object to the existing
:class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object through its
:meth:`~tudatpy.numerical_simulation.environment.SystemOfBodies.create_empty_body` method:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

which adds a body with no properties to the system.


.. _decorate_empty_body:

Addition of properties to a body
=================================

Properties can be added to an existing body after the body's creation (with the limitations mentioned above). For an artificial body, typical properties are:

* Mass
* Aerodynamic coefficients
* Radiation pressure properties
* Engine model
*

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/create_system_of_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_body_properties.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

In this example, the settings for the aerodynamic coefficients and radiation pressure are defined as the most simple models available (constant drag-only aerodynamic coefficients, and cannonball radiation pressure). The above approach uses the settings for environment models, just as the `creation of bodies from settings<creation_celestial_body_settings>` (which is the preferred and recommended approach in most cases). However, instead of storing these environment settings in a larger object defining the settings for the full bodies, and for all bodies together, here we use the environment model settings *one at a time*. For each supported environment model, an ``add....`` function is provided in the :mod:`~tudatpy.numerical_simulation.environment_setup` module.  

Note that a similar approach is typically taken to add ground stations to a body (see :ref:`ground_stations`)

.. seealso::
   A comprehensive list of settings for both types of models can be found in :ref:`available_environment_models`.
