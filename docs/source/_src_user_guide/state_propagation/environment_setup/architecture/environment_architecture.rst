.. _environment_architecture:

==================================
Environment - Overall Architecture
==================================

On this page, we give an overview of the top-level software architecture of the environment models in Tudat, primarily the :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` class that defines a set of bodies, the :class:`~tudatpy.numerical_simulation.environment.Body` class that defines a single body, and the various classes that define the specific environment models. Since the underlying code is written in C++, in various places we will limit ourselves to the C++ implementation. Wherever possible, we will provide links to the Tudatpy API where the classes/functions that are discussed are also exposed to Python.

Top-level architecture
======================

An overview of the architecture of the Tudat environment is given in the figure below (TODO). 

* The environment is defined by a single :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` object.
* The :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` contains a list of :class:`~tudatpy.numerical_simulation.environment.Body` objects, each of which represents a single natural or artificial body, and contains all of this body's properties. In the C++ code, each body is stored as a ``shared_ptr< Body >``. Every body is assigned a unique name by which it can be retrieved. A body can be extracted using the :func:`~tudatpy.numerical_simulation.environment.SystemOfBodies.get` functionn.
* Each :class:`~tudatpy.numerical_simulation.environment.Body` object contains a number of environment models (see :ref:`available_environment_models` for a complete list). By default, each of these objects is initialized as a ``nullptr``, and is only assigned when specified during the creation of the body (:ref:`TODO`) or if added after the creation of the body (:ref:`TODO`).

Interdependencies of environment models
=======================================

Updating the environment during propagation
===========================================



