.. _estimationSettings:

Estimation Settings
====================

Having defined the link ends, observation models, and having loaded/simulated all the relevant observations, the settings for the estimations can be created.

The definition of the parameters that are to be fit to the (simulated) data are defined as described in :ref:`parameter_settings`, and the dynamical model used to propagate initial states is defined identically as for the :ref:`propagation of dynamics <propagation_setup>`.

The remaining settings for the data analysis relate to how the (simulated) data is to be used in the further analysis. We distinguish between two different types of analyses:

* **A covariance analysis**: no actual estimation is performed, but the data uncertainty is propagated onto the parameter uncertainty. In essence, it determines what the parameter uncertainty would be *if* we were to do an actual estimation. The validity of the covariance analysis depends on a number of assumptions
  * The weight matrix (see below) is a perfect representation of the noise properties of the observations
  * The ideal observation models (without random noise) are a perfect representation of reality
  * The dynamics model is a perfect representation of reality
* **Batch least-squares estimation**: an iterative batch-least squares estimation is performed. The full estimation requires all settings that the coviariance analysis does. In addition, it requires a specification on when to terminate the iteration process.

.. _covarianceSettings:

Covariance analysis settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The covariance analysis solves the following equation:

.. math::

 \mathbf{P}=\left(\mathbf{H}^{T}\cdot \mathbf{W}\cdot \mathbf{H} + \mathbf{P}_{0}^{-1} \right)^{-1}
 
The design matrix :math:`\mathbf{H}` is created from the observation model, propagated state and variational equations, and is fully defined by the specifics of the observations, dynamical model and observation model. The weight matrix :math:`\mathbf{W}` must be specified by the user (and is set to the identity matrix by default). The inverse a priori covariance :math:`P_{0}^{-1}` can be specified by the user, and is set to a 0 matrix by default.

The basic definition of settings for a covariance analysis only requires the observations that are simulated (as well as the size of the estimated parameter vector), which can be done as follows:

.. code-block:: python

    # Create parameters to estimate
    parameters_to_estimate = estimation_setup.create_parameter_set(parameter_settings, bodies)
    ...
    # Simulate observations
    simulated_observations = estimation.simulate_observations(
        observation_simulation_settings,  estimator.observation_simulators, bodies)
    ...
    # Create settings for observation models
    covariance_analysis_settings = estimation_setup.covariance_analysis_input(
        simulated_observations, parameters_to_estimate.parameter_set_size)

Where the *inverse* a priori covariance matrix can be provided as an optional input argument (see :func:`~tudatpy.numerical_simulation.estimation.observation.covariance_analysis_input`). The resulting object ``covariance_analysis_settings`` (of type :class:`~tudatpy.numerical_simulation.estimation.observation.CovarianceAnalysisInput`) can be used to tune the exact behaviour of the covariance analysis process (see :func:`~tudatpy.numerical_simulation.estimation.observation.CovarianceAnalysisInput.define_covariance_settings` for details).

The weight matrix is typically not provided as a full matrix, as the its size of :math:`N_{obs}\times N_{obs}` leads to prohibitive memory usage. Presently, we only support the definition of a diagonal weights matrix. Note that the weight matrix diagonal entry :math:`W_{i,i}` is related to the observation's Gaussian noise as :math:`W_{i,i}=1/\sigma_{i}^{2}`. Several options are provided to set the weights matrix diagonal (as :class:`~tudatpy.numerical_simulation.estimation.observation.CovarianceAnalysisInput` member functions):

* Constant weight for all observation.
* Constant weight for all observations of a given observation type
* Constant weight for all observations of a given observation type, with a given set of link ends
* Manual link end definition, per observation. See :ref:`here <accessing_observations>` for the meaning of entry :math:`i` in the observations vector.

.. _fullEstimationSettings:

Full estimation settings
~~~~~~~~~~~~~~~~~~~~~~~~

