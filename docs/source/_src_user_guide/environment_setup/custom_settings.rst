===============
Custom settings
===============

When working with a very specific model or application, it often happens that the model you want to use is not implemented in Tudat. If this is the case, we have the option for users to define 'custom' models for various models in both the environment and propagation setup modukes. The use of these custom settings requires the user to define their own function for the specific model, as is shown on this page with a number of examples. Below, you can find a list of the currently supported custom environment models in Tudat:

Custom environment models:

* :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.custom`
* :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_constant_temperature`
* :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_four_dimensional_constant_temperature`
* :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_wind_model`
* :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.custom`

Custom propagation models:

* :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.custom_termination`
* :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_orientation`
* :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_direction`
* :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude`
* :func:`~tudatpy.numerical_simulation.propagation_setup.torque.custom`
* :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.custom`
* :func:`~tudatpy.numerical_simulation.propagation_setup.mass_rate.custom`

In each case, the user is required to define their own function, with a predefined set of inputs and outputs, which are different for each specific environment model (see API documentation links above).

For most environment models, the custom model can be fully defined by a standalone function , and can be fully defined by a free function (which may of course call other functions from tudat, other packages or your own code

Example custom model: Neptune ephemeris
=======================================

Tudat has a number of ephemeris models implemented, but there are various cases where a user may want to define their own specific model. Here, we show an example of an ephemeris model that will be both faster, and less accurate, than the models implemented in Tudat. This may be advantageous for preliminary simulation. The model is very simple: a perfectly circular orbit in the :math:`xy-`plane of the ``ECLIPJ2000`` frame.

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

                :language: python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/custom_ephemeris_example.py
             :language: python


         .. tab:: C++
         
In the above example, the user-define function ``neptune_state_function`` is provided when creating the custom ephemeris settings. The only requirement on this custom function is that it takes a single float as argument (representing time since J2000), and returns a 6-dimensional vector (representing the Cartesian state in the frame specified)



Example custom model: Mars atmosphere
=====================================



