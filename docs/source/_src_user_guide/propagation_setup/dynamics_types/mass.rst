=============
Mass Dynamics
=============

Propagating the mass of a body is typically (but not exclusively) coupled with the use of a :ref:`thrust model <thrust_guidance>`. Defining mass propagation settings is done similarly to the translational and rotational dynamics:

    .. tabs::

         .. tab:: Python

          .. toggle-header:: 
             :header: Required **Show/Hide**

          .. literalinclude:: /_src_snippets/simulation/environment_setup/full_mass_setup.py
             :language: python

         .. tab:: C++

          .. literalinclude:: /_src_snippets/simulation/environment_setup/req_create_bodies.cpp
             :language: cpp

where the final two inputs are optional (see :func:`~tudatpy.numerical_simulation.propagation_setup.propagator.mass`).

The definition of mass rate models is discussed :ref:`here <mass_rate_model_setup>`. For a full description of available functions, see associated pages of `mass-rate models <https://tudatpy.readthedocs.io/en/latest/mass_rate.html>`_ and `thrust models <https://tudatpy.readthedocs.io/en/latest/thrust.html>`_ in the API.
