love_number = 0.1
time_lag = 100.0

acceleration_settings_on_Io = dict(
            Jupiter = [ propagation_setup.acceleration.direct_tidal_dissipation(love_number, time_lag, False, False) ] 
        )