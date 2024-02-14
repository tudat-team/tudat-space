##########################
Frequently Asked Questions
##########################

This page covers some frequently asked questions that have been (and are being) gathered over time.

Frequently Asked Questions - Tudat functionality
################################################

Below you can find a number of frequently asked questions on the usage and functionality of Tudat.

How do I retrieve the body properties of a Body object?
=======================================================

If you have created a system of bodies of type `SystemOfBodies <https://py.api.tudat.space/en/latest/environment.html#tudatpy.numerical_simulation.environment.SystemOfBodies>`_ stored in a variable ``bodies`` and want to retrieve certain Body properties from the environment, you can retrieve them by calling (for example): 

.. code-block::

    bodies.get(“Earth”).gravity_field_model.gravitational_parameter

which would return the gravitational parameter of the Earth as used by tudat. A full list of all Body properties you can retrieve can be accessed `here <https://py.api.tudat.space/en/latest/environment.html#tudatpy.numerical_simulation.environment.Body>`_. Note that first the ``gravity_field_model`` environment model is entered before the gravitational parameter is retrieved. A full list of environment models available can be accessed on the `Environment Models page <https://docs.tudat.space/en/latest/_src_user_guide/state_propagation/environment_setup/environment_models.html>`_.

How do I retrieve the orbital period of a Body object?
======================================================

While it is not possible (right now) to directly retrieve the orbital period of a Body object, it is possible to calculate it. This can be done by storing the Keplerian state of a numerically propagated Body as a `dependent variable <https://py.api.tudat.space/en/latest/dependent_variable.html>`_, from which the orbital period can directly be calculated.

Alternatively, if the Body is not numerically propagated, or you prefer not to store the Keplerian state as a dependent variable, this can also be done by accessing the `state <https://py.api.tudat.space/en/latest/environment.html#tudatpy.numerical_simulation.environment.Body.state>`_ property of a Body, which returns its translational state at the current time step in Cartesian elements w.r.t. the global frame origin, with axes along the global frame orientation. Note that if the Body is numerically propagated, this information is retrieved from the propagated state vector. If it is not numerically propagated, it is retrieved from the body’s ephemeris. This state can then be converted to Keplerian elements using the :func:`~tudatpy.astro.element_conversion.cartesian_to_keplerian` function, from which the orbital period can be calculated.

Why are the number of function evaluations the same for fixed-timestep multi-stage integrators?
===============================================================================================

Let’s assume we have a variable-timestep RKF7(8)-integrator. To perform a single variable-timestep, the integrator

* Computes the state derivative at a number of stages
* Computes a single step with the 7th order integrator
* Computes a single step with the 8th order integrator
* Compares the two steps to do the size-control (and, if needed, iterate)

If we were to make use of a *fixed*-timestep RKF7(8)-integrator, *the first step is still the same*. Depending on whether we choose the lower or higher order integrator, the second or third step is taken by the fixed-timestep integrator. Since in the first step the state derivative is already calculated, this results in no difference in function evaluations between the lower and higher order fixed-timestep integrators. Do note that this approach is slightly inefficient as more function evaluations will be taken than what is needed for the lower-order integrator, the additional computation time is however negligible.

How can I create a more detailed gravity field (i.e. higher degree and order spherical harmonic expansion)?
===========================================================================================================

If you wish to create a more detailed gravity field of a Body, this is possible using the :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.from_file_spherical_harmonic` function. As one of the inputs it will take a file path which indicates where the spherical harmonic gravity field file is located. These should be stored in the resources directory. To return the full file path pointing to this gravity file, you can use the :func:`~tudatpy.io.get_gravity_models_path` function. Storing the output from :func:`~tudatpy.numerical_simulation.environment_setup.gravity_field.from_file_spherical_harmonic` under ``file``, you can then update a Body’s gravity field settings by overwriting the default gravity field with ``file``. Make sure to do this *before* creating your environment.

How can I add Spice kernels myself?
=================================== 

A list of default Spice kernels loaded into tudat can be accessed `here <https://py.api.tudat.space/en/latest/spice.html#tudatpy.interface.spice.load_standard_kernels>`_. If you wish to add a Spice kernel that is not loaded into tudat by default, you can do so using the :func:`~tudatpy.interface.spice.load_kernel` function. This takes a file path to the Spice kernel file as input and will load the file into the pool, from which you can now use it as any other kernel. A list of available kernels can be accessed through the `Spice toolkit <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/>`_.


Frequently Asked Questions - Tudat errors
#########################################

Below you can find a number of frequently asked questions on common errors that occur when running a Tudatpy script.

Tudat cannot find data files that it needs
==========================================

The following error (or similar)::

   terminate called after throwing an instance of 'std::runtime_error'

   what(): Data file could not be opened./home/MYNAME/.tudat/resource/earth_orientation/eopc04_14_IAU2000.62-now.txt

   Aborted (core dumped)
   
is caused by the ``tudat-resources`` conda package (which is a dependency of tudat and tudatpy) not being installed properly. You can manually download the missing data, and place them in the directory specified by the error. In the `tudat-resources releases <https://github.com/tudat-team/tudat-resources/releases>`_, select the latest release and under 'assets' download and unpack the ``resource.tar.gz`` in the specified directory. 


Frequently Asked Questions - Installation
#########################################

Below you can find a number of frequently asked questions on the installation of Tudatpy:

I am getting an error 'DLL not found' when importing tudatpy
============================================================

The following error (or similar)::

   from tudatpy.kernel import \
   ImportError: DLL load failed while importing kernel: A dynamic link library (DLL) initialization routine failed.
   
have been known to be caused by virus scanners being overzealous, and seeing tudatpy as unsafe. Check the settings of your virus scanner to ensure that this is not the case.

How can I compile tudat and the tudatpy kernel from source?
===========================================================

Our recommended procedure is to use the `tudat-bundle repository <https://github.com/tudat-team/tudat-bundle/>`_. The README of this repository provides instructions on how to build tudat from source. Some more background can be found under :ref:`using_tudat_source`. 



