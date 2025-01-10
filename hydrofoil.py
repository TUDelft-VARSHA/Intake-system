import numpy as np
from inputs import *

def get_cavitation_number():
    rho = environmental_parameters["Water density"]
    v = performance_parameters["Velocity"]
    pv = environmental_parameters["Water vapor pressure"]
    p = environmental_parameters["Air pressure"] + rho * environmental_parameters["Gravity"] * performance_parameters["Altitude small aircraft"]
    return (p - pv) / (.5 * rho * v**2)


def get_cavitator_cd(sigma):
    beta = supercavitating_structure_geometries["Cavitator cone angle"]
    return 0.0015 * beta * sigma + 0.5484 * sigma + 0.0047 * beta + 0.0545
    

def get_cavity_geometry(cd, sigma):      # Get these relations
    dc = supercavitating_structure_geometries["Cavitator diameter"]
    cavity_diameter = dc * np.sqrt(cd / sigma)
    cavity_length = (dc / sigma) * np.sqrt(cd * np.log(1 / sigma))
    return cavity_diameter, cavity_length


def get_supercavitating_structure_drag(cd):
    submerged_length = supercavitating_structure_geometries["Vertical length"] - performance_parameters["Altitude small aircraft"]
    diameter = supercavitating_structure_geometries["Cavitator diameter"]
    rho = environmental_parameters["Water density"]
    v = performance_parameters["Velocity"]
    return .5 * rho * v**2 * cd * submerged_length * diameter


def get_hydrofoil_downforce_and_drag(supercavitating_structure_drag, intake_drag, aircraft_mass, cg_location):      # Solve for hydrofoil downforce and drag
    submerged_length = supercavitating_structure_geometries["Vertical length"] - performance_parameters["Altitude small aircraft"]

    hydrofoil_location = hydrofoil_geometries["Vertical location"]
    intake_location = intake_geometries["Vertical location"]
    hose_location = airplane_geometries["Hose attachment location"]
    foil_location = np.tan(np.deg2rad(airplane_geometries["Foil angle"])) * hydrofoil_location
    liftdrag = hydrofoil_geometries["L/D"]

    # Assuming privot point is at the center of mass
    hydrofoil_downforce = (supercavitating_structure_drag * (performance_parameters["Altitude small aircraft"] + 0.5 * submerged_length) + intake_drag * intake_location) / (foil_location - hose_location + liftdrag**-1 * hydrofoil_location)
    hydrofoil_drag = hydrofoil_downforce * liftdrag**-1
    return hydrofoil_downforce, hydrofoil_drag


def get_hydrofoil_span(hydrofoil_downforce, Dc):     # Solve for hydrofoil span
    v = performance_parameters["Velocity"]
    rho = environmental_parameters["Water density"]
    chord = supercavitating_structure_geometries["Afterbody"]
    downforce_span = 2 * hydrofoil_downforce / (chord * v**2 * rho)
    return downforce_span + Dc