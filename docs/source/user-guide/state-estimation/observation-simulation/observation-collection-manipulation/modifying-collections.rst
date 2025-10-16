.. _modifying_observation_collections:

==========================
Modifying Collections
==========================

This page describes how to modify the contents and properties of an :class:`~tudatpy.estimation.observations.ObservationCollection`.

Setting Weights
===============

To perform a statistically meaningful estimation, it's crucial to assign weights to observations based on their uncertainty. The weight matrix **W** is used in the least-squares fit. The diagonal entries are typically set as :math:`W_{i,i} = 1/\sigma_{i}^{2}`, where :math:`\sigma_{i}` is the observation's standard deviation, assuming the observation noise is Gaussian, uncorrelated, and zero-mean.

You can set weights for subsets of the :class:`~tudatpy.estimation.observations.ObservationCollection` using a parser:

Constant Weights
----------------

:meth:`~tudatpy.estimation.observations.ObservationCollection.set_constant_weight` assigns a constant scalar or vector weight:

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Set weights based on observable type
    range_weight = 1.0 / (1.0**2)  # Assuming 1.0m noise
    doppler_weight = 1.0 / (0.001**2)  # Assuming 1 mm/s noise
    
    observation_collection.set_constant_weight(
        range_weight,
        observations.observation_parser(one_way_range)
    )
    observation_collection.set_constant_weight(
        doppler_weight,
        observations.observation_parser(one_way_doppler)
    )

Tabulated Weights
-----------------

:meth:`~tudatpy.estimation.observations.ObservationCollection.set_tabulated_weights` provides a vector of weights for each observation in a selection:

.. code-block:: python

    # Set weights for the entire collection
    tabulated_weights = ...  # numpy array with size matching the observation vector
    observation_collection.set_tabulated_weights(tabulated_weights)

.. note::
   When providing a single vector of tabulated weights for the entire collection, a parser cannot be used. You must provide a vector whose size matches the total number of observations.

Defining Reference Points
==========================

When loading real observation data, the reference point on a spacecraft defaults to its center of mass. You can update this to the correct antenna position *a posteriori*.

Single, Constant Reference Point
---------------------------------

For a **single, constant** reference point:

.. code-block:: python

    antenna_position = np.array([1.0, 0.0, 0.0])  # In the body-fixed frame
    observation_collection.set_reference_point(
        bodies,
        antenna_position,
        "AntennaName",
        "SpacecraftName",
        observations.receiver
    )

.. warning::
   The reference point position must always be provided in the reference frame fixed to the body to which it belongs. This is a critical requirement to ensure correct geometric calculations.

Computing Residuals
===================

Residuals (observed - computed values) are not available by default and must be computed. The :func:`~tudatpy.estimation.observations_setup.observations_wrapper.compute_residuals_and_dependent_variables` function simulates observations based on your models and calculates the residuals against the values stored in the :class:`~tudatpy.estimation.observations.ObservationCollection`.

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    # Create observation simulators from your models
    observation_simulators = observations_setup.create_observation_simulators(
        observation_model_settings,
        bodies
    )
    
    # Compute residuals and store them in the observation_collection
    observations_setup.observations_wrapper.compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )
    
    # Retrieve the computed residuals
    residuals = observation_collection.get_concatenated_residuals()

This function performs the following operations:

1. Simulates observations using the current state of the environment and observation models
2. Computes the difference between observed and simulated values
3. Stores the residuals in each :class:`~tudatpy.estimation.observations.SingleObservationSet`
4. Computes any dependent variables that have been defined (see next section)

The residuals can then be used for:

- Quality assessment of the observations
- Outlier detection
- Convergence checking during estimation
- Post-estimation analysis
