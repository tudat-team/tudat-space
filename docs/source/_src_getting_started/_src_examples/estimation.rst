.. _estimation_examples:

====================
Estimation
====================

Estimation using simulated observations
***************************************

In the following examples, observations are simulated and then used as input for a covariance analysis and/or estimation.

.. nbgallery::

  ./tudatpy-examples/estimation/covariance_estimated_parameters.ipynb
  ./tudatpy-examples/estimation/covariance_propagation_example.ipynb
  ./tudatpy-examples/estimation/full_estimation_example.ipynb
  ./tudatpy-examples/estimation/estimation_dynamical_models.ipynb

Functionality to support estimation
***********************************

In the following examples, functionality is showcased that can be used to support (pre- and/or post-processing of observations) estimation

.. nbgallery::

  ./tudatpy-examples/estimation/tudat_azimuth_elevation_example.ipynb


.. _estimation_using_pseudo_observations:

Estimation using pseudo-observations data
*****************************************

In the following examples, Cartesian positions of bodies are taken from an external source and used as observations to which a Tudat dynamical model is fit.

.. nbgallery::

  ./tudatpy-examples/estimation/galilean_moons_state_estimation.ipynb
  

.. _estimation_using_real_observations:

Estimation using real observations
**********************************

In the following examples, real observations are used to fit compute residuals and/or compute dynamics of spacecraft and/or natural bodies.

.. nbgallery::

  ./tudatpy-examples/estimation/retrieving_mpc_observation_data.ipynb
  ./tudatpy-examples/estimation/estimation_with_mpc.ipynb
  ./tudatpy-examples/estimation/improved_estimation_with_mpc.ipynb
  ./tudatpy-examples/estimation/mro_range_estimation.ipynb

Estimation using real observations - Python only
************************************************

We also have the following examples that showcase the reading of, and estimation from radio tracking data from DSN/ESTRACK. Using these examples requires tudatpy to have been compiled by high-precision time representation (which is not currently available through these conda packages) The examples provide instructions on how to compile your own tudatpy kernel with the required settings.

.. workaround until the .py files are available as .ipynb files

.. toctree::

  doppler-data-analysis/mro_residuals_analysis
  doppler-data-analysis/grail_odf_estimation
  doppler-data-analysis/grail_residuals
  doppler-data-analysis/grail_spice_fit
 
