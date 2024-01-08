
.. _environment_model_overview:

==================
Environment Models
==================

   
On this page, we provide an overview of the categories of environment models that are available, how to create them, how to access them, as well as some general notes on their usages, typical pitfalls, hints, etc. How to define the settings for an environment model is discussed :ref:`here <custom_body_settings>`. Summarizing, settings for an environment model are stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object, a list of which (one for each body) is stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings` object. We reiterate that these objects themselves do not have any "functionality", except providing settings that define how to create the actual (potentially interconnected and interdependent environment models). After creating the environment, you can access any relevant functionality of the environment models (ephemerides, rotation models, etc.) outside the context of a propagation.

.. note::
    For details on how to access the environment *during a propagation* (for custom models, typically), see :ref:`this page <environment_during_propagation>`

In Tudat, the full environment is stored in a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object, which in turn stores environment models inside :class:`~tudatpy.numerical_simulation.environment.Body` objects (one for each natural or artifical body in your model). From each object representing a body, you can extract each separate environment model (see list below). For instance, to retrieve the :class:`~tudatpy.numerical_simulation.environment.Ephemeris` object from the body named ``Earth``, you can use the following:

    .. code-block:: python

        bodies = .... // Create system of bodies
        earth_ephemeris = bodies.get('Earth').ephemeris

Below, we provide an overview of the different types of environment models for which you can define settings, along with links to submodules of ``environment_setup`` in the `API documentation <https://py.api.tudat.space/en/latest/environment_setup.html>`_, where a comprehensive list of all environment model settings can be found. In addition, we list how to extract the resulting environment model from the ``Body`` objects

.. _available_environment_models:

Available Model Types
=====================

The complete list of available environment model settings can be found on our API documentation. Below is a list with the different categories of models, and a link to the corresponding Tudatpy module

* `Aerodynamic coefficients <https://py.api.tudat.space/en/latest/aerodynamic_coefficients.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.aerodynamic_coefficient_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define aerodynamics force (and if required, moment) coefficients of a body.
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.aerodynamic_coefficient_interface`, which provides a :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface`

* `Atmosphere models <https://py.api.tudat.space/en/latest/atmosphere.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.atmosphere_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  

   * These models provide various ways in which to define atmospheric properties of a body. For state propagation, the density will typically be the most important one. However, many of the models here include outputs of temperature, density, etc. as well. Depending on the model, the atmospheric properties may be only altitude-dependent, or fully time- and position-dependent. Note that the atmosphere settings can include wind settings (default: none)
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.atmosphere_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.AtmosphereModel`


* `Ephemeris models <https://py.api.tudat.space/en/latest/ephemeris.html>`_, , to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.ephemeris_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  
  
   * These models provide various ways in which to define predetermined (e.g. not coming from a Tudat propagation) translational states of bodies in the solar system
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.ephemeris`, which provides a :class:`~tudatpy.numerical_simulation.environment.Ephemeris`
  
* `Gravity field models <https://py.api.tudat.space/en/latest/gravity_field.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  

   * These models provide various ways in which to define the gravitational field of solar system bodies. Note: the mass associated with these gravitational field is the gravitational mass, which does *not* need to be equal to its inertial mass.
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.gravity_field_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.GravityFieldModel` (note that gravity field variations are stored inside this object)
  
* `Gravity field variation models <https://py.api.tudat.space/en/latest/gravity_field_variation.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_variation_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. Note: this attribute is a list, and any number of variation models may be added.  

   * These models provide various ways in which to define the time-variability of a body's (spherical harmonic) gravity field.
   * Unlike most environment models, the gravity field variations are stored inside the gravity field model, rather than directly in the body object.
  
* `Rotation models <https://py.api.tudat.space/en/latest/rotation_model.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rotation_model_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define the orientation of a body w.r.t. inertial space, and produces a quaternion/rotation matrix, and angular velocity vector/rotation matrix derivative. Note that Tudat can also produce such models by numerical propagation of the Euler equations (see :ref:`rotational_dynamics`).
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.rotation_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris`

