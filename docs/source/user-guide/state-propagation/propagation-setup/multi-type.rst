.. _multi_type_dynamics:

===================
Multi-type dynamics
===================

Tudat permits the propagation of any combination of types of dynamics, for any number of bodies. One example is the simulation of coupled translational-rotational dynamics of one or more bodies, or the combined translational and mass dynamics of a body (e.g. spacecraft under thrust).

To define multi-type propagator settings, you must first define the propagator settings for each type of dynamics separately, after which you combine these using the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.multitype` function as follows: 

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
      :sync: python

      .. dropdown:: Required
         :color: muted

         .. literalinclude:: /_src_snippets/simulation/environment_setup/full_translational_setup.py
         .. literalinclude:: /_src_snippets/simulation/environment_setup/full_rotational_setup.py
         .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
            :language: python

      .. literalinclude:: /_src_snippets/simulation/environment_setup/full_multitype_setup.py
         :language: python

This example (note the collapsed combined code for the translational, rotational, and mass dynamics examples) shows the use of the translational, rotational and mass dynamics of a single body ``Spacecraft``. However, the framework is not limited to propagating the different types of dynamics for only one body. You may for instance propagate the translational state and mass of a spacecraft concurrently with the rotational state of the Earth. Also, you may propagate any number of any type of dynamics of any body, e.g. translational dynamics of 6 bodies, rotational dynamics of 4 bodies and mass of 2 bodies, where these three sets of bodies may but need not fully or partially overlap.

When using multi-type propagator settings, the following settings:

- **Output variables**
- **Termination settings**
- **Integrator settings**
- **Initial time**
- **Console output and processing settings**

that are passed to the ``propagation_setup.propagator.multitype`` function are used. Settings of the same kind are also stored in the constituent single-type propagator settings (above, in the ``propagator_settings_list`` input), but these *are fully ignored when using multi-type settings*! Only the settings of these types explicitly added to the ``propagation_setup.propagator.multitype`` function are used.

Conversely, the ``propagation_setup.propagator.multitype`` function does not take any initial states as inputs. The complete, multitype, initial state vector is set up from its constituent single-arc settings (with the order as noted below)

.. note::
   
  The order of the state entries in the multi-type state vector will, in general, be different from the order provided in the `propagator_settings_list` When different state types are propagated, the state output contains the states in following order:

  - Translational state ( **T** )
  - Rotational state ( **R** )
  - Body mass state ( **M** )
  - Custom state ( **C** )

  To retrieve the definition of the multitype state vector, see :ref:`console_output`.
