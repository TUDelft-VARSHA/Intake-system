import numpy as np
import matplotlib.pyplot as plt

def get_S(AR, b):
    return (b**2)/AR


def get_averagechord(Cr, Ct):
    return (Cr + Ct)/2


def get_chords(S, b, lam):
    cr = 2 * S / (b * (1 + lam))
    ct = lam * cr
    return cr, ct


def get_span(S, AR):
    return np.sqrt(S * AR)


def get_cmac(Cr, lam):
    return Cr * (2 / 3) * ((1 + lam + (lam**2)) / (1 + lam))


def get_Cl(rho, v, L, S, sweep):
    Cl = 1.1 * 2 * L / (rho * v**2 * S)
    return Cl/((np.cos(np.deg2rad(sweep)))**2)


def get_Cdi(Cl, AR, e):
    return Cl**2 / (np.pi * AR * e)


def get_drag_air(cd, rho, v, S):
    return .5 * cd * rho * v**2 * S


def get_lift_air(cl, rho, v, S):
    return .5 * cl * rho * v**2 * S


def get_Lh(L, Wair, xcgw, Wboom, Dboom, lh):
    return -L * xcgw + Wair * xcgw + Wboom * 3 - Dboom * 3 / (lh + xcgw)


def calculate_wing_weight(Wdg, Nz, S, AR, tc, lam, sweep, Scontrol):
    return .0051 * (Wdg + Nz) ** .557 * S ** .649 * AR ** .5 * tc ** -.4 * (1 + lam) ** .1 * np.cos(np.deg2rad(sweep)) ** -1 * Scontrol ** .1


def print_dimensions():
    print("These are the dimensions of the surfaces of the airplane:")
    print()
    print("Sw: ", Sw, "m^2")
    print("Crw: ", Crw, "m")
    print("Ctw: ", Ctw, "m")
    print("cmac: ", cmacw, "m")
    print("bw: ", bw, "m")
    print()
    print("Sh: ", Sh, "m^2")
    print("Crh: ", Crh, "m")
    print("Cth: ", Cth, "m")
    print("cmach: ", cmach, "m")
    print("bh: ", bh, "m")
    print()
    print("Sv: ", Sv, "m^2")
    print("Crv: ", Crv, "m")
    print("Ctv: ", Ctv, "m")
    print("cmacv: ", cmacv, "m")
    print("bv: ", bv, "m")
    print()
    print("lh: ", lh, "m")
    print("lv: ", lv, "m")


def print_masses():
    print("Gross weight: ", Wdg / 9.81, "kg")
    print("Structure weight: ", scooping_structure / 9.81, "kg")



def print_forces():
    print("Lift: ", L / 1000, "kN")
    print("Lift tail: ", Lh / 1000, "kN")
    print("Drag air: ", D_air / 1000, "kN")
    print("Drag boom: ", D_boom / 1000, "kN")
    print("Drag: ", D_total / 1000, "kN")
    print("Tension: ", T / 1000, "kN")
    print("Scoop drag: ", scoop_drag / 1000, "kN")


# Constants
rho = 1.225
v = 80

Ch = .671
Cv = .0550

lf = 10

lambda_w = .26
sweep_w = 33.5
ARw = 7.8

lambda_h = .45
sweep_h = 38.5
ARh = 3.9

lambda_v = .45
sweep_v = 18
ARv = 1.7

lh_percentage = .47
lv_percentage = .447

bw = 14
Sw = get_S(ARw, bw)
Crw, Ctw = get_chords(Sw, bw, lambda_w)
cmacw = get_cmac(Crw, lambda_w)

lh = lf * lh_percentage
lv = lf * lv_percentage

Sh = Ch * Sw * cmacw / lh
Sv = Cv * Sw * bw / lv
Sv = Sv / 2

bh = get_span(Sh, ARh)
bv = get_span(Sv, ARv)

Crh, Cth = get_chords(Sh, bh, lambda_h)
Crv, Ctv = get_chords(Sv, bv, lambda_v)

cmach = get_cmac(Crh, lambda_h)
cmacv = get_cmac(Crv, lambda_v)

scooping_structure = 4000 * 9.81
Wair = 457 * 9.81
Wdg = scooping_structure + Wair
Nz = 1.9

L = 42500
Cd0 = 0.016

D_boom = .5 * rho * v**2 * .12 * 6 * 1.55

dL = 1000
while dL > 0.001:
    Li = L
    Cl = get_Cl(rho, v, L, Sw, sweep_w)
    Cd = Cd0 + get_Cdi(Cl, ARw, .8186)
    ClCd = Cl / Cd
    D_air = L * ClCd**-1
    D_total = D_boom + D_air
    # Wair = L - scooping_structure
    # Wdg = scooping_structure + Wair
    T = D_total / np.cos(np.deg2rad(38))
    L = Wdg - np.sin(np.deg2rad(38)) * T
    dL = np.abs(Li - L)
    print("L: ", L / 1000, "kN")
    print("Wdg: ", Wdg / 9.81, "kg")

scoop_drag = .5 * rho * v**2 * Sw * Cd0

print("Cl/Cd: ", ClCd)
print("Cl: ", Cl)
print("Cd: ", Cd)


xcgw = 104654.765 / (L - 9810)
xcgw = 4.5
Lh = get_Lh(L, Wair, xcgw, scooping_structure, D_boom, lh)

Clh = get_Cl(rho, v, Lh, Sh, sweep_h)
print("Clh: ", Clh)

print_dimensions()
print_masses()
print_forces()

Lw = 46250
Lh = -7631
Clw = get_Cl(rho, v, Lw, Sw, sweep_w)
Clh = get_Cl(rho, v, Lh, Sh, sweep_h)
print("Clw: ", Clw)
print("Clh: ", Clh)