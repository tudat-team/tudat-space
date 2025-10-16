.. _observation_dependent_variables_usage:

=============================
Using Dependent Variables
=============================

Observation dependent variables (e.g., elevation angle, range distance) can be calculated and stored alongside observations. This is useful for analyzing observation geometry and estimation results.

Adding Dependent Variables
===========================

First, you define the settings for the dependent variable you want to compute. Then, you add these settings to the :class:`~tudatpy.estimation.observations.ObservationCollection`.

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    # Define settings to calculate the elevation angle at the transmitter
    elevation_angle_settings = observations_setup.dependent_variable.elevation_angle_dependent_variable(
        link_end_type=transmitter
    )
    
    # Add the settings to the collection
    # This returns a parser for the sets where the variable is defined
    elevation_angle_parser = observation_collection.add_dependent_variable_settings(
        elevation_angle_settings,
        bodies
    )

The values themselves are not computed until you call :func:`~tudatpy.estimation.observations_setup.observations_wrapper.compute_residuals_and_dependent_variables`, which simulates the observations and calculates the dependent variables simultaneously.

When to Add Dependent Variables
--------------------------------

.. note::
   When creating an :class:`~tudatpy.estimation.observations.ObservationCollection` from **simulated data**, you can add the dependent variable settings directly to the simulation settings. The values will then be computed automatically when :func:`~tudatpy.estimation.observations_setup.observations_wrapper.simulate_observations` is called. For an :class:`~tudatpy.estimation.observations.ObservationCollection` created from **real data**, you must add the settings after creation and then call :func:`~tudatpy.estimation.observations_setup.observations_wrapper.compute_residuals_and_dependent_variables`.

Retrieving Dependent Variables
===============================

You can retrieve the computed values using the :meth:`~tudatpy.estimation.observations.ObservationCollection.dependent_variable` method. This method returns the dependent variable values and a parser that identifies which :class:`~tudatpy.estimation.observations.SingleObservationSet` objects contain this variable.

.. code-block:: python

    from tudatpy.estimation import observations_setup
    
    # Define settings for the elevation angle at the transmitter
    elevation_angle_settings = observations_setup.dependent_variable.elevation_angle_dependent_variable(
        link_end_type=transmitter
    )
    
    # Retrieve the computed values and the corresponding parser
    elevation_angle_values, elevation_angle_parser = observation_collection.dependent_variable(
        elevation_angle_settings
    )
    
    # Use the parser to get the corresponding observation times and values for plotting
    elevation_angle_times = observation_collection.get_concatenated_observation_times(
        elevation_angle_parser
    )
    elevation_angle_obs = observation_collection.get_concatenated_observations(
        elevation_angle_parser
    )

Available Dependent Variables
==============================

The following dependent variables are commonly used:

- **Elevation angle**: Angle of the target above the local horizon at a ground station
- **Azimuth angle**: Horizontal angle of the target from a reference direction
- **Range distance**: Distance between link ends
- **Line-of-sight vector**: Unit vector from one link end to another
- **Doppler shift**: Frequency shift due to relative motion

For a complete list of available dependent variables, see the API documentation for :mod:`tudatpy.estimation.observations_setup.dependent_variable`.

Example: Plotting Elevation Angle
==================================

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    
    # Compute residuals and dependent variables
    observations_setup.observations_wrapper.compute_residuals_and_dependent_variables(
        observation_collection,
        observation_simulators,
        bodies
    )
    
    # Define and retrieve elevation angle
    elevation_settings = observations_setup.dependent_variable.elevation_angle_dependent_variable(
        link_end_type=transmitter
    )
    elevation_values, elevation_parser = observation_collection.dependent_variable(elevation_settings)
    elevation_times = observation_collection.get_concatenated_observation_times(elevation_parser)
    
    # Plot elevation angle over time
    plt.figure(figsize=(10, 6))
    plt.plot(elevation_times, np.rad2deg(elevation_values))
    plt.xlabel('Time [s]')
    plt.ylabel('Elevation Angle [deg]')
    plt.title('Ground Station Elevation Angle')
    plt.grid(True)
    plt.show()
