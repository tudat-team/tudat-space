===============================
Valid Time-Range of Environment
===============================

Most of the environment models are valid for any time, but there is a key exception. In particular, the default settings do not directly use the Spice ephemerides, but retrieve the state for each body from Spice, and then create a ``tabulated_ephemeris`` (which is only valid in the given time range), as opposed to a ``spice_ephemeris``, which is valid for the entire time interval that the Spice kernels contain data. This approach is taken for computational reasons: retrieving a state from Spice is very time-consuming, much more so than retrieving it from a 6th- or 8th-order Lagrange interpolator that is used here for the tabulated ephemeris. An additional consequence of this is that the start and end time of the environment must be slightly (3 times the integration time step) larger than that which is used for the actual propagation, as a Lagrange interpolator can be unreliable at the edges of its domain. It is also possible to use the ``spice_ephemeris`` directly, at the expense of longer runtimes, by creating the ``bodies`` as:

.. code-block:: python

	bodies_to_create = [ "...", "..." ]
	body_settings = environment_setup.get_default_body_settings( bodies_to_create )

	bodies = environment_setup.create_system_of_bodies( body_settings )

