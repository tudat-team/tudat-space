.. _available_torque_models:

====================================
List of all Available Torque Models
====================================


Aerodynamic Torque
######################

Torque exerted by a body with an atmosphere model and shape model on another body.
The settings are created as follows, for an aerodynamic torque exerted by "Earth" on the propagated body "Vehicle":

.. tabs::

     .. tab:: Python

      .. toggle-header::
         :header: Required **Show/Hide**

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/aerodynamic_torque_example.py
         :language: python

     .. tab:: C++

      .. code-block:: cpp

            SelectedTorqueMap selectedTorqueModelMap;
            selectedTorqueModelMap[ "Vehicle" ][ "Earth" ].push_back( std::make_shared< TorqueSettings >( aerodynamic_torque ) );


Requires the following environment models to be defined:

* Atmospheric model for body exerting torque (see :ref:`environment_atmosphere_model`)

* Shape model for body exerting torque (see :ref:`environment_shape_model`).

* Aerodynamic coefficient interface for body undergoing torque (see :ref:`environment_aerodynamic_coefficient_interface`).

.. note::

    In the case that the aerodynamic coefficients are defined as a function of the vehicle orientation (e.g. angle of attack and sideslip angle), these angles can be manually or automatically defined.

* Current state of bodies undergoing and exerting torque, either from an Ephemeris model (see :ref:`environment_ephemeris_model`) or from the numerical propagation.


Second Degree Gravitational Torque
###################################

Torque exerted by a point mass on a body with a defined inertia tensor.
The settings are created as follows, for a torque exerted by body "Earth" on propagated body "Vehicle":

.. tabs::

     .. tab:: Python

      .. toggle-header::
         :header: Required **Show/Hide**

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/seconddegree_torque_example.py
         :language: python

     .. tab:: C++

      .. code-block:: cpp

            SelectedTorqueMap selectedTorqueModelMap;
            selectedTorqueModelMap[ "Vehicle" ][ "Earth" ].push_back( std::make_shared< TorqueSettings >( second_order_gravitational_torque ) );


Requires the following environment models to be defined:

* Gravity field (at least point-mass) for body exerting torque (see :ref:`environment_gravity_field_model`).

* Inertia tensor of body undergoing torque (see :ref:`environment_inertia_tensor`).

* Current state of bodies undergoing and exerting torque, either from an Ephemeris model (see :ref:`environment_ephemeris_model`) or from the numerical propagation.



.. tip::

    This implementation of the gravitational torque model uses the inertia tensor if the body undergoing the torque to infer its degree two spherical harmonics gravity field.
    It is therefore convenient for modelling the gravitational torque acting on a custom body, such as a vehicle, because its custom spherical harmonics model does not have to be created manually.



Spherical Harmonics Gravitational Torque
##########################################

Torque exerted by a point mass on a body with an arbitrary degree/order spherical harmonics mass distribution.
As an example, for a spherical harmonic torque, expanded to degree and order 8, exerted by body "Earth" on propagated body "Moon":

.. tabs::

     .. tab:: Python

      .. toggle-header::
         :header: Required **Show/Hide**

      .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/sphericalharmonics_torque_example.py
         :language: python

     .. tab:: C++

      .. code-block:: cpp

            SelectedTorqueMap selectedTorqueModelMap;
            int maximumDegree = 8;
            int maximumOrder = 8;
            selectedTorqueModelMap[ "Moon" ][ "Earth" ].push_back( std::make_shared< SphericalHarmonicTorqueSettings >( maximumDegree, maximumOrder ) );


Requires the following environment models to be defined:

* Gravity field (at least point-mass) for body exerting torque (see :ref:`environment_gravity_field_model`).

* Spherical harmonic gravity field for body undergoing torque (see :ref:`environment_gravity_field_model`).

* Current state of bodies undergoing and exerting torque, either from an Ephemeris model (see :ref:`environment_ephemeris_model`) or from the numerical propagation.



.. tip::

    In contrast to the second degree gravitational torque, the spherical harmonics gravity torque implementation requires the spherical harmonics gravity field model of the torque-undergoing body.
    It is therefore more suited for modelling the gravity torques acting on "standard" celestial bodies, for which spherical harmonics mass distributions are readily available.



Custom Torque
#################

This section is WIP and will be updated soon.
