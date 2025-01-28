.. _perform_estimation:

Performing the estimation
=========================

Having created all the relevant settings for the physical environment (see :ref:`environment_setup`)
dynamical model (see :ref:`propagation_setup`), the parameters that are to be estimated (see :ref:`parameter_settings`),
the settings for the observation models (see :ref:`observationModelSetup`)
and the actual observations (simulated or real; see :ref:`observationSimulation`), the estimation can be performed.

Both a full estimation and a covariance analysis are performed by using the :class:`~tudatpy.numerical_simulation.Estimator` object,
which is created as follows:

.. code-block:: python

    estimator = numerical_simulation.Estimator(
        bodies,
        parameters_to_estimate,
        observation_settings_list,
        propagator_settings)
        
where the propagator settings may be single-, multi- or hybrid arc. Creating an ``Estimator`` object automatically propagates
the dynamics and variational equations for the specific propagator and parameter settings.

Covariance analysis
-------------------

The settings for a covariance analysis described :ref:`here <covarianceSettings>` can be used to compute the covariance
using the :func:`~tudatpy.numerical_simulation.Estimator.compute_covariance` function.

.. code-block:: python

    covariance_analysis_output = estimator.compute_covariance(
        covariance_analysis_settings)
        
where the ``covariance_analysis_output`` is an object of type :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput`
from which the design matrix, covariance, etc. can be retrieved. During the calculation of the covariance, the
columns of the design matrix :math:`\mathbf{H}` are normalized (see :ref:`below <covariance_normalization>`), and
both the regular and normalized quantities (design matrix :math:`\mathbf{H}`, covariance :math:`\mathbf{P}`, inverse covariance :math:`\mathbf{P}^{-1}`)
can be retrieved. For most applications, the regular (unnormalized) quantities are the ones that are of interest.
Use of the normalized quantities should be limited to those applications where a manual inversion is performed.

In addition to the quantities listed above, formal errors and correlations (directly obtained from the unnormalized covariance) can
be obtained from the :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput` class.


.. _covariance_normalization:

Normalization
^^^^^^^^^^^^^

The partial derivative matrix :math:`\mathbf{H}=\frac{\partial\mathbf{h}}{\partial\mathbf{p}}` is computed automatically for all observations and parameters, from which the inverse covariance :math:`\mathbf{P}^{-1}` is then computed, as described :ref:`here <covarianceSettings>`. However, due to the potentially huge difference in order of magnitude of the estimated parameters (for instance, the Sun's gravitational parameter, at approximately :math:` 1.3267 \cdot 10^{20}` m^3/s^2, and the bias of a VLBI observation, at :math:`10^{-9}` radians), the inversion of the matrix :math:`\mathbf{P}^{-1}` can be extremely ill-posed. We partly correct for this problem by normalizing the parameters.

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

.. note::
   To estimate the initial state of a body, its associated ephemeris must be tabulated. When specifying an ephemeris for
   any of the estimated bodies, convert its type to tabulated using the
   :func:`~tudatpy.numerical_simulation.environment_setup.ephemeris.tabulated_from_existing` setting (for estimated translational dynamics)

Similarly, the settings for a full estimation described :ref:`here <fullEstimationSettings>` can be used to perform
the full estimation using the :func:`~tudatpy.numerical_simulation.Estimator.perform_estimation` function.

.. code-block:: python

    estimation_output = estimator.perform_estimation(
        estimation_settings)
        
where the ``estimation_output`` is an object of type :class:`~tudatpy.numerical_simulation.estimation.EstimationOutput`,
which (in addition to all information in :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisOutput`)
contains information on the estimation process. Note that the covariances *etc.* that are saved are those from the iteration
where the residual was lowest.

The specific additional information that is retained for the
:class:`~tudatpy.numerical_simulation.estimation.EstimationOutput` is defined by the
:func:`~tudatpy.numerical_simulation.estimation.EstimationInput.define_estimation_settings` function of the :class:`~tudatpy.numerical_simulation.estimation.EstimationInput`
class. We note that saving all information from each iteration may not be recommended for larger applications, as the memory
consumption that is required may be prohibitive.

After the estimation is finished, the properties of both the environment (in the ``bodies``) and the estimated parameters
(in the ``parameters_to_estimate``) are modified as follows:

* The ephemerides of all propagated/estimated bodies will be set to the propagation results of the last iteration in the estimation. For instance, when estimating the state of body "Delfi-C3", the (tabulated) ephemeris of this body will be set to contain the numerical results of the last iteration of the estimation
* The values of the parameter values in the ``parameters_to_estimate`` object are those of the last iteration of the estimation. Note that, if the ``apply_final_parameter_correction`` parameter to the :class:`~tudatpy.numerical_simulation.estimation.EstimationInput` is set to ``True``, the parameter correction computed at the end of the last iteration (for which the performance has *not* been computed) has been used to update the parameters vector

The main results of the estimation are characterized by two quantities:

* The residual vector of the iteration that had the lowest residual, from the :attr:`~tudatpy.numerical_simulation.estimation.EstimationOutput.final_residuals` attribute of the :class:`~tudatpy.numerical_simulation.estimation.EstimationOutput` class
* The values of the parameters at the iteration that had the lowest residual, from the :attr:`~tudatpy.numerical_simulation.estimation.EstimationOutput.final_parameters` attribute of the :class:`~tudatpy.numerical_simulation.estimation.EstimationOutput` class




 





 


