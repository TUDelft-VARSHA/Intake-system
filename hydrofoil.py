def get_cavity_geometry():    # Get drag coefficient and cavity radius and length
    return cavity_radius, cavity_length


def get_supercavitating_structure_drag(cavitation_drag_coefficient, submerged_span, rho, velocity):        # Which area to use?
    return .5 * rho * velocity**2 * cavitation_drag_coefficient * ...          


def get_hydrofoil_downforce_and_drag(supercavitating_structure_drag, intake_drag, submerged_span, aeriated_span, intake_location, hydrofoil_location, hose_location, foil_location, liftdrag):      # Solve for hydrofoil downforce and drag
    hydrofoil_downforce = (supercavitating_structure_drag * (aeriated_span + 0.5 * submerged_span) + intake_drag * intake_location) / (foil_location - hose_location + liftdrag**-1 * hydrofoil_location)
    hydrofoil_drag = hydrofoil_downforce * liftdrag**-1
    return hydrofoil_downforce, hydrofoil_drag


def get_hydrofoil_span(hydrofoil_downforce, cavity_radius, chord, velocity, density):     # Solve for hydrofoil span
    chord = chord - 1
    downforce_span = 2 * hydrofoil_downforce / (chord * velocity**2 * density)
    return downforce_span + cavity_radius


if __name__ == "__main__":
    print("Hello")

    cavitation_drag, cavity_radius, cavity_length = get_cavitation_properties() # Use cavitator cone angle and environmental parameters

    supercavitating_structure_drag = get_supercavitating_structure_drag() # Use cavitation_drag

    hydrofoil_lift, hydrofoil_drag = get_hydrofoil_lift_and_drag() # Use hose location and all drags and their locations

    hydrofoil_span, hydrofoil_chord = get_hydrofoil_geometry() # Use hydrofoil_lift and hydrofoil_drag and cavity radius and length