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

For a single body, the user-specified settings are organized in nested dictionaries ``dict[str,dict[str,list[TorqueSettings]]]``,
with the first ``str`` denoting the body undergoing acceleration, the second ``str`` denoting the body exerting the acceleration, and the
list of :class:`~tudatpy.numerical_simulation.propagation_setup.torque.TorqueSettings` objects is created using the functions in the
:doc:`torque` module.

This nested dictionary will be supplied to the
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

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. dropdown:: Required
      :color: muted

      .. code-block:: python

        from tudatpy.numerical_simulation import propagation_setup

    .. literalinclude:: /_snippets/simulation/propagation_setup/torque_models/torque_setup.py
        :language: python

When propagating multiple bodies (see :ref:`multi_body_dynamics`), the same list of settings may be re-used for
multiple bodies. Below, an example is given for the definition of ``torque_settings`` for multiple bodies
(``Vehicle1`` and ``Vehicle2``) which are undergoing identical torques:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. dropdown:: Required
      :color: muted

      .. code-block:: python

        from tudatpy.numerical_simulation import propagation_setup

    .. literalinclude:: /_snippets/simulation/propagation_setup/torque_models/torque_setup_multi_vehicle.py
        :language: python

Below, an example for such a case is given when propagating the Earth and Moon:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. dropdown:: Required
      :color: muted

      .. code-block:: python

        from tudatpy.numerical_simulation import propagation_setup

    .. literalinclude:: /_snippets/simulation/propagation_setup/torque_models/torque_setup_multi.py
        :language: python