* `Shape models <https://py.api.tudat.space/en/latest/shape.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.shape_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define the exterior of a *natural* body and is typically used to calculate (for instance) altitude, ground station position, etc. Note: the exterior shape of an artificial body, from which aerodynamic and radiation pressure properties can be evaluated, uses a different interface, which is currently under development
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.shape_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.ShapeModel`

* `Shape deformation models <https://py.api.tudat.space/en/latest/shape_deformation.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.shape_deformation_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  Note: this attribute is a list, and any number of deformation models may be added.  

   * These models provide various ways in which to define time variability of the shape of a body. These are typically relevant for detailed position models of ground stations (note that the models assigned here are global; station-specific models can be assigned to individual stations)
 
* `Radiation pressure source and target models <https://py.api.tudat.space/en/latest/radiation_pressure.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.radiation_source_settings` and :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.radiation_pressure_target_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

   * These models provide various ways in which to define the radiation flux emitted by a body, and a response of a body to incident radation pressure. More details are provided on a :ref:`dedicated page <radiation_pressure_acceleration>`
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.radiation_pressure_source` and :attr:`~tudatpy.numerical_simulation.environment.Body.radiation_pressure_target`, which provides a :class:`~tudatpy.numerical_simulation.environment.RadiationSourceModel` and a :class:`~tudatpy.numerical_simulation.environment.RadiationPressureTargetModel`, respectively.


* `Rigid body properties <https://py.api.tudat.space/en/latest/rigid_body.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rigid_body_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.   

   * This property defines the mass, center of mass and inertia tensor of a body. If the body has a gravity field, corresponding rigid body properties are automatically created (but, defining rigid body properties does not define a gravity field!) Note: If defined manually, the inertia tensor must be provided in the body-fixed frame (the orientation of which is defined by the body's rotation model), and must *not* be normalized. 
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.rigid_body_properties`, which provides a :class:`~tudatpy.numerical_simulation.environment.RigidBodyProperties`

* `Ground stations <https://py.api.tudat.space/en/latest/ground_station.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.ground_station_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  Note: this attribute is a list, and any number of stations may be added.  

   * These models define ground stations (which includes planetary landers) on a celestial body. Each ground station may have any number of station motion models assigned to it. 
   * The dictionary of all ground stations is extracted from a :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.ground_station_list`, which has :class:`~tudatpy.numerical_simulation.environment.GroundStation` objects as dictionary values

* `Vehicle systems <https://py.api.tudat.space/en/latest/vehicle_systems.html>`_, currently limited to the vehicle exterior shape, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.vehicle_shape_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

   * These models define physical characteristics and hardware systems of the vehicle. This functionality is currently in a preliminary state, and its use in the body settings is limited to the vehicle's exterior shape.
   * The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.system_models`, which provides a :class:`~tudatpy.numerical_simulation.environment.VehicleSystems`

  
.. _specific_environment_considerations:


Points of attention
===================

On this page, we give an overview of some specific aspects of the environment models that may be useful for a user to
know, in order to properly select and understand their choice of environment models.
This page is meant to supplement the API documentation, and is *not* a comprehensive overview of all environment models.


Aerodynamic coefficients
------------------------

See the section on :ref:`aerodynamic coefficients during the propagation <aerodynamics_during_propagation>`
concerning a number of points of attention regarding the aerodynamic coefficients, such as the frame in which
they are defined, definition of their independent variables, control surfaces, etc.


Ephemeris models
----------------

**Spice-based models** For many typical applications, natural body ephemerides will be calculated from :ref:`Spice kernels <spice_in_tudat>`.
In some cases, a user may find that the default Spice kernels are insufficient for their purposes, due to one of two reasons:

* The body for which the state is required *is* in the ephemeris Spice kernel, but the time at which the state is needed lies outside of the bounds for which the Spice kernel has data
* The body for which the state is required *is not* in the ephemeris Spice kernel

In both cases, a user should load additional Spice kernels. This can be done using the :func:`~tudatpy.interface.spice.load_kernel`. Spice kernels for many bodies may be found in a number of places.
The 'goto' place for Spice kernels for ephemerides is the NAIF website (developers of Spice), which you can find
`here <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/>`_.

**Use of scaled models** For a sensitivity analysis (among others) it may be useful to modify the ephemeris of a body, for instance
to emulate the influence of a 1 km offset in the state provided by the nominal ephemeris. Unlike most other environment models,
this cannot be achieved (at least not for most types of ephemerides) by modifying a single defining parameter of the model.
Instead, we provide the functions
:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector` and
:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.scaled_by_vector_function`,
which take nominal ephemeris settings, and add a user-defined variation (constant or time-varying; absolute or relative) to the
inertial Cartesian state elements produced by the ephemeris.

**Using the ephemeris outside the propagation** In various cases, the ephemeris object is useful to use independently of the propagation. Details can be found in the API entry for :class:`~tudatpy.numerical_simulation.environment.Ephemeris`, but we provide a short example here as well.

    .. code-block:: python

        bodies = .... // Create system of bodies
        earth_ephemeris = bodies.get('Earth').ephemeris
        earth_state_at_epoch = earth_ephemeris.cartesian_state( epoch )

where the ``epoch`` input is (as always in Tudat) the time in seconds since J2000. The ``earth_state_at_epoch`` is always in a frame with inertial orientation. The specific orientation and origin can be access from the :attr:`~tudatpy.numerical_simulation.environment.Ephemeris.frame_orientation` and :attr:`~tudatpy.numerical_simulation.environment.Ephemeris.frame_origin` attributes.

Gravity fields
--------------

Unlike most other environment model options in Tudat, there are multiple options for creating either a spherical harmonic gravity field, and a point mass gravity field:

* Point mass: defining the gravitational parameter manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central`) or requiring the gravitational parameter to be extracted from Spice (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.central_spice`).
* Spherical harmonics: defining all the settings manually (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic`), loading a pre-defined model for a soalr system body (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.from_file_spherical_harmonic`) or calculating the spherical harmonic coefficients (up to a given degree) based on an ellipsoidal homogeneous mass distribution (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.spherical_harmonic_triaxial_body`)

