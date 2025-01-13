# All spacial dimensions are in m, m^2 or m^3
# All speed/velocity dimensions are in m/s
# All acceleration dimensions are in m/s^2
# All time dimensions are in s
# All mass dimensions are in kg
# All angle dimensions are in radians
# All density dimensions are in kg/m^3
# All pressure dimensions are in Pa

environmental_parameters = {
    "Water density": 1000,
    "Water kinematic viscosity": 1e-6,
    "Water vapor pressure": 2339,
    "Air density": 1.225,
    "Air pressure": 101325,
    "Gravity": 9.81,
}

airplane_geometries = {
    "Hose attachment location": 0.5,    # From the front
    "Foil attachment location": 0.5,    # From the front
    "Foil angle": 45,                    # w.r.t. vertical
}

supercavitating_structure_geometries = {
    "Vertical length": 6,
    "Forebody": 0.325,
    "Afterbody": 0.4,
    "Base": 0.12,
    "Cavitator cone angle": 45,     
    "Cavitator diameter": 0.05,
}

hydrofoil_geometries = {
    "Vertical location": 6,      # From the top

    # Asummed constant for low sigma's
    "Cl": 0.42,           # at 5 degrees angle of attack
    "L/D": 12.17,         # at 5 degrees angle of attack
}

intake_geometries = {
    "Diameter": 0.08,
    "Hose diameter": 0.125,
    "Roughness": 0.00005,       # PVC
    "Vertical location": 5.5,                # From the top
}

performance_parameters = {
    "Velocity": 80,
    "Altitude A380": 47,
    "Altitude small aircraft": 4,
    "Capacity": 100,
}