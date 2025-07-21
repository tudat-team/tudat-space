.. _faq:

##########################
Frequently Asked Questions
##########################

.. contents:: Content of this page
   :local:

This page covers some frequently asked questions that have been (and are being) gathered over time.

Tudat functionality
################################################

Below you can find a number of frequently asked questions on the usage and functionality of Tudat.

How do I retrieve the body properties of a Body object?
=======================================================

If you have created a system of bodies of type :class:`~tudatpy.dynamics.environment.SystemOfBodies` stored in a variable ``bodies`` and want to retrieve certain Body properties from the environment, you can retrieve them by calling (for example):

.. code-block:: python

   bodies.get("Earth").gravity_field_model.gravitational_parameter

which would return the gravitational parameter of the Earth as used by tudat. A full list of all Body properties you can retrieve can be accessed from the :class:`~tudatpy.dynamics.environment.Body` class. Note that first the ``gravity_field_model`` environment model is entered before the gravitational parameter is retrieved. A full list of environment models available can be accessed on the :ref:`Environment Models page <environment_model_overview>`.

How do I retrieve the orbital period of a Body object?
======================================================

While it is not possible (right now) to directly retrieve the orbital period of a Body object, it is possible to calculate it. This can be done by storing the Keplerian state of a numerically propagated Body as a :doc:`dependent_variable`, from which the orbital period can directly be calculated.

Alternatively, if the Body is not numerically propagated, or you prefer not to store the Keplerian state as a dependent variable, this can also be done by accessing the :attr:`~tudatpy.dynamics.environment.Body.state` property of a Body, which returns its translational state at the current time step in Cartesian elements w.r.t. the global frame origin, with axes along the global frame orientation. Note that if the Body is numerically propagated, this information is retrieved from the propagated state vector. If it is not numerically propagated, it is retrieved from the body's ephemeris. This state can then be converted to Keplerian elements using the :func:`~tudatpy.astro.element_conversion.cartesian_to_keplerian` function, from which the orbital period can be calculated.

Why are the number of function evaluations the same for fixed-timestep multi-stage integrators?
===============================================================================================

Let's assume we have a variable-timestep RKF7(8)-integrator. To perform a single variable-timestep, the integrator

* Computes the state derivative at a number of stages
* Computes a single step with the 7th order integrator
* Computes a single step with the 8th order integrator
* Compares the two steps to do the size-control (and, if needed, iterate)

If we were to make use of a *fixed*-timestep RKF7(8)-integrator, *the first step is still the same*. Depending on whether we choose the lower or higher order integrator, the second or third step is taken by the fixed-timestep integrator. Since in the first step the state derivative is already calculated, this results in no difference in function evaluations between the lower and higher order fixed-timestep integrators. Do note that this approach is slightly inefficient as more function evaluations will be taken than what is needed for the lower-order integrator, the additional computation time is however negligible.

How can I create a more detailed gravity field (i.e. higher degree and order spherical harmonic expansion)?
===========================================================================================================

If you wish to create a more detailed gravity field of a Body, this is possible using the :func:`~tudatpy.dynamics.environment_setup.gravity_field.from_file_spherical_harmonic` function. As one of the inputs it will take a file path which indicates where the spherical harmonic gravity field file is located. These should be stored in the resources directory. To return the full file path pointing to this gravity file, you can use the :func:`~tudatpy.data.get_gravity_models_path` function. Storing the output from :func:`~tudatpy.dynamics.environment_setup.gravity_field.from_file_spherical_harmonic` under ``file``, you can then update a Body's gravity field settings by overwriting the default gravity field with ``file``. Make sure to do this *before* creating your environment.

How can I add SPICE kernels myself?
=================================== 

A list of SPICE kernels can be loaded using the :func:`~tudatpy.interface.spice.load_standard_kernels` function. If you wish to add a SPICE kernel that is not loaded into tudat by default, you can do so using the :func:`~tudatpy.interface.spice.load_kernel` function. This takes a file path to the SPICE kernel file as input and will load the file into the pool, from which you can now use it as any other kernel. A list of available kernels can be accessed through the `SPICE toolkit <https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/>`_.


Tudat errors
#########################################

Below you can find a number of frequently asked questions on common errors that occur when running a Tudatpy script.

Tudat cannot find data files that it needs
==========================================

The following error (or similar)::

   terminate called after throwing an instance of 'std::runtime_error'

   what(): Data file could not be opened./home/MYNAME/.tudat/resource/earth_orientation/eopc04_14_IAU2000.62-now.txt

   Aborted (core dumped)
   
or::

   SPICE(NOSUCHFILE) --
   The attempt to load
   "./home/MYNAME/.tudat/resource/spice_kernels/codes_300ast_20100725.tf" by the
   routine FURNSH failed. It could not be located.
   A traceback follows.  The name of the highest level module is first.
   furnsh_c --> FURNSH --> ZZLDKER
   
is caused by the ``tudat-resources`` conda package (which is a dependency of tudatpy) not being installed properly, or being outdated. You can manually download the missing data, and place them in the directory specified by the error. In the `tudat-resources releases <https://github.com/tudat-team/tudat-resources/releases>`_, select the latest release and under 'assets' download and unpack the ``resource.tar.gz`` in the specified directory.


Installation
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

You can compile our `tudatpy repository <https://github.com/tudat-team/tudatpy/>`_ repository easily using a ``build.py`` file we've provided. The README of this repository provides complete instructions on how to build tudat from source. Some more background can be found under :ref:`using_tudat_source`.

Tudat(Py) is not updating to the latest version in my conda environment, how can I solve this?
==============================================================================================

This is a recurring issue that we do not yet know how to solve properly. To get the latest version, create a new conda environment using the steps in :ref:`getting_started_installation`. To do so, you must either first delete your current conda environment, or create one with a new name by change the name in the ``environment.yaml`` file to something other than ``tudat-space``.

