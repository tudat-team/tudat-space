.. _perform_estimation:

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

Covariance analysis
-------------------

The settings for a covariance analysis described :ref:`here <covarianceSettings>` can be used to compute the covariance using the :func:`~tudatpy.numerical_simulation.Estimator.compute_covariance` function.

.. code-block:: python

    covariance_analysis_output = estimator.compute_covariance(
        covariance_analysis_settings)
        
where the ``covariance_analysis_settings`` is an object of type :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput` from which the design matrix, covariance, etc. can be retrieved. 

.. _covariance_normalization:

Normalization
^^^^^^^^^^^^^

The partial derivative matrix :math:`\mathbf{H}=\frac{\partial\mathbf{h}}{\partial\mathbf{p}}` is computed automatically for all observations and parameters, from which the inverse covariance :math:`\mathbf{P}^{-1}` is then computed, as described :ref:`here <covarianceSettings>`. However, due to the potentially huge difference in order of magnitude of the estimated parameters (for instance, the Sun's gravitational parameter, at approximately 1.3267:math:`\cdot 10^{20}` m^3/s^2, and the bias of a VLBI observaion, at :math:`10^{-9}` radians), the inversion of the matrix :math:`\mathbf{P}^{-1}` can be extremely ill-posed. We partly correct for this problem by normalizing the parameters.

The normalization is achieved by computing a vector :math:`\mathbf{N}` (of the same size as the parameter vector :math:`\mathbf{p}`, such that for each column of the matrix :math:`\mathbf{H}`, we have:

.. math::

  \max_{i}\left| \frac{H_{ij}}{N_{j}}\right|=1
 
That is, the entries of :math:`\mathbf{N}` are chosen such that they normalize the corresponding column of :math:`\mathbf{H}` to be in the range :math:`[-1,1]`. We denote the normalized quantities with a tilde, so that:


.. math::

  \tilde{H}_{ij}=\frac{H_{ij}}{N{j}}\\
  \tilde{P}_{ij}=P_{ij}N_{i}N_{j}

When inverting the normal equations, normalized quantities are always used. Both the normalized and regular quantities can be retrieved from the :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput` class.

Full estimation
---------------

Similarly, the settings for a full estimation described :ref:`here <fullEstimationSettings>` can be used to perform the full estimation using the :func:`~tudatpy.numerical_simulation.Estimator.perform_estimation` function.

.. code-block:: python

    estimation_output = estimator.perform_estimation(
        estimation_settings)
        
where the ``estimation_output`` is an object of type :class:`~tudatpy.numerical_simulation.estimation.EstimationOutput`, which (in addition to all information in :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput`) contains information on the iteration process (depending on the specific output settings provided in ``estimation_settings``.


 





 


