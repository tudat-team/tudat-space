.. _modifying_observation_collections:

==========================
Modifying Collections
==========================

This page describes how to modify the contents and properties of an :class:`~tudatpy.estimation.observations.ObservationCollection`.

When creating an observation collection - either from simulated or real data - the residuals and weights are in most cases set to their default values (zero and one, respectively) and no observation dependent variable is created by default. This can be changed *a posteriori*, as discussed below.

Setting Weights
===============

To obtain statistically realistic results when performing an orbit determination and/or parameters estimation analysis, it is critical to account for the quality of each observation used in the fit. To this end, the weight matrix :math:`\mathbf{W}` of size :math:`N_h \times N_h` describes our knowledge of the observation uncertainties and ensures that this is accounted for in a covariance or full estimation analysis. The weight matrix diagonal entries :math:`\mathbf{W}_{i,i}` should ideally be related to the observation's Gaussian noise :math:`\sigma_i` as :math:`\mathbf{W}_{i,i} = 1/\sigma_i^2`. The default weight values assume :math:`\sigma_i = 1`.

.. note::
   We currently only support the definition of a diagonal weight matrix, as using a full-sized matrix would lead to prohibitive memory usage. Diagonal weight matrices are anyway perfectly suited for covariance analyses and widely used in real data analyses as well.

The parsing functionality can be very useful to define the observation weights at the observation collection level. In general, two main options exist:

- Setting weights to a constant value (or a constant vector if the observation size is larger than 1), using :meth:`~tudatpy.estimation.observations.ObservationCollection.set_constant_weight`
- Providing a full vector of tabulated weight values, using :meth:`~tudatpy.estimation.observations.ObservationCollection.set_tabulated_weights`

Constant Weights
----------------

The :meth:`~tudatpy.estimation.observations.ObservationCollection.set_constant_weight` method assigns a constant scalar or vector weight. The weight setting functions can make use of an optional parser input to specify which weights should be assigned to which observation sets within the observation collection.

The example below shows two equivalent ways of assigning different (constant) weights depending on the observable type:

.. code-block:: python

    from tudatpy.estimation import observations
    
    # Set weights based on observable type
    range_weight = 1.0 / (1.0**2)  # Assuming 1.0m noise
    doppler_weight = 1.0 / (1.0e-12**2)  # Assuming 1.0e-12 Hz noise
    
    # Approach 1: Set weights individually
    observation_collection.set_constant_weight(
        range_weight,
        observations.observation_parser(one_way_range)
    )
    observation_collection.set_constant_weight(
        doppler_weight,
        observations.observation_parser(one_way_doppler)
    )
    
    # Approach 2: Set weights using a dictionary
    weights_per_type = dict()
    weights_per_type[observations.observation_parser(one_way_range)] = range_weight
    weights_per_type[observations.observation_parser(one_way_doppler)] = doppler_weight
    observation_collection.set_constant_weight(weights_per_type)

Tabulated Weights
-----------------

The :meth:`~tudatpy.estimation.observations.ObservationCollection.set_tabulated_weights` method provides a vector of weights for each observation in a selection. If no parser is specified, the weights are applied to the entire observation collection:

.. code-block:: python

    # Set weights for the entire collection
    tabulated_weights = ...  # numpy array with size matching the observation vector
    observation_collection.set_tabulated_weights(tabulated_weights)

.. note::
   When setting tabulated weights, the size of the weight vector should match either the total size of the observation vector within the observation collection (all sets combined), or the size of each individual observation set. The latter is however only possible in the unlikely scenario where all observation sets are of the same size. It might nonetheless be useful for simulated observations where the user has more control on the number of observations per set.

Defining Reference Points
==========================

When creating an observation collection by loading real data files, the reference point on the spacecraft is automatically set to the center-of-mass, and not to the antenna position. This choice follows from the name and position of the antenna not being available in the data files (unlike e.g., the names of the stations on Earth). It is however possible to set the position of the reference point *a posteriori* once the observation collection has been created. Note that this can also be useful in other cases, and not only when creating an observation collection from real data.

There are three options currently implemented to set the reference point position in an observation collection:

Single, Constant Reference Point
---------------------------------

For a **single** reference point whose position is **constant** in the body-fixed frame:

.. code-block:: python

    import numpy as np
    from tudatpy.estimation import observations
    
    # Define the antenna position in the spacecraft-fixed frame
    antenna_position = np.array([1.0, 0.0, 0.0])
    
    # Set the antenna as reference point for the entire observation collection
    observation_collection.set_reference_point(
        bodies,
        antenna_position,
        "AntennaName",
        "SpacecraftName",
        observations.reflector1
    )

