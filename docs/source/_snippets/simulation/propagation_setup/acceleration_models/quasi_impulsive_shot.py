thrust_mid_times =  [ 1.0 * 3600.0, 2.0 * 3600.0, 3.0 * 3600.0 ]
delta_v_values [ [ 0.3E-3, -2.5E-3, 3.4E-3 ],
				 [ 2.0E-3, 5.9E-3, -0.5E-3 ],
				 [ -1.6E-3, 4.4E-3, -5.8E-3] ]

total_maneuver_time = 90.0
maneuver_rise_time = 15.0


acceleration_settings_on_vehicle = dict(
            Apollo = [ propagation_setup.acceleration.quasi_impulsive_shot( thrust_mid_times, delta_v_values, total_maneuver_time, maneuver_rise_time) ] 
        )