.. _rotation_model_specifics:

Rotation models
---------------

Tudat has a broad range of rotation models available. In principle, these models can be assigned to both celestial bodies and natural bodies. 
However, a subset of these models is typically only applied to natural *or* artificial bodies. Rotation models have a wide range of,
sometimes indirect, influences on the dynamics

* A spherical harmonic acceleration exerted by a central body is first evaluated in a body-fixed frame, and the transformed to an inertial frame. Consequently, the central body's rotation has a fundamental influence on the exerted spherical harmonic acceleration
* A :ref:`thrust acceleration <thrust_models>` in Tudat is calculated from two models: (1) an engine model, which defined the body-fixed direction of the thrust, and the magnitude of the thrust (2) the orientation of the body in space, defined by its rotation model
* For a non-spherical central body shape models, the current orientation of this central body has an indirect influence on the altitude at which a vehicle with a given *inertial* state is located

**Rotation and thrust** Two rotation models, which are typically used for vehicles under :ref:`thrust <thrust_models>`, and/or vehicles undergoing :ref:`aerodynamic forces <aerodynamic_models>`, are the following:

* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`, which calculates the body's rotation based on the angle of attack, sideslip angle and bank angle. Note that these angles are definend w.r.t. the relative wind. This model is typical when using, for instance, a re-entry simulation. It imposes these three angles, and calculates the body orientation by combination with the latitude, longitude, heading angle, flight path angles. There is a related model, :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based`, that uses the same setup, but does not impose the angle of attack, but caculates by imposing aerodynamic pitch trim (zero pitch moment).
* The rotation model :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based`, which is typical when calculating dynamics of a vehicle under thrust. It is based on linking a body-fixed  direction (now limited to the body-fixed x-axis) to an arbitrary inertial direction. This allows the thrust (assuming that this is aligned with this same body-fixed direction) to be guided in an inertial direction determined by a user-defined model. 

**Relation to gravity field** When modifying the rotation model settings, the name of the body-fixed frame may also be changed (as is the case for, for instance, the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs`, where the body-fixed frame has the name "ITRS").
One consequence of this is that you may get an error from the spherical harmonic gravity field, which can no longer find the frame to which it is associated. This can be resolved by (for instance) associating the gravity field to the new frame. For the above example, this would be done by the following:

