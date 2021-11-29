
.. _create_bodies_from_settings:

Creation of system of bodies from settings
===========================================

Once all settings for the bodies are defined as described in :ref:`create_celestial_body_settings`, the bodies are
created and linked as shown in the example below, using the :func:`~tudatpy.numerical_simulation.environment_setup.create_system_of_bodies` function:

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


The body system (``bodies`` in the above simulation) are the heart of many Tudat simulations: they contain all
properties of your
celestial and manmade bodies, and are used to retieve properties of your accelerations, state derivative models, output
variables, etc.

It is crucial to understand the distinction between ``body_settings`` (of type :func:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings`) and ``bodies`` (of type :func:`~tudatpy.numerical_simulation.environment.SystemOfBodies`). The former is merely a list of
settings for the models in the environment, and do not provide any functionality to perform any specific
calculations: it describes what the models should do. The latter (``bodies``) is the object which is actually used
during the propagation, and performs all required calculations (updating an ephemeris to the current time, calculating
body orientations, determining atmospheric properties at a given location, *etc*). Since the creation of the ``bodies``
requires many steps, links with other packages, links between bodies, links between environment objects, frame
transformations, `etc.`, we have chose to not require a manual definition of its contents by the user. Manual creation
of a ``Body`` is possible, and can be useful approach for :ref:`creating_artificial_bodies`, which typically have less
complex interdependencies with the rest of the environment.

