.. _processed_propagated_states:

=======================================
Processed vs. Propagated State Elements
=======================================

In Tudat, we distinguish between 'processed' and 'propagated' state elements, wi. Below, we describe distinction.
Note that in most cases, users will have to specify (for initial states) or interact with (for custom models)
the *processed* states.

.. _processed_states:

Processed Elements
---------------------

The processed elements are used to describe the state of the object(s) in any place *other* than the state vector
that is being solved for by the numerical integrator.

For the supported dynamics types, the following formulations are defined to be the processed formulation:

- **Translational Motion**: Cartesian coordinates (w.r.t central body, if relevant)
- **Rotational Motion**: Quaternions defining rotation from inertial to body-fixed frame (see :ref:`quaternion_definition`), angular velocity vector of the body in body-fixed frame
- **Mass Dynamics**: Current mass (no other formulation is used)

You will find and need to use *processed* coordinates in these scenarios:

- To describe the initial conditions of an object when creating propagator settings (typically using the
  :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` or
  :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` functions)
- As an output from the numerical propagation, extracted from the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.state_history` of the
  :class:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults` (see :ref:`propagation_results`)


- When extracting the current state from a :class:`~tudatpy.numerical_simulation.environment.Body` object during the propagation

Internally, Tudat uses the *processed* state in the following places:

- To update the environment model of an object (this also means that the states extracted from the body are expressed In
  the processed coordinates);
- To update the acceleration model of an object.


Propagated Elements
-------------------

The *propagated* coordinates, on the other hand, are used *only* to describe the state in the actual differential equations
being used. A list of options for translational and rotational dynamics is given in
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.TranslationalPropagatorType` and
:class:`~tudatpy.numerical_simulation.propagation_setup.propagator.RotationalPropagatorType`, respectively.
The choice of formulation for translational and
rotational motion is specified when calling the  :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` and
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` functions, respectively.

In Tudat, you will find the propagated elements in the following place:

- As an output from the numerical propagation, extracted from the
  :attr:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults.unprocessed_state_history` of the
  :class:`~tudatpy.numerical_simulation.propagation.SingleArcSimulationResults` (see :ref:`propagation_results`)

Internally, Tudat uses the *propagated* state in the following place:

- As the input/output of the numerical integrator's state derivative function (see :ref:`single_propagation_evaluation` for more details).

As a user, you will generally only interact with the processed coordinates, but you will have the choice over which
propagated coordinate to use for propagation/integration. Even though you may rarely interact with the propagated
coordinates, a judicious choice of formulation of equations of motion (*e.g.*, definition of propagated coordinates)
can have a significant influence on the quality of your numerical results.

.. note::

    Since the processed coordinates are used to update the environment and accelerations of the bodies, but the
    propagated coordinates are the ones used in propagation, you can see that whenever the processed and propagated
    coordinates differ, there is a need to convert between the two at every time step (or even multiple times, if the time
    step is divided in multiple steps for integration). Therefore, this leads to a set of extra operations to be performed
    during propagation, which may in turn lead to a longer computation time for a single evaluation of the state derivative
    and/or increased numerical error. However, these aspects are rarely influential.

.. note::

    Another fact to consider, is that sometimes there may be a difference between the size of the processed and
    propagates states. For instance, a Cartesian state is expressed with 6 elements, but the USM7 state with 7. This may
    lead to some confusion when extracting the results, so keep this in mind.
