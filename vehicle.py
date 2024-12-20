def get_vehicle_mass(airplane):   # Get airplane
    pass


def get_vehicle_downforce(vehicle_mass, hydrofoil_downforce):
    return vehicle_mass * environmental_parameters["Gravity"] + hydrofoil_downforce


def get_vehicle_drag(aero_drag, hydrofoil_drag, supercavitating_structure_drag, intake_drag):
    return aero_drag + hydrofoil_drag + supercavitating_structure_drag + intake_drag