source_body = "Sun"
area = 20.0
radiation_pressure_coefficient = 1.2
occulting_bodies = ["Earth"]

body_settings[ "Spacecraft" ].radiation_pressure_settings[ source_body ](source_body, area, radiation_pressure_coefficient, occulting_bodies)