.. code-block:: python
                
    body_settings.get( "Earth" ).gravity_field_settings.associated_reference_frame = "ITRS"
    
**High-accuracy Earth rotation model** The :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.gcrs_to_itrs` creates a high accuracy rotation model, following the IERS 2010 Conventions. This includes small variations that are not predicted by models, but are instead measured by geodetic techniques and published as tabulated data by the IERS. If so desired, the exact files used for these corrections may be adapted by the user (see :func:`~tudatpy.astro.earth_orientation.EarthOrientationAnglesCalculator`), which includes specific settings for daily variations in earth rotation angle, which influences the UTC - UT1 time conversion. 

**Using the rotation model outside the propagation** In various cases, the rotation model object is useful to use independently of the propagation. Details can be found in the API entry for :class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris`, but we provide a short example here as well.

    .. code-block:: python

        bodies = .... // Create system of bodies
        earth_rotation_model = bodies.get('Earth').rotation_model
        earth_rotation_at_epoch = earth_rotation_model.body_fixed_to_inertial_rotation( epoch )

where the ``epoch`` input is (as always in Tudat) the time in seconds since J2000. The specific rotation model provides the orientation from the :attr:`~tudatpy.numerical_simulation.environment.RotationalEphemeris.inertial_frame_name` to the :attr:`~tudatpy.numerical_simulation.environment.RotationalEphemeris.body_fixed_frame_name` frames. In the above example, the rotation matrix from the body-fixed to the inertial frame is extracted. Other functions are available in the :class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris` to extract the inverse rotation, its time-derivative, and the angular velocity vector of the body-fixed frame. Finally, note that the :func:`~tudatpy.numerical_simulation.environment.transform_to_inertial_orientation`, which uses the rotation model to rotation a body-fixed to an inertial state, may be useful in this context for some applications.

.. _rigid_body_gravity_field:
    
Rigid body properties and gravity fields
-----------------------------------------

Rigid body properties will always be created automatically when a body is endowed with a gravity field, as described below:

* Point-mass gravity field: mass computed from gravitational parameter; zero inertia tensor, and center of mass at origin of body-fixed frame
* Spherical harmonic gravity field: mass computed from gravitational parameter, center of mass computed from degree 1 gravity field coefficients, inertia tensor as described below
* Polyhedron gravity field: mass computed from gravitational parameter, center of mass and inertia tensor computed from homogeneous mas distribution inside body

For the spherical harmonic gravity field, the normalized mean moment of inertia must be set by the user, to allow an inertia tensor to be computed. This is done using the :attr:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings.scaled_mean_moment_of_inertia` attribute of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.SphericalHarmonicsGravityFieldSettings` class, as in the example below

        .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/adding_inertia_tensor.py
             :language: python
             
This code snippet will automatically create a rigid body properties for Mars, with the inertia tensor computed from this value of 0.365 and the degree 2 gravity field coefficients. Note that, if gravity field variations are used for the body, time-variability of the degree 1- and 2- coefficients will be reflected in time-variability of the body's center of mass and inertia tensor. 


    
Wind models
-----------

Wind models may be added to an atmosphere model by using the :attr:`~tudatpy.numerical_simulation.environment_setup.atmosphere.AtmosphereSettings.wind_settings` attribute of the atmosphere settings, as in the following example:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/adding_wind.py
             :language: python

Here, a wind vector in the positive z-direction of the :ref:`vertical frame<aero_frames>` (downward) of 10 m/s is added, using the :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.constant_wind_model`.
            
By default, an atmosphere has 'zero wind', which means that the atmosphere corotates with the body. A user may add a wind model to this atmosphere model, which will modify the freestream velocity that a vehicle in the atmosphere experiences


.. _ground_stations:

Ground stations
---------------

Although ground stations are considered part of the environment in Tudat (as properties of a ``Body`` object), they do not influence the numerical propagation (unless a custom model imposing this is implemented by the user). Ground stations can be defined through the ``BodySettings`` as any other model. But, as the rest of the environment does not depend on them, they can safely be added to a body after it is created. The process is similar to the one described for :ref: `decorate_empty_body`. Specifically, ground station settings are created, and these are then used to create a ground station and add it to the body. The specifics of creating ground station settings is described `in the API documentation <https://py.api.tudat.space/en/latest/ground_stations.html>`_. An example is given below:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/add_ground_station.py
             :language: python
             
