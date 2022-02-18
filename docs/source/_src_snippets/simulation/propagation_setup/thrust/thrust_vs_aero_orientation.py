# Define thrust direction settings from state guidance
thrust_direction_settings = thrust.thrust_direction_from_state_guidance(
    central_body,
    is_colinear_with_velocity=True,
    direction_is_opposite_to_vector=True
)

# Use constant thrust magnitude settings
thrust_magnitude_settings = thrust.constant_thrust_magnitude(thrust_magnitude=1.5e3, specific_impulse=315)

# Create the dictionary containing the thrust acceleration
acceleration_dict = {
    "Vehicle":
        {"Vehicle": [
            propagation_setup.acceleration.thrust_from_direction_and_magnitude(
                thrust_direction_settings,
                thrust_magnitude_settings
            )
        ]}
}
# Create the acceleration model in the system of bodies
acceleration_model = propagation_setup.create_acceleration_models(
    system_of_bodies, accelerations_on_vehicle_dict, bodies_to_propagate, central_bodies
)

# Define aerodynamic guidance
class AeroGuidance(propagation.AerodynamicGuidance):

    def __init__(self):
        # Call the base class constructor
        propagation.AerodynamicGuidance.__init__(self)

    def updateGuidance(self, current_time):
        # Update angle of attack
        self.angle_of_attack = np.deg2rad(1.5) * np.sin(current_time*np.pi/750)

# Add the aerodynamic guidance to the Vehicle body
environment_setup.set_aerodynamic_guidance(AeroGuidance(), system_of_bodies.get("Vehicle"), silence_warnings=True)