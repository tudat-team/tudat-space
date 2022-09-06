.. _dependent_variables:

Dependent Variables
##########################

Dependent variables can be added to the propagation settings by first defining
a list of desired dependent variables, which is supplied as input argument to the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`,
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.`,
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass`
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.custom_state` or
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.multitype`

Each dependent variable is created via a dedicated factory function. See the example below for the definition of four separate dependent variables:


.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

this list is then added to one of the propagator setting functions listed above.

You can find a full list of dependent variables that can be saved `in our API documentation <https://tudatpy.readthedocs.io/en/latest/dependent_variable.html#functions>`_. Notet that **all** dependent variables are porivded in SI units (meters, radians, kilograms, seconds since J2000).
