=====================================
Use of Environment During Propagation
=====================================

Each body object and its constituent members is updated to the current state and time automatically during the numerical propagation. We stress that only those models that are relevant for a given propagation are updated every time step (this is handled automatically, without user intervention). Some time-dependent properties of the body are set in the environment models themselves. Others are updated and stored directly in the Body object. Below is a full list of (possibly) time varying environment models, and how to retrieve them from a body object during propagation.

- **The current translational state**

	Retrieved directly with the ``get_state`` function as Cartesian elements. Note that this state is always in the global frame origin and orientation.

	.. tip:: 

		Separate ``get_position`` and ``get_velocity`` functions are also available.

- **The current rotational state**

	The current orientation is defined by the body’s rotation model, and is retrieved as a quaternion. To get the quaternion to transform a vector from inertial (e.g. with global frame orientation) to the body-fixed frame, the ``get_current_rotation_to_local_frame`` can be used. The inverse rotation can be obtained from ``get_current_rotation_to_global_frame``. The time-derivative of the orientation is provided in two formulations (with equivalent information content): the angular velocity vector, and the time derivative of the rotation matrix. The angular velocity vector, in inertial and body-fixed coordinates, is obtained from the ``get_current_angular_velocity_vector_in_global_frame`` and ``get_current_angular_velocity_vector_in_local_frame`` functions respectively. The time-derivative of the rotation matrix from inertial to body-fixed frame is given by ``get_current_rotation_matrix_derivative_to_local_frame``, while the derivative of the inverse rotation is taken from ``get_current_rotation_matrix_derivative_to_global_frame``.

- **The current body mass**

	Retrieved directly with the ``get_body_mass`` function.

- **Spherical harmonic gravity field coefficients**

	These coefficients may be time variable. The cosine and sine coefficients can be retrieved from a body object through its gravity field model. A piece of example code on retrieving these coefficients is given below for the case of Earth: (TODO-Dominic)

	.. code-block:: python

		bodies = ....

		try:
			spherical_harmonics_gravity_field = bodies.at( "Earth " ).spherical_harmonics_gravity_field
			cosine_coefficients = spherical_harmonics_gravity_field.get_cosine_coefficients( )
			sine_coefficients = spherical_harmonics_gravity_field.get_sine_coefficients( )

		except:
			print( "Error when retrieving spherical harmonic coefficients: Earth does not have a spherical harmonics gravity field" )

	Note the ``try/except`` blocks in the code. These checks are very helpful in ascertaining the reason for a crashing program.

- **The current flight conditions**

	The ``flight_conditions`` class, and its derived class ``atmospheric_flight_conditions`` stores data relating to altitude, flight angles, atmospheric properties, etc. Follow the links for their detailed description (TODO).


.. note::

	As a user, you will typically not access these variables directly. Important examples of cases where users can explicitly access them, are custom aerodynamic or thrust guidance.