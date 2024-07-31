
.. _environment_model_overview:

==================
Environment Models
==================

   
On this page, we provide an overview of the categories of environment models that are available, how to create them, how to access them, as well as some general notes on their usages, typical pitfalls, hints, etc. How to define the settings for an environment model is discussed :ref:`here <custom_body_settings>`. Summarizing, settings for an environment model are stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object, a list of which (one for each body) is stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings` object. We reiterate that these objects themselves do not have any "functionality", except providing settings that define how to create the actual (potentially interconnected and interdependent environment models). After creating the environment, you can access any relevant functionality of the environment models (ephemerides, rotation models, etc.) outside the context of a propagation.

.. note::
    For details on how to access the environment *during a propagation* (for custom models, typically), see :ref:`this page <environment_during_propagation>`

In Tudat, the full environment is stored in a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object, which in turn stores environment models inside :class:`~tudatpy.numerical_simulation.environment.Body` objects (one for each natural or artificial body in your model). From each object representing a body, you can extract each separate environment model (see list below). For instance, to retrieve the :class:`~tudatpy.numerical_simulation.environment.Ephemeris` object from the body named ``Earth``, you can use the following:

    .. code-block:: python

        bodies = .... // Create system of bodies
        earth_ephemeris = bodies.get('Earth').ephemeris

Below, we provide an overview of the different types of environment models for which you can define settings, along with links to submodules of ``environment_setup`` in the `API documentation <https://py.api.tudat.space/en/latest/environment_setup.html>`_, where a comprehensive list of all environment model settings can be found. In addition, we list how to extract the resulting environment model from the ``Body`` objects

.. _available_environment_models:

Available Model Types
=====================

The complete list of available environment model settings can be found on our API documentation. Below is a list with the different categories of models, and a link to the corresponding Tudatpy module

* `Aerodynamic coefficients <https://py.api.tudat.space/en/latest/aerodynamic_coefficients.html>`_, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.aerodynamic_coefficient_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. 

   * These models provide various ways in which to define aerodynamics force (and if required, moment) coefficients of a body. See the section on :ref:`aerodynamic coefficients during the propagation <aerodynamics_during_propagation>` concerning a number of points of attention regarding the aerodynamic coefficients, such as the frame in which they are defined, definition of their independent variables, control surfaces, etc.
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

   * These models provide various ways in which to define the radiation flux emitted by a body, and a response of a body to incident radiation pressure. More details are provided on a :ref:`dedicated page <radiation_pressure_acceleration>`
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
