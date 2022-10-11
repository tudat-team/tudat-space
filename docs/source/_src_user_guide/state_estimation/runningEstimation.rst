.. _runningEstimation:

Performing the estimation
=========================

Having created all the relevant settings for the physical environment (see :ref:`environment_setup`) dynamical model (see :ref:`propagation_setup`), the parameters that are to be estimatd (see :ref:`parameter_settings`), the settins for the observation models (see :ref:`observationModelSetup`) and the actual observations (simulated or real; see :ref:`observationSimulation`), the estimation can be performed. Both a full estimation and a covariance analysis are performed by using the :class:`~tudatpy.numerical_simulation.Estimator` object, which is created as follows:

.. code-block:: python

    estimator = numerical_simulation.Estimator(
        bodies,
        parameters_to_estimate,
        observation_settings_list,
        propagator_settings)
        
where the propagator settings may be single-, multi- or hybrid arc. Creating an ``Estimator`` object automatically propagates the dynamics and variational equations for the specifief propagator and parameter settings.

The settings for a covariance analysis described :ref:`here <covarianceSettings>` can be used to compute the covariance using the :func:`~tudatpy.numerical_simulation.Estimator.compute_covariance` function.

.. code-block:: python

    covariance_analysis_output = estimator.compute_covariance(
        covariance_analysis_settings)
        
where the ``covariance_analysis_settings`` is an object of type :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput` from which the design matrix, covariance, etc. can be retrieved.

Similarly, the settings for a full estimation described :ref:`here <fullEstimationSettings>` can be used to perform the full estimation using the :func:`~tudatpy.numerical_simulation.Estimator.perform_estimation` function.

.. code-block:: python

    estimation_output = estimator.perform_estimation(
        estimation_settings)
        
where the ``estimation_output`` is an object of type :class: `~tudatpy.numerical_simulation.estimation.EstimationOutput`, which (in addition to all information in :class: `~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput`) contains information on the iteration process (depending on the specific output settings provided in ``estimation_settings``.


 





 


