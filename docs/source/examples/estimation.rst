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
  ./tudatpy-examples/estimation/mission_data_downloader.ipynb


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
  ./tudatpy-examples/estimation/kosmos482_reentry.ipynb


Estimation using real observations from DSN/ESTRACK
***************************************************

We also have the following examples that showcase the reading of, and estimation from radio tracking data from DSN/ESTRACK.

.. nbgallery::

  ./tudatpy-examples/estimation/mro_tnf_residuals_analysis.ipynb
  ./tudatpy-examples/estimation/grail_residuals.ipynb
  ./tudatpy-examples/estimation/grail_odf_estimation.ipynb
  ./tudatpy-examples/estimation/grail_spice_fit.ipynb
 
