# Create the aerodynamic guidance object
aerodynamic_guidance_object = STSAerodynamicGuidance(bodies)

# Link getAerodynamicAngles function of aerodynamic_guidance_object to rotation model settings
rotation_model_settings = environment_setup.rotation_model.aerodynamic_angle_based(
    'Earth', '', 'STS_Fixed', aerodynamic_guidance_object.getAerodynamicAngles )

# Create rotation model from rotation model settings
environment_setup.add_rotation_model( bodies, 'STS', rotation_model_settings )
