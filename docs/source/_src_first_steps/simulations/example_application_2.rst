Propagating a Spacecraft with Perturbations
===========================================

In this example, we will propagate a spacecraft with several perturbations. Furthermore, we demonstrate how to plot your results in a variety of ways.

Import Statements and Setup
###########################

The first lines of code in your script should always be the (``tudatpy``) import statements. These import statements allow you to use the tools in ``tudatpy``.

.. code-block:: python

    import numpy as np
    from tudatpy.kernel import constants
    from tudatpy.kernel.interface import spice_interface
    from tudatpy.kernel.simulation import environment_setup
    from tudatpy.kernel.simulation import propagation_setup
    from tudatpy.kernel.astro import conversion


Important first steps to take are to (1) load the spice kernels, and (2) to set the start- and end epochs of your simulation. In ``tudat``, J2000 is t = 0, with all times given in seconds. The simulation end epoch is set to be one Julian day, which equals 86400 s.

.. code-block:: python

    spice_interface.load_standard_kernels()

    simulation_start_epoch = 0.0
    simulation_end_epoch = constants.JULIAN_DAY



Environment Setup
#################

Let's create the environment for your simulation. This setup covers the creation of (celestial) bodies, vehicle(s), and environment interfaces.

Create bodies
-------------

Bodies can be created by making a list of strings with the bodies you want to include in your simulation. The default body settings (such as atmosphere, body shape, rotation model) are taken from spice. These settings can be adjusted to your preference, see :ref:`available_environment_models` for more detail. Finally, the system of bodies is created using your settings and stored into the variable ``bodies``. 

.. code-block:: python
  
    bodies_to_create = ["Sun", "Earth", "Moon", "Mars", "Venus"]

    body_settings = environment_setup.get_default_body_settings(
        bodies_to_create,
        simulation_start_epoch,
        simulation_end_epoch,
        "Earth","J2000")

    bodies = environment_setup.create_system_of_bodies(body_settings)


Create vehicle
--------------

Now it's time to create your vehicle. In the following code, a vehicle named *Delfi-C3* is made, with a body mass of 400 kg.

.. code-block:: python
  
    bodies.create_empty_body( "Delfi-C3" )

    bodies.get_body( "Delfi-C3").set_constant_mass( 400.0 )

Create interfaces
-----------------

Interfaces define the interaction of the environment on the vehicle. This step is important for later defining accelerations that are dependent on
parameters defining the nature of the interaction. Below the aerodynamics coefficients interface and the radiation pressure interface are defined. For all the options, visit :ref:`available_environment_models`.

- **Aerodynamic Coefficients**
  


  .. code-block:: python
    
      reference_area = 4.0
      drag_coefficient = 1.2

      aero_coefficient_settings = environment_setup.aerodynamic_coefficients.constant(
          reference_area,[drag_coefficient,0,0],
          are_coefficients_in_aerodynamic_frame=True,
          are_coefficients_in_negative_axis_direction=True
      )

      environment_setup.add_aerodynamic_coefficient_interface(
                  bodies, "Delfi-C3", aero_coefficient_settings )


- **Radiation Pressure**

  .. code-block:: python

      reference_area_radiation = 4.0
      radiation_pressure_coefficient = 1.2
      occulting_bodies = ["Earth"]
      radiation_pressure_settings = environment_setup.radiation_pressure.cannonball(
          "Sun", reference_area_radiation, radiation_pressure_coefficient, occulting_bodies
      )

      environment_setup.add_radiation_pressure_interface(
                  bodies, "Delfi-C3", radiation_pressure_settings )


Propagation Setup
#################

Now that the environment is created, the propagation setup is defined. First, the bodies to be propagated and the central bodies will be defined, as given below.

.. code-block:: python

    bodies_to_propagate = ["Delfi-C3"]

    central_bodies = ["Earth"]

Create acceleration models
--------------------------

