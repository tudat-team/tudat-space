.. _available_dependent_variables:

Saving Dependent Variables
##########################

All variables are saved in SI units. Dependent variables can be added to the propagation settings by first defining a list of desired dependent variables.


.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

Then, add this list to the :ref:`propagating settings <propagator_setup>`, through the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`, :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational` or :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass` functions.

You can find a full list of dependent variables that can be saved `in our API <https://tudatpy.readthedocs.io/en/latest/dependent_variable.html#functions>`_.

				