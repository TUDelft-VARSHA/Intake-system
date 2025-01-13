import numpy as np

def get_chords(S, b, lam):
    cr = 2 * S / (b * (1 + lam))
    ct = lam * cr
    return cr, ct


def get_span(S, AR):
    return np.sqrt(S * AR)


def get_cmac(Cr, lam):
    return Cr * (2 / 3) * ((1 + lam + (lam**2)) / (1 + lam))


def calculate_wing_weight(Wdg, Nz, S, AR, tc, lam, sweep, Scontrol):
    return .0051 * (Wdg + Nz) ** .557 * S ** .649 * AR ** .5 * tc ** -.4 * (1 + lam) ** .1 * np.cos(np.deg2rad(sweep)) ** -1 * Scontrol ** .1


# Constants
Ch = .671
Cv = .0550

lf = 7.77

lambda_w = .2252
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

Sw = ...
Sw = 6.28
cmac = ...
cmac = 1.0170679
bw = ...
bw = 7

Crw, Ctw = get_chords(Sw, bw, lambda_w)

lh = lf * lh_percentage
lv = lf * lv_percentage

Sh = Ch * Sw * cmac / lh
Sv = Cv * Sw * bw / lv

bh = get_span(Sh, ARh)
bv = get_span(Sv, ARv)

Crh, Cth = get_chords(Sh, bh, lambda_h)
Crv, Ctv = get_chords(Sv, bv, lambda_v)

cmach = get_cmac(Crh, lambda_h)
cmacv = get_cmac(Crv, lambda_v)




print("These are the dimensions of the surfaces of the airplane:")
print()
print("Sw: ", Sw, "m^2")
print("Crw: ", Crw, "m")
print("Ctw: ", Ctw, "m")
print("cmac: ", cmac, "m")
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

Wwing = 3000
Scooping_structure = 4000 * 9.81
Nz = 1.9

Wdg = Wwing + Scooping_structure
dw = 1000

while dw > 0.01:
    Wi = Wdg
    Wwing = calculate_wing_weight(Wdg, Nz, Sw, ARw, .12, lambda_w, sweep_w, 0.10 * Sw)
    Wdg = Wwing + Scooping_structure
    dw = np.abs(Wi - Wdg)
    print(dw)
    

    
print("Wing weight: ", Wwing, "N")
print("Wing mass: ", Wwing / 9.81, "kg")
print("Wing loading: ", Wdg * 1.9 / Sw, "N/m^2")