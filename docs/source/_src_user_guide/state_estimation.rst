******************
State Estimation
******************

In this section, we discuss the functionality that is required for state estimation in TudatPy. Before starting this section, make sure to go through our page on :ref:`state_propagation_intro`, since the state *estimation* function requires the full functionality from state *propagation*.

Estimation Inputs
=================

In addition to the inputs required for state propagation, we need the following input types:

- **Parameter setup**: definition of the parameters that are to be estimated, as discussed :ref:`here <parameter_settings>` in the context of variational equation propagation
- **Link end setup**: define the stations/spacecraft involved in an observation, and define their role for a particular observable (receiver, transmitter, *etc.*)
- **Observation model setup**: define the type and properties of a given (idealized) observation model, such as range, Doppler, *etc.*
- **Simulating observations** OR **Loading observations**: depending on whether you are considering estimation in a simulated environment (in which case you simulate the observables in TudatPy) or using real data (in which case you load them from files), you must create/load observations, and define properties such as times, noise, *etc.*.
- **Estimation settings**: define the *a priori* knowledge, convergence criteria, *etc.*

.. toctree::
   :titlesonly:
   :maxdepth: 1

   state_estimation/link_ends
   state_estimation/observation_model_setup
   state_estimation/observation_simulation


Simulation/Analysis & Output
============================

Once all the settings are in place, the solution can be generated, the (simulated) observations can be fit to the dynamical model that has been defined to perform the fitting. Alternatively, the same functionality can be used for a covariance analysis, in which case no fit is attempted.

.. toctree::
   :maxdepth: 1

   state_estimation/running_estimation

