=====================
Create default models
=====================

Ephemeris Model
###############

.. class:: Approximate Planet Positions Settings

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
             :language: python

  where the first constructor argument is taken from the enum in approximatePlanetPositionsBase.h, and the second argument (false) denotes that the circular coplanar approximation is not made.

.. class:: Direct Spice Ephemeris Settings

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
             :language: python

  creating a barycentric (SSB) ephemeris with axes along J2000, with data directly from spice.


.. class:: Interpolated Spice Ephemeris Settings

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
             :language: python

  creating a barycentric (SSB) ephemeris with axes along J2000, with data retrieved from Spice at 3600 s intervals between t=0 and t=1.0E8, using a 6th order Lagrange interpolator. Settings for the interpolator (discussed here, can be added as a sixth argument if you wish to use a different interpolation method)

.. class:: Tabulated Ephemeris Settings

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
             :language: python

  creating an ephemeris interpolated (with 6th order Lagrange interpolation) from the data in bodyStateHistory, which contains the Cartesian state (w.r.t. SSB; axes along J2000) for a given number of times (map keys, valid time range between first and last time in this map).


.. class:: Kepler Ephemeris Settings
  
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
             :language: python

  creating a Kepler orbit as ephemeris using the given kepler elements and associated initial time and gravitational parameter. See Frame/State Transformations for more details on orbital elements in Tudat.


.. class:: Constant Ephemeris Settings

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
             :language: python

.. class:: Multi-Arc Ephemeris Settings

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
             :language: python

.. class:: Custom Ephemeris Settings

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
             :language: python


Gravity Field Model
###################

.. class:: Point Mass Gravity Settings

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

.. class:: Point Mass Gravity from Spice Settings


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
             :language: python


.. class:: Spherical Harmonics Gravity Settings


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
             :language: python

  The associatedReferenceFrame reference frame must presently be the same frame as the target frame of the body’s rotation model (see below). It represents the frame to which the spherical harmonic field is fixed.

  .. warning::
      Spherical harmonic coefficients used for this environment model must ALWAYS be fully normalized.


Gravity field time-variations
#############################

Atmosphere Model
################

.. class:: Exponential Atmosphere Settings

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
               :language: python


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

.. class:: Tabulated Atmosphere Settings
  
  Due to the extensive customization available for the tabulated atmosphere, you can find the settings for this class in a separate page: :ref:`_tabulated-atmosphere-settings`.

.. class:: Custom Constant Temperature Atmosphere Settings

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
               :language: python


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
               :language: python  


.. class:: Custom Wind Model Settings

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
               :language: python  

  where :literal:`windFunction` is a function with inputs; altitude, longitude, latitude and time.

Shape
#####

Rotation
########

Aerodynamic coefficient
#######################

Constant Aerodynamic Coefficients Settings
------------------------------------------

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



Radiation pressure
##################

Cannonball Radiation Pressure Interface
---------------------------------------
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
.. note::
    Occultations by multiple bodies are not yet supported. Please contact the Tudat suppport team if you wish to use multiple occultations.

Mass
####

Vehicle system
##############

