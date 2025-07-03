.. _aerodynamic_models:

===================
Use of aerodynamics
===================

When including aerodynamics in the orbit propagation, it may often be desirable to have the aerodynamic properties of the vehicle depend on the vehicle's state, and its interaction with the environment. This is the case for ascent and entry for instance. Also, control surface deflections may be needed to modify the vehicle's behaviour. Both options are included in Tudat, and the interfaces are described below.

An aerodynamic acceleration combines various environment properties for its computation:

* Atmosphere model for the central body, used to compute the density :math:`\rho`. Depending on the selected :doc:`atmosphere models <atmosphere>`, this density may be dependent on altitude only, or on time and the vehicle's position (e.g. altitude, latitude, longitude)
* Aerodynamic coefficients of the body. The :doc:`aerodynamic coefficients <aerodynamic_coefficients>` may be defined in the aerodynamic frame (:math:`[C_{D}, C_{S}, C_{L}]`) or the body-fixed frame (:math:`[C_{X}, C_{Y}, C_{Z}]`). These coefficients may be a function of any number of independent variables (see :class:`~tudatpy.numerical_simulation.environment.AerodynamicCoefficientsIndependentVariables` for available dependencies).
* The orientation of the vehicle w.r.t. the inertial frame.  This is required to rotate the acceleration to the inertial frame from the aerodynamic or body-fixed frame (see :ref:`aerodynamics_during_propagation`). See :ref:`below <aerodynamic_orientation>` for details on typical approaches in the context of aerodynamics
* The current state of the vehicle (taken from the state vector during propagation) is needed to compute the altitude (typical input for density), the latitude, longitude, vertical and trajectory frames, which are used to transform the acceleration to an inertial frame, and may also have an influence on the aerodynamic coefficients (for instance, if they are Mach number dependent).
* The current deflection of control surfaces (if the vehicle is equipped with control surfaces). The definition of, and interaction with, control surfaces is discussed in more detail :ref:`below <control_surfaces>`

Below, some issues specific to the setup of a simulation using aerodynamics are presented. A number of considerations related to concurrent thrust and aerodynamic forces are provided :ref:`here <thrust_and_aerodynamics>`

.. _aerodynamic_orientation:

Vehicle orientation
===================

A rotation model for the vehicle undergoing aerodynamic acceleration is required, which is used to provide the rotation from aerodynamic to inertial frame :math:`\mathbf{R}^{(I/A)}` or from body-fixed to inertial frame :math:`\mathbf{R}^{(I/B)}` (depending on the frame in which the aerodynamic coefficients are calculated). Depending on the models that are used, one or more of the angles :math:`\alpha`, :math:`\beta` and :math:`\sigma` (angle of attack, sideslip angle, bank angle) are required.

For the determination of the matrix :math:`\mathbf{R}^{(I/B)}`, we can distinguish three different approaches in the context of aerodynamics:
  
*  The vehicle has a rotation model defined using the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based` (or, related, the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based`) model. By using one of these functions, the rotation between inertial and  body-fixed frame is *defined by* a user-provided input of the angles :math:`\alpha`, :math:`\beta` and :math:`\sigma`, in combination with quantities computed from the vehicle's current translational state w.r.t. its central body (see :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based` for details).
*  The vehicle has any other rotation model defined, in this case the angles :math:`\alpha`, :math:`\beta` and :math:`\sigma` are computed from the :math:`\mathbf{R}^{(I/B)}` matrix produced by this rotation model.
*  The rotational dynamics of the vehicle is propagated, and the orientation of the vehicle is taken from the current rotational state. The angles :math:`\alpha`, :math:`\beta` and :math:`\sigma` are then computed from the current rotational state of the vehicle.

