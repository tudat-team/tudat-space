
.. _tudatpy_submodules:

==================
TudatPy Submodules
==================

TudatPy has its functionality divided into a number of submodules. A brief description of each submodule, as well as a detailed listing of all functions/class in each submodule, can be found on our `API reference <https://py.api.tudat.space/en/latest/>`_. On this page, we give a brief top-level overview of which type of functionality is in which (group of) submodules, and why.

Top-level submodules
====================

The top-level submodules of tudatpy are:

* :doc:`tudatpy.dynamics <dynamics>`: This submodule contains the interfaces for one of core application of Tudatpy: numerical state propagation. The functionality in this submodule consists of a large number of interconnected elements that work together as a whole. The usability of separate functions/classes in this submodule *outside* of the Tudatpy framework can be limited, and this functionality is typically only used within a Tudatpy numerical simulation. Its further subdivision into submodules is discussed in more detail below.
* :doc:`tudatpy.estimation <estimation>`: This submodule contains the interfaces for the other core application of Tudatpy: numerical state and parameter estimation. As with the ``dynamics`` module, the functionality in this submodule consists of a large number of interconnected elements that work together as a whole. Moreover, the ``estimation`` submodule relies heavily on the ``estimation`` submodule.
* :doc:`tudatpy.astro <astro>`: This submodule contains various (semi-)standalone functions for astrodynamics applications, which can be used very well outside of a Tudat application/propagation. Submodules contain lists of frame conversions, element conversion, elementary orbit calculations, *etc.*.
* :doc:`tudatpy.trajectory_design <trajectory_design>`: This submodule contains functionality for the preliminary design of a full (transfer) orbit, using for instance a Multiple Gravity Assist (MGA) or a low-thrust system. It relies on functionality in the ``astro`` submodule. It is largely independent of the ``dynamics`` and ``estimation`` submodule, but does contain interface functions to allow the preliminary design to be used as an initial guess for a full numerical propagation.
* :doc:`tudatpy.math <math>`:  This submodule contains various functions and classes for purely mathematical operations, such as numerical interpolation, *etc.*.
* :doc:`tudatpy.interface <interface>`: This submodule contains functionality to interface with various external packages which Tudat uses, such as `SPICE <https://naif.jpl.nasa.gov/naif/toolkit.html>`_
* :doc:`tudatpy.plotting <plotting>`: This submodule contains various pieces of functionality to support the easy plotting of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written in Python
* :doc:`tudatpy.util <util>`: This submodule contains various small pieces of functionality to support the easy post-processing of results generated with Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written in Python
* :doc:`tudatpy.data <data>`: This submodule contains various pieces of functionality for file input-output in Tudatpy. Unlike most of the main Tudatpy submodules (which are written in C++, and exposed to Python), this submodule is written partially in Python

The dynamics and estimation submodules
======================================

The dynamics and estimation submodules contain the core propagation and estimation functionality in Tudat, and is each subdivided into  a number of submodules. They are structured in a similar manner, with their submodules divided between ``foo`` and ``foo_setup`` libraries. For instance:

* :doc:`tudatpy.dynamics.environment_setup <environment_setup>`/ :doc:`tudatpy.dynamics.environment <environment>`: Functionality related to the physical environment (properties of natural and celestial bodies)
* :doc:`tudatpy.dynamics.propagation_setup <propagation_setup>`/ :doc:`tudatpy.dynamics.propagation <propagation>`: Functionality related to numerical propagation of states (state types, acceleration models, output variables, *etc.*)
* :doc:`tudatpy.estimation.observable_models_setup <observable_models_setup>`/ :doc:`tudatpy.estimation.observable_models <observable_models>`: Functionality related to observation models (objects that allow calculation of range, Doppler, angular position etc.)

The distinction between the ``foo`` and ``foo_setup`` libraries is the following:

* The ``dynamics.foo_setup``/``estimation.foo_setup`` submodule contains no actual functionality to perform any calculations. It contains a long list of *settings* that are used to create the models that do the actual calculations. The functionality in this library largely consists of factory functions to create ``Settings`` objects.
* The ``dynamics.foo``/``estimation.foo`` submodule contains the functionality to perform the actual calculations. Typically, the objects in this submodule are created from one or more ``Settings`` objects created in the ``foo_setup`` library. These objects may have various interdependencies which are difficult to manually implement, but straightforward to conceptually define with a string, boolean, etc. For instance: it is easy to state that a set of aerodynamic coefficients dependent on angle of attack (this is defined in the ``environment_setup`` submodule), while it is rather cumbersome to manually extract the angle of attack, and input it to the aerodynamic coefficient during every time step. The objects that do this automatically come from the ``environment`` submodule. In addition, the ``dynamics.foo``/``estimation.foo`` libraries also contain a number of functions that can be used to process propagation and estimation results, or extract information from one or more objects in the ``dynamics.foo``/``estimation.foo``  modules.

Finally, the objects that perform the actual calculations are group in the :doc:`simulation` module and :doc:`estimation_analysis` submodules (for dynamics and estimation, respectively). There, the creation and implementation of objects that perform propagation of states and variational equations, and the state and parameter estimation from tracking data, can be found.
