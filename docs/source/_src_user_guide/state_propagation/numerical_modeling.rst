.. _integrator_setup:

Integrator Setup
=================

The environment and formulation of dynamical equations are now in place. In order to solve these equations you still need to define the numerical integrator settings. These settings specify *how* the equations are solved. In Tudat(Py) you can choose between different types of integrators.


Since the choice of integrator strongly depends on the nature of the dynamical problem and the requirements of the user, there is no 'best' integrator that works in all cases. Details about the different types will **not** be given here; you are referred to existing literature on the topic of numerical integrators. We only show you how to create the integrator settings, given on the following page:

.. toctree::
  :maxdepth: 1

  integrator_setup/settings
