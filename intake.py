import numpy as np
from inputs import *
import matplotlib.pyplot as plt

def get_intake_area():
    D = intake_geometries["Diameter"]
    return np.pi * D**2 / 4


def get_intake_force(intake_area):   # Not sure if this is correct
    v = performance_parameters["Velocity"]
    rho = environmental_parameters["Water density"]
    return v**2 * intake_area * rho


def get_intake_pressure(): # Total pressure at intake
    p_atm = environmental_parameters["Air pressure"]
    rho = environmental_parameters["Water density"]
    g = environmental_parameters["Gravity"]
    v = performance_parameters["Velocity"]
    intake_location = intake_geometries["Vertical location"]
    aeriated_length = performance_parameters["Altitude small aircraft"]
    p_dynamic = .5 * rho * v**2
    p_static = p_atm + rho * g * (intake_location - aeriated_length)
    intake_pressure = p_dynamic + p_static
    return intake_pressure


def get_intake_pressure_losses(v, L, tow_angle):
    rho = environmental_parameters["Water density"]
    nu = environmental_parameters["Water kinematic viscosity"]
    epsilon = intake_geometries["Roughness"]
    D = intake_geometries["Diameter"]

    # Calculate the losses due to the hose

    # Calculate Reynolds number
    Re = (v * D) / nu

    f = 1.325 * (np.log(epsilon / (3.7 * D) + 5.74 / Re**.9))**-2

    p_loss_hose = f * rho * v**2 * L / (2 * D)

    # Calculate the losses due to bends
    beta = airplane_geometries["Foil angle"]
    bends = [90 + beta, np.abs(90 - beta - tow_angle)]
    p_loss_bends = []
    for bend in bends:
        R, D, theta = 3 * intake_geometries["Diameter"] / 2, intake_geometries["Diameter"], bend
        kf = (0.0733 + 0.923 * (D / R)**3.5)* np.sqrt(np.deg2rad(theta))

        p_loss_bend = .5 * kf * rho * v**2

        p_loss_bends.append(p_loss_bend)

    p_loss_total = p_loss_height + p_loss_hose + sum(p_loss_bends)

    return p_loss_total


def gravity_pressure_loss():
    h = performance_parameters["Altitude A380"]
    rho = environmental_parameters["Water density"]
    g = environmental_parameters["Gravity"]
    return rho * g * (h + supercavitating_structure_geometries["Vertical length"] - performance_parameters["Altitude small aircraft"])


def hose_pressure_loss(D, L, v):
    rho = environmental_parameters["Water density"]
    nu = environmental_parameters["Water kinematic viscosity"]
    epsilon = intake_geometries["Roughness"]

    # Calculate Reynolds number
    Re = (v * D) / nu

    f = 1.325 * (np.log(epsilon / (3.7 * D) + 5.74 / Re**.9))**-2

    return f * rho * v**2 * L / (2 * D)


def bend_pressure_loss(v, theta):
    rho = environmental_parameters["Water density"]
    R, D = 3 * intake_geometries["Diameter"] / 2, intake_geometries["Diameter"]
    kf = (0.0733 + 0.923 * (D / R)**3.5)* np.sqrt(np.deg2rad(theta))
    return .5 * kf * rho * v**2


def expansion_pressure_loss(v):
    D1 = intake_geometries["Diameter"]
    D2 = intake_geometries["Hose diameter"]
    L = 3 * intake_geometries["Diameter"]
    rho = environmental_parameters["Water density"]
    alpha = 2 * np.arctan((D2 - D1) / (2 * L))
    r = D2 / D1
    kf = ((.25 / (alpha**3)) * (1 + (.6 / (r**1.67)) * ( (np.pi - alpha)/ alpha))**(.533 * r - 2.6))**-.5
    return .5 * kf * rho * v**2


def get_intake_velocity(intake_pressure, intake_pressure_losses):
    p_atm = environmental_parameters["Air pressure"]
    rho = environmental_parameters["Water density"]
    intake_velocity = np.sqrt(2 * (intake_pressure - intake_pressure_losses - p_atm) / rho)
    return intake_velocity


if __name__ == "__main__":
    intake_pressure = get_intake_pressure()
    v = np.arange(0, 70, 0.1)
    L = 60
    D = 0.12
    losses_darcy1_ = np.zeros(len(v))
    losses_darcy2_ = np.zeros(len(v))
    losses_HazenWilliams_ = np.zeros(len(v))
    bend_loss_ = np.zeros(len(v))
    for i in v:
        losses_darcy1_[int(i * 10)] = losses_darcy1(D, L, i)
        losses_darcy2_[int(i * 10)] = losses_darcy2(D, L, i)
        bend_loss_[int(i * 10)] = bend_loss(D, i, 45)
    plt.plot(v, losses_darcy1_, label="Darcy 1")
    plt.plot(v, losses_darcy2_, label="Darcy 2")
    plt.plot(v, losses_HazenWilliams_, label="Hazen-Williams")
    plt.plot(v, bend_loss_, label="Bend loss")
    plt.legend()
    plt.show()

    filling_time = 600
    Q = 100 / filling_time
    Intake_area = np.pi * D**2 / 4
    v = Q / Intake_area

    losses_darcy1 = losses_darcy1(D, L, v)
    losses_darcy2 = losses_darcy2(D, L, v)
    bend_loss = bend_loss(D, v, 45)

    print("Intake velocity: ", v)

        
    print("Darcy 1: ", losses_darcy1 / 100000, "bar")
    print("Darcy 2: ", losses_darcy2 / 100000, "bar")
    print("Bend loss: ", bend_loss / 100000, "bar")
    