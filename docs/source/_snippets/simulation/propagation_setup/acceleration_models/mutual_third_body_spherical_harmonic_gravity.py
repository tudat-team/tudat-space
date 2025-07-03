maximum_degree_of_io = 12
maximum_order_of_io = 12
maximum_degree_of_ganymede = 4
maximum_order_of_ganymede = 4
maximum_degree_of_jupiter = 4
maximum_order_of_jupiter = 4

acceleration_settings_on_io = dict(
            Earth = [ propagation_setup.acceleration.mutual_spherical_harmonic_gravity(
            	maximum_degree_of_jupiter, maximum_order_of_jupiter, maximum_degree_of_ganymede, maximum_order_of_ganymede
            	maximum_degree_of_io, maximum_order_of_io) ] 
        )