.. _backwards_incompatibility:

==================================================
Thrust and Aerodynamic Orientation - Code Refactor
==================================================

.. attention::

  This page discusses the non-backwards compatible changes that were introduced in Tudatpy from version 0.7.

.. toctree::
   :titlesonly:
   :hidden:
   :maxdepth: 1

   thrust_refactor/thrust_old
   
The framework in Tudat to calculate inertial thrust direction and aerodynamic guidance was overhauled in mid-2022. The reasons for this were:

* Uninformative error warnings for certain models (primarily: custom thrust directions)
* Inconsistent ways in which a vehicle's orientation is defined (implicitly by both aerodynamic guidance and thrust guidance)
* Unclear interaction between thrust and aerodynamics: both can define a body's orientation, so what happens if you use both?

The refactor has addressed these issues, as well as a number of related points. Most of the changes in functionality have been made 'under the hood', and are not visble to users. However, two important aspects of the interfaces have been modified in a manner which is *not* backwards compatible. If a user accesses the 'old' function, they will be redirected to this page. Below is an overview of what has changes, why, and how to convert your old code to new code.

Specifically, you are likely here because one of two pieces of code is no longer working: the definition of a thrust acceleration, or the definition of aerodynamic guidance. Below, we describe how to modify your old code to the new setup of Tudat, while retaining the identical functionality.

Main modification - vehicle rotation
====================================

The driver behind the lack of backwards compatibility is the following new paradigm:

* **All** methods in which to define a vehicle's orientation (with the exception of the numerical propagation of the vehicle's rotational dynamics) have to happen by *explicitly* setting the vehicle's rotation model. This addresses the issues listed above concerning the old setup, where it was often not clear which setting overrode/interacted with which other model. Currently, a user will know exactly which rotation model is used: they *have* to define it explicitly. This means that 

  * The definition of thrust direction settings, which implicitly define a body-fixed frame, through thrust acceleration settings
  * The definition of an ``AerodynamicGuidance``-derived class (which could only be created and added *after* the aerodynamic acceleration was created....)

are no long supported. Below, we provide a guide on how to convert code that utilizes this to the new setup.

Aerodynamic guidance
====================

In the older version of Tudat, the explicit definition of the aerodynamic angles of attack, sideslip angle, and bank angle (:math:`\alpha`, :math:`\beta` and :math:`\sigma`) had to be done through a user-defined class derived from the ``AerodynamicGuidance``-derived class. This class should then set ``currentAngleOfAttack_`` (and similar for other angles) values in the ``updateGuidance`` function, which was called at each time step.  

Old code
--------

An example of the application of this is in the `example application (old version) <https://github.com/tudat-team/tudatpy-examples/blob/9c658213e661e8afc31738eba04f4973c38c90e2/propagation/reentry_trajectory.py>`_. Specifically, a class was created as follows:


    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/guidance_class_old.py
             :language: python

this class had a number of specific requirements in terms of variable/function naming, inheritance. It was linked to the environment as follows (here, linked to the body named "STS"):

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/guidance_class_old_linking.py          
             :language: python

which could only be done *after* the creation of ``FlightConditions`` of the body "STS" (typically after an aerodynamic acceleration acting on it was created). 

Not only was the above structure specific for aerodynamic orientation, it also had a number of specific ad arbitrary requirements that made it somewhat unwieldy.

Alternatively, the ``set_body_orientation_angles`` and ``set_body_orientation_angle_functions`` of the :class:`tudatpy.numerical_simulation.environment.AerodynamicAngleCalculator` could be called the directly to set either constant, or time-variable aerodynamic angles. This interface is no longer supported, as the :class:`tudatpy.numerical_simulation.environment.AerodynamicAngleCalculator` class is no longer responsible for calculating these angles, it only extracts them from where the *are* calculated: in the vehicle's rotation model.           

New code
--------


In the new version of the code, the definition of a body's orientation through aerodynamic angles is allowed in one way: through the creation of a rotation model for the body. Details are discussed on a :ref:`dedicated page <aerodynamic_orientation>`. The above example can be 'translated' to the new setup as follows 

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/guidance_class_new.py
             :language: python

The main requirement on this new guidance class is the following: it should have a function that takes time as input, and returns a vector containing [:math:`\alpha`, :math:`\beta`, :math:`\sigma`]

It is then linked to the environment as follows:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/guidance_class_new_linking.py          
             :language: python

The function computing the aerodynamic angles in the guidance object (``aerodynamic_guidance_object.getAerodynamicAngles``) is linked to the specific rotation model settings :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`` which defines the rotation model we want.

The above example is discussed in detail on the `entry example page <https://docs.tudat.space/en/stable/_src_getting_started/_src_examples/notebooks/propagation/reentry_trajectory.html>`_. Note that in the above code snippet, we have used a slightly more simplified guidance object than in the example application. They are functionally equivalent, but the code in the example application lends itself better to incorporation into more complex guidance classes. The type of guidance class used in the code snippet and the example application are of the type :ref:`single_custom_models` and :ref:`couple_custom_models`, respectively.

Summary
-------

