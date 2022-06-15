==================
Tudatpy Submodules
==================

Tudatpy has its functionality divided into a number of submodules. A brief description of each submodule, as well as a detailed listing of all functions/class in each submodule, can be found on our `API documentation <https://tudatpy.readthedocs.io>`_ website. On this page, we give a brief top-level overview of which type of functionality is in which (group of) submodules, and why.

Top-level submodules
====================

The top-level submodules of tuduatpy are:

* `tudatpy.numerical_simulation <https://py.api.tudat.space/en/latest/astro.html>`_ This submodule contains the interfaces for the primary application of Tudatpy: numerical state propagation and estimation. The functionality in this submodule consists of a large number of interconnected elements that work together as a whole. The usability of separate functions/classes in this submodule *outside* of the Tudatpy framework is very limited, and this functionaluty is typically only used within a Tudatpy numerical simulation. Its further subdivision into submodules is discussed in more detail below.
* `tudatpy.astro <https://py.api.tudat.space/en/latest/astro.html>`_ This submodule contains various (semi-)standalone functions for astrodynamics applications, which can be used very well outside of a Tudat application/propagation. Submodules contain lists of frame conversions, element conversion, elementary orbit calculations, *etc.*.
* `tudatpy.trajectory_design <https://py.api.tudat.space/en/latest/trajectory_design.html>`_ This submodule contains functionality for the preliminary design of a full (transfer) orbit, using for instance a Muliple Gravity Assist (MGA) or a low-thrust system. It relies of functionality in the ``astro`` submodule. It is largely independent of the ``numerical_simulation`` submodule, but does contain interface functitons to allow the preliminary design to be used as an initial guess for a full numerical propagation.
* `tudatpy.math <https://py.api.tudat.space/en/latest/math.html>`_  This submodule contains various functions and classes for purely mathematical operations, such as numerical interpolation, numerical integration, *etc.*.
* `tudatpy.interface <https://py.api.tudat.space/en/latest/interface.html>`_ This submodule contains functionality to interface with various external packages which Tudat uses, such as `Spice <https://naif.jpl.nasa.gov/naif/toolkit.html>`_
* `tudatpy.plotting <https://py.api.tudat.space/en/latest/plotting.html>`_ This submodule contains various pieces of functionality to support the easy plotting of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written largely in Python
* `tudatpy.util <https://py.api.tudat.space/en/latest/util.html>`_ This submodule contains various small pieces of functionality to support the easy post-processing of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written largely in Python
* `tudatpy.io <https://py.api.tudat.space/en/latest/io.html>`_ This submodule contains various pieces of functionality for file input-output in Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written largely in Python

The numerical_simulation submodules
===================================

This submodule contains the bulk of the functionality in Tudat, and is subdivided into six submodules, two for functionality related to the environment, propagation and estimation:

* `tudatpy.numerical_simulation.environment_setup <https://py.api.tudat.space/en/latest/environment_setup.html>`_/`tudatpy.numerical_simulation.environment <https://py.api.tudat.space/en/latest/environment.html>`_ Functionality related to the physical environment (properties of natural and celestial bodies)
* `tudatpy.numerical_simulation.propagation_setup <https://py.api.tudat.space/en/latest/propagation_setup.html>`_/`tudatpy.numerical_simulation.propagation <https://py.api.tudat.space/en/latest/propagation.html>`_ Functionality related to numerical propagation of states (state types, acceleration models, ouput variables, *etc.*)
* `tudatpy.numerical_simulation.estimation_setup <https://py.api.tudat.space/en/latest/estimation_setup.html>`_/`tudatpy.numerical_simulation.estimation <https://py.api.tudat.space/en/latest/estimation.html>`_ Functionality related to state estimation (estimated parameters, observation models, *etc.*)

The distinction betweenn the ``foo` and ``foo_setup` libraries is the following:

* The ``numerical_simulation.foo_setup`` submodule contains no actual functionality to perform any calculations. It contains a long list of *settings* that are used to create the models that do the actual calculations. The functionality in this library largely consists of factory functions to create ``Settings`` objects.
* The ``numerical_simulation.foo`` submodule contains the functionality to perform the actual calculations. Typically, the objects in this submodule are created from one or more ``Settings`` objects created in the ``foo_setup`` library. These objects may have various interdependencies which are difficult to manually implement, but straightforward to conceptually define with a string, boolean, etc. For instance: it is easy to state that a set of aerodynamic coefficients dependent on angle of attack (this is defined in the ``environment_setup`` submodule), while it is rather cumbersome to manually extract the angle of attack, and input it to the aerodynamic coefficient during every time step. The objects that do this automatically come from the ``environment`` submodule. In addition, the ``numerical_simulation.foo`` libraries also contain a number of functions that can be used to process propagation results, or extract information from one or more objects in the ``numerical_simulation.foo`` library.

The numerical_simulation submodules - an example
================================================

TODO?





