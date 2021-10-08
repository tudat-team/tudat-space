===========================
Custom environment settings
===========================

When working with a very specific model or application, it may happen that the model you want to use is not implemented in Tudat. If this is the case, we have the option for users to define 'custom' environment models. The use of these custom settings requires the user to define their own function for the specific environment model, as is shown below with a number of examples. Below, you can find a list of the currently supported custom environment models in Tudat:

:func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.custom`

:class:`~tudatpy.numerical_simulation.environment_setup.atmosphere.ExponentialAtmosphereSettings`
:func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.constant_wind_model`
In each case, the user is required to define their own function, with a predefined set of inputs and outputs, which are different for each specific environment model (see API links above). 

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



