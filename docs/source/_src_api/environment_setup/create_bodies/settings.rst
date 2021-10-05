.. _creating_celestial_bodies:

=========================
Creating Celestial Bodies
=========================


Creating a set of celestial bodies is done by creating a list of settings for all bodies, after which these settings are parsed to create a set of ``body`` objects. In creating this system of bodies, all interdependencies between them are automatically processed. The typical first step, when defining celestial bodies, is to retrieve their 'default' settings as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

where the ``global_frame_origin`` and ``global_frame_orientation`` define the reference frame in which state vectors stored in the environment `during` propagation are represented. In general, it is recommended to choose this as the most 'intuitive' frame origin for your propagation (e.g. SSB or Sun for solar system scale propagations, Earth for an Earth orbiter, Mars for a Martian mission, etc.). This frame definition is *distinct* from the center of propagation that you can define in your :ref:`propagator setup<simulation_propagator_setup>`.  See the page on :ref:`reference frames<propagation_reference_frames>` for details on the distinction between them.

The following options are currently available:

 * ``global_frame_origin`` Any of the bodies in the environment (provided it has an ephemeris defined), or the solar system barycenter (SSB)
 * ``global_frame_orientation`` Presently, options are limited to the ``J2000`` and ``ECLIP_J2000`` frame (see `reference frames<propagation_reference_frames>` for details)

Generating default settings prevents a user from having to manually define a varity of 'typical' models for solar-system bodies. The full list of default body settings is discussed :ref:`here<default_environment_models>`. Note that the ephemerides that are used by default are only valid for a somewhat limited time interval (on the order of a century, depending on the specific body).

In addition to the above method of creating default bodies, we offer an alternative which is more computationally efficient, at the expense of higher RAM usage and a more limited time interval in which the environment is valid. Such an approach is typically only used when computational speed is very important, and is described in more detail :ref:`here<valid_time_range>`.

Default settings may be overridden as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

Where the above example overrides the default setting for the Sun's gravity field, and sets a point-mass gravity field with a gravitational parameter of 1.32712440042 :math:`\cdot` 10 :superscript:`20` m :superscript:`3` / s :superscript:`2`. A comprehensive list of *all* environment models, and how their settings can be defined and overridden as above, is given in this :ref:`available_environment_models`.
Once all settings for the bodies are defined as desired, the bodies are created and linked as follows:

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

This ``bodies`` in the above simulation are the heart of many Tudat simulations: they contain all properties of your celestial and manmade bodies, and are used to retieve properties of your accelerations, state derivative models, output variables, etc. 

It is crucial to understand the distinction between ``body_settings`` and ``bodies``. The former is merely a list of settings for the models in the environment, and do not provide any functionality to perform any specific calculations: it describes what the models should do. The latter (``bodies``) is the object which is actually used during the propagation, and performs all required calculations (updating an ephemeris to the current time, calculating body orientations, determining atmospheric properties at a given location, *etc*). Since the creation of the ``bodies`` requires many steps, links with other packages, links between bodies, links between environment objects, frame transformations, `etc.`, we have chose to not require a manual definition of its contents by the user. Manual creation of a ``Body`` is possible, and can be useful approach for :ref:`creating_artificial_bodies`, which typically have less complex interdependencies with the rest of the environment.



