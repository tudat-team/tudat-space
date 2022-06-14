# Create the aerodynamic guidance object
guidance_object = STSAerodynamicGuidance(bodies)

# Set aerodynamic guidance (this line links the STSAerodynamicGuidance settings with the propagation)
environment_setup.set_aerodynamic_guidance(guidance_object, bodies.get_body("STS"))
