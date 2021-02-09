.. _convention_propagated_coordinates:

=======================================
Conventional vs. Propagated Coordinates
=======================================

In the description of some of the objects in this part of the wiki about the simulation setup, you may have noticed the use of two names to describe the states of an object. These two names are conventional and propagated, and they describe two slightly different concepts. In this part of the wiki, you will get to know in what ways they differ and how that may affect your application.

.. class:: Conventional Coordinates

	These coordinates are mainly used to describe the state of the object(s) you are propagating outside of integration. This means that you will find *conventional* coordinates in these scenarios:

	- To describe the initial conditions of an object
	- To update the acceleration model of an object
	- To update the environment model of an object; this also means that the states extracted from the body are expressed in the conventional coordinates
	- As an output to the ``state_history`` function of the ``dynamics_simulator`` object


	For sake of completeness, below you will find the conventional coordinates for each propagator type which supports a multiple propagated coordinates:

	- **Translational Motion**: Cartesian coordinates
	- **Rotational Motion**: Quaternions


.. class:: Propagated Coordinates

	The *propagated coordinates*, on the other hand, are mainly used to describe the state of an object inside the integration environment. Thus, you can expect to see these elements here:

	- To describe the equations of motion
	- To describe the state and state derivative during integration
	- As an output to the ``unprocessed_state_history`` function of the ``dynamics_simulator`` object

As a user, you will generally only interact with the conventional coordinates, but you will have the choice over which propagated coordinate to use for propagation/integration. 



Important To Keep In Mind
-------------------------

Since the conventional coordinates are used to update the environment and accelerations of the bodies, but the propagated coordinates are the ones used in propagation, you can see that whenever the conventional and propagated coordinates differ, there is a need to convert between the two at every time step (or even multiple times, if the time step is divided in multiple steps for integration). Thus, this leads to a set of extra stages to be perfomed during propagation, which may in turn lead to a longer computation time. This conversion is also necessary when outputting the conventional state at the end of propagation.

.. note::

	The fact that using a different set of propagated coordinates may lead to a longer computation time is not always true. As a matter of fact, the default translational propagator (i.e., cowell) is considerably slower and less accurate than other propagators, in certain situations. Check out Comparison of Propagator Types to get an idea of the difference in performance among the various translational propagators offered by Tudat.

Another fact to consider, is that sometimes there may be a difference between the size of the conventional and propagates states. For instance, a Cartesian state is expressed with 6 elements, but the USM7 state with 7. This may lead to some confusion when extracting the results, so keep this in mind. In the next section, you can find the size of each propagated type used in Tudat.

For a full list of propagater types in Tudat, see :ref:`translational_dynamics` and :ref:`rotational_dynamics`.
