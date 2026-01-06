.. _estimationSettings:

Performing the estimation
=========================

Having created all the relevant settings for the physical environment (see :ref:`environment_setup`)
dynamical model (see :ref:`propagation_setup`), the parameters that are to be estimated (see :ref:`parameter_settings`),
the settings for the observation models (see :ref:`observationModelSetup`)
and the actual observations (simulated or real; see :ref:`observationSimulation`), the estimation can be performed.

The remaining settings for the data analysis relate to how the data is to be used in the further analysis.
We distinguish between two different types of analyses:

* **A covariance analysis**: no actual estimation is performed, but the data uncertainty is propagated onto the parameter uncertainty. In essence, it determines what the parameter uncertainty would be *if* we were to do an actual estimation. The validity of the covariance analysis depends on a number of assumptions

  * The weight matrix (see below) is a perfect representation of the noise properties of the observations
  * The ideal observation models (without random noise) are a perfect representation of reality
  * The dynamics model is a perfect representation of reality
* **Batch least-squares estimation**: an iterative batch-least squares estimation is performed. The full estimation requires all settings that the covariance analysis does. In addition, it requires a specification on when to terminate the iteration process.

Both are performed by using the :class:`~tudatpy.estimation.estimation_analysis.Estimator` object,
which is created as follows:

.. code-block:: python

    estimator = estimation.estimation_analysis.Estimator(
        bodies,
        parameters_to_estimate,
        observation_settings_list,
        propagator_settings)

where the propagator settings may be single-, multi- or hybrid arc. Creating an :class:`~tudatpy.estimation.estimation_analysis.Estimator` object as above automatically propagates
the dynamics and variational equations for the specific propagator and parameter settings.

.. _covarianceSettings:

Covariance analysis
~~~~~~~~~~~~~~~~~~~


The basic definition of settings for a covariance analysis only requires the observations that are simulated, as follows:

.. code-block:: python

    # Create parameters to estimate
    parameters_to_estimate = dynamics.parameters_setup.create_parameter_set(parameter_settings, bodies)
    ...
    # Simulate observations
    simulated_observations = estimation.estimation_analysis.simulate_observations(
        observation_simulation_settings,  estimator.observation_simulators, bodies)
    ...
    # Create settings for observation models
    covariance_analysis_settings = estimation.estimation_analysis.CovarianceAnalysisInput(
        simulated_observations)

Where the *inverse* a priori covariance matrix can be provided as an additional optional input argument to the
:class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisInput` constructor.

The resulting object ``covariance_analysis_settings`` can be used to tune the exact behaviour of the covariance analysis process
(see the :meth:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisInput.define_covariance_settings` method of this class for details),
such as whether to reintegrate the dynamics, or which terminal output to provide.

The weight matrix is typically not provided as a full matrix in a covariance analysis, as the its size of :math:`N_{obs}\times N_{obs}` leads to prohibitive memory usage. Presently, we only support the definition of a diagonal weights matrix. The weights of observations are set in the object containing the observations themselves (see :ref:`setting_weight`)

When using consider covariance (e.g. when consider parameters are defined in the :ref:`parameterSettings`), the consider parameter covariance matrix :math:`\mathbf{C}`
is also provided to the :class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisInput` constructor.

These settings are used to compute the covariance
using the :meth:`~tudatpy.estimation.estimation_analysis.Estimator.compute_covariance` method as follows:

.. code-block:: python

    estimator = estimation.estimation_analysis.Estimator(
        bodies,
        parameters_to_estimate,
        observation_settings_list,
        propagator_settings)
    covariance_analysis_output = estimator.compute_covariance(
        covariance_analysis_settings)

where the ``covariance_analysis_output`` is an object of type :class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisOutput`
from which the design matrix, covariance, formal errors, correlations etc. can be retrieved. During the calculation of the covariance, the
columns of the design matrix :math:`\mathbf{H}` are normalized (see :class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisOutput` documentation).
Both the regular and normalized quantities (design matrix :math:`\mathbf{H}`, covariance :math:`\mathbf{P}`, inverse covariance :math:`\mathbf{P}^{-1}`)
can be retrieved. For most applications, the regular (unnormalized) quantities are the ones that are of interest.
Use of the normalized quantities should be limited to those applications where a manual inversion is performed.

.. _fullEstimationSettings:

Full estimation
~~~~~~~~~~~~~~~

The full estimation performs an iterative differential correction of the estimated parameters. The settings for a full estimation are created in an essentially identical manner as those for a covariance analysis:

.. code-block:: python

    # Create parameters to estimate
    parameters_to_estimate = dynamics.parameters_setup.create_parameter_set(parameter_settings, bodies)
    ...
    # Simulate observations
    simulated_observations = estimation.estimation_analysis.simulate_observations(
        observation_simulation_settings,  estimator.observation_simulators, bodies)
    ...
    # Create settings for observation models
    estimation_settings = estimation.estimation_analysis.EstimationInput(
        simulated_observations)

where, in fact, the :class:`~tudatpy.estimation.estimation_analysis.EstimationInput` is derived from
the :class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisInput`. For the estimation settings,
however, there are a number of additional options available, such as the definition for 'convergence'
(default: perform three iterations of the least squares).

The :class:`~tudatpy.estimation.estimation_analysis.EstimationInput` class also has as function to
tune the exact behaviour of the estimation process (see the
:meth:`~tudatpy.estimation.estimation_analysis.EstimationInput.define_estimation_settings` function of this class for details),
such as whether to save all intermediate results for the user.

.. note::
   To estimate the initial state of a body, its associated ephemeris must be tabulated. When specifying an ephemeris for
   any of the estimated bodies, convert its type to tabulated using the
   :func:`~tudatpy.dynamics.environment_setup.ephemeris.tabulated_from_existing` setting (for estimated translational dynamics)

These settings can then be used to perform
the full estimation using the :meth:`~tudatpy.estimation.estimation_analysis.Estimator.perform_estimation` method.

.. code-block:: python

    estimator = estimation.estimation_analysis.Estimator(
        bodies,
        parameters_to_estimate,
        observation_settings_list,
        propagator_settings)
    estimation_output = estimator.perform_estimation(
        estimation_settings)

where the ``estimation_output`` is an object of type :class:`~tudatpy.estimation.estimation_analysis.EstimationOutput`,
which (in addition to all information in :class:`~tudatpy.estimation.estimation_analysis.CovarianceAnalysisOutput`, which this class derives from)
contains information on the estimation process. Note that the covariances *etc.* that are always saved are those from the iteration
where the residual was lowest.

The specific additional information that is retained for the
:class:`~tudatpy.estimation.estimation_analysis.EstimationOutput` is defined by the
:meth:`~tudatpy.estimation.estimation_analysis.EstimationInput.define_estimation_settings` method of the :class:`~tudatpy.estimation.estimation_analysis.EstimationInput`
class. We note that saving all information from each iteration may not be recommended for larger applications, as the memory
consumption that is required may be prohibitive.



