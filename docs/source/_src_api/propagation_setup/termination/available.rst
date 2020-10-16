.. _available_termination_settings:

==============================
Available Termination Settings
==============================

The termination settings are a key parameter in the propagation of a body’s orbit, since these will determine the computational time and the size of the output file. Depending on the application, the user may want to end the body propagation according to different criteria. Currently, the following termination settings are offered in Tudat:

- Termination once a certain **time** has passed.
- Termination once a certain **CPU time** is reached.
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

	The propagation settings are then subsequently created using

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


- Termination once a **user-defined function** returns true.
- Termination once **multiple criteria** are met.





