.. _custom_models:

=============
Custom models
=============

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   custom_models/environment_during_propagation

When working with a very specific model or application, it often happens that the model you want to use is not implemented in Tudat. Two important examples are:

* :ref:`Aerodynamic models and guidance <aerodynamic_models>`
* :ref:`Thrust models and guidance <thrust_models>`

If this is the case, we have the option for users to define 'custom' models for various models in both the environment and propagation setup modules. The use of these custom settings requires the user to define their own function for the specific model, as is shown on this page with a number of examples. Below, you can find a list of the currently supported custom environment models in Tudat. In most cases, the input to the custom function is the current time *only*. In case the user wants to define other state/environment dependencies, these can be implemented using a user-defined custom class, as shown below. Custom functions that have additional dependencies are noted explicitly below. The *output* of the custom function will differ per model type (*e.g.* density custom model: float output; state custom model: vector output), and are specified in the API entries that are linked to.

Custom environment models:

* Custom aerodynamic coefficients (with supported dependencies from :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientsIndependentVariables`) :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.custom_aerodynamic_force_coefficients` or :func:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.custom_aerodynamic_force_and_moment_coefficients` (only force, and force and moment coefficients, respectively)
* Custom atmospheric density model (function of time only) :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_constant_temperature`
* Custom atmospheric density model (function of position and time) :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_four_dimensional_constant_temperature` *Note:* this custom function has current time, altitude, latitude and longitude as input.
* Custom wind model: :func:`~tudatpy.numerical_simulation.environment_setup.atmosphere.custom_wind_model`
* Custom ephemeris: :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.custom_ephemeris`
* Custom body orientation :func:`~tudatpy.numerical_simulation.propagation_setup.rotation.custom_rotation_model`
* Custom inertial direction (typical for basic thrust guidance) :func:`~tudatpy.numerical_simulation.propagation_setup.rotation.custom_inertial_direction_based`

Custom propagation models:

* Custom thrust magnitude :func:`~tudatpy.numerical_simulation.propagation_setup.thrust.custom_thrust_magnitude`
* Custom torque :func:`~tudatpy.numerical_simulation.propagation_setup.torque.custom_torque`
* Custom acceleration :func:`~tudatpy.numerical_simulation.propagation_setup.acceleration.custom_acceleration`
* Custom mass rate :func:`~tudatpy.numerical_simulation.propagation_setup.mass_rate.custom_mass_rate`
* Custom state :func:`~tudatpy.numerical_simulation.propagation_setup.propagation.custom_state` *Note:* this custom function has current time, and the current custom state, as input
* Custom termination setting :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.custom_termination`  *Note:* this custom function takes no inputs, if the current time is needed, it can be retrieved from the :attr:`~tudatpy.numerical_simulation.environment.SystemOfBodies.current_time` attribute of the :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`
* Custom dependent variable :func:`~tudatpy.numerical_simulation.propagation_setup.dependent_variable.custom_dependent_variable` *Note:* this custom function takes no inputs, if the current time is needed, it can be retrieved from the :attr:`~tudatpy.numerical_simulation.environment.SystemOfBodies.current_time` attribute of the :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies`

In each case, the user is required to define their own function, with a predefined set of inputs and outputs, which are different for each specific environment model (see API documentation links above). We can distinguish (roughly) three different ways in which to provide such custom functions to Tudat:

* As a Python free function, which is responsible for calculating a single custom model
* As a member function of a Python class, which is responsible for calculating a single custom model
* As a member function of a Python class, which is responsible for calculating a multiple custom model

The latter choice permits complex guidance algorithms to be implemented, in which (for instance) the algorithm for the control surface deflection, thrust magnitude and body-fixed thrust direction (thrust vector control) are calculated in a coupled manner.

For most environment models, the custom model can be fully defined by a standalone function , and can be fully defined by a free function (which may of course call other functions from tudat, other packages or your own code. A custom function will, in numerous cases, have to depend on properties of bodies (states, altitude, density, etc.). How to access such properties of the environment *during* the propagation is described on the page on :ref:`environment_during_propagation`.

Custom model, free function
===========================

Here, we show an example of an ephemeris model that will be both faster, and less accurate, than the models implemented in Tudat. This may be advantageous for preliminary simulation. The model is very simple: a perfectly circular orbit in the :math:`xy-`plane of the ``ECLIPJ2000`` frame.

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/custom_ephemeris_example.py
             :language: python

 
In the above example, the user-define function ``neptune_state_function`` is provided when creating the custom ephemeris settings. The only requirement on this custom function is that it takes a single float as argument (representing time since J2000), and returns a 6-dimensional vector (representing the Cartesian state in the frame specified), as can be seen in the :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.custom` API entry.

.. _single_custom_models:

Custom model (single), class member
===================================

Below, a skeleton is given for a custom class for the calculation of the thrust magnitude.

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/custom_class_single.py
             :language: python

         
This setup allows the guidance model to directly access any of the properties of the bodies named 'Earth' and 'Vehicle', which were set as class attributes of the ``SimpleCustomGuidanceModel`` class (note: the inputs to the constructor, and the manner in which they are used is entirely up to the user, here we give just one example).
       
The custom thrust magnitude model can then be used as follows to define the thrust magnitude that is to be exerted by an engine:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/custom_thrust_magnitude_example.py
             :language: python

.. _couple_custom_models:

Custom model (multiple), class member
=====================================

Below, a skeleton is given for a custom class for the calculation of both thrust magnitude and aerodynamic angles.

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/custom_class_multiple.py
             :language: python

         
Here, we see a different setup compared to the previous case. There is a single function, named ``update_guidance`` that calculates both the thrust magnitude and the aerodynamic angles. This allows the calculation of the two models to be coupled, which is required for many more advanced applications. The two functions ``getAerodynamicAngles`` and ``getThrustMagnitude`` are then linked to the environment as follows:

    .. tabs::

         .. tab:: Python
         
          .. literalinclude:: /_src_snippets/simulation/environment_setup/coupled_thrust_aerodynamics_example.py
             :language: python


In setting up the custom guidance class, we now need to take care of one crucial point: even though data is retrieved from the object *twice* per function evaluation of the state derivative, the calculation should only be done *once*. Since it is often difficult to predict which of the custom functions will be called first, we use a different setup: defining a ``current_time`` member variable, and letting the code check whether an update needs to be done. This is achieved as follows:

* After the guidance function is evaluated, the class member time is set to the input time, and the guidance is not evaluated a second time during the same state derivative function evaluation
* At the very start of a state derivative function evaluation, the ``update_guidance`` function is called with a NaN input (done by each custom function) signalling that a new function evaluation has started, and the class needs to recompute the guidance. This is done to support integrators such as the RK4 integrator, where two successive state derivatives are evaluated using the same time, but different states
* If the current time of the class is NaN, the guidance is by definition recomputed when called

