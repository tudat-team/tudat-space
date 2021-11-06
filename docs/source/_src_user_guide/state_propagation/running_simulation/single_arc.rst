
.. _single_arc_propagation:

======================
Single-Arc Propagation
======================

Example usage
--------------

For propagation of the system state along a single arc, the ``SingleArcSimulator`` class derived from the ``Simulator``
class should be used. An example is provided below:

.. tabs::

     .. tab:: Python

          .. toggle-header::
             :header: Required **Show/Hide**

          .. code-block:: python

                # Create simulation object and propagate dynamics
                dynamics_simulator = propagation_setup.SingleArcSimulator(
                        bodies, integrator_settings, propagator_settings)

                # OUTPUT:

                # Cartesian states
                states = dynamics_simulator.state_history
                # States actually used during the numerical integration
                unprocessed_states = dynamics_simulator.unprocessed_state_history
                # Dependent variables
                dependent_variable_history = dynamics_simulator.dependent_variable_history

                # Check if the propagation was successful
                print("Propagation successful:", dynamics_simulator.integration_completed_successfully)
                print("Termination reason:", dynamics_simulator.propagation_termination_details.termination_reason)

     .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_setup.cpp
             :language: cpp

First, a ``SingleArcSimulator`` is created using the system of bodies, integrator settings, and propagator settings
objects. Using the function as above, Tudat will then automatically set up and solve the dynamics accordingly.
In our API documentation, you can find several additional options for creating the
:class:`~tudatpy.numerical_simulation.SingleArcSimulator`.

Retrieving the output
---------------------

The state history is retrieved in the next line by accessing the
:attr:`~tudatpy.numerical_simulation.SingleArcSimulator.state_history` attribute of ``SingleArcSimulator``.
The :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.state_history` attribute is a dictionary and contains
the
numerically propagated state (as value) at each epoch (as key), which can be exported or used for subsequent
analysis.


If the user chose to export dependent variables, they can be extracted from the dynamics simulator by the
:attr:`~tudatpy.numerical_simulation.SingleArcSimulator.dependent_variable_history` attribute. The order of the
dependent variables that are stored are printed to the terminal if the ``print_dependent_variable_data`` input to
the :class:`~tudatpy.numerical_simulation.SingleArcSimulator` constructor is set to True.
Alternatively, the :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.dependent_variable_ids` attribute can be
used to extract this information in the form of a dictionary.

Understanding the state output
------------------------------

It is important to realize that, *regardless* of the formulation of the equations of motion (for translational
dynamics: Cowell, Gauss-Kepler, etc., see :ref:`translational_dynamics`),
the :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.state_history` attribute will always provide the results
of the propagation in Cartesian elements (for the case of translational dynamics).
In the case where a different formulation than the Cowell formulation is used, the states that were actually used
during the numerical integration can be accessed through the
:attr:`~tudatpy.numerical_simulation.SingleArcSimulator.unprocessed_state_history`. For instance, whe using the
``gauss_keplerian`` propagator (as input to :func:`~tudatpy.numerical_simulation.propagation_setup.propagator
.translational`), it is the equations of motion in Keplerian elements which are solved numerically.
The :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.unprocessed_state_history` attribute of the
``SingleArcSimulator`` class will provide you with the history of the Keplerian elements, which were directly solved
for by the integrator, while the  :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.state_history` provides
the Cartesian elements, obtained from the conversion of the propagated Keplerian elements (see
:ref:`convention_propagated_coordinates` for more details).

Checking the outcome of the propagation
---------------------------------------

For various reasons, occurence of a NaN or Inf value, segmentation fault in underlying (user-defined) code, *etc.*,
the propagation may not propagate succesfully to the final user-specified conditions.
Even in the case of a segmentation fault during the propagation, the propagation results - up until the time of
termination - will be saved and accessible as indicated above. To determine whether the propagation encountered any
issues, the :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.integration_completed_successfully`
boolean can be extracted from the ``SingleArcSimulator``.
More details on the specifics of the termination can be extracted from the
:attr:`~tudatpy.numerical_simulation.SingleArcSimulator.propagation_termination_details` attribute, which provides the
specific reason for termination.

.. seealso::
   For a complete example of a perturbed single-arc propagation, please see the tutorial
   :ref:`propagating_a_spacecraft_with_perturbations`.
