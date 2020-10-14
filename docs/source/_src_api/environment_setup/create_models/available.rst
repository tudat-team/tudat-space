============================
Available Environment Models
============================

.. _environment_ephemeris_model:

Ephemeris Models
################

.. class:: Approximate Planet Positions

  Highly simplified model of ephemerides of major Solar system bodies (model described here). Both a three-dimensional, and circular coplanar approximation may be used.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/approximate_planet_positions_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/approximate_planet_positions_ephemeris.cpp
             :language: cpp

  where the first constructor argument is taken from the enum in approximatePlanetPositionsBase.h, and the second argument (false) denotes that the circular coplanar approximation is not made.

.. class:: Direct Spice Ephemeris

  Ephemeris retrieved directly using Spice.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/direct_spice_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/direct_spice_ephemeris.cpp
             :language: cpp

  creating a barycentric (SSB) ephemeris with axes along J2000, with data directly from spice.


.. class:: Interpolated Spice Ephemeris

  Using this option the state of the body is retrieved at regular intervals, and used to create an interpolator, before setting up environment. This has the advantage of only requiring calls to Spice outside of the propagation inner loop, reducing computation time. However, it has the downside of begin applicable only during a limited time interval.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/interpolated_spice_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/interpolated_spice_ephemeris.cpp
             :language: cpp

  creating a barycentric (SSB) ephemeris with axes along J2000, with data retrieved from Spice at 3600 s intervals between t=0 and t=1.0E8, using a 6th order Lagrange interpolator. Settings for the interpolator (discussed here, can be added as a sixth argument if you wish to use a different interpolation method)

.. class:: Tabulated Ephemeris

  Ephemeris created directly by interpolating user-specified states as a function of time.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/tabulated_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/tabulated_ephemeris.cpp
             :language: cpp

  creating an ephemeris interpolated (with 6th order Lagrange interpolation) from the data in bodyStateHistory, which contains the Cartesian state (w.r.t. SSB; axes along J2000) for a given number of times (map keys, valid time range between first and last time in this map).


.. class:: Kepler Ephemeris
  
  Ephemeris modelled as being a perfect Kepler orbit.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/kepler_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/kepler_ephemeris.cpp
             :language: cpp

  creating a Kepler orbit as ephemeris using the given kepler elements and associated initial time and gravitational parameter. See Frame/State Transformations for more details on orbital elements in Tudat.


.. class:: Constant Ephemeris

  Ephemeris modelled as being independent of time.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/constant_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/constant_ephemeris.cpp
             :language: cpp

.. class:: Multi-Arc Ephemeris

  An ephemeris model (for translational state) that allows the body’s state to be defined by distinct ephemeris models over different arcs. Class is implemented to support multi-arc propagation/estimation. 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/multi_arc_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/multi_arc_ephemeris.cpp
             :language: cpp

.. class:: Custom Ephemeris

  Allows user to provide arbitrary function as ephemeris model.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_ephemeris.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_ephemeris.cpp
             :language: cpp

.. _environment_gravity_field_model:

Gravity Field Models
####################

.. class:: Point Mass Gravity

    Point-mass gravity field model, with user-defined gravitational parameter.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/point_mass_gravity.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/point_mass_gravity.cpp
             :language: cpp

.. class:: Point Mass Gravity from Spice


  Point-mass gravity field model, with gravitational parameter from Spice.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/point_mass_gravity_spice.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/point_mass_gravity_spice.cpp
             :language: cpp

.. _environment_spherical_harmonics_gravity:

.. class:: Spherical Harmonics Gravity


  Gravity field model as a spherical harmonic expansion.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_harmonics_gravity.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_harmonics_gravity.cpp
             :language: cpp

  The associatedReferenceFrame reference frame must presently be the same frame as the target frame of the body’s rotation model (see below). It represents the frame to which the spherical harmonic field is fixed.

  .. warning::
      Spherical harmonic coefficients used for this environment model must ALWAYS be fully normalized.


Time-variations of the Gravity Field
####################################

.. class:: Basic Solid Body Gravity Field Variation

  Tidal variation of the gravity field using first-order tidal theory.

.. class:: Tabulated Gravity Field Variation

  Variations in spherical harmonic coefficients tabulated as a function of time.

.. _environment_atmosphere_model:

Atmosphere Models
#################