This is the place to define the accelerations acting on your vehicle, and create the acceleration models for propagation. For our vehicle, the *Delfi-C3*, we want the cannonball radiation pressure and aerodynamic accelerations as given by the interfaces defined above. Furthermore, gravitational accelerations are also defined; a spherical harmonic gravity exerted by Earth up to degree and order 5, and a point mass (central) gravity for the other celestial bodies.

- **Define Accelerations**

  .. code-block:: python

      accelerations_settings_delfi_c3 = dict(
          Sun=
          [
              propagation_setup.acceleration.cannonball_radiation_pressure(),
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Earth=
          [
              propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
              propagation_setup.acceleration.aerodynamic()
          ],
          Moon=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Mars=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ],
          Venus=
          [
              propagation_setup.acceleration.point_mass_gravity()
          ]
          )


  .. note::
    
    A more compact way of adding a point mass gravity of all bodies *except* a small selection, such as Earth in this case, can be done using the ``.difference()`` function in python. The same accelerations can be added in a more elegant manner, as given below:

    .. code-block:: python

        accelerations_settings_delfi_c3 = dict(
          Sun=
          [
              propagation_setup.acceleration.cannonball_radiation_pressure(),
          ],
          Earth=
          [
              propagation_setup.acceleration.spherical_harmonic_gravity(5, 5),
              propagation_setup.acceleration.aerodynamic()
          ]
          )
        
        for other in set(bodies_to_create).difference( { "Earth" } ):
          accelerations_settings_delfi_c3[other] = 
          [
              propagation_setup.acceleration.point_mass_gravity()
          ]


- **Create acceleration models**

  With the accelerations defined, the acceleration models are created by the code given below.

  .. code-block:: python
        
      acceleration_settings = {"Delfi-C3": accelerations_settings_delfi_c3}

      acceleration_models = propagation_setup.create_acceleration_models(
          bodies,
          acceleration_settings,
          bodies_to_propagate,
          central_bodies)


Define Initial System State
---------------------------

At the beginning of your script, you have defined a simulation start epoch, but you also need to define the initial state of your vehicle. For this case, we define a point along a Kepler orbit around Earth to be the initial state of *Delfi-C3*, and subsequently transform it to a Cartesian state using the ``conversion.keplerian_to_cartesian()`` function. Obviously, we need the gravitational parameter of our central body, Earth, which we can retrieve from the ``bodies`` variable.

.. code-block:: python
      
    earth_gravitational_parameter = bodies.get_body( "Earth" ).gravitational_parameter

    initial_state = conversion.keplerian_to_cartesian(
        gravitational_parameter = earth_gravitational_parameter,
        semi_major_axis = 7500.0E3,
        eccentricity = 0.1,
        inclination = np.deg2rad(85.3),
        argument_of_periapsis = np.deg2rad(235.7),
        longitude_of_ascending_node = np.deg2rad(23.4),
        true_anomaly = np.deg2rad(139.87)
    )


Define dependent variables to save
----------------------------------

Apart from the state history, you can specify certain dependent variables to be saved, which you can later use for analysis. For *Delfi-C3*, we want to save the total acceleration, Keplerian state, latitude and longitude and the acceleration norms of all the accelerations, which we will plot later. Here is a list of all the :ref:`available_dependent_variables`.

