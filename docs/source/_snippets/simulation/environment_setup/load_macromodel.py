# Define material properties
hga_material_properties = {
    'HGA_front': environment_setup.vehicle_systems.material_properties(...),
    'HGA_back': environment_setup.vehicle_systems.material_properties(...)
    }

# Define re-radiation settings
hga_reradiation_settings = {
    'HGA_front': True,
    'HGA_back': True
    }

# Define frame origin
hga_frame_origin = np.array([
    0.0, -3.15, -1.52
    ])

# Load .dae part
hga_panels = environment_setup.vehicle_systems.body_panel_settings_list_from_dae(
    "path/to/hga.dae",
    hga_frame_origin,
    hga_material_properties,
    hga_reradiation_settings,
    "mm",                        # units of .dae part
    "MRO_HGA_OUTER_GIMBAL"      # omit this if it coincides to the body-fixed frame
    )  

# Add rotation settings for moving parts
hga_rotation_settings = environment_setup.rotation_model.spice(
 'MRO_SPACECRAFT','MRO_HGA_OUTER_GIMBAL', ""
 )