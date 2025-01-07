import numpy as np

def get_hose_properties(vehicle_downforce, vehicle_drag):
    tow_tension = np.sqrt(vehicle_downforce**2 + vehicle_drag**2)
    tow_angle = np.arctan(vehicle_downforce / vehicle_drag)
    return tow_tension, tow_angle


def get_hose_length(altitude, tow_angle):
    return altitude / np.sin(tow_angle)