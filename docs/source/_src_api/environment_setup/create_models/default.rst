=====================
Create default models
=====================

Ephemeris
#########

Gravity field
#############

Point Mass Gravity
------------------
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


Point Mass Gravity from Spice
-----------------------------

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



Spherical Harmonics Gravity
---------------------------

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

The associatedReferenceFrame reference frame must presently be the same frame as the target frame of the body’s rotation model (see below). It represents the frame to which the spherical harmonic field is fixed.

.. warning::
    Spherical harmonic coefficients used for this environment model must ALWAYS be fully normalized.


Gravity field time-variations
#############################

Atmosphere
##########

Exponential Atmosphere
----------------------

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

Shape
#####

Rotation
########

Aerodynamic coefficient
#######################

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

