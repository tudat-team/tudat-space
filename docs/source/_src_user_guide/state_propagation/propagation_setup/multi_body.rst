.. _multi_body_dynamics:

===================
Multi-body dynamics
===================

The propagation framework in Tudat is implemented such that any number of bodies may be propagated numerically. Taking the translational dynamics as an example, propagating multiple bodies is achieved simply by extending the list of propagated bodies and central bodies:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

Where the ``acceleration_models`` should contain a set of acceleration models acting upon each propagated body (if one or more of the bodies is omitted from the ``acceleration_models``, no accelerations are assumed to act on this body, without warning or error).

When propagating multiple bodies, the initial states of the bodies need to be provided in a single vector through the ``initial_state`` input (in the example above) to the :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.translational` function. This initial state vector should, in order, contain the initial states of the propagated bodies, w.r.t. their respective central bodies. For the example above, entry 0-5 of the ``initial_state`` should be the initial state of Earth w.r.t. SSB, entry 6-11 Mars w.r.t. SSB, entry 12-17 Sun w.r.t. SSB, and 18-23 Moon w.r.t. SSB. 

The use of a 'hierarchical' system is also supported by Tudat. For instance, one can propagate the Earth and Mars w.r.t. the Sun, the Sun w.r.t. the barycenter, the Moon w.r.t the Earth:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/basic_multi_hierarchy_translational_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

In either case, any and all physical interactions are automatically formulated as required for the specific dynamical system under consideration. Specifically, the use of direct and third-body gravitational accelerations, and the definition of the correct effective gravitational parameter, are automatically handled when creating the acceleration models (see :ref:`available_acceleration_models`)

When propagating multiple bodies simultaneously, acceleration models for each need to be defined (for the case of translational dynamics). See :ref:`acceleration_models_setup` on details how to define this. The initial states that are to be provided to the propagator settings should be in the form of a single vector, with the states of the propagated bodies concatenated. In each of the above examples, for instance, the initial states should be provided as a column vector with 24 entries, with element 0-5 representing the state of the Earth, element 6-11 the state of Mars, 7-17 the state of the Sun, and element 18-23 the state of the Moon. Note that in the second example, where each propagated body has a different central body, the initial state of each body must be defined w.r.t. its own central body. To retrieve the definition of the full state vector, see :ref:`console_output`.
