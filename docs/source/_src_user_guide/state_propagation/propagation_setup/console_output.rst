.. _printing_processing_results:

###################################
Printing and processing the results
###################################

The results of the numerical propagation are stored in the :ref:`propagation results <propagation_results>`, which can be used to perform further
analysis of the simulation, and the details of the propagation process. In addition, there are a number of processing and
output steps that Tudat can perform before, during and after the propagation. Although such settings can be provided directly
when creating propagator settings (for instance, when calling the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`
function), it is typically more convenient to modify these settings afterwards:

.. code-block:: python

    propagator_settings = propagator.translational( ... )
    console_print_settings = propagator_settings.print_settings
    post_processing_settings = propagator_settings.processing_settings

where, the resulting settings object for console printing and post-processing are of type
:class:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings` and
:class:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings`
(with derived class :class:`~tudatpy.numerical_simulation.propagation_setup.SingleArcsPropagatorProcessingSettings`
for single-arc propagation), respectively. Below, the options available in both these settings objects are described in more
detail.

.. _auto_processing:

Automatic processing
====================

Retrieving the results of the numerical propagation is discussed in detail :ref:`here <propagation_results>`.
In addition to returning data for further analysis by the user, Tudat can be set up to automatically use
the results of the numerical propagation to update the environment upon the successful completion of the propagation.
This option can be toggled using the boolean attribute :attr:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings.set_integrated_result` of
the :class:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings` class:

.. code-block:: python

    propagator_settings = propagator.translational( ... )
    propagator_settings.processing_settings.set_integrated_result = True

Specifically, this will result in:

* Translational dynamics: use the numerical results to update the ephemeris of the body with (using the default)
  a 6-th order Lagrange interpolation scheme to create a tabulated ephemeris
* Rotational dynamics: use the numerical results to update the rotational ephemeris of the body with (using the default)
  a 6-th order Lagrange interpolation scheme to create a tabulated rotation model
* Mass dynamics: use the numerical results to update the mass function of the body with (using the default)
  a 6-th order Lagrange interpolation scheme
* Multi-type dynamics: automatically processes all of the constituent dynamics as listed above
* Custom dynamics: no action

To be able to perform the reset of the ephemeris (or other environment model), the existing ephemeris must be of the suitable type.
This means that it must either be a tabulated ephemeris already (in which case the tabulation is reset) or the body must contain no ephemeris
(in which case one is created on the fly when :ref:`creating the dynamics simulator <running_simulation>`.

In cases where a user wants to use a
non-tabulated ephemeris for a body, but still use the functionality described here to reset the ephemeris later on, the ephemeris type of the
body can be redefined using :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated_from_existing`
when :ref:`defining the body settings <override_body_settings>`. In essence, this converts any ephemeris into a tabulated ephemeris,
where the tabulated ephemeris is populated by states from the original (non-tabulated) ephemeris.

For specific applications, most notably a state estimation, a user may want the numerical solution to *only* be used to reset the environment,
while not needing access to the numerical results directly.
To enable this behavious, the boolean attribute
:attr:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings.clear_solution` of
the :class:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings` class is provided.
When set to try, the numerical results of the propagation are completely deleted after the propagation is performed.
When this option is selected, the numerical results 'live on' *only* in the updated environment models,
but are no longer available from the :ref:`propagation results <propagation_results>`.
This option may be attractive when memory usage of the application is a concern.

Multi- and hybrid-arc considerations
------------------------------------

For the multi- and hybrid arc propagation, the setting of the numerical results in the environment,
and the clearing of the numerical solution, is *always* consistent between all the arcs.
As a result, these settings in the constituent single-arc propagation settings is overridden
by the settings in the multi- or hybrid-arc propagation settings.

To reset the dynamics of a body with the results of a multi-arc propagation (e.g. if the
:attr:`~tudatpy.numerical_simulation.propagation_setup.PropagatorProcessingSettings.set_integrated_result` option is set to true),
the ephemeris of this body must be a multi-arc ephemeris. If the body has no ephemeris before propagation,
one is created on the fly when :ref:`creating the dynamics simulator <running_simulation>`.
In cases where a user wants to use a
single-arc ephemeris for a body, but still use the functionality described here to reset the ephemeris from multi-arc results later on,
the ephemeris type can be forced to multi-arc by using the
:attr:`~tudatpy.numerical_simulation.propagation_setup.ephemeris.EphemerisSettings.make_multi_arc_ephemeris` attribute of the
:class:`~tudatpy.numerical_simulation.propagation_setup.ephemeris.EphemerisSettings` when :ref:`defining the body settings <override_body_settings>`.
For example, to reset the ephemeris of the Earth from a multi-arc propagation result, the following can be used to permit this:

.. code-block:: python

   # Create body settings
   body_settings = environment_setup.get_default_body_settings( ... )
   body_settings.get("Earth").ephemeris_settings.make_multi_arc_ephemeris = True



.. _console_output:

Console Output
==============

Tudat also provides a range of options on information to be printed to the console *during* the process of the propagation.
These settings are specified through an :class:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings` object.
Typical examples of information that can be printed to the console are:

* The indices in the full dependent variable vector
  (:attr:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.print_dependent_variable_indices`;
  see :ref:`dependent_variables`) where each separate dependent variable is stored,
  with a brief text description of the associated dependent variable (printed before the propagation starts)