.. class:: Exponential Atmosphere

  Simple atmosphere model independent of time, latitude and longitude based on an exponentially decaying density profile with a constant temperature. 

  For example for an exponential atmosphere with a scale height of 7200 m, a constant temperature of 290 K, a density at 0 m altitude of 1.225 kg/m^3 and a specific gas constant of 287.06 J/(kg K):

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/exponential_atmosphere.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/exponential_atmosphere.cpp
               :language: cpp


  If you want to model the exponential atmosphere for Earth or Mars, you can also simply input ``aerodynamics::earth`` or ``aerodynamics::mars`` to load the default settings, which are defined in the table below.

  .. list-table:: Default settings for the exponential atmospheres of Earth and Mars.
     :widths: 25 25 25 25
     :header-rows: 1

     * - Property
       - Earth
       - Mars
       - Units
     * - Scale Height
       - 7.2
       - 1.11
       - km
     * - Density at Zero Altitude
       - 1.225
       - 0.02
       - kg/m^3
     * - Constant Temperature
       - 246.0
       - 215.0
       - K
     * - Specific Gas Constant
       - 287.0
       - 197.0
       - J/kg/K
     * - Ratio of Specific Heats
       - 1.4
       - 1.3
       - --

  References for the values above are:

  - **Earth**: Lecture notes, Rocket Motion by Prof. Ir. B.A.C. Ambrosius, November 2009
  - **Mars**: Spohn, T., Breuer, D., and Johnson, T., Eds., Encyclopedia of the Solar System, 3rd ed. Elsevier, 2014

.. class:: Tabulated Atmosphere
  
  Due to the extensive customization available for the tabulated atmosphere, you can find the settings for this class in a separate page: :ref:`tabulated-atmosphere-settings`.

.. class:: Custom Constant Temperature Atmosphere

  You can define your own constant temperature atmosphere, which computes the atmospheric properties based on an input function. For instance, one can link a function to the settings as such:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_constant_temperature_atmosphere.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_constant_temperature_atmosphere.cpp
               :language: cpp


  As shown in the example above, the user-defined function, is required to have those inputs, and in that specific order. The value of pressure is computed by assuming hydrostatic equilibrium, whereas temperature, gas constant and the ratio of specific heats are assumed to be constant.

.. tip::

  Note that in C++, by using :literal:`std::bind`, you can have more inputs than the ones in :literal:`customDensityFunction`. However, keep in mind that :literal:`std::bind` only allows up to 9 inputs.

.. class:: NRLMSISE-00

  This can be used to select the NRLMSISE-00 atmosphere model. To use this model, the :literal:`USE_NRLMSISE` flag in your top-level CMakeLists must be set to true.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/nrlmsise-00.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/nrlmsise-00.cpp
               :language: cpp


.. class:: Custom Wind Model

  Custom wind model which can be used to retrieve a wind vector. This wind vector is in the body-fixed, body-centered reference frame.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_wind_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/custom_wind_model.cpp
               :language: cpp

  where :literal:`windFunction` is a function with inputs; altitude, longitude, latitude and time.

Body Shape Models
#################

.. class:: Spherical Body Shape

  Model defining a body shape as a perfect sphere, with the sphere radius provided by the user.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_body_shape_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_body_shape_model.cpp
               :language: cpp

.. class:: Spherical Body Shape from Spice

  Model defining a body shape as a perfect sphere, with the sphere radius retrieved from Spice. 

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_body_shape_model_spice.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spherical_body_shape_model_spice.cpp
               :language: cpp 

.. class:: Oblate Spherical Body Shape
  
  Model defining a body shape as a flattened sphere, with the equatorial radius and flattening provided by the user.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/oblate_spherical_body_shape_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/oblate_spherical_body_shape_model.cpp
               :language: cpp 

.. _environment_rotational_model:

Rotational Models
#################

.. class:: Simple Rotation Model

  Rotation model with constant orientation of the rotation axis, and constant rotation rate about local z-axis.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/simple_rotation_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/simple_rotation_model.cpp
               :language: cpp

where the rotation from the original frame to the target frame at initial time is given by the initial orientation quaternion. This is mapped to other times using the rotation rate.


.. class:: Spice Rotation Model

  Rotation model directly obtained from Spice.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spice_rotation_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/spice_rotation_model.cpp
               :language: cpp


.. class:: Gcrs to Itrs Rotation Model

  High-accuracy rotation model of the Earth, according to the IERS 2010 Conventions. This class has various options to deviate from the default settings, here we only show the main options (typical applications will use default):

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/gcrs_to_itrs_rotation_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/gcrs_to_itrs_rotation_model.cpp
               :language: cpp

  Note that for this model the original frame must be J2000, ECLIPJ2000 or GCRS. The precession-nutation theory may be :literal:`iau_2000a`, :literal:`iau_2000b` or :literal:`iau_2006`, as implemented in the SOFA toolbox. Alternative options to modify (not shown above) include the EOP correction file, input time scale, short period UT1 and polar motion variations. Please see the Dosygen documentation for details.

