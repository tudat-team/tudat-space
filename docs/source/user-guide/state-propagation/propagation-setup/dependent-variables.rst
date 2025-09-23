.. _dependent_variables:

Dependent Variables
###################

Dependent variables can be added to the propagation settings by first defining
a list of desired dependent variables, which is supplied as input argument to the
:func:`~tudatpy.dynamics.propagation_setup.propagator.translational`,
:func:`~tudatpy.dynamics.propagation_setup.propagator.rotational`,
:func:`~tudatpy.dynamics.propagation_setup.propagator.mass`,
:func:`~tudatpy.dynamics.propagation_setup.propagator.custom_state` or
:func:`~tudatpy.dynamics.propagation_setup.propagator.multitype`
propagators.

Each dependent variable is created via a dedicated factory function. See the example below for the definition of four separate dependent variables:


.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" )
    ]

this list is then added to one of the propagator setting functions listed above.

You can find a full list of dependent variables that can be saved :doc:`in our API documentation <dependent_variable>`. Note that **all** dependent variables are provided in SI units (meters, radians, kilograms, seconds since J2000).