* The current time and state can be printed *during* the propagation
  (:attr:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.state_print_interval`),
  at a simulation time interval specified by the user
* Total runtime, number of function evaluations of the state derivative, and the reason for the termination of the propagation
  (printed after the propagation is finished; see
  :attr:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.print_propagation_clock_time`,
  :attr:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.print_number_of_function_evaluations` and
  :attr:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.print_termination_reason`)

In most cases, the separate print settings (as attributes of the :class:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings` class)
are defined by a boolean (print this information: yes or no).
For specific cases, such as the interval at which information should be printed to the console during a propagation,
are to be provided as a floating point value. To enable all console printing that can be defined by a boolean, the
:func:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.enable_all_printing` function can be used.
To disable *all* console printing, us the :func:`~tudatpy.numerical_simulation.propagation_setup.PropagationPrintSettings.disable_all_printing`
function.

An example of defining console output is:

.. code-block:: python

    propagator_settings = propagator.translational( ... )
    console_print_settings = propagator_settings.print_settings
    console_print_settings.print_state_indices = True
    console_print_settings.print_dependent_variable_indices = True
    console_print_settings.print_propagation_clock_time = True
    console_print_settings.print_termination_reason = True
    console_print_settings.print_number_of_function_evaluations = True
    
which will result in the following terminal output (for a specific script propagating dynamics of Delfi C-3 w.r.t. Earth):

.. code-block:: python

   ===============  STARTING SINGLE-ARC PROPAGATION  ===============

   PROCESSED STATE VECTOR CONTENTS:
   [Vector entries], content description
   [0:5], Translational state of body Delfi-C3 w.r.t. Earth

   DEPENDENT VARIABLE VECTOR CONTENTS:
   [Vector entries], content description
   [0:2], Total acceleration in inertial frame of Delfi-C3
   [3:8], Kepler elements of Delfi-C3 w.r.t. Earth

   PROPAGATION FINISHED.
   Total Number of Function Evaluations: 43201
   Total propagation clock time: 2.94223 seconds
   Termination reason: Propagation successful; termination condition exceeded

   =================================================================


.. _console_output_multi_arc:

Multi- and hybrid-arc console output
------------------------------------

For the multi- and hybrid arc simulations, the console output is specified in its constituent single-arc propagation settings where,
in principle, these settings can be different for each arc, and are processed independently.
However, a number of additional options are available for printing output to the console for multi- and hybrid-arc propagation,
in the :class:`~tudatpy.numerical_simulation.propagation_setup.MultiArcPropagatorProcessingSettings` and
:class:`~tudatpy.numerical_simulation.propagation_setup.HybridArcPropagatorProcessingSettings` classes.

* For the multi-arc propagation, there is an option to ensure identical print settings for each arc (see :attr:`~tudatpy.numerical_simulation.propagation_setup.MultiArcPropagatorProcessingSettings.set_consistent_print_settings`)
* For the multi-arc propagation, there is an option to automatically suppress all output for all arcs *except* the first arc (see :attr:`~tudatpy.numerical_simulation.propagation_setup.MultiArcPropagatorProcessingSettings.print_first_arc_only`)
  This is typically used in cases where the settings for each arc are largely identical







