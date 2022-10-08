Printing and processing the results
###################################

The results of the numerical propagation are stored in the :ref:`propagation_results`, which can be used to perform further analysis of the simulation, and the details of the propagation process. In addition, there are a number of processing and output steps that Tudat can perform.


.. _auto_processing:

Automatic processing
====================

The results of the numerical propagation are stored in the :ref:`propagation_results`, which can be used to perform further analysis of the simulation, and the details of the propagation process. In addition, Tudat can be set up to automatically use the results of the numerical propagation to update the environment. Specifically:

* Translational dynamics: use the numerical results to update the ephemeris of the body with (using the default) a 6-th order Lagrange interpolation scheme to create a tabulated ephemeris
* Rotational dynamics: use the numerical results to update the rotational ephemeris of the body with (using the default) a 6-th order Lagrange interpolation scheme to create a tabulated rotation model
* Mass dynamics: use the numerical results to update the mass function of the body with (using the default) a 6-th order Lagrange interpolation scheme
* Multi-type dynamics: automatically processes all of the constituent dynamics as listed above
* Custom dynamics: no action

To be able to perform the reset of the ephemeris (or other environment model), the existing ephemeris must be of the suitable type. This means that it must either be a tabulated ephemeris already (in which case the tabulation is reset) or the body must contain no ephemeris (in which case one is created on the fly when creating the dynamics simulator (see AAAA). In cases where a user wants to use a non-tabulated ephemeris for a body, but still use the functionality described here, the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated_from_existing` can be used when :ref:`defining the body settings <override_body_settings>`.

For specific applications, most notably a state estimation, a user may want the numerical solution to *only* be used to reset the environment, while not needing access to the numerical results directly. When this is the case, a setting is provided (see AAAA) to completely delete the numerical results of the propagation after the propagation is performed. When this option is selected, the numerical results 'live on' *only* in the updated environment models, but are no longer available from the :ref:`propagation_results`. This option may be attractive when memory usage of the application is a concern.

For the multi- and hybrid arc propagation, the setting of the numerical results in the environment, and the clearing of the numerical solution, is *always* consistent between all the arcs. As a result, these settings in the constituent single-arc propagation settings is overridden by the settings in the multi- or hybrid-arc propagation settings.

.. _console_output:

Console Output
==============

Tudat provides a range of options on information to be printed to the console *during* the process of the propagation. 

The results of the numerical propagation are stored in the :ref:`propagation_results`, which can be used to perform further analysis of the simulation, and the details of the propagation process. However, Tudat also provides a range of options on information to be printed to the console *during* the process of the propagation. These settings are specified through an `AAAA` object, which is stored in the propagator settings (for a single-arc propagation). Typical examples of information that can be printed to the console are:

* The indices in thee full dependent variable vector (see AAAA) where each separate dependent variable is stored, with a brief text description of the associated dependent variable (printed before the propagation starts)
* The current time and state can be printed *during* the propagation, at a simulation time interval specified by the user
* Total runtime, number of function evaluations of the state derivative, and the reason for the termination of the propagation (printen after the propagation is finished)

In most cases, the separate print settings are defined by a boolean (print this information: yes or no). For specific cases, such as the frequency at which information should be printed to the console during a propagation, are to be provided as a floating point value.

.. _console_output_multi_arc:

Multi-arc output
----------------

For the multi- and hybrid arc simulations, the console output is specified in its constituent single-arc propagaion settings where, in principle, these settings can be different for each arc, and are processed independently. However, a number of additional options are available for printing output to the console for multi- and hybrid-arc propagation:

* For the multi-arc propagation, there is an option to ensure identical print settings for each arc (see AAAAA)
*  For the multi-arc propagation, there is an option to automatically suppress all output for all arcs *except* the first arc. This is typically used in cases where the settings for each arc are largely identical







