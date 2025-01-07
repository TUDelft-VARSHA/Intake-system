import numpy as np
from inputs import *
from airplane import *
from intake import *
from hydrofoil import *
from vehicle import *
from hose import *


if __name__ == "__main__":
    # 1. Get airplane properties


    # 2. Get intake properties
    intake_pressure = get_intake_pressure(performance_parameters["Filling time"],
                                          performance_parameters["Capacity"],
                                          performance_parameters["Velocity"])

    intake_area = get_intake_area()

    intake_force = get_intake_force() # Use intake_pressure and intake_area
    intake_drag = get_intake_drag()

    intake_pressure_losses = get_intake_pressure_losses() # Use intake_pressure and intake_area

    intake_exit_pressure = get_intake_exit_pressure() # Use intake_pressure_losses

    intake_cavitation_load_case() # Use intake_exit_pressure

    # 3. Get supercavitating structure properties
    cavitation_drag_coefficient, cavity_radius, cavity_length = get_cavitation_properties() # Use cavitator cone angle and environmental parameters

    supercavitating_structure_drag = get_supercavitating_structure_drag() # Use cavitation_drag

    # 4. Get hydrofoil properties
    hydrofoil_downforce, hydrofoil_drag = get_hydrofoil_downforce_and_drag() # Use hose location and all drags and their locations

    hydrofoil_span, hydrofoil_chord = get_hydrofoil_geometry() # Use hydrofoil_downforce and hydrofoil_drag and cavity radius and length

    # 5. Get vehicle materials and thicknesses

    # structural stuff

    # 6. Get vehicle properties
    vehicle_mass = get_vehicle_mass()

    vehicle_downforce = get_vehicle_downforce(vehicle_mass, hydrofoil_downforce)

    vehicle_drag = get_vehicle_drag()
    
    # 7. Get hose properties

    tow_tension, tow_angle = get_hose_properties(vehicle_downforce, vehicle_drag)

    hose_length = get_hose_length(altitude, tow_angle)