.. _available_torque_models:

====================================
List of all Available Torque Models
====================================

%! add python code snippets, introduce final example snippets correctly in text
%! I have taken out the repeated requirements (they were in introductory text block as well as bullet pointed in the end - now only bullet-pointed).
%! References to objects (e.g. set by BodyShapeSettings) may only apply to C++, how do we handle this?


Aerodynamic Torque
######################

    Torque exerted by a body with an atmosphere model and shape model on another body.
    The settings are created as follows, for an aerodynamic torque exerted by "Earth" on body "Apollo":

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/acceleration_example.py
             :language: python

         .. tab:: C++

          .. code-block:: cpp

                SelectedTorqueMap selectedTorqueModelMap;
                selectedTorqueModelMap[ "Apollo" ][ "Earth" ].push_back( std::make_shared< TorqueSettings >( aerodynamic_torque ) );


    Requires the following environment models to be defined:

    * Atmosphere model for body exerting torque (set by AtmosphereSettings).

    * Shape model for body exerting torque (set by BodyShapeSettings).

    * Aerodynamic coefficient interface for body undergoing torque (set by AerodynamicCoefficientSettings). NOTE: In the case that the aerodynamic coefficients are defined as a function of the vehicle orientation (e.g. angle of attack and sideslip angle), these angles can be manually or automatically defined.

    * Current state of body undergoing torque and body with atmosphere.


Second Degree Gravitational Torque
###################################

    Torque exerted by a point mass on a body with a degree two spherical harmonics mass distribution.
    The settings are created as follows, for a torque exerted by AAA on body BBB:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/acceleration_example.py
             :language: python

         .. tab:: C++

          .. code-block:: cpp

                SelectedTorqueMap selectedTorqueModelMap;
                selectedTorqueModelMap[ "Apollo" ][ "Earth" ].push_back( std::make_shared< TorqueSettings >( second_order_gravitational_torque ) );



    Requires the following environment models to be defined:

    * Gravity field (at least point-mass) for body exerting torque (set by GravityFieldSettings).

    * Inertia tensor (%!) of body undergoing torque.

    * Current state of bodies undergoing and exerting torque, either from an Ephemeris model (set by EphemerisSettings) or from the numerical propagation.



Spherical Harmonics Gravitational Torque
##########################################

    Torque exerted by a point mass on a body with an arbitrary degree/order spherical harmonics mass distribution.

    As an example, for a spherical harmonic torque, expanded to degree and order 8, exerted by AAA on body BBB:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/acceleration_example.py
             :language: python

         .. tab:: C++

          .. code-block:: cpp

                SelectedTorqueMap selectedTorqueModelMap;
                int maximumDegree = 8;
                int maximumOrder = 8;
                selectedTorqueModelMap[ "Apollo" ][ "Earth" ].push_back( std::make_shared< SphericalHarmonicTorqueSettings >( maximumDegree, maximumOrder ) );


    Requires the following environment models to be defined:

    * Gravity field (at least point-mass) for body exerting torque (set by GravityFieldSettings).

    * Spherical harmonic gravity field for body undergoing torque (set by SphericalHarmonicsGravityFieldSettings)..

    * Current state of bodies undergoing and exerting torque, either from an Ephemeris model (set by EphemerisSettings) or from the numerical propagation.


Custom Torque
#################

    %! info.
