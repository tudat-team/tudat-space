.. _creation_celestial_body_settings:

===================================
Creation of celestial body settings
===================================

The usual workflow to create celestial body settings is composed of two subsequent steps, described separately:

1. :ref:`default_body_settings`
2. :ref:`custom_body_settings`

.. warning::
   Body settings are not used in the propagation: they are only used to define the *settings* of the body objects, and are used to create ``Body`` objects, which are used during the propagation and contain the actual objects/functions performing the relevant calculations. This procedure is
   described in the separate page :ref:`create_modifying_bodies`.


.. _default_body_settings:

Creating body settings
======================

In most cases, the starting point for the creation of body settings will be the extraction of *default settings*. This prevents a user from having to manually define a variety of 'typical' models for
solar-system bodies. The full list of default body settings is given at :ref:`default_env_models`, and
 can be retrieved as follows, using the :func:`~tudatpy.numerical_simulation.environment_setup.get_default_body_settings` function:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
             :language: python
    

where the ``global_frame_origin`` and ``global_frame_orientation`` define the reference frame in which state vectors
stored in the environment `during` propagation are represented. In general, it is recommended to choose this as the most 'intuitive' frame origin for your propagation
(e.g. SSB or Sun for solar system scale propagations, Earth for an Earth orbiter, Mars for a Martian mission, etc.). The `frame_orientation` may be omitted altogether, in which case the default ECLIPJ2000 is used. The above function creates an object of type :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings`, which stores the settings for all bodies (as a list of :class:`tudatpy.numerical_simulation.environment_setup.BodySettings` objects)

Note that the frame origin definitions is *distinct* from the 
center of propagation that you can define for the propagation of translational dynamics (see :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` function, and the :ref:`translational_dynamics` page). For more information about this distinction, and the use of these reference frames in general, see :ref:`reference_frames`.

In addition to the above method of creating default bodies, we offer an alternative which is more computationally efficient, at the expense of higher RAM usage and a more limited time interval in which the environment is valid. Such an approach is typically only used when computational speed is very important, and is described in more detail :ref:`here<default_bodies_limited_time_range>`.

Finally, in case you want to initialize body settings without *any* default settings, the ``body_settings`` in the above script can also be created manually as:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/body_list_settings_manual.py
             :language: python

where the frame origin and orientation have been defined manually as "Earth" and "J2000", respectively.


.. _custom_body_settings:

Customization of body settings
==============================

Although the default body settings are often very useful, there are various cases where a user will want to override these default settings, or where these default settings cannot be use. The manner in which to overrride the default settings can be divided into three categories:

* Modifying the *type* of the default model that is used. Example: using a spherical harmonic gravity field instead of a point-mass gravity field
* Modifying the specific *parameters* inside a given default model setting. Example: modifying the value of the gravitational parameter used for the given default model
* Created body settings from scratch, without any use of the default settings.

Below we show each manner to modify the settings with a representative example. 

.. seealso::
   A comprehensive list of *all* environment models, and how their settings can be defined and overridden as above, is
   given in the page about :ref:`available_environment_models`.

.. _override_body_settings:

Overriding existing settings objects
------------------------------------

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
             
The above works equally well if the existing environment model settings are empty. Where the above example creates a new gravity field settings object, and overrides the default setting for the Sun's gravity field with this new object. The new settings define a point-mass gravity field with a gravitational parameter of 1.32712440042 :math:`\cdot` 10 :superscript:`20` m :superscript:`3` / s :superscript:`2`.


Modifying parameters in existing settings objects
-------------------------------------------------

Default settings may be overridden as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default_parameters.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

Where the value of the gravitational parameter in the Sun's gravity field is changed to 1.32712440042 :math:`\cdot` 10 :superscript:`20` m :superscript:`3` / s :superscript:`2`. Functionally, this example is identical to the previous one, but it permits different kinds of modifications to be made. It allows only a *single* property of the environment model to be modified, while in the previous example, it is required that *all* properties are redefined by the user (for the point-mass gravity field, which has only one property in the settings, this point is moot). The present example therefor allows for more 'fine-grained' control of the settings, but limits the user to a modifying the properties of the settings, without providing the flexibility to modify the *type* of settings (which is allowed in the previous example).

To understand how to know the syntax of the above example, but for different types of environment models:

* The type of the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_settings` attribute of the :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` is  :class:`tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings`, as shown in the API documentation.
* The :attr:`~tudatpy.numerical_simulation.environment_setup.gravity_field.CentralGravityFieldSettings.gravitational_parameter` attribute of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings` is a ``float``, and can be modified by a user, as shown in the API documentation.
* So: provided that the body settings for the Sun has *any* gravity field settings, the above will work. If it does not, you should first create such settings (see :ref:`override_body_settings`)

Below is a slightly more involved example, which does not use a property of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings` base class, but rather the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings` derived class. Therefore, the example below will only work if the current gravity field settings for the Earth already define a spherical harmonic gravity field:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/override_default_parameters_sh.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp
           
Here, we extracted, modified, and then reset the :attr:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings.normalized_cosine_coefficients` property of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings`.

Creating a new settings object
------------------------------

Some bodies do not have any default settings, and in some cases all default settings may be different from what a user desired. In such cases, manually creating the settings can also be done.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_new_body_settings.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

In this example, empty body settings for a body 'Oumuamua' are first added. When adding such settings, no properties whatsoever are assigned to the body, the only thing that it assigned to it is its existence, but it has no ephemeris, gravity field, etc. Each environment model setting has to be manually added.

The above setup is also one that is typically used for artificial bodies, for which no default settings are currently implemented. Even though the type and settings of a vehicle's constituent environment (and system) models are typically very different from a natural body, the manner in which such a body is set up is not fundamentally different in Tudat. See below for a representative example:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.py
             .. literalinclude:: /_src_snippets/simulation/environment_setup/default_bodies.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_new_vehicle_settings.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp
             
In the above code snippet, you may notice two seemingly different aspects from the other environment models:

* The settings for the radiation pressure interface, which has ``Sun`` as key, unlike any of the other environment models. This is due to the fact that a body may have radiation pressure settings for any number of source bodies
* The body mass, which is set directly as a value (here 500 kg). This is due to the fact that the mass is stored in the :class:`~tudatpy.numerical_simulation.environment.Body` object directly as a value (or a function, if it is time-variable) rather than as a dedicated environment model class