.. code-block:: python
      
    dependent_variables_to_save = [
        propagation_setup.dependent_variable.total_acceleration( "Delfi-C3" ),
        propagation_setup.dependent_variable.keplerian_state( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.latitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.longitude( "Delfi-C3", "Earth" ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Sun" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Moon" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Mars" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.point_mass_gravity_type, "Delfi-C3", "Venus" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.spherical_harmonic_gravity_type, "Delfi-C3", "Earth" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.aerodynamic_type, "Delfi-C3", "Earth" 
        ),
        propagation_setup.dependent_variable.single_acceleration_norm( 
            propagation_setup.acceleration.cannonball_radiation_pressure_type, "Delfi-C3", "Sun" 
        )
        ]



Create propagator settings
--------------------------

We have defined all the ingredients for the propagator settings. Let's create translational propagator settings for this case. For more detailes, also for other propagator dynamics, visit :ref:`simulation_propagator_setup`.

.. code-block:: python
      
    propagator_settings = propagation_setup.propagator.translational(
        central_bodies,
        acceleration_models,
        bodies_to_propagate,
        initial_state,
        simulation_end_epoch,
        output_variables = dependent_variables_to_save
    )


Create integrator settings
--------------------------

The simulator also required an integrator to be defined. The integrator settings for a Runge-Kutta 4 integrator can be defined as given below. We have chosen to use a step size of 10.0 s, you might want to change that for your simulation, depending on the type of integrator and propagation time. For more integrator settings, please visit :ref:`simulation_integrator_settings`.

.. code-block:: python
      
    fixed_step_size = 10.0

    integrator_settings = propagation_setup.integrator.runge_kutta_4(
        simulation_start_epoch,
        fixed_step_size
    )

Simulator Usage
###############

Let's simulate our vehicle for the given epochs. This is done by creating a dynamics simulator with your bodies and integrator- and propagator settings.

Create dynamics simulator
-------------------------

.. code-block:: python
      
    dynamics_simulator = propagation_setup.SingleArcDynamicsSimulator(
        bodies, integrator_settings, propagator_settings)

Retrieve result
---------------

You can retrieve the states and dependent variables at time step in your simulation by using ``.state_history`` and ``.dependent_variable_history``, respectively, on the dynamics simulator object.

.. code-block:: python
      
    states = dynamics_simulator.state_history

    dependent_variables = dynamics_simulator.dependent_variable_history

Visualize results
-----------------

Let's make some plots to visualize our simulation results. In order to make plots in python, import pyplot from matplotlib.

.. code-block:: python
      
    from matplotlib import pyplot as plt


- **Pre-processing**

  The first step we have to take is to extract relevant variables from our dependent_variables dictionary. The times are stored in the keys, and can be extracted using the ``.keys( )`` function. The actual dependent variables are in the values of the dictionary, and we use ``.values( )`` to extract these, and subsequently stack them vertically using ``np.vstack( )`` in order to select the desired columns.

  .. code-block:: python
        
      time = dependent_variables.keys( )

      dependent_variable_list = np.vstack( list( dependent_variables.values( ) ) )



  .. note::

    These columns correspond to the dependent variables we have saved. To make your own list, visit :ref:`available_dependent_variables`.

    .. list-table:: Column indices for the dependent variables.
     :widths: 50 50
     :header-rows: 1

     * - Column Indices
       - Dependent variable
     * - 0-2
       - Total Acceleration
     * - 3-8
       - Keplerian State
     * - 9
       - Latitude
     * - 10
       - Longitude
     * - 11-17
       - Acceleration Norms

  We also convert the time axis to be in the units of hours instead of seconds, which is optional. For this, we make use of *list comprehensions* in python:

  .. code-block:: python

      time_hours = [ t / 3600 for t in time]

  .. note::

    Using

    .. code-block:: python

      time_hours = time / 3600

    will **not** work in python, it will result in an ``TypeError``.


- **Total Acceleration**

  Let's plot the first dependent variable: total acceleration. The first three columns in the ``dependent_variable_list`` are the total acceleration in each Cartesian direction. Let's take the norm of these vectors for each time, to obtain the total accceleration norm. Note that we could have also used the ``total_acceleration_norm`` dependent variable.

  .. code-block:: python

      total_acceleration_norm = np.sqrt( dependent_variable_list[:,0] ** 2 + dependent_variable_list[:,1] ** 2 + dependent_variable_list[:,2] ** 2 )


  The first step is to make a figure to make your plot in.

  .. code-block:: python

      plt.figure( figsize=(17,5) )


  Next, let's plot the total acceleration norm as a function of time.

  .. code-block:: python

      plt.plot( time_hours , total_acceleration_norm )

  We can set the axis labels using ``plt.xlabel( )`` and ``plt.ylabel( )``.

  .. code-block:: python

      plt.xlabel( 'Time [hr]' )
      plt.ylabel( 'Total Acceleration [m/s$^2$]' )


  Also, for better appearance, we limit the horizontal axis to the minimum and maximum values of time using ``plt.xlim()``. In addition, we add a grid to the plot using ``plt.grid( )``.

  .. code-block:: python

      plt.xlim( [min(time_hours), max(time_hours)] )
      plt.grid()

  We save the figure using ``plt.savefig( )``. As an argument, we use ``bbox_inches='tight'``, this will result in less redundant white space around your figure.

  .. code-block:: python

      plt.savefig( fname = 'total_acceleration.eps', bbox_inches='tight')

  Which results in the following figure:

  .. image:: figures/total_acceleration.png

- **Ground Track**

  Let's repeat the same to obtain a plot for the ground track. The latitude and longitude are stored as columns 9 and 10 in ``dependent_variable_list``. We only want the ground track of the first three hours of our simulation. The plotting procedure is the same as before, with two differences.

  1. Here we use a scatter plot, by using the command ``plt.scatter( )``, due to the nature of the plot. The argument ``s`` inside represent the size of each bullet.
  2. We modify the vertical ticks using ``plt.yticks( )`` command. We want it to have a tick every 45 degrees.

  .. code-block:: python

      latitude = dependent_variable_list[:,9]
      longitude = dependent_variable_list[:,10]

      hours = 3
      subset = int( len(time) / 24 * hours )
      latitude = np.rad2deg( latitude[ 0 : subset ] )
      longitude = np.rad2deg( longitude[ 0 : subset ] )

      plt.figure( figsize=(17,5))
      
      plt.scatter( longitude, latitude, s=1 )

      plt.xlabel( 'Longitude [deg]' )
      plt.ylabel( 'Latitude [deg]' )

      plt.xlim( [min(longitude), max(longitude)] )
      plt.yticks(np.arange(-90, 91, step=45))
      plt.grid()
      plt.savefig( fname = 'ground_track.eps', bbox_inches='tight')


  Which results in the following figure:

  .. image:: figures/ground_track.png

- **Kepler Elements**
  
  Plotting of the Kepler elements can be done exactly the same as shown before, just by selecting the right column in the ``dependent_variable_list``. However, here we take it one step further. We want to plot each Kepler element in a single plot, using six subplots.

  First, let's extract the Kepler elements from the dependent variables.
  
  .. code-block:: python

    kepler_elements = dependent_variable_list[ :, 3:9 ]


  First step in making the subplots is to define which arrangement you want. Here we specify a 3x2 arrangement.

  .. code-block:: python

    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots( 3, 2, figsize = (20,17) )


  So let's plot each Kepler element in a subplot. The procedure is exactly the same as before, only we use the ``ax`` for our plot command, and we use ``set_ylabel( )`` to make the vertical axis labels. Since the horizontal axis label for each plot is the same (time), we will set this in a single command later.

  .. code-block:: python

    # Semi-major Axis
    semi_major_axis = [ element/1000 for element in kepler_elements[:,0] ]
    ax1.plot( time_hours, semi_major_axis )
    ax1.set_ylabel( 'Semi-major axis [km]' )

    # Eccentricity
    eccentricity = kepler_elements[:,1]
    ax2.plot( time_hours, eccentricity )
    ax2.set_ylabel( 'Eccentricity [-]' )

    # Inclination
    inclination = [ np.rad2deg( element ) for element in kepler_elements[:,2] ]
    ax3.plot( time_hours, inclination )
    ax3.set_ylabel( 'Inclination [deg]')

    # Argument of Periapsis
    argument_of_periapsis = [ np.rad2deg( element ) for element in kepler_elements[:,3] ]
    ax4.plot( time_hours, argument_of_periapsis )
    ax4.set_ylabel( 'Argument of Periapsis [deg]' )

    # Right Ascension of the Ascending Node
    raan = [ np.rad2deg( element ) for element in kepler_elements[:,4] ]
    ax5.plot( time_hours, raan )
    ax5.set_ylabel( 'RAAN [deg]' )

    # True Anomaly
    true_anomaly = [ np.rad2deg( element ) for element in kepler_elements[:,5] ]
    ax6.scatter( time_hours, true_anomaly, s=1 )
    ax6.set_ylabel( 'True Anomaly [deg]' )
    ax6.set_yticks(np.arange(0, 361, step=60))

  As you can see, we make use of list comprehensions to convert some Kepler elements from radians to degrees, or to convert the semi-major axis from m to km. Also, we use the scatter plot for the True Anomaly. 

  As previously mentioned, let's set each horizontal axis label as time in a single command. Also, we will tweak the horizontal axis limits again to the minimum and maximum time in the history, and add a grid to each subplot. Finally, we save the image.

  .. code-block:: python

    for ax in fig.get_axes():
      ax.set_xlabel('Time [hr]')
      ax.set_xlim( [min(time_hours), max(time_hours)] )
      ax.grid()

    fig.savefig( fname = 'kepler_elements.eps', bbox_inches='tight')


  Which results in the following figure:

  .. image:: figures/kepler_elements.png

- **Acceleration Norms**

  For this plot, we want to combine all the different acceleration norms into a *single* figure, color each line, and add a legend. Furthermore, due to the large difference in order of magnitude of each acceleration, we will demonstrate how to use a vertical log scale in your plot.

  Let's start by plotting each acceleration norm in a single figure. The colors are automatically assigned to each plot. You can see that we already label each plot using the ``label=' '`` argument. Again, we add a grid, set the horizontal axis limits, and set axis labels.

  .. code-block:: python

    plt.figure( figsize=(17,5))

    # Point Mass Gravity Acceleration Sun
    acceleration_norm_pm_sun = dependent_variable_list[:, 11]
    plt.plot( time_hours, acceleration_norm_pm_sun, label='PM Sun')

    # Point Mass Gravity Acceleration Moon
    acceleration_norm_pm_moon = dependent_variable_list[:, 12]
    plt.plot( time_hours, acceleration_norm_pm_moon, label='PM Moon')

    # Point Mass Gravity Acceleration Mars
    acceleration_norm_pm_mars = dependent_variable_list[:, 13]
    plt.plot( time_hours, acceleration_norm_pm_mars, label='PM Mars')

    # Point Mass Gravity Acceleration Venus
    acceleration_norm_pm_venus = dependent_variable_list[:, 14]
    plt.plot( time_hours, acceleration_norm_pm_venus, label='PM Venus')

    # Spherical Harmonic Gravity Acceleration Earth
    acceleration_norm_sh_earth = dependent_variable_list[:, 15]
    plt.plot( time_hours, acceleration_norm_sh_earth, label='SH Earth')

    # Aerodynamic Acceleration Earth
    acceleration_norm_aero_earth = dependent_variable_list[:, 16]
    plt.plot( time_hours, acceleration_norm_aero_earth, label='Aerodynamic Earth')

    # Cannonball Radiation Pressure Acceleration Sun
    acceleration_norm_rp_sun = dependent_variable_list[:, 17]
    plt.plot( time_hours, acceleration_norm_rp_sun, label='Radiation Pressure Sun')

    plt.grid()
    
    plt.xlim( [min(time_hours), max(time_hours)])
    plt.xlabel( 'Time [hr]' )
    plt.ylabel( 'Acceleration Norm [m/s$^2$]' )


  In order to include a legend in our plot, we use ``plt.legend( )``. Furthermore, we use the ``bbox_to_anchor`` argument to position the legend *outside* of our figure.

  .. code-block:: python

    plt.legend( bbox_to_anchor=(1.04,1) )


  We use a vertical log scale simply by:

  .. code-block:: python 

    plt.yscale('log')

  Finally, we save the figure.

  .. code-block:: python

    plt.savefig( fname = 'acceleration_norms.eps', bbox_inches='tight')

  Which results in the following figure:
  
  .. image:: figures/acceleration_norms.png

    










