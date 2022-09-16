class STSAerodynamicGuidance(propagation.AerodynamicGuidance):

    def __init__(self, bodies: environment.SystemOfBodies):
        # Call the base class constructor
        propagation.AerodynamicGuidance.__init__(self)
        ...

    # Function that is called at each simulation time step to update the ideal bank angle of the vehicle
    def updateGuidance(self, current_time: float):

        self.angle_of_attack = ...
	self.bank_angle = ...