Single, Time-Varying Reference Point
------------------------------------

For a **single** reference point whose position **varies** in the body-fixed frame:

.. code-block:: python

    from tudatpy.numerical_simulation import environment_setup
    from tudatpy.estimation import observations
    
    # Retrieve the MRO antenna (SPICE ID: -74214) ephemeris in the spacecraft-fixed frame
    # (SPICE ID of the frame origin: -74000)
    antenna_ephemeris_settings = environment_setup.ephemeris.direct_spice(
        "-74000",
        "MRO_SPACECRAFT"
    )
    antenna_ephemeris = environment_setup.ephemeris.create_ephemeris(
        antenna_ephemeris_settings,
        "-76214"
    )
    
    # Set the antenna as reference point
    observation_collection.set_reference_point(
        bodies,
        antenna_ephemeris,
        "Antenna",
        "MRO",
        observations.reflector1
    )

Multiple Reference Points with Switching
----------------------------------------

For **multiple** reference points whose positions are **constant** in the body-fixed frame, with the actual reference point used at time :math:`t` switching between those (useful for a multi-antenna case, for instance):

.. code-block:: python

    import numpy as np
    from tudatpy.estimation import observations
    
    position_antenna_1 = np.array([1.0, 0.0, 0.0])
    position_antenna_2 = np.array([0.0, 1.0, 0.0])
    
    # Define the antenna switch history
    antenna_switch_history = dict()
    antenna_switch_history[t0] = position_antenna_1
    antenna_switch_history[t1] = position_antenna_2
    antenna_switch_history[t2] = ...
    
    # Set the reference point position to follow the antenna switch history
    observation_collection.set_reference_points(
        bodies,
        antenna_switch_history,
        "SpacecraftName",
        observations.reflector1
    )

.. warning::
   The reference point position must always be provided in the reference frame fixed to the body to which it belongs. This implies that setting an antenna as reference point requires knowing (typically via the use of the corresponding SPICE kernels):
   
   - The position of the antenna with respect to the spacecraft's center-of-mass, in the spacecraft-fixed frame (this can be constant or time-variable)
   - The orientation of the spacecraft (required for Tudat to later convert the antenna's spacecraft-fixed position to an inertial frame)
   
   This can require the use of multiple SPICE kernels, as shown for the MRO test case in the :ref:`examples <estimation_examples>` (spacecraft structure file, spacecraft frames definition file, antenna and spacecraft orientation files, etc.).

Using Parsers with Reference Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   All :meth:`~tudatpy.estimation.observations.ObservationCollection.set_reference_point` and :meth:`~tudatpy.estimation.observations.ObservationCollection.set_reference_points` functions can take an observation parser as an optional argument, allowing you to set the reference point position over a subset of the observation collection:

   .. code-block:: python

       # Set the reference point position for one_way_range observables only
       observation_collection.set_reference_point(
           bodies,
           antenna_position,
           "AntennaName",
           "SpacecraftName",
           observations.reflector1,
           observations.observation_parser(one_way_range)
       )

Computing Residuals
===================

Residuals are defined as the difference between computed (i.e., simulated) and observed (i.e., real) data. They are set to zeros by default, but can be computed by simulating observations according to given observation models, and calculating the difference with respect to the observation values contained in the observation collection.

- For observation collections created from loading **real** data, residuals indicate how much the real observations depart from the values predicted by our observation model(s).
- For observation collections created from **simulated** data, residuals should theoretically be equal to zero unless artificial measurement (bias and/or noise) or dynamical errors are introduced.

Computing the residuals for a given observation collection can be done using the :func:`~tudatpy.estimation.observations_setup.observations_wrapper.compute_residuals_and_dependent_variables` function. It only requires the observation collection, observation simulators (see :func:`~tudatpy.estimation.observations_setup.create_observation_simulators`), and the usual :class:`~tudatpy.numerical_simulation.environment.SystemOfBodies` as inputs.

The :func:`~tudatpy.estimation.observations_setup.observations_wrapper.compute_residuals_and_dependent_variables` function automatically generates the simulation settings to match the observations contained within the observation collection, and uses such settings - combined with the observation simulators - to get the computed observation values:

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    # Create observation simulators
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

1. Automatically generates simulation settings matching the observations in the collection
2. Simulates observations using the current state of the environment and observation models
3. Computes the difference between observed and simulated values
4. Stores the residuals in each :class:`~tudatpy.estimation.observations.SingleObservationSet`
5. Computes any dependent variables that have been defined (see :ref:`next section <observation_dependent_variables_usage>`)

The residuals can then be used for:

- Quality assessment of the observations
- Outlier detection
- Convergence checking during estimation
- Post-estimation analysis
