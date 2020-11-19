.. _translational_dynamics:

======================
Translational Dynamics
======================

Basic settings for propagating translational dynamics require:

* The names of the bodies that are to be propagated
* The centers of propagation w.r.t. which they are to be propagated
* Acceleration models that are to be used for the dynamics
* Initial state, in Cartesian elements with the same frame orientation as the environment (see :ref:`creating_celestial_bodies`)
* Termination time of propagation

Such a propagation is defined as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

With these settings, the body "Vehicle" will be propagated w.r.t. body "Earth", using given acceleration models (see :ref:`acceleration_model_setup`), a given initial state which defines the initial Cartesian state of the center of mass of "Vehicle" w.r.t. the center of mass of "Earth". The propagation will terminate once the ``simulation_end_epoch`` epoch is reached.

Additional options that can be used for the propagation:

* Specifying alternative termination conditions (see :ref:`available_termination_settings`), this input replaces the ``simulation_end_epoch`` above
* Specifying an alternative formulation for the translational state (see list below). Default: Cowell formulation (Cartesian position and velocity) is used
* Specifying variables that are to be saved during the propagation (see :ref:`simulation_propagator_setup`). Default: None
* Requesting terminal output during the propagation (see :ref:`simulation_output_variables`) . Default: None

These additional options can be provided as follows:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

Where the three final, and optional, input arguments can be used with both when ``termination_settings`` and ``simulation_end_epoch`` input. 

.. class:: Translational Motion Propagators

  - Cartesian coordinates (with ``cowell`` propagator); state size: 6
  - Cartesian coordinates (with ``encke`` propagator); state size: 6
  - Keplerian elements (with ``gauss_keplerian propagator``); state size: 6
  - Modified equinoctial elements (with ``gauss_modified_equinoctial`` propagator); state size: 6
  - Unified state model with quaternions, or USM7 (with ``unified_state_model_quaternions`` propagator); state size: 7
  - Unified state model with modified Rodrigues parameters, or USM6 (with ``unified_state_model_modified_rodrigues_parameters`` propagator); state size: 7
  - Unified state model with exponential map, or USMEM (with ``unified_state_model_exponential_map`` propagator); state size: 7
