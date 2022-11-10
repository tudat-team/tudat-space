
.. _propagation_results:

===================
Propagation results
===================

After numerically propagating the dynamics, as follows:

.. code-block:: python

    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        body_system, propagator_settings)
    propagation_results = dynamics_simulator.propagation_results

the results are stored in the
``propagation_results`` object. For a single-arc propagation, this object is of the type
:class:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults`.
Multi- and hybrid-arc results are discussed briefly :ref:`below <multi_hybrid_arc_results>`.

The three primary numerical results of the propagation are:

- The numerical results of the propagation, in 'conventional' coordinates
  (e.g. Cartesian elements for translational dynamics, see :ref:`conventional_states`), stored in the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_history.state_history` attribute
- The numerical results of the propagation, in the propagated coordinates, stored in the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_history.unprocessed_state_history` attribute
- The dependent variables of the propagation (if any, see :ref:`dependent_variables`), stored in the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_history.dependent_variable_history` attribute

Each of these is returned as a dictionary, with the numerical integration epochs as key, and the current state/dependent variable
as value. For example:

.. code-block:: python

    # Propagate dynamics
    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        body_system, propagator_settings)

    # Retrieve object with full results
    propagation_results = dynamics_simulator.propagation_results

    # Retrieve the individual result histories
    states = propagation_results.state_history
    unprocessed_states = propagation_results.unprocessed_state_history
    dependent_variables = propagation_results.dependent_variable_history

The order of the entries of the state/dependent variable vector at every epoch can be printed to the consol before propagation as
described :ref:`here <console_output>`. This information can also be retrieved as dictionaries from the
:attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.state_ids`
:attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.unprocessed_state_ids` and
:attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_ids`
attributes.

Additional results of the propagation, such as the runtime (e.g. real clock time) and number of function
evaluations as a function of simulation time  (e.g. epoch in th simulation) can also be extracted from
the :class:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResult` class.

Understanding the state output
------------------------------

It is important to realize that, *regardless* of the propagator that is used (for translational
dynamics: Cowell, Gauss-Kepler, etc., see :ref:`translational_dynamics`)
the :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_history.state_history` attribute
will always provide the results of the propagation in Cartesian elements (for the case of translational dynamics).
In the case where a different formulation than the Cowell formulation is used, the states that were actually used
during the numerical integration can be accessed through the
:attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.dependent_variable_history`. For instance, whe using the
``gauss_keplerian`` propagator, it is the equations of motion in Keplerian elements which are solved numerically.
The :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.unprocessed_state_history` attribute will thn provide
you with the history of the Keplerian elements, which were directly solved
for by the integrator, while the  :attr:`~tudatpy.numerical_simulation.SingleArcSimulator.state_history` provides
the Cartesian elements, obtained from the conversion of the propagated Keplerian elements (see
:ref:`conventional_propagated_states` for more details).


Checking the outcome of the propagation
---------------------------------------

For various reasons, such as the occurrence of a NaN or Inf value in the state during a propagation,
segmentation fault in underlying (user-defined) code, *etc.*,
the propagation may not propagate successfully to the final :ref:`user-specified conditions <termination_settings>`.
In the case of any such errors, the propagation results will be saved and are accessible as indicated above
- up until the time of termination.

To determine whether the propagation encountered any
issues, the :attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.integration_completed_successfully`
boolean of the :class:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults` class can be queried

More details on the specifics of the reason for termination can be extracted from the
:attr:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults.propagation_termination_details` attribute
of the :class:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults` class.

.. seealso::
   For a complete example of a perturbed single-arc propagation, please see the tutorial
   :ref:`propagating_a_spacecraft_with_perturbations`.

.. _multi_hybrid_arc_results:

Multi- and hybrid-arc results
---------------------------------------

When performing a multi- or hybrid-arc propagation, the results are stored in a
:class:`~tudatpy.numerical_simulation.propagation.MultiArcPropagatorResults` and
:class:`~tudatpy.numerical_simulation.propagation.HybridArcPropagatorResults` object, respectively.
The main contents of these objects are a set of :class:`~tudatpy.numerical_simulation.propagation.SingleArcPropagatorResults`
objects, which contain the results of the constituent single arcs, as described above.
In addition, the multi- and hybrid arc results objects contain a number of pieces of information that are specific to the
full propagation, as opposed to its separate arcs. The reader is referred to the `API documentation <https://py.api.tudat.space/en/latest/>`_ for more details. A small example is shown below:

.. code-block:: python

    # Propagate multi-arc dynamics (as defined by propagator_settings object)
    dynamics_simulator = numerical_simulation.create_dynamics_simulator(
        body_system, propagator_settings)

    # Extract multi-arc results
    propagation_results = dynamics_simulator.propagation_results
    number_of_arcs = propagation_results.number_of_arcs

    # Extract full results of first arc, and retrieve the propagated states
    first_arc_propagation_results = propagation_results.get_arc_results( 0 )
    first_arc_states = first_arc_propagation_results.state_history


