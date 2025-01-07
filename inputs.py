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
    "Air density": 1.225,
    "Air pressure": 101325,
    "Gravity": 9.81,
    "Wind speed": 0,
    "Wind angle": 0,
}

airplane_geometries = {
    "Fuselage": {
        "length": 10,
        "radius": 1,
    },
    "Wing": {
        "span": 10,
        "chord": 1,
    },
    "Horizontal stabiliser": {
        "span": 5,
        "chord": 1,
    },
    "Vertical stabiliser": {
        "height": 5,
        "chord": 1,
    },
    "Hose location": 0.5,       # From the front
    "Foil location": 0.5,       # From the front
}

supercavitating_structure_geometries = {
    "Submerged span": 5,
    "Aeriated span": 5,
    "Chord": 1,
    "Cavitator cone angle": 10,     # Probably set this to 45 degrees
    "Intake location": 0.5,         # From the top
    "Hydrofoil location": 0.5,      # From the top
    "Hydrofoil Cl": 0.42,           # at 5 degrees angle of attack
    "Hydrofoil L/D": 12.17,         # at 5 degrees angle of attack
}

performance_parameters = {
    "Velocity": 62,
    "Altitude": 80,
    "Capacity": 100,
    "Filling time": 10,
    "Deployment time": 10,
    "Retraction time": 10,
}
