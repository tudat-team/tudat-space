
.. _single_arc_propagation:

======================
Single-arc Propagation
======================

For propagation of the system state along a single arc, the ``SingleArcSimulator`` derivative of the ``Simulator`` class should be used:

.. tabs::

     .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. code-block:: python

                # Create simulation object and propagate dynamics.
                dynamics_simulator = propagation_setup.SingleArcSimulator(
                        bodies, integrator_settings, propagator_settings)

                states = dynamics_simulator.state_history
                unprocessed_states = dynamics_simulator.unprocessed_state_history
                dependent_variable_history = dynamics_simulator.dependent_variable_history

     .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

First, a ``SingleArcSimulator`` is created using the system of bodies, integrator settings, and propagator settings objects.
Tudat will then automatically read and setup the simulation accordingly.
The state history is retrieved in the next line by accessing the ``state_history`` attribute of the ``Simulator``.
The ``state_history`` attribute is of type dictionary (Python) or map (C++) and contains the state of the propagated body at each epoch, which can be exported or used for subsequent analysis.

It's important to realize that, *regardless* of the formulation of the equations of motion (Cowell, Gauss-Kepler, etc.), the ``state_history`` attribute will always provide the results of the propagation, converted to Cartesian elements (for the case of translational dynamics).
In the case where a different formulation than the Cowell formulation is used, the states that were actually used during the numerical integration can be accessed through the ``unprocessed_state_history``. For instance, whe using the ``gauss_keplerian`` propagator, it is the equations of motion in Keplerian elements which are solved numerically.
The ``unprocessed_state_history`` will provide you with the history of the Keplerian elements (as directly solved for by the integrator), while the  ``state_history`` provides the Cartesian elements, obtained from the conversion of the propagated Keplerian elements(see :ref:`convention_propagated_coordinates` for more details).

If the user chose to export dependent variables, they can be extracted from the dynamics simulator as follows.
Just like the ``state_history``, the ``dependent_variable_history`` attribute is of kind dictionary (Python) or map (C++):


For a complete example of a perturbed single-arc propagation, please see the tutorial :ref:`propagating_a_spacecraft_with_perturbations`.
