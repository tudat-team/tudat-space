
.. _environment_model_overview:

==================
Environment Models
==================

   
On this page, we provide an overview of the categories of environment models that are available, how to create them, how to access them, as well as some general notes on their usages, typical pitfalls, hints, etc. How to define the settings for an environment model is discussed :ref:`here <custom_body_settings>`. Summarizing, settings for an environment model are stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings` object, a list of which (one for each body) is stored in a :class:`~tudatpy.numerical_simulation.environment_setup.BodyListSettings` object. We reiterate that these objects themselves do not have any "functionality", except providing settings that define how to create the actual (potentially interconnected and interdependent environment models). After creating the environment, you can access any relevant functionality of the environment models (ephemerides, rotation models, etc.) outside the context of a propagation.

.. note::
    For details on how to access the environment *during a propagation* (for custom models, typically), see :ref:`this page <environment_during_propagation>`.

In Tudat, the full environment is stored in a :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object, which in turn stores environment models inside :class:`~tudatpy.numerical_simulation.environment.Body` objects (one for each natural or artificial body in your model). From each object representing a body, you can extract each separate environment model (see list below). For instance, to retrieve the :class:`~tudatpy.numerical_simulation.environment.Ephemeris` object from the body named ``Earth``, you can use the following:

.. code-block:: python

   bodies = ... # Create system of bodies
   earth_ephemeris = bodies.get('Earth').ephemeris

Below, we provide an overview of the different types of environment models for which you can define settings, along with links to submodules of ``environment_setup`` in the :doc:`API documentation <environment_setup>`, where a comprehensive list of all environment model settings can be found. In addition, we list how to extract the resulting environment model from the ``Body`` objects.

Aerodynamic coefficients
========================

The :doc:`Aerodynamic coefficients <aerodynamic_coefficients>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings`  to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.aerodynamic_coefficient_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define aerodynamics force (and if required, moment) coefficients of a body. See the section on :ref:`aerodynamic coefficients during the propagation <aerodynamics_during_propagation>` concerning a number of points of attention regarding the aerodynamic coefficients, such as the frame in which they are defined, definition of their independent variables, control surfaces, etc.
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.aerodynamic_coefficient_interface`, which provides a :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientInterface`
* The following code block gives an overview of the steps to define, create, and extract an aerodynamic coefficient model, for the specific example of constant
  drag (:math:`C_{D}=1.5`, :math:`S_{ref}=2` m\ :sup:`2`)

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Add empty settings for Vehicle, since no default is defined
      body_settings.add_empty_settings( 'Vehicle' )

      # Add aerodynamic model settings (base class type AerodynamicCoefficientSettings)
      body_settings( 'Vehicle' ).aerodynamic_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
          reference_area = 2.0,
          constant_force_coefficient = [1.5, 0.0, 0.0])

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract aerodynamic coefficient model (base class type AerodynamicCoefficientInterface) from Vehicle
      vehicle_aerodynamic_coefficient_model = bodies.get( 'Vehicle' ).aerodynamic_coefficient_interface


Atmosphere models
=================

The :doc:`Atmosphere models <atmosphere>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.atmosphere.AtmosphereSettings` to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.atmosphere_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define atmospheric properties of a body. For state propagation, the density will typically be the most important one. However, many of the models here include outputs of temperature, density, etc. as well. Depending on the model, the atmospheric properties may be only altitude-dependent, or fully time- and position-dependent. Note that the atmosphere settings can include wind settings (default: none)
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.atmosphere_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.AtmosphereModel`
* The following code block gives an overview of the steps to define, create, and extract an atmosphere model, for the specific example of exponential atmosphere
  drag (:math:`\rho_{0}=1.225` kg/m\ :sup:`3`, :math:`H=7200` m)

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify atmosphere model settings (base class type AtmosphereSettings)
      body_settings( 'Earth' ).atmosphere_settings = environment_setup.atmosphere.exponential(
          scale_height = 7200.0,
          surface_density = 1.225 )

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract atmosphere model (base class type AtmosphereModel) from Earth
      earth_atmosphere_model = bodies.get( 'Earth' ).atmosphere_model


Ephemeris models
================

The :doc:`Ephemeris models <ephemeris>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.ephemeris.EphemerisSettings` to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.ephemeris_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.
  
