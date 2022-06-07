class SimpleCustomGuidanceModel:

    def __init__(self, bodies: environment.SystemOfBodies):

        # Extract the STS and Earth bodies
        self.vehicle = bodies.get_body("Vehicle")
        self.earth = bodies.get_body("Earth")


    def getThrustMagnitude(self, current_time: float):

	if( current_time == current_time ):

            # Update the class to the current time
            self.thrust_magnitude = ...
        
            # Return angles calculated by update function
            return self.thrust_magnitude