.. class:: Tabulated Rotation Model

  Rotation model obtained from an interpolator, with dependent variable a Eigen::VectorXd of size 7: the four entries (w,x,y,z) of the quaternion from the target frame to the base frame, and body’s angular velocity vector, expressed in its body-fixed frame. The tabulated rotational ephemeris can be implemented as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/tabulated_rotation_model.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/tabulated_rotation_model.cpp
               :language: cpp

.. class:: Constant Rotation Model
  
  Rotation model with a constant value for the rotation. Currently the settings interface is not yet implemented.

.. _environment_aerodynamic_coefficient_interface:

Aerodynamic Coefficient Interfaces
##################################

.. class:: Constant Aerodynamic Coefficient

  Settings for constant (not a function of any independent variables) aerodynamic coefficients. For example for constant drag coefficient of 1.5 and lift coefficient of 0.3.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/constant_aerodynamic_coefficients.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/constant_aerodynamic_coefficients.cpp
               :language: cpp

.. class:: Tabulated Aerodynamic Coefficient

  Settings for tabulated aerodynamic coefficients as a function of given independent variables. These tables can be defined either manually or loaded from a file, as discussed in more detail on the :ref:`aerodynamic_coefficients` page. Coefficients can be defined as a function of angle of sideslip, angle of attack, Mach number or altitude. If you simulation requires any other dependencies for the coefficients, please open an issue on Github requesting feature.

.. class:: Local Inclination Methods
  
  Settings for aerodynamic coefficients computed internally using a shape model of the vehicle, valid for hypersonic Mach numbers. Currently, this type of aerodynamic coefficients can only be set manually in the :literal:`Body` object directly.

.. _environment_radiation_pressure_interface:

Radiation Pressure Interfaces
#############################

.. class:: Cannonball Radiation Pressure

  Properties for a cannonball radiation pressure model, i.e. effective force colinear with vector from source to target. For example creating cannonball radiation pressure settings for radiation due to the Sun, acting on the “Spacecraft” body, where the occultations due to the Earth are taken into account.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/cannonball_radiation_pressure.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/cannonball_radiation_pressure.cpp
               :language: cpp

  .. note::
      Occultations by multiple bodies are not yet supported. Please contact the Tudat suppport team if you wish to use multiple occultations.

.. class:: Panelled Radiation Pressure

  Properties for a panelled radiation pressure model, i.e. solar radiation pressure force derived from a so-called boxes-and-wings model.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/panelled_radiation_pressure.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/panelled_radiation_pressure.cpp
               :language: cpp

  Creating panelled radiation pressure settings for radiation due to the Sun, acting on the “Vehicle” body, from the following input variables:

  - Name of the source body of the radiation pressure.
  - Vector containing the emissivities of the different panels.
  - Vector containing the areas of the panels.
  - Vector containing the diffusion coefficient of each panel.
  - Vector containing the functions that return the normals of the panels surfaces, in body-fixed reference frame.
  - Vector with the names of the occulting bodies.


.. class:: Solar Sail Radiation Interface

  Properties for a solar sail radiation pressure model, i.e. solar radiation pressure force derived from a solar sail characteristics and orientation.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/solar_sail_radiation_pressure.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/req_environment_models_after.py
              :language: python

         .. tab:: C++

            .. literalinclude:: /_src_snippets/simulation/environment_setup/environment_models/solar_sail_radiation_pressure.cpp
               :language: cpp



  Creating solar sail radiation pressure settings for radiation due to the Sun, acting on the “Vehicle” body, where the occultations due to the Earth are taken into account. The input variables for the solar sail radiation pressure settings are:

  - Name of the radiation pressure source body.
  - Area of the solar sail.
  - Function returning the cone angle of the solar sail as a function of time (in the above example, the cone angle function is constant).
  - Function returning the clock angle of the solar sail as a function of time (in the above example, the clock angle function is constant).
  - Emissivity coefficient of the front face of the solar sail.
  - Emissivity coefficient of the back face of the solar sail.
  - Lambertian coefficient of the front face of the solar sail.
  - Lambertian coefficient of the back face of the solar sail.
  - Reflectvity coefficient of the solar sail.
  - Specular reflection coefficient of the solar sail.
  - Vector with the names of the occulting bodies.