.. _convention_propagated_coordinates:

=======================================
Conventional vs. Propagated Coordinates
=======================================

In the description of some of the objects in this part of the wiki about the simulation setup, you may have noticed the use of two names to describe the propagated states of an object. These two names are *conventional* state and *propagated* state. They describe two different manners to describe the state, and are used in different parts of the code. In this part of the wiki, you will get to know in what ways they differ and how that may affect your application. 

The two terms are only used for the states that are being numerically propagated (so not for those taken from an ephemeris, for instance). Taking translational dynamics as an example, the short distinction between the two concepts is that the conventional formulation is the state in Cartesian elements, and the propagated formulation is the state that is actually being propagated numerically (see :ref:`here<translational_dynamics_propagators>` for a list of options). For instance, when using the formulation of the equations of motion in Keplerian elements, the propagated state is the current state, as defined in Keplerian elements, and the conventional state is its conversion to Cartesian elements. 

**Conventional Coordinates**

	These coordinates are mainly used to describe the state of the object(s) in any place *other* than the state vector that is being fed to the numerical integrator. 

	For the supported dynamics types, the following formulations are defined to be the conventional formulation
	
	- **Translational Motion**: Cartesian coordinates
	- **Rotational Motion**: Quaternions defining rotation to body-fixed frame, angular velocity vector in body-fixed frame (see :ref:`rotational_dynamics`)
	- **Mass Dynamics**: Current mass (no other formulation is used)

    You will find and need to use *conventional* coordinates in these scenarios:

        - To describe the initial conditions of an object when creating propagator settings (typically using the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` or :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` functions)
        - As an output to the ``state_history`` function from a ``Simulator`` object (such as the :class:`~tudatpy.numerical_simulation.SingleArcSimulator` class)
        - When extracting the current state from a :class:`~tudatpy.numerical_simulation.environment.Body` object
`
    Internally, Tudat uses the *conventional* state in the following places:

	- To update the environment model of an object; this also means that the states extracted from the body are expressed in the conventional coordinates
	- To update the acceleration model of an object


**Propagated Coordinates**

	The *propagated*, on the other hand, are used to describe the state in the actual differential equations being used. Thus, you will find these elements here:

        - As an output to the ``unprocessed_state_history`` function of a ``Simulator`` object (such as the :class:`~tudatpy.numerical_simulation.SingleArcSimulator` class)

    Internally, Tudat uses the *propagated* state in the following place:

    - As the input/output of the numerical integrator's state derivative funcion

As a user, you will generally only interact with the conventional coordinates, but you will have the choice over which propagated coordinate to use for propagation/integration. Even though you may rarely interact with the propagated coordinates, a judicious choice of formulation of equations of motion (*e.g.* definition of propagated coordinates) can have a significant influence on the quality of your numerical resuls. 



Important To Keep In Mind
-------------------------

Since the conventional coordinates are used to update the environment and accelerations of the bodies, but the propagated coordinates are the ones used in propagation, you can see that whenever the conventional and propagated coordinates differ, there is a need to convert between the two at every time step (or even multiple times, if the time step is divided in multiple steps for integration). Therefore, this leads to a set of extra operations to be perfomed during propagation, which may in turn lead to a longer computation time for a single evaluatuon of the state derivative and/or increased numerical error. However, these aspects are rarely influential.

Another fact to consider, is that sometimes there may be a difference between the size of the conventional and propagates states. For instance, a Cartesian state is expressed with 6 elements, but the USM7 state with 7. This may lead to some confusion when extracting the results, so keep this in mind. In the next section, you can find the size of each propagated type used in Tudat.
