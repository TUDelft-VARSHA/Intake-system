
import numpy as np
from math import *
import matplotlib.pyplot as plt


#Wing planform variables
AR = 7.8 #aspect ratio [m] #same aspect ratio as A380
b = 14 #wingspan [m] #max value based on diameter of the fuselage A380
labda = 0.26 #taper ratio [m] from A380. 
Sweep_LE = ((33.5/180)*pi) #sweep angle [rad], same as for A380
# W_wing = 200 #weight of the wing [kg], guess number

def wing(AR,b,labda):
    A_wing = (b**2)/AR #wing surface area [m]

    # C_avg = (Cr + Ct)/2 #average chord [m]

    Cr = (2*A_wing)/(b*(1+labda))   #rootchord [m]

    Ct = labda*Cr #tipchord [m]

   
    MAC = Cr * (2/3) * (( 1 + labda + (labda**2) ) / ( 1 + labda ))

    return A_wing, Cr, Ct, MAC, 

A_wing, Cr, Ct, MAC = wing(AR,b,labda)
print(A_wing, Cr, Ct, MAC)

# def wing_2(b, CL, )

weight_boom = (4000*9.81)/1000 #weight of the boom [KN]
weight_aircraft = (2000*9.81)/1000 #weight of the boom [kg] guess in kN
Force_hydrofoil = 0#110 #force downwards by the hydrofoil [kN]
Tension = 10.8 #force in the cable [KN]
Force_tension_y = Tension * sin((38/180)*pi)
Force_tension_x = Tension * cos((38/180)*pi)
# print(Force_tension_x)
# Lift = weight_boom - Force_tension_y +Force_hydrofoil + weight_aircraft 
Lift = weight_boom - Force_tension_y + weight_aircraft
Lift = 42.5
Lift = 38.4
D_dis = 0#48000 #distributed drag [N/m]
D_int = 0#33000 #intake drag [N]
D_hyd = 0#9000 #hydrofoil drag [N]
Drag = (Force_tension_x*1000) - D_int - D_hyd - (D_dis * 2)
# print(Drag)

height = 47 #height while scooping [m]
rho = 1.2195 
V = 80 #speed aircraft while sc
q = 0.5 * rho * (V**2) #dynamic pressure
A_wing = A_wing
print(A_wing)

def CL(q, Lift, A_wing, Sweep_LE):
    Cl_1 = 1.1 * (1/q) * (Lift*1000/A_wing)
    Cl_des = Cl_1/((cos(Sweep_LE))**2)

    return Cl_1, Cl_des

print("CL=",CL(q, Lift, A_wing, Sweep_LE))
Cl_1, Cl_des = CL(q, Lift, A_wing, Sweep_LE)
print(Cl_des)
# print(Lift)


#Determine drag of small aircraft

e = 0.8186
cd0 =0.016
cdi = (Cl_des**2)/(np.pi * AR* e)
print(cdi)
CD = cdi + cd0 #random number
print(CD)
q = 0.5 * rho * (V**2) #dynamic pressure
rho = 1.2195 
V = 80 #speed aircraft while sc
q = 0.5 * rho * (V**2) #dynamic pressure
A_wing = A_wing


def drag(CD, q, A_wing): #drag adds to total drag of A380
    Drag = CD * q * A_wing
    return Drag

drag = drag(CD,q,A_wing)
print(drag)


def Cd(Drag, V, A_wing, rho):
    Cd = (2*Drag)/(rho*(V**2)*A_wing)
    return Cd

# print(Cd(138000,V,A_wing,rho))

def Cd0(Cd, CL, e, AR):
    Cd0 = Cd - ((CL**2)/(pi*e*AR))
    return Cd0



# FD = #distributed drag force
# FI = #drag at intake
# FD_h = # drag hydrofoil
# Fh = #force hydrofoil
# x_ac = #horizontal distance to aerodynamic center
# x_c = #horizontal distance to cable hook up point
# x_cg = #horizontal distance to centre of gravity
# x_n = #horizontal distance to neutral point
# x_b = #horizontal distance to boom
# x_h = #horizontal distance to hydrofoil
# y_D = #vertical distance to distributed drag force
# y_D_h = #vertical distance to drag of hydrofoil
# y_I = #vertical distance to the drag of intake

# M_ac = 2

# M_cg = (-L * (x_cg - x_ac)) - M_ac + (L_h* (x_h -x_cg))

# M_HT = M_ac + weight_aircraft*(x_cg - x_ac) + (FD*y_D) + (FI*y_I) + (FD_h*y_D_h) + (Fh*(x_b-x_ac)) - (Force_tension_y *(x_h-x_ac))+(weight_boom*(x_b-x_ac))
