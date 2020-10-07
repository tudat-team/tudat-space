
Available Acceleration Models
#############################

Point Mass Gravity
------------------


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
       
  Requires the following environment models to be defined:

  - Gravity field for body exerting acceleration.
  - Current state of bodies undergoing and exerting acceleration, either from an Ephemeris model or from the numerical propagation.

Spherical Harmonic Gravity
--------------------------

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

where the gravity field will be expanded up to degree and order 12 in the acceleration model.

.. note::
    The spherical harmonic acceleration up to degree N and order M includes the point-mass gravity acceleration (which is the degree and order 0 term).

Third Body Gravity
------------------
.. note::
    When creating an object of the AccelerationSettings type (or its derived class), you must not provide any of the third body acceleration types (third_body_central_gravity, third_body_spherical_harmonic_gravity, third_body_mutual_spherical_harmonic_gravity) as input. If you wish to use a third-body gravity acceleration (typically from a point mass), simply provide central_gravity as input. Depending on the settings for your central bodies, the code will automatically create the corresponding acceleration object (central or third-body).

Aerodynamic Acceleration
------------------------

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

Requires the following environment models to be defined:

- Atmosphere model for body exerting acceleration.
- Aerodynamic coefficient interface for body undergoing acceleration (set by AerodynamicCoefficientSettings).
- Mass model for body undergoing acceleration.
- Current state of body undergoing acceleration and body with atmosphere.


.. warning::
    Defining settings for a vehicle’s orientation, which may influence your aerodynamic force, is done after creating the acceleration models, as discussed here.

Cannonball Radiation Pressure
-----------------------------
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


Requires the following environment models to be defined:

- Radiation pressure model for body undergoing acceleration (from source equal to body exerting acceleration).
- Current state of body undergoing and body emitting radiation



Panelled Radiation Pressure
---------------------------

Solar sailing Acceleration
--------------------------

Thrust Acceleration
--------------------

Quasi Impulsive Shot Acceleration
---------------------------------

Relativistic Acceleration Correction
------------------------------------

IERS 2010 Conventions

Empirical Accelerations
-----------------------

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

Where the three input variables represent:

- Vector containing the constant terms of the accelerations in the R, S and W directions.
- Vector containing the sine terms of the accelerations in the R, S and W directions.
- Vector containing the cosine terms of the accelerations in the R, S and W directions.

Tidal effect on natural satellites
----------------------------------


