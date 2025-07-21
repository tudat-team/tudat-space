.. _environment_architecture:

==================================
Environment - Overall Architecture
==================================

On this page, we give an overview of the top-level software architecture of the environment models in Tudat, primarily the :class:`~tudatpy.dynamics.environment.SystemOfBodies` class that defines a set of bodies, the :class:`~tudatpy.dynamics.environment.Body` class that defines a single body, and the various classes that define the specific environment models. Since the underlying code is written in C++, in various places we will limit ourselves to the C++ implementation. Wherever possible, we will provide links to the Tudatpy API where the classes/functions that are discussed are also exposed to Python.

Top-level architecture
======================

An overview of the architecture of the Tudat environment is given in the figure below (TODO). 

* The environment is defined by a single :class:`~tudatpy.dynamics.environment.SystemOfBodies` object.
* The :class:`~tudatpy.dynamics.environment.SystemOfBodies` contains a list of :class:`~tudatpy.dynamics.environment.Body` objects, each of which represents a single natural or artificial body, and contains all of this body's properties. In the C++ code, each body is stored as a ``shared_ptr< Body >``. Every body is assigned a unique name by which it can be retrieved. A body can be extracted using the :meth:`~tudatpy.dynamics.environment.SystemOfBodies.get` method.
* Each :class:`~tudatpy.dynamics.environment.Body` object contains a number of environment models (see :ref:`environment_model_overview` for a complete list). By default, each of these objects is initialized as a ``nullptr``, and is only assigned when specified during the creation of the body (:ref:`create_bodies_from_settings_first`), or when added after the creation of the body (:ref:`decorate_empty_body`).

As discussed :ref:`here <single_propagation_evaluation>`, the properties in the environment get updated to the current time and state of the numerical integration at the start of every function evaluation. Only those properties that are relevant for the propagation being performed are updated. Interaction with the environment during the propagation is described in more detail :ref:`here <environment_during_propagation>`


Interdependencies of environment models
=======================================

TODO





