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

For a single body, the user-specified settings are organized in nested dictionaries ``dict[str,dict[str,list[AccelerationSettings]]]``,
with the first ``str`` denoting the body undergoing acceleration, the second ``str`` denoting the body exerting the acceleration, and the
list of :class:`~tudatpy.numerical_simulation.propagation_setup.acceleration.AccelerationSettings` objects is created using the functions in the
:doc:`acceleration` module.

This nested dictionary will be supplied to the
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



.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
        :color: muted

        .. code-block:: python

            from tudatpy.numerical_simulation import propagation_setup

      .. literalinclude:: /_snippets/simulation/propagation_setup/acceleration_models/acceleration_example.py
          :language: python

When propagating multiple bodies, the same list of settings may be re-used for multiple bodies. Below,
an example is given for the definition of ``acceleration_settings`` for multiple bodies (``Vehicle1`` and
``Vehicle2``) which are undergoing identical accelerations:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
        :color: muted

        .. code-block:: python

            from tudatpy.numerical_simulation import propagation_setup

      .. literalinclude:: /_snippets/simulation/propagation_setup/acceleration_models/acceleration_example_multi_vehicle.py
          :language: python

Alternatively, separate acceleration settings may be defined for separate bodies and then combined into an
``acceleration_settings`` variable. Below, an example for such a case is given when propagating the Earth and Moon:

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
        :color: muted

        .. code-block:: python

            from tudatpy.numerical_simulation import propagation_setup

      .. literalinclude:: /_snippets/simulation/propagation_setup/acceleration_models/acceleration_example_multi.py
          :language: python


