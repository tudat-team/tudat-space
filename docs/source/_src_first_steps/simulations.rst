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

Create bodies
#############

The definition of bodies present within the simulation largely involves the
th

.. tabs::

   .. tab:: Default

      .. tabs::

         .. tab:: C++

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_bodies.cpp
                :language: c++

          .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_bodies_1.cpp
             :language: c++

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

             .. literalinclude:: ../_src_snippets/simulation/environment_setup/req_create_bodies.py
                :language: python

          .. literalinclude:: ../_src_snippets/simulation/environment_setup/create_bodies_1.py
             :language: python

   .. tab:: Custom

      .. warning:: This is only recommended for advanced users.


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
