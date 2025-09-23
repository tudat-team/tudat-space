class CustomGuidanceModel:

    def __init__(self, bodies: environment.SystemOfBodies):

        # Extract the STS and Earth bodies
        self.vehicle = bodies.get_body("Vehicle")
        self.earth = bodies.get_body("Earth")

        self.current_time = float("NaN")

    def get_aerodynamic_angles(self, current_time: float):

        # Update the class to the current time
        self.update_guidance( current_time )
        
        # Return angles calculated by update function
        return np.array([self.angle_of_attack, 0.0, self.bank_angle])

    def get_thrust_magnitude(self, current_time: float):

        # Update the class to the current time
        self.update_guidance( current_time )
        
        # Return angles calculated by update function
        return self.thrust_magnitude

    def update_guidance(self, current_time: float):

        if( math.isnan( current_time ) ):
	    # Set the model's current time to NaN, indicating that it needs to be updated 
            self.current_time = float("NaN")
        elif( current_time != self.current_time ):

            # Calculate current body orientation through angle of attack and bank angle
            self.angle_of_attack = ...
            self.bank_angle = ...

            # Calculate current thrust magnitude
            self.thrust_magnitude = ...

	    # Set the model's current time, indicating that it has been updated
            self.current_time = current_time
