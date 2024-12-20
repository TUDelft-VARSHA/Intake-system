def get_cavitation_properties():    # Get drag/m and cavity radius and length
    pass


def get_supercavitating_structure_drag(cavitation_drag, submerged_span):
    return cavitation_drag * submerged_span


def get_hydrofoil_lift_and_drag():
    pass


def get_hydrofoil_geometry():
    pass


def get_super_cavitating_structure_mass():
    pass

def get_hydofoil_mass():
    pass


if __name__ == "__main__":
    print("Hello")

    cavitation_drag, cavity_radius, cavity_length = get_cavitation_properties() # Use cavitator cone angle and environmental parameters

    supercavitating_structure_drag = get_supercavitating_structure_drag() # Use cavitation_drag

    hydrofoil_lift, hydrofoil_drag = get_hydrofoil_lift_and_drag() # Use hose location and all drags and their locations

    hydrofoil_span, hydrofoil_chord = get_hydrofoil_geometry() # Use hydrofoil_lift and hydrofoil_drag and cavity radius and length