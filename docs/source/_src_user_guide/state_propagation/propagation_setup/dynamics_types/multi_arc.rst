.. _multi_arc_dynamics:

==============================
Multi- and hybrid-arc dynamics
==============================

Multi-arc dynamics
------------------

For various types of applications, the dynamics of a given body will not be propagated over a single continuous arc, but will be split over several independent propagations that may or may not be overlapping in time, or contiguous in state. A number of examples are:

* Orbit determination of a spacecraft, where the state is typically propagated (and estimated) over a set of (partially overlapping) period of several days, to prevent dynamical model errors from accumulating in the state estimation/
* Propagating spacecraft dynamics only during specific periods of interest. For instance, for a spacecraft like JUICE or Cassini, the user may only be interested in propagating the dynamics of the spacecraft during the flybys of the Jovian/Saturnian moons, without needing a numerical result in the intermediate time periods.

Multi-arc propagation settings are defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.multi_arc` function. For the multi-arc propagation, the primary input is a list of single-arc settings (see :ref:`here <propagation_setup_intro>` for a list of single-arc dynamics types), which define the dynamics type, initial time, initial state, etc. to be used for the separate arcs. The propagations overe the separate single arcs are done almost entirely independently, with a number of (optional) links between the different arcs:

* The processing of the numerical results (in particular, resetting the ephemeris of the body or not, see :ref:`auto_processing`) is defined consistently for each of the arcs in the multi-arc propagation. NOTE : the processing settings in the single-arc propagations are automatically overwritten by the multi-arc processing settings.
* When propagating multi-arc dynamics of the same body or set of bodies over each arc, where subsequent arcs overlap with one another, the initial state of arc :math:`N` *may* de extracted (using interpolatiton) from the numerical results of arc :math:`N-1`, using the ``transfer_state_to_next_arc`` input. In this manner, the propagation is performed over multiple arcs, while still enforcing a continuous numerical solution over the full multi-arc time interval. Additionally, only a single initial state needs to be provided (initial states for any arc other than the first  are ignored, and can be defined arbitrarily)
* There are a number of options to manipulate the console print settings for the separate arcs in a simple manner, as discussed :ref:`here <console_output_multi_arc>`

Hybrid-arc dynamics
-------------------

In addition for certain applications, typically those involving the propagation of the dynamics of natural bodies as well as artificial bodies over longer periods of time, a so-called 'hybrid' arc propagation can be used, in which a number of bodies bodies (typically the natural ones) are propagated over a single arc, and other bosdies (typically the artificial ones) are propagated in a multi-arc fashion. Propagator settings are then defined using the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.hybrid_arc` function. 

An important limitation on this method is:

* The dynamical model of the bodies propagated over a single-arc must be independent of the state of the bodies propagated in a multi-arc fashion (using the example above: the dynamics of the natural bodies must not be perturbed by the artificial bodies)

The hybrid-arc propagation settings consist of a single- and a multi-arc propagation settings object. These are processed and defined independently, with the above being the only constraint on their relative definition. In addition, there are a small number of additional options to manipulate the console print settings for the single- and multi-arc propagation at the same time, as discussed :ref:`here <console_output_multi_arc>`.