The first option, in which the user provides models for the angles :math:`\alpha`, :math:`\beta` and :math:`\sigma` directly, is discussed in more detail here, as this is a model typically applied for applications driven by aerodynamics (such as re-entry). Particularly, we will discuss a number of ways in which to define aerodynamic angles directly through the :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`.

Constant angles
~~~~~~~~~~~~~~~

In simple simulations, a user may want to define a constant :math:`\alpha`, :math:`\beta` and/or :math:`\sigma`. The code block below gives an example on how to do this (:math:`\alpha=40^{\circ}`, :math:`\beta=0^{\circ}` and :math:`\sigma=20^{\circ}`):

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. code-block:: python

        # Define constant angles
        angle_of_attack = np.deg2rad( 40.0 )
        bank_angle = np.deg2rad( 20.0 )
        
        # Define angle function (required for input to rotation settings)   
        angle_function = lambda time : np.array([angle_of_attack, 0.0, bank_angle])
        
        # Create settings for rotation model
        rotation_model_settings = environment_setup.rotation_model.aerodynamic_angle_based(
            central_body="Earth",
            target_frame = "VehicleFixed",
            angle_function = angle_function ) 
            
This defines settings for the rotation model, which can then be assigned the body settings, see :ref:`override_body_settings`, or used directly to update the rotation model, see :ref:`decorate_empty_body`. The above will *not* result in a constant :math:`\mathbf{R}^{(I/B)}` rotation matrix, since the vehicle's translational state will still change over time, leading to a change in the orientation of the trajectory frame (see :func:`~tudatpy.numerical_simulation.environment_setup.rotation_model.aerodynamic_angle_based`). What the above will do is define the vehicle to have a constant orientation *w.r.t. the oncoming flow*. Note that if the above function is used without ``angle_function`` input, the three angles will be set to 0.

Alternatively, the angle of attack may be defined based on pitch trim, so that the value of :math:`\alpha` is found for which :math:`C_{m}=0`. This requires :math:`\alpha`-dependent aerodynamic moment coefficients to be defined). When doing so, the sideslip and bank angle are left free and are 0 by default. However, a user may specify these angles as follows"

.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python
    
    .. code-block:: python

        # Define constant angles
        bank_angle = np.deg2rad( 20.0 ) 
        
        # Define angle function (required for input to rotation settings)   
        angle_function = lambda time : np.ndarray([0.0, bank_angle])
        
        # Create settings for rotation model
        rotation_model_settings = environment_setup.rotation_model.zero_pitch_moment_aerodynamic_angle_based(
            central_body="Earth",
            target_frame = "VehicleFixed",
        )

Note that the ``angle_function`` now returns only two angles, instead of the three angles in the previous example, as the :math:`\alpha` is no longer user-specified.
                
Time- and environment-dependent angles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A more complicated algorithm to compute the aerodynamic angles may be defined using custom models. Below, a simple example (depending only on time) is provided for illustrative purposes. A discussion of the definition of more complex models (depending on state, environment, time, *etc.*) is describe on the dedicated :ref:`custom_models` page.


.. tab-set::
   :sync-group: coding-language

   .. tab-item:: Python
    :sync: python

    .. literalinclude:: /_snippets/simulation/environment_setup/custom_class_simple_aero_angles.py
        :language: python

The above example will apply the model :math:`\alpha=\dot{\alpha}(t-t_{0})` (and similar for :math:`\sigma`), so that the angles vary linearly over time.

Aerodynamic moments
===================

In Tudat, aerodynamic moment coefficients can be provided and used in the same manner as aerodynamic force coefficients when (for instance) propagating rotational dynamics. Nominally, the aerodynamic force coefficients are *not* used to compute a correction to the aerodynamic moments, implicitly assuming that the aerodynamic moment reference point is equal to the vehicle's center of mass. However, in some cases, for instance where the center-of-mass is time-variable, the contribution of the force coefficients to the moment coefficients is to be taken into account. This is handled by the :attr:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings.add_force_contribution_to_moments` attribute of the :attr:`~tudatpy.numerical_simulation.environment_setup.aerodynamic_coefficients.AerodynamicCoefficientSettings` class. If a (non-NaN) moment reference point is provided to the aerodynamic coefficient settings, this boolean is automatically set to True. To disable the addition of the force contribution to the moment coefficients, this attribute can be manually set to False after the creation of the aerodynamic coefficient settings. 

.. _control_surfaces:

Control surfaces
================

For a high-fidelity vehicle entry/ascent trajectory propagation, it will often be necessary to include control surface deflections in the numerical propagation. How to define and use the aerodynamic influence of control surfaces is discussed here. The control surfaces of a vehicle influence is behaviour by incrementing the aerodynamic forces and moments. In Tudat, each control surface is defined by:
 
* A dedicated aerodynamic coefficient interface
* A name (which is used to reference the specific control surface)
* A current deflection (initiated at 0)

A control surface is created as follows: 

If a body has :math:`N` control surfaces assigned to it, the coefficient increments will be added to the total coefficients during each time step, without any required user interaction. User interaction with the control surfaces is typically limited to defining an algorithm defining the deflections as a function of time. 

TODO: write documentation for implementation in Tudat