* These models provide various ways in which to define predetermined (e.g. not coming from a Tudat propagation) translational states of bodies in the solar system
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.ephemeris`, which provides a :class:`~tudatpy.numerical_simulation.environment.Ephemeris`
* The following code block gives an overview of the steps to define, create, and extract an ephemeris model, for the specific example of ephemeris of the Earth  from Spice, with the Sun as ephemeris origin (and J2000 frame orientation).

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify ephemeris model settings (base class type EphemerisSettings)
      body_settings( 'Earth' ).ephemeris_settings = environment_setup.ephemeris.direct_spice(
          frame_origin = 'Sun',
          frame_orientation = 'J2000' )

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract ephemeris model (base class type Ephemeris) from Earth
      earth_ephemeris_model = bodies.get( 'Earth' ).ephemeris


Gravity field models
====================

The :doc:`Gravity field models <gravity_field>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings` to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define the gravitational field of solar system bodies. Note: the mass associated with these gravitational field is the gravitational mass, which does *not* need to be equal to its inertial mass.
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.gravity_field_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.GravityFieldModel` (note that gravity field variations are stored inside this object)
* The following code block gives an overview of the steps to define, create, and extract a gravity field model, for the specific example of a point-mass model with :math:`\mu=3.986004418\cdot 10^{14}` m\ :sup:`3`/s\ :sup:`2`.

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify gravity field model settings (base class type GravityFieldSettings)
      body_settings( 'Earth' ).gravity_field_settings = environment_setup.gravity_field.central(
          gravitational_parameter = 3.986004418E14 )

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract gravity field model (base class type GravityFieldModel) from Earth
      earth_gravity_field_model = bodies.get( 'Earth' ).gravity_field_model


Gravity field variation models
==============================

The :doc:`Gravity field variation models <gravity_field_variation>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field_variation.GravityFieldVariationSettings` to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.gravity_field_variation_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. Note: this attribute is a list, and any number of variation models may be added.

* These models provide various ways in which to define the time-variability of a body's (spherical harmonic) gravity field.
* Unlike most environment models, the gravity field variations are stored inside the gravity field model, rather than directly in the body object
  The gravity field variations can be extracted from the :class:`~tudatpy.numerical_simulation.environment.TimeDependentSphericalHarmonicsGravityField` object (a derived class of :class:`~tudatpy.numerical_simulation.environment.GravityFieldModel`) using :attr:`~tudatpy.numerical_simulation.environment.TimeDependentSphericalHarmonicsGravityField.gravity_field_variation_models`, which provides a list of :class:`~tudatpy.numerical_simulation.environment.GravityFieldVariationModel` objects
* The following code block gives an overview of the steps to define, create, and extract a gravity field variation model, for the specific example of a
  constant :math:`k_{2}=0.301` Love number, and both the Sun and Moon as tide-raising bodies.

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify gravity field variation settings (base class type GravityFieldVariationSettings)
      # NOTE, this requires the body_settings( 'Earth' ).gravity_field_settings to define a spherical harmonic gravity field
      body_settings( 'Earth' ).gravity_field_variation_settings = [
          environment_setup.gravity_field_variation.solid_body_tide(
             tide_raising_body = 'Sun',
             love_number = 0.301,
             degree = 2 ),
          environment_setup.gravity_field_variation.solid_body_tide(
             tide_raising_body = 'Moon',
             love_number = 0.301,
             degree = 2 ) ]

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract list of gravity field variation model (base class type GravityFieldVariationModel) from Vehicle
      earth_gravity_field_variation_models = bodies.get( 'Earth' ).gravity_field_model.gravity_field_variation_models


Rotation models
===============

