.. _termination_settings:

==============================
Termination Settings
==============================

The termination settings are a key parameter in the propagation of a body’s orbit, since these will determine the computational time and the size of the output file. Depending on the application, the user may want to end the body propagation according to different criteria. Once the ``termination_settings`` have been defined, the propagation settings are then subsequently created using

.. code-block:: python
	:emphasize-lines: 6

	propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        termination_settings,
        output_variables = dependent_variables_to_save)



Currently, the following termination settings are offered in Tudat:

- Termination once a certain **time** has passed.

	As the name suggests, these settings will cause the propagation to terminate after a certain simulated time has passed. You can set the termination settings as follows:

	.. code-block:: python

		termination_time = 86400.0
		termination_settings = propagation_setup.propagator.time_termination( termination_time )

        where the propagation will terminate once :math:`t=86400`. Note that the termination time is set as the absolute time (in seconds since J2000), not the time since the start of the propagation. Depending on the sign of the time step of the numerical integrator, the termination time will be treated as an upper bound (for positive time step) or lower bound (for negative time step).

        
        Please note that the simulator will normally finish the final time-step, which may cause the termination time to be slightly exceeded. This behaviour can be suppressed by providing the optional input argument ``terminate_exactly_on_final_condition=True``, in which case the final propagation step will be *exactly* on the specified time (note that to reach this final time exactly, state derivative function evaluations beyond the final time may be required by the propagator). 

- Termination once a certain **CPU time** is reached.

	You may want to make sure that the propagation does not exceed a certain computation time. In this case, you can easily set the termination settings as follows:

	.. code-block:: python

		cpu_termination_time = 120.0
		termination_settings = propagation_setup.propagator.cpu_time_termination( cpu_termination_time )

	which will terminate the propagation once your computer has run it for 120 seconds.

- Termination once a **dependent variable** meets a certain criterion.

	The termination variable can be any :ref:`available_dependent_variables`. Below, an example is shown for termination on a given vehicle altitude.

	.. code-block:: python

		termination_variable = propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )
		termination_settings = propagation_setup.propagator.dependent_variable_termination( 
			dependent_variable_settings = termination_variable,
			limit_value = 25.0E3,
			use_as_lower_limit = True)

	The exact termination condition is defined in the ``termination_settings``. The propagation is terminated once the *lower* limit of 25 km in altitude is reached (as the ``use_as_lower_limit`` is set to ``True``). To use the above settings to terminate when an *upper* limit of 25 km is reached, set this boolean to ``False``. 

        Please note that the simulator will normally finish the final time-step, which may cause the termination condition to be slightly exceeded. This behaviour can be suppressed by providing the optional input argument ``terminate_exactly_on_final_condition=True``, in which case the final propagation step will be *almost exactly* on the specified condition (note that to reach this final condition, state derivative function evaluations beyond the final time may be required by the propagator). Reaching the final condition exactly is an iterative process, and very minor deviations from the specified final condition

- Termination once a **user-defined function** returns true.

	You can set a custom function that based on some internal calculations, which will return whether to stop propagation. Your custom function should take the current time as input, and output a Boolean:

	.. code-block:: python

		custom_termination_function = ...
		termination_settings = propagation_setup.propagator.custom_termination( 
			custom_termination_function)

        The ``custom_termination_function`` should be a function pointer taking a float as input (representing time), and returning a boolean as output. The propagation will continue to run, so long as this function returns `False`. 

- Termination once **multiple criteria** are met.

	It may be possible that the user desires to terminate a propagation according several criteria, where such criteria may or may not be fulfilled simulataneously. The constructor for this derived class is:


	.. code-block:: python

		termination_time = 86400.0
		time_termination_settings = propagation_setup.propagator.time_termination( termination_time )

		termination_variable = propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )
		altitude_termination_settings = propagation_setup.propagator.dependent_variable_termination( 
			dependent_variable_settings = termination_variable,
			limit_value = 25.0E3,
			use_as_lower_limit = True)

		cpu_termination_time = 120.0
		cpu_termination_settings = propagation_setup.propagator.cpu_time_termination( cpu_termination_time )

    		termination_settings_list = [time_termination_settings, altitude_termination_settings, cpu_termination_settings ]
		termination_settings = propagation_setup.propagator.hybrid_termination( termination_settings_list, fulfill_single_condition = True )

	By using this setup, the propagation will terminate once *one of the three* constituent termination settings (simulated time, cpu time, altitude) has reached the imposed limit value. The ``fulfill_single_condition`` variable determines whether the propagation terminates once a *single* condition is met (if True, as above) or once *all* conditions must be met (False).

	.. tip::

		When using a dependent variable as termination condition, it is adviced to also include a (cpu) time termination condition, to ensure that your simulation will terminate.






