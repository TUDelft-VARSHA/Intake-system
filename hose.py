import numpy as np
from inputs import *

def get_hose_properties(vehicle_downforce, vehicle_drag):
    tow_tension = np.sqrt(vehicle_downforce**2 + vehicle_drag**2)
    tow_angle = np.rad2deg(np.arctan(vehicle_downforce / vehicle_drag))
    return tow_tension, tow_angle


def get_hose_length(tow_angle):
    altitude = performance_parameters["Altitude A380"]
    return altitude / np.sin(np.deg2rad(tow_angle))