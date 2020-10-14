
Available Acceleration Models
#############################

.. class:: Point Mass Gravity

    Settings for a point mass gravity acceleration. For example of acceleration exerted on “Apollo” by “Earth”:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

             .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
                :language: python

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.py
             :language: python

          .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/point_mass_gravity.cpp
             :language: cpp
         
    Requires the following environment models to be defined:

    - Gravity field for body exerting acceleration.
    - Current state of bodies undergoing and exerting acceleration, either from an Ephemeris model or from the numerical propagation.

.. class:: Spherical Harmonic Gravity

  Settings for a spherical harmonic gravity acceleration. For example of acceleration exerted on “Apollo” by “Earth”:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required before **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity.cpp
           :language: cpp

  where the gravity field will be expanded up to degree and order 12 in the acceleration model.

  .. note::
      The spherical harmonic acceleration up to degree N and order M includes the point-mass gravity acceleration (which is the degree and order 0 term).

.. class:: Third Body Gravity

  .. note::
      When creating an object of the AccelerationSettings type (or its derived class), you must not provide any of the third body acceleration types (third_body_central_gravity, third_body_spherical_harmonic_gravity, third_body_mutual_spherical_harmonic_gravity) as input. If you wish to use a third-body gravity acceleration (typically from a point mass), simply provide central_gravity as input. Depending on the settings for your central bodies, the code will automatically create the corresponding acceleration object (central or third-body).

.. class:: Aerodynamic Acceleration


  Settings for an aerodynamic acceleration. For example of acceleration exerted on "Apollo" by "Earth" (e.g. atmosphere model belonging to Earth):

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/aerodynamic.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/aerodynamic.cpp
           :language: cpp

  Requires the following environment models to be defined:

  - Atmosphere model for body exerting acceleration.
  - Aerodynamic coefficient interface for body undergoing acceleration.
  - Mass model for body undergoing acceleration.
  - Current state of body undergoing acceleration and body with atmosphere.


  .. warning::
      Defining settings for a vehicle’s orientation, which may influence your aerodynamic force, is done after creating the acceleration models, as discussed here.

.. class:: Cannonball Radiation Pressure

  Settings for a cannonball radiation pressure acceleration. For example of acceleration exerted on "Apollo" by "Sun":

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_cannonball_radiation_pressure.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/cannonball_radiation_pressure.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/cannonball_radiation_pressure.cpp
           :language: cpp


  Requires the following environment models to be defined:

  - Radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration).
  - Current state of body undergoing and body emitting radiation

.. class:: Relativistic Acceleration Correction

  A first-order (in 1/c^2) correction to the acceleration due to the influence of relativity. It implements the model of Chapter 10, Section 3 of the IERS 2010 Conventions. For example that includes all three contributions (Schwarzschild, Lense-Thirring and de Sitter):

  .. tabs::

     .. tab:: Python

      .. toggle-header:: 
         :header: Required **Show/Hide**

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/relativistic.py
         :language: python

      .. toggle-header:: 
         :header: Required after **Show/Hide**

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
            :language: python

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/relativistic.cpp
         :language: cpp

  Here, the ‘primary body’ for a planetary orbiter should always be set as the Sun (only relevant for de Sitter correction). The angular momentum vector of the orbited body is only relevant for Lense-Thirring correction.

.. class:: Empirical Accelerations


  A constant/once-per-orbit acceleration, expressed in the RSW frame, for which the magnitude is determined empirically (typically during an orbit determination process). The acceleration components are defined according to Montenbruck and Gill (2000), with a total of 9 components: a constant, sine and cosine term (with true anomaly as argument) for each of the three independent directions of the RSW frame. The settings object (for a vehicle called “Orbiter” around Mars) is created as:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/empirical.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/empirical.cpp
           :language: cpp

  Where the three input variables represent:

  - Vector containing the constant terms of the accelerations in the R, S and W directions.
  - Vector containing the sine terms of the accelerations in the R, S and W directions.
  - Vector containing the cosine terms of the accelerations in the R, S and W directions.


.. class:: Panelled Radiation Pressure
  
  Settings for a panelled radiation pressure acceleration. For example of acceleration exerted on “Apollo” by “Sun”:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_cannonball_radiation_pressure.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/panelled_radiation_pressure.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/panelled_radiation_pressure.cpp
           :language: cpp

  Requires the following environment models to be defined:

  - Panelled radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration).
  - Current state of body undergoing and body emitting radiation

