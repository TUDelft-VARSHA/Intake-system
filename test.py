import numpy as np
from math import *

#Wing planform variables
AR = 6 #aspect ratio [m] #typical for small aircrafts
b = 7 #wingspan [m] #max value based on diameter of the fuselage
labda = 0.6 #taper ratio [m] from literature. 

def wing(AR,b,labda):
    A_wing = (b**2)/AR #wing surface area [m]

    Cr = (2*A_wing)/(b*(1+labda))   #rootchord [m]

    Ct = labda*Cr #tipchord [m]

    C_avg = (Cr + Ct)/2 #average chord [m]

    return A_wing, Cr, Ct, C_avg

print (wing(6,7,0.6))

