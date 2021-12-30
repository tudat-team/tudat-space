.. _acceleration_models_setup:

========================
Acceleration Model Setup
========================

Acceleration models can be created through the factory function
:func:`~tudatpy.numerical_simulation.propagation_setup.create_acceleration_models`.

How to select accelerations
============================

In Tudat, an acceleration acting on a body is defined by:

*  the body undergoing acceleration;
*  the body exerting the acceleration;
*  the type and settings of the acceleration.

These settings are defined via factory functions for each acceleration in the simulation.

.. seealso::
   A comprehensive list of all available acceleration models in Tudat and the manner in which to define
   them is given in :ref:`available_acceleration_models`.

These settings are organized in nested key-value containers (``std::map<>`` in C++, ``dict`` in Python). In general:

- ``key``: body undergoing acceleration
- ``value``: dictionary with:

  - ``key``: body exerting the acceleration
  - ``value``: :class:`~tudatpy.numerical_simulation.propagation_setup.acceleration.AccelerationSettings` object.

This container will be supplied to the
:func:`~tudatpy.numerical_simulation.propagation_setup.create_acceleration_models` function to create the
acceleration models. This is illustrated in the example below.

Example
=======

In this example, the following accelerations are exerted on the vehicle:

- by the Earth:

    - spherical harmonic gravitational acceleration (degree and order 5)
    - aerodynamic acceleration

- by the Sun:
    - point-mass gravity

- by the Moon:
    - point-mass gravity

The variable ``accelerations_settings_vehicle`` denotes the list of bodies exerting accelerations and the types of
accelerations, while the variable ``acceleration_settings`` associates this list with the body undergoing the
acceleration.
The
function :func:`~tudatpy.numerical_simulation.propagation_setup.create_acceleration_models` creates the list of
models that compute the accelerations during the propagation.



    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/acceleration_example.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

When propagating multiple bodies, the same list of settings may be re-used for multiple bodies. Below,
an example is given for the definition of ``acceleration_settings`` for multiple bodies (``Vehicle1`` and
``Vehicle2``) which are undergoing identical accelerations:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/acceleration_example_multi_vehicle.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

Alternatively, separate acceleration settings may be defined for separate bodies and then combined into an
``acceleration_settings`` variable. Below, an example for such a case is given when propagating the Earth and Moon:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/acceleration_models/acceleration_example_multi.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp


