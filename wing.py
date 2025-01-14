
import numpy as np
from math import *
import matplotlib.pyplot as plt


#Wing planform variables
AR = 7.8 #aspect ratio [m] #same aspect ratio as A380
b = 7 #wingspan [m] #max value based on diameter of the fuselage A380
labda = 0.2252 #taper ratio [m] from A380. 
Sweep_LE = 33.5 #sweep angle [deg], same as for A380
W_wing = 200 #weight of the wing [kg], guess number

def wing(AR,b,labda):
    A_wing = (b**2)/AR #wing surface area [m]

    C_avg = (Cr + Ct)/2 #average chord [m]

    Cr = (2*A_wing)/(b*(1+labda))   #rootchord [m]

    Ct = labda*Cr #tipchord [m]

   
    cmac = Cr * (2/3) * (( 1 + labda + (labda**2) ) / ( 1 + labda ))

    return A_wing, Cr, Ct, C_avg, cmac

A_wing, Cr, Ct, C_avg, MAC = wing(AR,b,labda)

weight_boom = 2500 #weight of the boom [kg]
height = 47 #height while scooping [m]
rho = 1.2195 
V = 80 #speed aircraft while sc
q = 0.5 * rho * (V**2) #dynamic pressure

def CL(q, weight_boom, A_wing,Sweep_LE):
    Cl_1 = 1.1 * (1/q) * (weight_boom/A_wing)
    Cl_des = Cl_1/((cos(Sweep_LE))**2)
    return Cl_1, Cl_des



#Fuselage variables
L_fus = 4.2 #length of fuselage estimated value [m]
R_fus = 1 #radius of fuselage estimated value [m]
W_fus = 4000 #weight of the fuselage

#conventional tail variables
C_H = 0.671 #horizontal tail volume coefficient (flying boat)
C_V = 0.0550 #vertical tail volume coefficient  (flying boat)

L_HT = 0.462 * L_fus  # Horizontal tail arm [m] from literature
L_VT = 0.418 * L_fus  # Vertical tail arm [m] from literature

# R_HT = S_HT/S_W #ratio between surface area horizontal tail and surface area wing
R_HT = 0.3 #from literature 
# R_VT = S_VT/S_W #ratio between surface area vertical tail and surface area wing
R_VT = 0.3 #guess?
W_tail = 200 #weight of tail

def tail(R_HT, A_wing, R_VT):
    S_HT = R_HT * A_wing
    S_VT = R_VT * A_wing
    return(S_HT, S_VT)

S_HT, S_VT = tail(R_HT, A_wing, R_VT)

#Determine drag of small aircraft
V = 76 #velocity of aircraft [m/s]
rho = 1.225 #random number
rho_water = 1 
cd0 = 0.015
e = 0.5 #oswald factor
CL = 0.02 #random number
cdi = (CL**2)/(np.pi * AR* e)
CD = cdi + cd0 #random number
q = 0.5 * rho * (V**2) #dynamic pressure


def drag(CD, q, A_wing): #drag adds to total drag of A380
    Drag = CD * q * A_wing
    return Drag

#Determine drag of hose/hydrofiel in water 
D_intake = 50666.66667 #intake drag [N], drag adds to total drag of A380 
D_hose = 13730.66667

#Determine lift of small aircraft
V = 76 #velocity of aircraft [m/s]
rho = 1.225 #random number
CL = 0.02 #random number
q = 0.5 * rho * (V**2) #dynamic pressure

def lift(CL, q, A_wing):
    Lift = CL * q * A_wing
    return Lift 

# check if lift created equals weight of small aircraft
def weight_check(W_fus, W_tail, W_wing, Lift):
    W_tot = W_fus + W_tail + W_wing
    if Lift >= W_tot:
        return "Lift is sufficient to balance the weight of the aircraft."
    else:
        return "Lift is insufficient"


#stability margin = (x_ac - x_cg)/c_mac

#Determine centre of gravity locations measured from nose

def center_of_gravity(W_fus, W_wing, W_tail, x_fus, x_wing, x_tail):
    total_weight = W_fus + W_wing + W_tail
    x_CG = (W_fus * x_fus + W_wing * x_wing + W_tail * x_tail) / total_weight
    return x_CG

#Determine aerodynamic center locations





###########################################################################################
# Sample defined variables (adjust these based on your actual aircraft data)
x_ac = 0.25  # Example aerodynamic center location (normalized to MAC)
MAC = 1.2  # Mean aerodynamic chord [m]
Cm_ac = -0.02  # Moment coefficient about the aerodynamic center
CL_Ah = 0.4  # Wing-body lift coefficient
CL_h = -0.35 * S_h**(1/3)        # Tail lift coefficient
CL_alpha_h = 4.4  # Horizontal tail lift curve slope
CL_alpha_Ah = 5.7  # Wing-body lift curve slope
de_da = 0.5  # Elevator effectiveness
S_h = 1.5  # Tail surface area [m²]
S = 5.0  # Wing surface area [m²]
l_h = 3.0  # Tail moment arm [m]
c_bar = MAC  # Mean aerodynamic chord [m]
V_h = 60  # Tail velocity [m/s]
V = 62  # Aircraft velocity [m/s]
###########################################################################################

#stability margin
#stability margin of 5 percent
def stability_margin(x_CG, x_AC, C_MAC):
    SM = (x_AC - x_CG) / C_MAC
    return SM


x_np = x_ac + (CL_alpha_h/CL_alpha_Ah)*(1 - (de_da))*((S_h*l_h)/(S*c_bar))*((V_h/V)**2)

# x_ac + (CL_alpha_h/CL_alpha_Ah)*(1 - (de/da))*((l_h)/(c_bar))*((V_h/V)**2)
SM = 0.05
x_c_g = x_np - SM

# R1 = S_h/S
x_c_g = np.arange(0, L_fus)/MAC  
R1 = []
for i in range(0, len(x_c_g)):
    x = ((1/(CL_alpha_h/CL_alpha_Ah)*(1 - (de_da))*((l_h)/(c_bar))*((V_h/V)**2))* x_c_g[i]) - ((x_ac - 0.05)/(CL_alpha_h/CL_alpha_Ah)*(1 - (de_da))*((l_h)/(c_bar))*((V_h/V)**2))
    R1.append(x)

print(x_c_g, "R1", R1)
# x_c_g = np.linspace(0, L_fus,100)/MAC #center of gravity range

#rear limit from stability
plt.plot(x_c_g, R1)
plt.show()


xcg = x_ac - (Cm_ac/CL_Ah) + (CL_h/CL_Ah)*((S_h*l_h)/(S * c_bar))*((V_h/V)**2)

       
xcg = np.linspace(0, L_fus, 100)     
xcg = np.arange(0, L_fus)/MAC  
R2 = []
for i in range(0, len(xcg)):
    x  = ((1/((CL_h/CL_Ah)*((l_h)/(c_bar))*((V_h/V)**2)))*xcg[i]) + ((Cm_ac/CL_Ah) - x_ac)/ ((CL_h/CL_Ah)*((l_h)/(c_bar))*((V_h/V)**2)) 
    R2.append(x)
print(xcg, "R2", R2)
#forward limit from control
plt.plot(xcg, R2)
plt.show()



# C_MGC = (2/3)* Cr * ((1+labda+(labda**2))/(1+labda)) #Mean geometric chord
# C_MAC = C_MGC
# Sweep_LE = 4 #sweep angle leading edge
# Y_MGC_LE = (b/6)*((1+2*labda)/labda) #Y-location of MGC_LE
# X_MGC_LE = Y_MGC_LE* np.tan(Sweep_LE) #X- locattion of MGC_LE
# Angle_c4 = np.arccos(Sweep_LE) + ((Cr/2*b)*(labda-1))

# S_HT = 4
# S_W = 8.2
# L_HT = 0.462 * L_fus #Lever arm s_cg - s_MAC_HT
# C_HT = (S_HT*L_HT)/(S_W* MAC) #tail volume coefficient for horizontal tail

# L_VT = 0.418 * L_fus #lever arm s_cg - s_MAC_VT
# C_VT = (S_VT * L_VT)/ (S_w * b) #tail volume coefficient vertical tail

#Lever arm must be estimated to determine the size of a tail. 
#Longer tail arm --> smaller tail area


#create loading diagram