The :doc:`Rotation models <rotation_model>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.rotation_model.RotationModelSettings`  to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rotation_model_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define the orientation of a body w.r.t. inertial space, and produces a quaternion/rotation matrix, and angular velocity vector/rotation matrix derivative. Note that Tudat can also produce such models by numerical propagation of the Euler equations (see :ref:`rotational_dynamics`).
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.rotation_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.RotationalEphemeris`
* The following code block gives an overview of the steps to define, create, and extract a rotation model, for the specific example of a simple rotation model
  (constant rotation rate and pole orientation), extracted from the Earth's pole and rotation rate according to the SPICE ``IAU_Earth`` frame at the given reference epoch. The resulting rotation model has ``J2000`` as inertial frame, and the identifier ``IAU_Earth_simplified`` as Earth-fixed frame.

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup
      from tudatpy.astro import time_conversion

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify rotation model settings (base class type RotationModelSettings)
      body_settings( 'Earth' ).rotation_model_settings = environment_setup.rotation_model.simple_from_spice(
          base_frame = 'J2000',
          target_frame = 'IAU_Earth',
          target_frame_spice = 'IAU_Earth_simplified',
          initial_time = time_conversion.date_time_from_iso_string( '2020-09-08T14:00:00.0' ).epoch( ) )

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract rotation model (base class type RotationalEphemeris) from Earth
      earth_rotation_model = bodies.get( 'Earth' ).rotation_model


Shape models
============

The :doc:`Shape models <shape>` module contains functions to create settings objects of type :class:`~tudatpy.numerical_simulation.environment_setup.shape.BodyShapeSettings`  to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.shape_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define the exterior of a *natural* body and is typically used to calculate (for instance) altitude, ground station position, etc. Note: the exterior shape of an artificial body, from which aerodynamic and radiation pressure properties can be evaluated, uses a different interface, which is currently under development
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.shape_model`, which provides a :class:`~tudatpy.numerical_simulation.environment.ShapeModel`
* The following code block gives an overview of the steps to define, create, and extract a shape model, for the specific example of an oblate spheroid shape model
  with :math:`R_{e}=3396.2` km equatorial radius, and flattening :math:`f=0.00589`

  .. code-block:: python

      from tudatpy.numerical_simulation import environment_setup
      from tudatpy.astro import time_conversion

      # Create body settings
      body_settings =  environment_setup.get_default_body_settings( ... ) # Typical way to instantiate body settings

      # Modify shape model settings (base class type BodyShapeSettings)
      body_settings( 'Mars' ).shape_settings = environment_setup.shape.oblate_spherical(
          equatorial_radius = 3396.2E3,
          flattening = 0.00589 )

      # Create bodies
      bodies = environment_setup.create_system_of_bodies(body_settings)

      # Extract shape model (base class type ShapeModel) from Earth
      mars_shape_model = bodies.get( 'Mars' ).shape_model


Shape deformation models
========================

The :doc:`Shape deformation models <shape_deformation>` are to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.shape_deformation_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`. Note: this attribute is a list, and any number of deformation models may be added.  

* These models provide various ways in which to define time variability of the shape of a body. These are typically relevant for detailed position models of ground stations (note that the models assigned here are global; station-specific models can be assigned to individual stations)
 

Radiation pressure models
=========================

The :doc:`Radiation pressure source and target models <radiation_pressure>` are to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.radiation_source_settings` and :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.radiation_pressure_target_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models provide various ways in which to define the radiation flux emitted by a body, and a response of a body to incident radiation pressure. More details are provided on a :ref:`dedicated page <radiation_pressure_acceleration>`
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.radiation_pressure_source` and :attr:`~tudatpy.numerical_simulation.environment.Body.radiation_pressure_target`, which provides a :class:`~tudatpy.numerical_simulation.environment.RadiationSourceModel` and a :class:`~tudatpy.numerical_simulation.environment.RadiationPressureTargetModel`, respectively.


Rigid body properties
======================

The :doc:`Rigid body properties <rigid_body>` are to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.rigid_body_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.   

* This property defines the mass, center of mass and inertia tensor of a body. If the body has a gravity field, corresponding rigid body properties are automatically created (but, defining rigid body properties does not define a gravity field!) Note: If defined manually, the inertia tensor must be provided in the body-fixed frame (the orientation of which is defined by the body's rotation model), and must *not* be normalized. 
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.rigid_body_properties`, which provides a :class:`~tudatpy.numerical_simulation.environment.RigidBodyProperties`

.. _ground_station_models:

Ground station models
=====================

The :doc:`Ground stations <ground_station>` settings are to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.ground_station_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.  Note: this attribute is a list, and any number of stations may be added.  

* These models define ground stations (which includes planetary landers) on a celestial body. Each ground station may have any number of station motion models assigned to it. 
* The dictionary of all ground stations is extracted from a :class:`~tudatpy.numerical_simulation.environment.Body` object using :attr:`~tudatpy.numerical_simulation.environment.Body.ground_station_list`, which has :class:`~tudatpy.numerical_simulation.environment.GroundStation` objects as dictionary values

Vehicle systems
===============

The :doc:`Vehicle systems <vehicle_systems>` are currently limited to the vehicle exterior shape, to be assigned to the :attr:`~tudatpy.numerical_simulation.environment_setup.BodySettings.vehicle_shape_settings` attribute of :class:`~tudatpy.numerical_simulation.environment_setup.BodySettings`.

* These models define physical characteristics and hardware systems of the vehicle. This functionality is currently in a preliminary state, and its use in the body settings is limited to the vehicle's exterior shape.
* The resulting model can be extracted from the :class:`~tudatpy.numerical_simulation.environment.Body` object extracted using :attr:`~tudatpy.numerical_simulation.environment.Body.system_models`, which provides a :class:`~tudatpy.numerical_simulation.environment.VehicleSystems`
