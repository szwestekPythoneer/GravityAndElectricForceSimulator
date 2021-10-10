import math
import math_utils
G = 1  # 6.6743015e-11
c = 30  # 29.9792458
k = -1000000  # -8.99e9
miZero = 1e-7
e = 1  # -1.602176634e-19
h = 6.62607004081e-34


def gravityAcc (itsMass, myPosition, itsPosition):
    rVector = math_utils.rVector(itsPosition, myPosition)
    rVectorOne = math_utils.rVectorOne(rVector)
    rScalarSquared = math_utils.rScalarSquared(rVector)
    return G * itsMass * rVectorOne / rScalarSquared


def potentialEnergy (myLoad, itsLoad, myPosition, itsPosition):
    rVector = math_utils.rVector(itsPosition, myPosition)
    rScalarSquared = math_utils.rScalarSquared(rVector)
    return k * itsLoad * myLoad * rVector / rScalarSquared


def energyToMass (energy):
    return energy / c ** 2


def speedToEnergy (myMass, mySpeed):
    return 0.5 * myMass * mySpeed ** 2


def massToEnergy (mass):
    return mass * c ** 2


def inertialMoment (mass, r):
    return 0.4 * mass * r ** 2


def spinSpeed (time):
    return 2 * math.pi / time


def kineticDilatation (speed):
    return math.sqrt(1 - speed ** 2 / c ** 2)


def gravityDilatation (r, mass):
    return math.sqrt (1 - 2 * G * mass / (r * c ** 2))


def schwarzschildRadius (mass):
    return 2 * G * mass / c ** 2


def potentialEnergyInside (mass, r):
    return -G * mass * 0.8 / r


def insideAcc (ep, r):
    return -ep / r


def evToKg (number):
    # rzeczywiście /c**2 tutaj bez tego by mieć dżul symulatorowy (evToJ)
    return number * abs (e)  # / c ** 2


def electrodynamicAcc (myPosition, itsPosition, myLoad, itsLoad, myMass, itsSpeed, time):
    rVector = math_utils.rVector(itsPosition, myPosition)
    rVectorOne = math_utils.rVectorOne(rVector)
    rScalarSquared = math_utils.rScalarSquared(rVector)
    coulomb = myLoad * itsLoad * k * rVectorOne / (rScalarSquared * myMass)
    lorentz = 2 * miZero * abs (myLoad) * abs (itsLoad) * itsSpeed * math_utils.rVectorDividedByR2(rVector)\
        / (myMass * time)
    return coulomb + lorentz


def electricAcc (myPosition, itsPosition, myLoad, itsLoad, myMass):
    rVector = math_utils.rVector(itsPosition, myPosition)
    rVectorOne = math_utils.rVectorOne(rVector)
    rScalarSquared = math_utils.rScalarSquared(rVector)
    return myLoad * itsLoad * k * rVectorOne / (rScalarSquared * myMass)


def spinToEnergy (spin):
    return math.sqrt (spin**2 + spin) * h / (2 * math.pi)
