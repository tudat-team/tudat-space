
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

       .. tab:: C++
       

Spherical Harmonic Gravity
--------------------------

Settings for a spherical harmonic gravity acceleration. For example of acceleration exerted on “Apollo” by “Earth”:

.. tabs::

     .. tab:: Python

      .. toggle-header:: 
         :header: Required **Show/Hide**

         .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/req_acceleration_models.py
            :language: python

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/spherical_harmonic_gravity.py
         :language: python

     .. tab:: C++

where the gravity field will be expanded up to degree and order 12 in the acceleration model.

.. note::
    The spherical harmonic acceleration up to degree N and order M includes the point-mass gravity acceleration (which is the degree and order 0 term).


Aerodynamic Acceleration
------------------------

Settings for an aerodynamic acceleration. For example of acceleration exerted on "Apollo" by "Earth" (e.g. atmosphere model belonging to Earth):

.. tabs::

     .. tab:: Python

      .. toggle-header:: 
         :header: Required **Show/Hide**

         .. literalinclude::
            :language: python

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/aerodynamic.py
         :language: python

     .. tab:: C++

Requires the following environment models to be defined:

- Atmosphere model for body exerting acceleration.
- Aerodynamic coefficient interface for body undergoing acceleration (set by AerodynamicCoefficientSettings). NOTE: In the case that the aerodynamic coefficients are defined as a function of the vehicle orientation (e.g. angle of attack and sideslip angle), these angles can be manually or automatically defined.
- Mass model for body undergoing acceleration.
- Current state of body undergoing acceleration and body with atmosphere.


.. warning::
    Defining settings for a vehicle’s orientation, which may influence your aerodynamic force, is done after creating the acceleration models, as discused here.

Cannonball Radiation Pressure
-----------------------------

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

Tidal effect on natural satellites
----------------------------------


