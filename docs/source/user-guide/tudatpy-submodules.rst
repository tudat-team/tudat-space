
.. _tudatpy_submodules:

==================
TudatPy Submodules
==================

TudatPy has its functionality divided into a number of submodules. A brief description of each submodule, as well as a detailed listing of all functions/class in each submodule, can be found on our `API reference <https://py.api.tudat.space/en/latest/>`_. On this page, we give a brief top-level overview of which type of functionality is in which (group of) submodules, and why.

Top-level submodules
====================

The top-level submodules of tudatpy are:

* :doc:`tudatpy.dynamics <numerical_simulation>`: This submodule contains the interfaces for the primary application of Tudatpy: numerical state propagation and estimation. The functionality in this submodule consists of a large number of interconnected elements that work together as a whole. The usability of separate functions/classes in this submodule *outside* of the Tudatpy framework is very limited, and this functionality is typically only used within a Tudatpy numerical simulation. Its further subdivision into submodules is discussed in more detail below.
* :doc:`tudatpy.astro <astro>`: This submodule contains various (semi-)standalone functions for astrodynamics applications, which can be used very well outside of a Tudat application/propagation. Submodules contain lists of frame conversions, element conversion, elementary orbit calculations, *etc.*.
* :doc:`tudatpy.trajectory_design <trajectory_design>`: This submodule contains functionality for the preliminary design of a full (transfer) orbit, using for instance a Multiple Gravity Assist (MGA) or a low-thrust system. It relies on functionality in the ``astro`` submodule. It is largely independent of the ``numerical_simulation`` submodule, but does contain interface functions to allow the preliminary design to be used as an initial guess for a full numerical propagation.
* :doc:`tudatpy.math <math>`:  This submodule contains various functions and classes for purely mathematical operations, such as numerical interpolation, *etc.*.
* :doc:`tudatpy.interface <interface>`: This submodule contains functionality to interface with various external packages which Tudat uses, such as `SPICE <https://naif.jpl.nasa.gov/naif/toolkit.html>`_
* :doc:`tudatpy.plotting <plotting>`: This submodule contains various pieces of functionality to support the easy plotting of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written in Python
* :doc:`tudatpy.util <util>`: This submodule contains various small pieces of functionality to support the easy post-processing of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written in Python
* :doc:`tudatpy.data <data>`: This submodule contains various pieces of functionality for file input-output in Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written partially in Python

The numerical_simulation submodules
===================================

This submodule contains the bulk of the functionality in Tudat, and is subdivided into six submodules, two for functionality related to the environment, propagation and estimation:

* :doc:`tudatpy.dynamics.environment_setup <environment_setup>`/ :doc:`tudatpy.dynamics.environment <environment>`: Functionality related to the physical environment (properties of natural and celestial bodies)
* :doc:`tudatpy.dynamics.propagation_setup <propagation_setup>`/ :doc:`tudatpy.dynamics.propagation <propagation>`: Functionality related to numerical propagation of states (state types, acceleration models, output variables, *etc.*)
* :doc:`tudatpy.numerical_simulation.estimation_setup <estimation_setup>`/ :doc:`tudatpy.numerical_simulation.estimation <estimation>`: Functionality related to state estimation (estimated parameters, observation models, *etc.*)

The distinction between the ``foo`` and ``foo_setup`` libraries is the following:

* The ``numerical_simulation.foo_setup`` submodule contains no actual functionality to perform any calculations. It contains a long list of *settings* that are used to create the models that do the actual calculations. The functionality in this library largely consists of factory functions to create ``Settings`` objects.
* The ``numerical_simulation.foo`` submodule contains the functionality to perform the actual calculations. Typically, the objects in this submodule are created from one or more ``Settings`` objects created in the ``foo_setup`` library. These objects may have various interdependencies which are difficult to manually implement, but straightforward to conceptually define with a string, boolean, etc. For instance: it is easy to state that a set of aerodynamic coefficients dependent on angle of attack (this is defined in the ``environment_setup`` submodule), while it is rather cumbersome to manually extract the angle of attack, and input it to the aerodynamic coefficient during every time step. The objects that do this automatically come from the ``environment`` submodule. In addition, the ``numerical_simulation.foo`` libraries also contain a number of functions that can be used to process propagation results, or extract information from one or more objects in the ``numerical_simulation.foo`` library.
