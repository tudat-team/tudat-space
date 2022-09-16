class STSAerodynamicGuidance:

    def __init__(self, bodies: environment.SystemOfBodies):
        ...

    # Function that is called at each simulation time step to update the ideal bank angle of the vehicle
    def getAerodynamicAngles(self, current_time: float):

        self.angle_of_attack = ...
	self.bank_angle = ...
	return np.array([self.angle_of_attack, 0.0, self.bank_angle])

