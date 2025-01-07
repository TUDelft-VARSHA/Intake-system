import numpy as np

def get_intake_area(filling_time, capacity, velocity):
    return capacity / (velocity * filling_time)


def get_intake_force(intake_area, velocity, density):   # Not sure if this is correct
    return velocity**2 * intake_area * density


def get_intake_drag(intake_force, intake_area):  # Not sure if this is correct
    return intake_force * intake_area


def get_intake_pressure(intake_force, intake_area): # Not sure if this is correct
    return intake_force / intake_area


def get_intake_pressure_losses():   # Should come from literature
    pass


def get_intake_exit_pressure(intake_pressure, intake_pressure_losses):
    return intake_pressure - intake_pressure_losses


def intake_cavitation_load_case():  # Should come from literature
    pass


if __name__ == "__main__":
    print("Hello")

    intake_area = get_intake_area()

    intake_force = get_intake_force() # Use intake_area

    intake_pressure = get_intake_pressure()

    intake_drag = get_intake_drag()

    intake_pressure_losses = get_intake_pressure_losses() # Use intake_pressure and intake_area

    intake_exit_pressure = get_intake_exit_pressure() # Use intake_pressure_losses

    intake_cavitation_load_case() # Use intake_exit_pressure