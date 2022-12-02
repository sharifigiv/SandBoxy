from numpy import dot
#from maths import *

g = 9.81

def Velocity_calculation(d, mass):
    t = (d / (0.5 * g)) ** 0.5

    v = g * mass * t
    return t

def Elastic_Collision_calculation(Object1, Object2):
    # vZMF = ( mA * uA + mB * uB ) / (mA + mB)

    muA = (Object1.cmVec.add(Object1.gmVec)).multiply(Object1.mass)
    muB = (Object2.cmVec.add(Object2.gmVec)).multiply(Object2.mass)

    vZMF = (muA.add(muB)).division((Object1.mass + Object2.mass))

    uAZMF = vZMF.minus(Object1.cmVec)
    uBZMF = vZMF.minus(Object2.cmVec)

    return uAZMF, uBZMF