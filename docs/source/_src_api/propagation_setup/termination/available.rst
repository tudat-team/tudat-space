.. _available_termination_settings:

==============================
Available Termination Settings
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
        output_variables = dependent_variables_to_save
	)



Currently, the following termination settings are offered in Tudat:

- Termination once a certain **time** has passed.

	As the name suggests, these settings will cause the propagation to terminate after a certain time has passed. Please note that the simulator will finish the final time-step, which may cause the termination time to be slightly overpassed. You can set the termination settings as follows:

	.. code-block:: python

		termination_time = ...
		terminate_exactly_on_final_condition = ... # Boolean

		termination_settings = propagation_setup.propagator.time_termination( termination_time, terminate_exactly_on_final_condition )

- Termination once a certain **CPU time** is reached.

	You may want to make sure that the propagation does not exceed a certain computation time. In this case, you can easily set the termination settings as follows:

	.. code-block:: python

		cpu_termination_time = ...

		termination_settings = propagation_setup.propagator.cpu_time_termination( cpu_termination_time )

- Termination once a **dependent variable** meets a certain criterion.

	The termination variable can be any :ref:`available_dependent_variables`, and is implemented here for vehicle altitude.

	.. code-block:: python

		termination_variable = propagation_setup.dependent_variable.altitude( "Spacecraft", "Earth" )

	The exact termination condition is defined in the ``termination_settings``. The propagation is terminated once the lower limit of 25 km in altitude is reached:

	.. code-block:: python

		termination_settings = propagation_setup.propagator.dependent_variable_termination( 
			dependent_variable_settings = termination_variable,
			limit_value = 25.0E3,
			use_as_lower_limit = True,
			terminate_exactly_on_final_condition = False
		)


- Termination once a **user-defined function** returns true.

	You can set a custom function that based on some internal calculations will return whether to stop propagation. Your custom function should take the current time as input, and output a Boolean:

	.. code-block:: python

		def custom_termination_function( current_time ):

			if current_time ...:
				return True
			else:
				return False

	The propagation settings are then set as follows:

	.. code-block:: python

		current_time = ...

		termination_settings = propagation_setup.propagator.custom_termination( custom_termination_function( current_time ) )


- Termination once **multiple criteria** are met.

	It may be possible that the user desires to terminate a propagation according several criteria, where such criteria may or may not be fulfilled simulataneously. The constructor for this derived class is:

	.. code-block:: python

		termination_settings_list = ... #TODO Dominic
		fulfill_single_condition = True

		termination_settings = propagation_setup.propagator.hybrid_termination( termination_settings_list, fulfill_single_condition )

	The ``fulfill_single_condition`` variable determines whether the propagation terminates once a single condition is met (true) or whether all conditions must be met (false).

	.. tip::

		It is possible to terminate both on time and dependent variable(s).

.. note:: 

	For both CPU Time and Custom termination, the termination cannot be set to occur exactly on the final condition.





