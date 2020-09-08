********************************
Getting Started with Simulations
********************************

Setting up basic simulations in the ``tudat`` API can be summarised into the
three fundamental procedural steps:

1. `Environment Setup`_
2. `Propagation Setup`_
3. `Simulator Usage`_

.. note::
    More advanced simulations that involve parameter estimation are not covered
    entirely by the following guide.

Environment Setup
=================

This guide separates the definition of environment models into two steps:
(1) ``create bodies``, which are bodies generally derived from default models, (2)
``create vehicle``, which is generally the definition of a simple custom body which
seldom involves complex model definition; and (3) ``create interfaces``, which
defines the models that determine the interaction between the vehicle and the
environment.

.. note::
    The sole definition of an 'interface' will not result in the associated
    acceleration to be accounted for during propagation. The `interface` provides
    the environment model which the acceleration model will later use during
    propagation.

Create bodies
#############

.. container:: content-tabs

    .. tab-container:: default
        :title: Default

        The definition of bodies present within the simulation can be carried out by
        creating a string list of bodies that are a subset of the following available
        default bodies. For transparency, all default models are explained in each
        bodies respective expand option.

        - Common:
            - **Shape**: SphericalBodyShapeSettings(**spice::bodvrd_c**)
            - **Ephemeris**: DirectSpiceEphemerisSettings
                - frame origin: Solar System Barycentric (SSB)
                - frame orientation: Ecliptic J2000 (ECLIPJ2000)
                - stellar aberration correction: False
                - converge light time aberration: False
            - **Gravity field**:
                If no gravity field is specified below, a point
                mass gravity field model will be generated with data from ``SPICE``.

        - Sun
        - Mercury
            - **Gravity model**:
            - **Rotation model**:
        - Venus
            - **Gravity model**:
            - **Rotation model**:
        - Earth
            - **Atmosphere model**: TabulatedAtmosphere(**USSA1976Until100kmPer100mUntil1000kmPer1000m.dat**)
            - **Gravity field model**: SphericalHarmonicsGravityField(**egm96**)
            - **Rotation model**:
        - Moon
            - **Gravity model**: SphericalHarmonicsGravityField(**lpe200**)
            - **Rotation model**:
        - Mars
            - **Gravity model**: SphericalHarmonicsGravityField(**jgmro120d**)
            - **Rotation model**:
        - Jupiter
            - **Ephemeris**:
            - **Gravity model**:
        - Io
        - Europa
        - Ganymede
        - Callisto
        - Saturn
            - **Ephemeris**:
            - **Gravity model**:
            - **Rotation model**:
        - Uranus
            - **Ephemeris**:
            - **Gravity model**:
            - **Rotation model**:
        - Neptune
            - **Ephemeris**:
            - **Gravity model**:
            - **Rotation model**:

        .. tabs::

             .. tab:: Python

              .. toggle-header::
                 :header: Required **Show/Hide**

                 .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_bodies.py
                    :language: python

              .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_bodies_1.py
                 :language: python

             .. tab:: C++

              .. toggle-header::
                 :header: Required **Show/Hide**

                 .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_bodies.cpp
                    :language: c++

              .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_bodies_1.cpp
                 :language: c++

    .. tab-container:: custom
        :title: Custom

        .. warning:: This is only recommended for advanced users (undocumented).


Create vehicle
##############

.. tabs::

      .. tab:: Basic

            .. tabs::

               .. tab:: C++

                  .. toggle-header::
                     :header: Required **Show/Hide**

                     .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_vehicle.cpp
                        :language: c++

                  .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_vehicle.cpp
                     :language: c++

               .. tab:: Python

                  .. toggle-header::
                     :header: Required **Show/Hide**

                     .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_vehicle.py
                        :language: python

                  .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_vehicle.py
                     :language: python

      .. tab:: Intermediate

            .. tabs::

               .. tab:: C++

                  .. toggle-header::
                     :header: Required **Show/Hide**

                     .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_vehicle.cpp
                        :language: c++

                  .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_vehicle.cpp
                     :language: c++

               .. tab:: Python

                  .. toggle-header::
                     :header: Required **Show/Hide**

                     .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_vehicle.py
                        :language: python

                  .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_vehicle.py
                     :language: python

Create interfaces
#################

Interfaces define the interaction of the environment on the vehicle. This step
is important for later defining accelerations that are dependent on
parameters that define the nature of the interaction.

Aerodynamic coefficient interface
_________________________________

.. tabs::

    .. tab:: Constant

        .. tabs::

            .. tab:: C++
            .. tab:: Python

Radiation pressure interface
____________________________

.. tabs::

   .. tab:: Cannonball

      .. tabs::

         .. tab:: C++
         .. tab:: Python

   .. tab:: Panelled


Finalize body creation
**********************

.. tabs::

   .. tab:: C++

      .. toggle-header::
         :header: Required **Show/Hide**

          .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_finalize_bodies.cpp
             :language: cpp

      .. literalinclude:: ../_src_snippets/simulation/environment_setup/finalize_bodies.cpp
         :language: cpp

   .. tab:: Python

      .. toggle-header::
         :header: Required **Show/Hide**

          .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_finalize_bodies.py
             :language: python

      .. literalinclude:: ../_src_snippets/simulation/environment_setup/finalize_bodies.py
         :language: python

Propagation Setup
=================

Define thrust guidance settings
*******************************

Create acceleration models
*******************************

Define Initial System State
*******************************

Create propagator settings
*******************************

Create integrator settings
*******************************

Simulator Usage
===============

Create dynamics simulator
*************************

Retrieve result
*************************

Visualize results
*************************
