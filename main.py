import numpy as np
from inputs import *
from airplane import *
from intake import *
from hydrofoil import *
from vehicle import *
from hose import *


if __name__ == "__main__":
    # 1. Get airplane properties

    airplane_drag = 1576
    airplane_mass = 457
    fuselage_length = 7.7
    cg_location = 0

    # 2. Get intake properties

    intake_pressure = get_intake_pressure()

    intake_area = get_intake_area()

    intake_drag = get_intake_force(intake_area) # Use intake_pressure and intake_area

    # 3. Get supercavitating structure properties

    cavitation_number = get_cavitation_number()

    cavitator_cd = get_cavitator_cd(cavitation_number)

    cavity_diameter, cavity_length = get_cavity_geometry(cavitator_cd, cavitation_number)

    if cavity_diameter < supercavitating_structure_geometries["Base"] or cavity_length < supercavitating_structure_geometries["Forebody"] + supercavitating_structure_geometries["Afterbody"]:
        print("Cavity diameter", cavity_diameter, "m")
        print("Cavity length", cavity_length, "m")
        print("Structure is not fully inside the cavity")
        exit()
        
    
    supercavitating_structure_drag = get_supercavitating_structure_drag(cavitator_cd)

    supercavitating_structure_length = supercavitating_structure_geometries["Vertical length"] / np.cos(np.deg2rad(airplane_geometries["Foil angle"]))

    # 4. Get hydrofoil properties
    hydrofoil_downforce, hydrofoil_drag = get_hydrofoil_downforce_and_drag(supercavitating_structure_drag, intake_drag, airplane_mass, cg_location)

    hydrofoil_span = get_hydrofoil_span(hydrofoil_downforce, cavity_diameter)

    # 5. Get vehicle materials and thicknesses

    hydrofoil_mass = 500
    supercavitating_structure_mass = 3500

    # 6. Get vehicle properties
    vehicle_mass = get_vehicle_mass(airplane_mass, supercavitating_structure_mass, hydrofoil_mass)

    vehicle_downforce = get_vehicle_downforce(vehicle_mass, hydrofoil_downforce)

    vehicle_drag = get_vehicle_drag(airplane_drag, hydrofoil_drag, supercavitating_structure_drag, intake_drag)
    
    # 7. Get hose properties

    tow_tension, tow_angle = get_hose_properties(vehicle_downforce, vehicle_drag)

    hose_length = get_hose_length(tow_angle)

    # 8. Get filling time

    intake_velocities = np.arange(0.01, 100, 0.0001)
    for v2 in intake_velocities:
        gravity_loss = gravity_pressure_loss()
        v1 = ((intake_geometries["Hose diameter"]**2) / (intake_geometries["Diameter"]**2)) * v2
        bend1_pressure_loss = bend_pressure_loss(v1, 90 + airplane_geometries["Foil angle"])
        bend2_pressure_loss = bend_pressure_loss(v1, np.abs(90 - airplane_geometries["Foil angle"] - tow_angle))
        expansion_loss = expansion_pressure_loss(v1)
        hose_pressure_loss1 = hose_pressure_loss(intake_geometries["Diameter"], supercavitating_structure_length, v1)
        hose_pressure_loss2 = hose_pressure_loss(intake_geometries["Hose diameter"], hose_length, v2)
        
        total_pressure_loss = gravity_loss + bend1_pressure_loss + bend2_pressure_loss + expansion_loss + hose_pressure_loss1 + hose_pressure_loss2

        intake_velocity = get_intake_velocity(intake_pressure, total_pressure_loss) # Use intake_pressure and intake_pressure_losses and intake_area

        print("v1", v1, "m/s")
        print("v2", v2, "m/s")
        print("Intake velocity", intake_velocity, "m/s")
        print("Total pressure loss", total_pressure_loss)

        if np.abs(intake_velocity - v2) < 0.1:
            break

    flow_rate = (np.pi * intake_geometries["Hose diameter"]**2 / 4) * intake_velocity
    filling_time = performance_parameters["Capacity"] / flow_rate

    # 9. Print results
    print()
    print("Tow tension: ", tow_tension / 1000, "kN")
    print("Tow angle: ", tow_angle, "deg")
    print("Hose length: ", hose_length, "m")
    print()
    print("Intake area: ", intake_area, "m^2")
    print("Intake pressure: ", intake_pressure / 100000, "bar")
    print("Gravity pressure loss: ", gravity_loss / 100000, "bar")
    print("Bend 1 pressure loss: ", bend1_pressure_loss / 100000, "bar")
    print("Bend 2 pressure loss: ", bend2_pressure_loss / 100000, "bar")
    print("Expansion pressure loss: ", expansion_loss / 100000, "bar")
    print("Hose pressure loss 1: ", hose_pressure_loss1 / 100000, "bar")
    print("Hose pressure loss 2: ", hose_pressure_loss2 / 100000, "bar")
    print("Total pressure loss: ", total_pressure_loss / 100000, "bar")
    print("Intake velocity: ", intake_velocity, "m/s")
    print("Flow rate: ", flow_rate, "m^3/s")
    print("Filling time: ", filling_time / 60, "min")
    print()
    print("Cavitation number: ", cavitation_number)
    print("Cavitator drag coefficient: ", cavitator_cd)
    print("Supercavitating structure drag: ", supercavitating_structure_drag / 1000, "kN")
    print("Supercavitating structure length", supercavitating_structure_length, "m")
    print("Intake drag: ", intake_drag / 1000, "kN")
    print("Hydrofoil drag: ", hydrofoil_drag / 1000, "kN")
    print("Hydrofoil downforce: ", hydrofoil_downforce / 1000, "kN")
    print("Hydrofoil span: ", hydrofoil_span, "m")
    print()
    print("Vehicle mass: ", vehicle_mass, "kg")
    print("Vehicle downforce: ", vehicle_downforce / 1000, "kN")
    print("Vehicle drag: ", vehicle_drag / 1000, "kN")
