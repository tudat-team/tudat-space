.. _estimationSettings:

Estimation Settings
====================

Having defined the link ends, observation models, and having loaded/simulated all the relevant observations, the settings for the estimation can be created.

The definition of the parameters that are to be fit to the (simulated) data are defined as described in :ref:`parameter_settings`, and the dynamical model
used to propagate initial states is defined identically as for the :ref:`propagation of dynamics <propagation_setup>`.

The remaining settings for the data analysis relate to how the data is to be used in the further analysis.
We distinguish between two different types of analyses:

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
 
The design matrix :math:`\mathbf{H}` is created from the observation model, propagated state and variational equations,
and is fully defined by the specifics of the observations, dynamical model and observation model.
The weight matrix :math:`\mathbf{W}` can be specified by the user (see below) and is set to the identity matrix by default.
The inverse a priori covariance :math:`P_{0}^{-1}` can be specified by the user, and is set to a 0 matrix by default.

The design matrix is defined by:

.. math::

  \mathbf{H}=\frac{\partial\mathbf{h}}{\partial\mathbf{p}}

with :math:`\mathbf{h}` the vector of computed observations, and :math:`\mathbf{p}` the vector of estimated parameters.

The basic definition of settings for a covariance analysis only requires the observations that are simulated, as follows:

.. code-block:: python

    # Create parameters to estimate
    parameters_to_estimate = estimation_setup.create_parameter_set(parameter_settings, bodies)
    ...
    # Simulate observations
    simulated_observations = estimation.simulate_observations(
        observation_simulation_settings,  estimator.observation_simulators, bodies)
    ...
    # Create settings for observation models
    covariance_analysis_settings = estimation.CovarianceAnalysisInput(
        simulated_observations)

Where the *inverse* a priori covariance matrix can be provided as an additional optional input argument to the
:class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput` constructor.

The resulting object ``covariance_analysis_settings`` can be used to tune the exact behaviour of the covariance analysis process
(see the :func:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.define_covariance_settings` function of this class for details),
such as whether to reintegrate the dynamics, or which terminal output to provide.

The weight matrix is typically not provided as a full matrix in a covariance analysis, as the its size of :math:`N_{obs}\times N_{obs}` leads to prohibitive memory usage.
Presently, we only support the definition of a diagonal weights matrix.
Note that the weight matrix diagonal entry :math:`W_{i,i}` should ideally be related to the observation's Gaussian noise as :math:`W_{i,i}=1/\sigma_{i}^{2}`.
Several options are provided to set the weights matrix diagonal
(as :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput` member functions):

* Constant weight for all observation, using the :meth:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_constant_weight` function,
* Constant weight for all observations of a given observation type, using the :meth:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_constant_single_observable_weight` function, or the :func:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_constant_single_observable_vector_weight` function for observables of size :math:`>1`, to for instance set different weights for right ascension and declination of an angular position observable
* Constant weight for all observations of a given observation type, with a given set of link ends, using the :meth:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_constant_single_observable_and_link_end_weight` function, or the :func:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_constant_single_observable_and_link_end_vector_weight` function for observables of size :math:`>1`
* Manual definition of full weight vector for all observations of a given observation type with a given set of link ends, using the :meth:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.set_total_single_observable_and_link_end_vector_weight` function,
* Manual definition of the full weight vector for all observations using the :meth:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput.weight_matrix_diagonal` attribute,

When using consider covariance (e.g. when consider parameters are defined in the :ref:`parameterSettings`), the consider parameter covariance matrix :math:`\mathbf{C}`
is also provided to the :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput` constructor, and the
calculation of the resulting covariance matrix becomes the matrix :math:`\mathbf{P}^{c}`, which is computed from the above as:

.. math::

  \mathbf{P}^{c}=\mathbf{P}+\left(\mathbf{P}\mathbf{H}^{T}\mathbf{W}\right)\left(\mathbf{H}_{c}\mathbf{C}\mathbf{H}_{c}^{T}\right)\left(\mathbf{P}\mathbf{H}^{T}\mathbf{W}\right)^{T}

where :math:`\mathbf{H}_{c}` is the design matrix for the consider parameters.

.. _fullEstimationSettings:

Full estimation settings
~~~~~~~~~~~~~~~~~~~~~~~~

The full estimation performs an iterative differential correction of the estimated parameters, where for iteration :math:`i` a correction
to the parameter vector :math:`\mathbf{p}` is computed according to:

.. math::

  \Delta\mathbf{p}_{i}&=\mathbf{P}_{i}\left(\mathbf{H}_{i}\mathbf{W}\Delta\mathbf{z}_{i}\right)\\
  \mathbf{p}_{i+1}&=\mathbf{p}_{i}+\Delta\mathbf{p}_{i}

where :math:`\mathbf{P}` is the covariance (see previous section; where using consider parameters, we have :math:`\mathbf{P}\rightarrow\mathbf{P}^{c}` in the above), and :math:`\Delta\mathbf{z}_{i}` is the observation residual at
iteration :math:`i`, computed from:

.. math::

  \Delta\mathbf{z}_{i} = \mathbf{z} - \mathbf{h}(\mathbf{p}_{i})

with :math:`\mathbf{z}` the vector of all observations provided as input to the data (observed data) and
:math:`\mathbf{h}(\mathbf{p}_{i})` the vector of all observations, as computed from the current
estimate of the parameters (computed data).

The above procedure is performed iteratively, until convergence has been reached.

The settings for the full estimation are created in an essentially idential manner as those for a covariance analysis:

.. code-block:: python

    # Create parameters to estimate
    parameters_to_estimate = estimation_setup.create_parameter_set(parameter_settings, bodies)
    ...
    # Simulate observations
    simulated_observations = estimation.simulate_observations(
        observation_simulation_settings,  estimator.observation_simulators, bodies)
    ...
    # Create settings for observation models
    estimation_settings = estimation.EstimationInput(
        simulated_observations)

where, in fact, the :class:`~tudatpy.numerical_simulation.estimation.EstimationInput` is derived from
the :class:`~tudatpy.numerical_simulation.estimation.CovarianceAnalysisInput`. For the estimation settings,
however, there are a number of additional options available, such as the definition for 'convergenve'
(default: perform three iterations of the least squares).

The :class:`~tudatpy.numerical_simulation.estimation.EstimationInput` class also has as function to
tune the exact behaviour of the estimation procsess (see the
:func:`~tudatpy.numerical_simulation.estimation.EstimationInput.define_estimation_settings` function of this class for details),
such as whether to save all intermediate results for the user.
