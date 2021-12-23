.. _dependent_variables:

Dependent Variables
##########################

Dependent variables can be added to the propagation settings by first defining
a list of desired dependent variables, which is supplied as input argument to the
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational`,
:func:`~tudatpy.numerical_simulation.propagation_setup.propagator.rotational`,
or :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass` functions.
Each dependent variable is created via a dedicated factory function. See the example below:


.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

.. note::

   All variables are saved in SI units.

.. seealso::
   You can find a full list of dependent variables that can be saved `in our API documentation <https://tudatpy.readthedocs.io/en/latest/dependent_variable.html#functions>`_.

				
