# Merge panels lists
list_panel_body_settings = [
    bus_panels, hga_panels, sapx_panels, samx_panels
    ]

# Merge rotation settings (BUS by default coincides with body-fixed frame)
dict_rotation_settings = {
    "MRO_HGA_OUTER_GIMBAL": hga_rotation_settings,
    "MRO_SAPX": sapx_rotation_settings,
    "MRO_SAMX": samx_rotation_settings
    }

# Create FullPanelledBodySettings
full_panelled_body = environment_setup.vehicle_systems.full_panelled_body_settings(
    list_panel_body_settings,
    dict_rotation_settings
    )

# Assign FullPanelledBodySettings to the vehicle (here MRO)
body_settings.get('MRO').vehicle_shape_settings = full_panelled_body