.. _torque_model_setup:

==================
Torque Model Setup
==================


Torque models can be created through the factory function
:func:`~tudatpy.numerical_simulation.propagation_setup.create_torque_models`.

How to select torques
============================

In Tudat, a torque acting on a body is defined by:

*  the body upon which the torque is acting;
*  the body exerting the torque;
*  the type and settings of the torque.

These settings are defined via factory functions for each torque in the simulation.

.. seealso::
   A comprehensive list of all available torque models in Tudat and the manner in which to define
   them is given in :ref:`available_torque_models`.

These settings are organized in nested key-value containers (``std::map<>`` in C++, ``dict`` in Python). In general:

- ``key``: body undergoing torque
- ``value``: dictionary with:

  - ``key``: body exerting the torque
  - ``value``: :class:`~tudatpy.numerical_simulation.propagation_setup.torque.TorqueSettings` object.

This container will be supplied to the
:func:`~tudatpy.numerical_simulation.propagation_setup.create_torque_models` function to create the
torque models. This is illustrated in the example below.

Example
=======

In this example, the following torques are exerted on the vehicle:

- by the Earth:

    - spherical-harmonic gravitational torque (up to order 4 and degree 4)
    - aerodynamic torque

- by the Sun:

    - second-degree gravitational torque

- by the Moon:

    - second-degree gravitational torque

The variable ``torques_settings_vehicle`` denotes the list of bodies exerting torques and the types of
torques, while the variable ``torque_settings`` associates this list with the body undergoing the
torque.
The function :func:`~tudatpy.numerical_simulation.propagation_setup.create_torque_models` creates the list of
models that compute the torques during the propagation.

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp


When propagating multiple bodies (see :ref:`multi_body_dynamics`), the same list of settings may be re-used for
multiple bodies. Below, an example is given for the definition of ``torque_settings`` for multiple bodies
(``Vehicle1`` and ``Vehicle2``) which are undergoing identical torques:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup_multi_vehicle.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

Or separate torque settings may be defined for separate bodies, and then combined into a ``torque_settings`` variable.
Below, an example for such a case is given when propagating the Earth and Moon:

    .. tabs::

         .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

                .. code-block:: python

                    from tudatpy.kernel.numerical_simulation import propagation_setup

          .. literalinclude:: /_src_snippets/simulation/propagation_setup/torque_models/torque_setup_multi.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp