.. _propagation_architecture:

========================
Propagation architecture
========================

The core of a numerical integration is the successive evaluation of the state derivative :math:`\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},s;\mathbf{p})`. Here, :math:`\mathbf{x}` is the propagated state. For a typical propagation, this is the translational state of a single body, but it may be a combination of any types of dynamics for any number of bodies (see :ref:`here <dynamics_types_intro>`), and may also include the variational equations associated with these dynamics. The variable :math:`s` is the independent variable of the differential equation governing the state (typically but not necessarily the time :math:`t`), and the vector :math:`\mathbf{p}` denotes a set of parameters which are held constant during the propagation, but which do influence the solution of the equations of motion.

.. _propagator_pre_processing:

Propagator pre-processing
=========================

Before starting the propagation, several steps are taken to initialize the variables/objects required for the propagation. Below, we provide an overview of the steps that are taken for the propagation of a single arc (typical Tudat propagation):

* It is checked whether the propagator settings are feasible (e.g. no body A propagated w.r.t. B, *and* body B propagated w.r.t. body A, etc.).
* Several objects are created that are used during/after the propagation
  
  * An ``EnvironmentUpdater`` object (in C++; not exposed to Python), which decides which environment models need to be updated for each function evaluation (:ref:`single_propagation_evaluation` and how)
  * A ``ReferenceFrameManager`` object (in C++; not *yet* exposed to Python), which allows translations between ephemerides with different origins to be performed
  * If the ``set_integrated_result`` to the :class:`~tudatpy.numerical_simulation.propagator.SingleArcOutputSettings` is set to true: A set of ``IntegratedStateProcessor`` objects (in C++; not exposed to Python) which is used to post-process the propagation results, and make any required transformations to reset the ephemerides of the propagated bodies.
  * A ``DynamicsStateDerivativeModel`` (in C++; not exposed to Python) object that handles the calculation of a single state derivative evaluation (see :ref:`single_propagation_evaluation`)
  * A ``PropagationTerminationCondition`` (in C++; not exposed to Python) object that checks whether the propagation is terminated for a given time/state pair
  * A set of functions that extract the dependent variables from the environment is created (if any)
* The initial state is converted from processed formulation (in which it *has* to be provided) to propagated formulation (see :ref:`processed_propagated_states`)

.. _single_propagation_evaluation:

A single function evaluation
============================

The top-level calculation of a single state derivative evaluation :math:`\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},s;\mathbf{p})` is handled by the ``DynamicsStateDerivativeModel`` class (in C++; not exposed to Python). In summary, a single function evaluation entails the following steps:

* Check that the independent variable or state are neither infinity nor NaN. If either one is, an exception is thrown.
* The current state of the environment from the previous time step (translational state; orientation, altitude, etc. of bodies) are cleared, ensuring that they are recomputed for the current time step.  (see :ref:`environment_during_propagation` for the properties of bodies that are set during a time step and how to retrieve them).
* The propagated state vector :math:`\mathbf{x}` is split into its constituent parts (*e.g.* translational, rotational, *etc.* states of separate bodies that are propagated).
* The separate propagated states, in 'propagated coordinates', are converted to 'processed coordinates' (see :ref:`processed_propagated_states`). For instance: if Kepler elements of the Moon w.r.t the Earth are propagated, this step converts those Kepler elements (propagated state) to Cartesian elements (processed state)
* Each propagated state, in processed coordinates, is set as the current state of the :class:`~tudatpy.numerical_simulation.environment.Body` object. Consequently, when the :attr:`~tudatpy.numerical_simulation.environment.Body.state` attribute of a propagated body is called during the propagation (see :ref:`environment_during_propagation`) the state from the state vector, converted to Cartesian elements (if needed) is retrieved. If the propagation origin is different from the global frame origin (see :ref:`translational_reference_frames`), a frame translation is applied before updating the body's current state. For instance, if the Kepler elements of the Moon w.r.t. Earth are propagated (propagation origin: Earth), and the global frame origin is the SSB, the :attr:`~tudatpy.numerical_simulation.environment.Body.state` attribute of the Moon will be the Cartesian state w.r.t. the SSB.
* The time-dependent properties of the environment are updated to the current time and propagated state. Only those time/state-dependent models that are needed for either the dynamics or the dependent variables are updated during each time step. For instance, if Jupiter is a body in the environment, but Jupiter's state plays no role in either the dynamics or in the dependent variables that are saved, its state is *not* updated at each time step.
* Each state derivative model (acceleration, torque, etc.) required for the calculation of the state derivative is evaluated. If variational equations are required, the state derivative partials are evaluated
* The derivative of each propagated state :math:`\mathbf{x}_{i}` is evaluated from the separate state derivatives (e.g. accelerations are used to compute derivative of Kepler elements, if propagating Kepler elements), and concatenated into the complete state derivative vector :math:`\dot{\mathbf{x}}`

.. _single_propagator_time_step:

A single time step
==================

Depending on the integrator that is used, a single time step may require one or several function evaluations of the state derivative function :math:`\mathbf{f}`. The full propagation loop, which successively calls the numerical integrator to advance the state, is in the ``integrateEquationsFromIntegrator`` function (in C++; not exposed to Python). The steps for a single time step are the following:
 
