import math

import numpy as np


def rVector (itsPosition, myPosition):
    return np.array([itsPosition [0] - myPosition [0], itsPosition [1] - myPosition [1], itsPosition [2] - myPosition [2]])


def rVectorOne (vector):
    return vector / math.sqrt (float (vector [0]) ** 2 + float (vector [1]) ** 2 + float (vector [2]) ** 2)


def rScalar (vector):
    return math.sqrt (float (vector [0]) ** 2 + float (vector [1]) ** 2 + float (vector [2]) ** 2)


def rScalarCubed (number):
    return number ** 3


def rScalarSquared (vector):
    return vector [0] ** 2 + vector [1] ** 2 + vector [2] ** 2


def rVectorDividedByR2 (vector):
    return vector / (vector [0] ** 2 + vector [1] ** 2 + vector [2] ** 2)