where a simple ground station is created (with only a name and a position), with its position defined in geodetic elements. The position of a ground station in a body-fixed frame can have two sources of time-variability:

* From `shape deformation models <https://py.api.tudat.space/en/latest/shape_deformation.html>`_ of the body on which it is located
* From a list of :class:`~tudatpy.numerical_simulation.environment_setup.ground_station.GroundStationMotionSettings` objects, which can be assigned to the ground station settings (see e.g. :func:`~tudatpy.numerical_simulation.environment_setup.ground_station.basic_station`). These models define time-variability of individual ground stations, in addition to the global shape deformation.

To automatically create a list of settings for all DSN stations (which are then typically assigned to the ``ground_station_settings`` of Earth), the :func:`~tudatpy.numerical_simulation.environment_setup.ground_station.dsn_station_settings` can be used.

Radiation pressure models
-------------------------

Details on the radiation pressure source and target models in Tudat are discussed on a :ref:`dedicated page <radiation_pressure_acceleration>`

.. _vehicle_shape_models:

Vehicle shape models
---------------------

For various high-accuracy models of non-conservative spacecraft dynamics, a so-called macromodel is required which defines
the external shape of the vehicle. This maromodel is typically define by a set of panels, with each panel assigned
specific properties of how it interacts with the environment. At present, the spacecraft macromodel in Tudat is only
used for the calculation of a panelled radiation pressure acceleration, but future updated will also use it for the
calculation of aerodynamic coefficients in both rarefied and hypersonic flow.

The current panels in Tudat allow a list of panels to be defined, with the geometrical properties of panel :math:`i` defined by the
surface normal vector :math:`\hat{\mathbf{n}}_{i}` and the surface area :math:`A_{i}`. Note that, since the panel shape or
location is not yet defined, computing torques due to surface forces, or incorporating shadowing into the panel
force calculatuion, is not yet supported.

The panel surface normal may be defined in either the body-fixed frame :math:`\mathcal{B}` of the vehicle, or to a 'vehicle-part-fixed frame'
:math:`\mathcal{F}_{j}`. A 'vehicle part' is defined as a part of the vehicle that can move/rotate w.r.t. the body-fixed frame of the
spacecraft. Typical examples are the solar arrays and an movable antenna.

The panel surface normal (in either the body frame or the part frame), may be defined by the
:func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.frame_fixed_panel_geometry`,
:func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.time_varying_panel_geometry` or
:func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.body_tracking_panel_geometry` functions,
where the latter is used to ensure that a panel normal automatically points to/away from another bodY (e.g. the Sun for solar panels).

A full panel is created by defining its geometry, and models for its interaction with the environment (currently limited to
a reflection law to compute the influence of radiation pressure) using the
:func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.body_panel_settings` function.

The vehicle macromodel, and the rotation models from the body-fixed frame to the (optional) part-fixed frames are defined by
using the :func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.full_panelled_body_settings` function, and
assigned to the ``vehicle_shape_settings`` attribute of the :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` class.
When a full macromodel is not available to the user, a 'box-wing' model may also be used, which creates the macromodel
bassed on user settings, using the :func:`~tudatpy.numerical_simulation.environment_setup.vehicle_systems.box_wing_panelled_body_settings` function.

Polyhedron models
-----------------
A polyhedron can be used to define both gravity (:func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.polyhedron_from_gravitational_parameter`)
and shape (:func:`~tudatpy.numerical_simulation.shape.gravity_field.polyhedron`) models. Since both models tend to be computationally intensive (the gravity
model more so), it is recommended to use polyhedra with the lowest number of facets that allows meeting the desired accuracy. The number of facets of a polyhedron
model can be reduced using any mesh processing software, for example `PyMeshLab <https://pymeshlab.readthedocs.io/en/latest/>`_.
Additionally, different functions to process a polyhedron are available in `Polyhedron utilities <https://py.api.tudat.space/en/latest/polyhedron_utilities.html>`_.