* Check that the independent variable or state are neither infinity nor NaN. If either one is, the propagation is tagged as being unsuccessful (``nan_or_inf_detected_in_state`` from :class:`~tudatpy.numerical_simulation.propagation.PropagationTerminationReason`) and the results up until the current point are returned.
* Advance the time and state from :math:`(t_{i},\mathbf{x}_{i})` to :math:`(t_{i+1},\mathbf{x}_{i+1})` by calling the ``performIntegrationStep`` function of the selected numerical integrator (which may involve one or more function evaluations :math:`\mathbf{f}`). The time step that is taken may be fixed, or may be adjusted by the integrator, depending on the selected integration algorithm.
  
  * If an exception is thrown during the propagation, the propagation is tagged as being unsuccessful (``runtime_error_caught_in_propagation`` from :class:`~tudatpy.numerical_simulation.propagation.PropagationTerminationReason`) and the results up until the current point are returned.
* If needed, the state :math:`\mathbf{x}_{i+1}` is corrected to account for matters such as normalization conditions. Possible corrections are:

  * If the propagated state involves one or more quaternions :math:`\mathbf{q}` representing a rotation, these are renormalized as :math:`\mathbf{q}\rightarrow \mathbf{q}/|\mathbf{q}|` to ensure that the norm of the quaternion is reset to unity
  * If the state contains a shadow parameter (modified Rodrigues parameters; exponential map), it is checked whether the element set has to switched to the shadow elements. Note that this will cause a discontinuity in the state history between :math:`\mathbf{x}_{i}` and :math:`\mathbf{x}_{i+1}`, but *not* a discontinuity in the 'processed' (for translational dynamics: Cartesian) state.
* If a termination condition was reached *during* one of the sub-stages of the time step, the propagation is stopped, and the results returned. Note that this only happens if the ``assess_termination_on_minor_steps`` input to one of the integrator setting functions in :doc:`integrator` is set to true (false by default)
* If output is to be saved at the current time step (default: saved every time step):

  * The pair :math:`(t_{i+1},\mathbf{x}_{i+1})` is added to the propagated state history
  * If any dependent variables are to be saved, the environment is updated to the current time/state :math:`(t_{i+1},\mathbf{x}_{i+1})`, see :ref:`single_propagation_evaluation`, and the dependent variables are extracted.
* It is checked whether the :math:`(t_{i+1},\mathbf{x}_{i+1})` pair meets the termination conditions. If the termination conditions are exceeded, and the ``terminate_exactly_on_final_condition`` input to the termination condition settings is set to false (see :doc:`propagator`), the propagation is finished, and the results are returned. If this variable is set to true:

  * If the termination condition is a given time (:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.time_termination`), the final time step is adjusted such that the final time is reached exactly
  * If the termination condition is a given dependent variable value (:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.dependent_variable_termination`), a root finding algorithm is used to iterate to the time :math:`t_{i+1}` at which the given value is achieved.
* In either case, the :class:`~tudatpy.numerical_simulation.propagation.PropagationTerminationReason` is set to `termination_condition_reached``, and the state and dependent variable history is returned.

.. _propagator_post_processing:

Propagator post-processing
==========================

After the propagation is finished, the following post-processing steps are performed before returning the simulation to the user:

* The propagated states are converted to processed states. After the propagation, the time histories of both may be extracted from the :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.unprocessed_state_history` and :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.state_history` attributes, respectively
* If the ``set_integrated_result`` to the :class:`~tudatpy.numerical_simulation.propagator.SingleArcOutputSettings` is set to true, the propagated states (in processed formulation) are used to reset the environment of the propagated body/bodies. For the different state types, this means:

  * Translational dynamics: the propagated translational state of the body is used to create an interpolator (:func:`~tudatpy.math.interpolators.lagrange_interpolation`, ``number_of_points`` =6), which is used to update the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated` ephemeris of the body. If needed, a translation from the propagation origin to the ephemeris origin is applied (see :ref:`translational_frame_origins`). NOTE: this is *only* possible if the body has a tabulated ephemeris already, or no ephemeris. In the latter case a tabulated ephemeris is created, with ephemeris origin equal to the propagation origin. In case you want to use a non-tabulated ephemeris for the propagated body, you can use the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated_from_existing` function to override existing body settings (see :ref:`override_body_settings`). When doing so, the behaviour of the non-tabulated ephemeris will be emulated by a non-tabulated ephemeris.
  *  Rotational dynamics: the propagated rotational state of the body is used to create an interpolator (:func:`~tudatpy.math.interpolators.lagrange_interpolation`, ``number_of_points`` = 6), which is used to create a tabulated rotation model (not yet exposed to Python). At present, this option is only possible if the propagated body starts out with *no* rotation model. An update to allow the same flexibility as for the translational dynamics (see above) is planned
  *  Mass dynamics: the propagated mass of the body is used to create an interpolator (:func:`~tudatpy.math.interpolators.lagrange_interpolation`, ``number_of_points`` =6), which is used to update the mass function of the body.
* If the ``clear_numerical_solutions`` to the :class:`~tudatpy.numerical_simulation.propagator.SingleArcOutputSettings` is set to true, the state
  (processed and unprocessed) and dependent variable history are deleted, *after* having reset the environment
  (if ``set_integrated_result`` was set to true; see above). In this case, the ephemerides are reset with the propagated dynamics,
  but the results of the propagation cannot be extracted from the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.unprocessed_state_history`,
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.state_history` and
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.dependent_variable_history` attributes.
  Note that the dependent variable history will be lost entirely in this case.