.. class:: Solar sailing Acceleration

  Settings for a solar sail acceleration. For example of acceleration exerted on “Apollo” by “Sun”:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_cannonball_radiation_pressure.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/solar_sailing.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/solar_sailing.cpp
           :language: cpp

  Requires the following environment models to be defined:

  - Solar sailing radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration).
  - Current state of body undergoing and body emitting radiation


.. class:: Thrust Acceleration
  
  Used to define the resulting accerelations of a thrust force, requiring:

  - Mass of body undergoing acceleration.
  - Settings for both the direction and magnitude of the thrust force. These models may in turn have additional environmental dependencies.

  Setting up a thrust acceleration is discussed in more detail on the page Thrust Guidance.

.. class:: Quasi Impulsive Shot Acceleration

  Settings used to define the resulting acceleration of a quasi-impulsive shot, requiring:

  - Mass of the body undergoing acceleration.
  - Settings for the characteristics of the quasi-impulsive shots (total duration, rise time, associated deltaVs), as well as the times at which they are applied.


  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required **Show/Hide**

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/quasi_impulsive_shot.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/quasi_impulsive_shot.cpp
           :language: cpp

  where the input variables represent:

  - Midtimes of the quasi-impulsive shots (assumed to be the time at which an ideal impulsive shot would have been applied).
  - DeltaVs (three-dimensional vectors) associated with the quasi-impulsive shots.
  - Total duration of the quasi-impulsive shots (same value for each of them).
  - Rise time, i.e. time required to reach the peak acceleration (same value for each impulsive shot).

.. class:: Tidal effect on natural satellites

  The direct of tidal effects in a satellite system, applied directly as an acceleration (as opposed to a modification of spherical harmonic coefficients). The model is based on Lainey et al. (2007,2012). It can compute either the acceleration due to tides, and in particular tidal dissipation, on a planetary satellites. The accelertion can compute either the effect of tide raised on the satellite by the planet, or on the planet by the satellite. The satellite is assumed to be tidally locked to the planet.

  .. tabs::

     .. tab:: Python

      .. toggle-header:: 
         :header: Required **Show/Hide**

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/direct_tidal_dissipation.py
         :language: python

      .. toggle-header:: 
         :header: Required after **Show/Hide**

     .. tab:: C++

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/direct_tidal_dissipation.cpp
         :language: cpp

  Where the three input variables represent:

  - Value of the k2 Love number (real value) that is used.
  - Value of the tidal time lag (in seconds) that is used.
  - Boolean denoting whether the term independent of the time lag is to be computed (default true)
  - Boolean denoting whether the tide raised on the planet is to be modelled (if true), or the tide raised on the satellite (if false). Default is true.


.. class:: Mutual Spherical Harmonic Gravity Acceleration

  Settings for a mutual spherical harmonic gravity acceleration. This model is typically only used for detailed propagation of planetary systems. For example of acceleration exerted on “Io” by “Jupiter”:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required before **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/mutual_spherical_harmonic_gravity.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/mutual_spherical_harmonic_gravity.cpp
           :language: cpp

  where the gravity fields of Io and Jupiter will be expanded up to degree and order 12 and 4, respectively, in the acceleration model. Requires the following environment models to be defined:

  - Spherical harmonic gravity field for body exerting acceleration and body undergoing acceleration.
  - Rotation model from the inertial frame to the body-fixed frame and body undergoing acceleration.
  - Current state of bodies undergoing and exerting acceleration, either from an Ephemeris model or from the numerical propagation.

  For the case where a third-body mutual spherical harmonic acceleration (e.g. Ganymede on Io when propagating w.r.t. Jupiter), additional parameters have to be provided that denote the expansion degree/order of the central body, so:

  .. tabs::

       .. tab:: Python

        .. toggle-header:: 
           :header: Required before **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
              :language: python

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/mutual_third_body_spherical_harmonic_gravity.py
           :language: python

        .. toggle-header:: 
           :header: Required after **Show/Hide**

           .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models_after.py
              :language: python

       .. tab:: C++

        .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/mutual_third_body_spherical_harmonic_gravity.cpp
           :language: cpp

  where Jupiter now takes the role of central body, instead of body exerting the acceleration.




