.. _creation_celestial_body_settings:

===================
Creating the bodies
===================

The usual workflow to create bodies in Tudat (both natural and artificial bodies!) is composed of three subsequent steps, described separately:

1. :ref:`default_body_settings`
2. :ref:`custom_body_settings`
3. :ref:`create_bodies_from_settings_first`

.. warning::
   Body settings are not used in the propagation: they are only used to define the *settings* of the body objects, and are used to create ``Body`` objects, which are used during the propagation and contain the actual objects/functions performing the relevant calculations. This procedure is
   described in the separate page :ref:`create_modifying_bodies`.


.. _default_body_settings:

Creating body settings
======================

In most cases, the starting point for the creation of body settings will be the retrieval of *default settings*. This
prevents a user from having to manually define a variety of 'typical' models for solar-system bodies. The full list of
default body settings is given at :ref:`default_env_models`, and can be retrieved using the
:func:`~tudatpy.numerical_simulation.environment_setup.get_default_body_settings` function:

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


where the ``global_frame_origin`` and ``global_frame_orientation`` define the reference frame in which state vectors
stored in the environment `during` propagation are represented. In general, it is recommended to choose this as the most 'intuitive' frame origin for your propagation
(e.g. SSB or Sun for solar system scale propagations, Earth for an Earth orbiter, Mars for a Martian mission, etc.). The above function creates an object of type :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings`, which stores the settings for all bodies.

.. note::

   The global frame origin definition is *distinct* from the 
   center of propagation that you can define for the propagation of translational dynamics (see :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` function, and the :ref:`translational_dynamics` page). For more information about this distinction, and the use of these reference frames in general, see :ref:`reference_frames`.

In addition to the above method of creating default bodies, we offer an alternative which is more computationally efficient, at the expense of higher RAM usage and a more limited time interval in which the environment is valid. Such an approach is typically only used when computational speed is very important, and is described in more detail :ref:`here<default_bodies_limited_time_range>`.

Finally, in case you want to initialize body settings without *any* default settings, ``body_settings`` can also be created manually as:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
            :language: python

      .. literalinclude:: /_src_snippets/simulation/environment_setup/body_list_settings_manual.py
         :language: python

where the frame origin and orientation have been defined manually as "Earth" and "J2000", respectively.


.. _custom_body_settings:

Customizing body settings
==============================

Although the default body settings are often very useful, there are various cases where a user will want to override these default settings, or where such default settings are not available. These cases can be divided into three categories:

* Modifying the *type* of the model that is used. Example: using a spherical harmonic gravity field instead of a point-mass gravity field
* Modifying the specific *parameters* inside a given default model setting. Example: modifying the value of the gravitational parameter used for the given default model
* Creating body settings from scratch, without any use of the default settings.

Below we show each manner to modify the settings with a representative example. 

.. seealso::
   A comprehensive list of *all* environment models, and how their settings can be defined and overridden as above, is
   given in the page about :ref:`environment_model_overview`.

.. _override_body_settings:

Overriding existing settings objects
------------------------------------

Default settings may be overridden as follows:

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

      .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default.py
         :language: python

The above works equally well if the existing environment model settings are empty or the default model is not suitable for the users simulation.
The new settings define a central gravity field with a gravitational parameter of :math:`1.32712440042 \cdot 10^{20}` m :superscript:`3` / s :superscript:`2` for the Sun.


Modifying parameters in existing settings objects
-------------------------------------------------

Parameters of default models may be overridden as follows:

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

      .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default_parameters.py
         :language: python

Functionally, this example is identical to the previous one, but it permits different kinds of modifications to be made. It allows only a *single* property of the environment model to be modified, while in the previous example, it is required that *all* properties are redefined by the user. The present example therefor allows for more 'fine-grained' control of the settings, but limits the user to a modifying the properties of the settings.

Below is a slightly more involved example, which does not use a property of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings` base class, but rather the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings` derived class. Therefore, the example below will only work if the current gravity field settings for the Earth already define a spherical harmonic gravity field:

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

      .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default_parameters_sh.py
         :language: python

Here, we extracted, modified, and then reset the :attr:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings.normalized_cosine_coefficients` property of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings`.

Provided that the body settings of the Sun and Earth have *any* gravity field settings, the above will work. If it does not, you should first create such settings (see :ref:`override_body_settings`).
For an overview of the relevant attributes, functions and classes for other environment models, see :ref:`environment_model_overview`.

.. _create_new_body_settings:

Creating a new settings object
------------------------------

Some bodies do not have any default settings, and in some cases all default settings may be different from what a user desired. In such cases, manually creating the settings can also be done.

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

      .. literalinclude:: /_src_snippets/simulation/environment_setup/add_new_body_settings.py
         :language: python

In this example, empty body settings for a body 'Oumuamua' are first added to the ``body_settings`` created previously. When adding such settings, no properties whatsoever are assigned to the body, the body is only given a name. Each environment model setting has to be manually added.

The above setup is also one that is typically used for artificial bodies, for which no default settings are currently implemented. Even though the type and settings of a vehicle's constituent environment (and system) models are typically very different from a natural body, the manner in which such a body is set up is not fundamentally different in Tudat. See below for a representative example:

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

      .. literalinclude:: /_src_snippets/simulation/environment_setup/add_new_vehicle_settings.py
         :language: python

In the above code snippet, you may notice that the body mass is set directly as a value (here 500 kg) in the :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. This is used as a 'shortcut' for the use of the :func:`~tudatpy.numerical_simulation.environment_setup.rigid_body.constant_rigid_body_properties` and assigning this to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rigid_body_settings`.

.. _create_bodies_from_settings_first:

Creating system of bodies from settings
===========================================

The :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` class is at the heart of many Tudat simulations. It contains all properties of your celestial and artificial bodies, and is used to retrieve properties of your accelerations, state derivative models, output variables, etc.
See the :ref:`environment_architecture` page for a more detailed discussion of the architecture of the :class:`~tudatpy.numerical_simulation.environment.Body` and :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` classes and the interdependencies between environment models.

The example below shows how to create a set of bodies from previously defined body settings, using the :func:`~tudatpy.numerical_simulation.environment_setup.create_system_of_bodies` function:

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


It is crucial to understand the distinction between ``body_settings`` (of type :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings`) and ``bodies`` (of type :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`). The former is merely a list of
settings for the models in the environment and is the main *input* to the body creation. It does not provide any functionality to perform any specific
calculations: it describes what the models *should* do when they are created. The latter (``bodies``) is the object which is actually used
during the propagation, and performs all required calculations (updating an ephemeris to the current time, calculating
body orientations, determining atmospheric properties at a given location, *etc*). Since the creation of the ``bodies``
requires many steps, links with other packages, links between bodies, links between environment objects, frame
transformations, *etc.*, we have chosen to not require a manual definition of its contents by the user, although such an approach is possible.