You may continue to use a very similar guidance class as before, but the class now requires a function that provides [:math:`\alpha`,:math:`\beta`,:math:`\sigma`], with :math:`t` as a input. This function is now linked to the environment not through an aerodynamics-specific function, but through the definition of a rotation model. An example of Python code using the old and new setup is found on our examples repository `here <https://github.com/tudat-team/tudatpy-examples/blob/9c658213e661e8afc31738eba04f4973c38c90e2/propagation/reentry_trajectory.py>`_ and `here <https://github.com/tudat-team/tudatpy-examples/blob/master/propagation/reentry_trajectory.py>`__, respectively.


Thrust acceleration
===================

The changes to the interfaces for defining a thrust acceleration have changed significantly. However, all underlying functionality is intact, and your code can be easily changed from the old to the new version. In both versions, the definition of thrust happens through (typically) separate objects for thrust direction and thrust magnitude. What is different, is *where* these two pieces of information are provided. In the old version:

* Both thrust direction and thrust magnitude settings were passed to the thrust acceleration settings using the :func:`tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_direction_and_magnitude` function. The guide below discusses how to modify your code to the new version if you are using this. 
* Directly defining the thrust vector using the :func:`tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_from_custom_function` or  :func:`tudatpy.numerical_simulation.propagation_setup.acceleration.thrust_and_isp_from_custom_function` function. A new interface for this is under development.

In the new version:

* Thrust magnitude settings are stored in an ``EngineModel`` that is assigned to the vehicle. This same object also defines the body-fixed direction of the thrust
* The thrust direction is obtained by rotating the body-fixed thrust direction (see above line) to the inertial frame using a rotation model assigned to the vehicle. Every option that was previously provided as a "thrust direction settings" has been refactored into a rotation model. Below, we provide a guide with a one-to-one correspondence between each of the old thrust direction settings, and the new rotation model settings.

A detailed guide on using thrust in the new version can be found on a dedicated page on :ref:`thrust_models`. The thrust guide of the old version is also retained under a dedicated page on :ref:`thrust_models_legacy`. Below, we provide a brief on how to convert old code to new code. n example of Python code using the old and new setup is found on our examples repository `here <https://github.com/tudat-team/tudatpy-examples/blob/9c658213e661e8afc31738eba04f4973c38c90e2/propagation/thrust_between_Earth_Moon.py>`__ and `here <https://github.com/tudat-team/tudatpy-examples/blob/master/propagation/thrust_between_Earth_Moon.py>`__, respectively.     

Converting thrust code
----------------------

In the old code, you typically defined a thrust acceleration through:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/thrust_acceleration_old.py          
             :language: python


In the new code, the equivalent functionality is provided through:

    .. tabs::

         .. tab:: Python

          .. literalinclude:: /_src_snippets/simulation/environment_setup/thrust_refactor/thrust_acceleration_new.py          
             :language: python

Here, we have chosen to define the rotation model settings, and create the rotation model, after creating the ``SystemOfBodies``, as discussed  :ref:`here <decorate_empty_body>`.

Details on the functioning of the two pieces of code can be found on the dedicated thrust pages of the new code, and the legacy code (see above). The steps to take:

* Convert your thrust direction settings to rotation model settings. See below for a one-to-one correspondence betwee individual models
* Using the same ``thrust_magnitude_settings`` as before, create an engine model using the :func:`~tudatpy.numerical_simulation.environment_setup.add_engine_model` function. In addition to containing information on the thrust magnitude, the engine object holds information on:

  * The name of the engine (used to link it to the acceleration, see below)
  * The body-fixed thrust direction (for a time-variable body-fixed thrust direction, use the :func:`~tudatpy.numerical_simulation.environment_setup.add_engine_model` instead.)
* Create the thrust acceleration, by specifying which engine(s) should be used in the calculation of the thrust acceleration. Here, the name provided to the engine model is used.

Converting thrust direction settings
------------------------------------

Each of the old thrust direction settings (in the ``propagation_setup.thrust`` submodule) is now reformulated as a rotation model setting. In addition to the inputs from the corresponding thrust direction settings, the rotation model settings require the ``base_frame`` (typically J2000 or ECLIPJ2000), and the ``target_frame`` to be defined. The ``target_frame`` is simply the identifier that the code uses for the body-fixed frame of the vehicle, and may be selected at will by the user.

**propagation_setup.thrust.thrust_from_existing_body_orientation** This option is now moot, *by definition* all thrust models now use the existing body orientation. If you were using this option, now additional action is needed.

**propagation_setup.thrust.custom_thrust_orientation**  This option is now replaced with the equivalent :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_rotation_model` option, with the addition of the frame identiers specified above. It defines the body-fixed orientation in a fully user-defined manner.

**propagation_setup.thrust.custom_thrust_direction**  This option is now replaced with the equivalent :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.custom_inertial_direction_based` option, with the addition of the frame identiers specified above. This rotation model is very typical for the use of thrust: it imposes that a body-fixed axis (now limited to the body-fixed x-axis) is pointed along an arbitrary user-defined inertial direction. As an extension of the old code, this model now allows he *full* rotation to be defined, but defining the free rotation about the body-fixed x-axis (thrust) axis.

**propagation_setup.thrust.thrust_direction_from_state_guidance**  This option is replaced by the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.orbital_state_direction_based`. The inputs are equivalent, with the addition of the frame identiers specified above. This rotation model is a typical example for a basic use of thrust: it imposes that a body-fixed axis (now limited to the body-fixed x-axis) is pointed along its inertial position or velocity vector.  As an extension of the old code, this model now allows he *full* rotation to be defined, but defining the free rotation about the body-fixed x-axis (thrust) axis.








