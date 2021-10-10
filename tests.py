import math
import unittest
import math_utils
import numpy as np
import physical_utils


class TestMath (unittest.TestCase):
    def test_rVector (self):
        myP = [0, 0, 1]
        its = [0, 0, 5]
        self.assertEqual(math_utils.rVector(its, myP) [2], 4)

    def test_rVectorOne (self):
        vector = np.array ([2, 3, 4])
        vecScalar = math.sqrt(2**2 + 3**2 + 4**2)
        result = vector / vecScalar
        self.assertEqual(math_utils.rVectorOne(vector) [0], result [0])
        self.assertEqual(math_utils.rVectorOne(vector)[1], result[1])
        self.assertEqual(math_utils.rVectorOne(vector)[2], result[2])

    def test_rScalar (self):
        vec = np.array ([2, 3, 4])
        scalar = math.sqrt(vec [0] ** 2 + vec [1] ** 2 + vec [2] ** 2)
        self.assertEqual(math_utils.rScalar(vec), scalar)

    def test_rScalarSquared (self):
        vec = np.array([2, 3, 4])
        self.assertEqual(math_utils.rScalarSquared(vec), 2**2+3**2+4**2)

    def test_rByr2 (self):
        vec = np.array([2, 3, 4])
        self.assertEqual(math_utils.rVectorDividedByR2(vec) [0], (vec / math_utils.rScalarSquared(vec)) [0])

    def test_gravity (self):
        myPos = np.array([0, 0, 2])
        itsPos = np.array([0, 0, 5])
        vec = np.array([0, 0, 3])
        itsMass = 10
        g = physical_utils.G
        r3 = 3**3
        result = g * itsMass * vec / r3
        self.assertEqual(physical_utils.gravityAcc(itsMass, itsPos, myPos) [0], result [0])
        self.assertEqual(physical_utils.gravityAcc(itsMass, itsPos, myPos)[1], result[1])
        self.assertEqual(physical_utils.gravityAcc(itsMass, itsPos, myPos)[2], result[2])

    def test_Ep (self):
        itsL = -physical_utils.e
        myL = physical_utils.e
        itsPos = np.array([0, 0, 3])
        myPos = np.array([0, 0, 6])
        k = physical_utils.k
        r2 = 9
        r = np.array([0, 0, -3])
        result = k * itsL * myL * r / r2
        self.assertEqual(physical_utils.potentialEnergy(itsL, myL, itsPos, myPos) [0], result [0])
        self.assertEqual(physical_utils.potentialEnergy(itsL, myL, itsPos, myPos) [1], result [1])
        self.assertEqual(physical_utils.potentialEnergy(itsL, myL, itsPos, myPos) [2], result [2])

    def test_speedToEnergy (self):
        speed = np.array([2, 3, 5])
        mass = 5
        energy = 0.5 * mass * speed ** 2
        self.assertEqual(physical_utils.speedToEnergy(mass, speed) [0], energy [0])

    def test_electrodynamicAcc (self):
        myPos = np.array ([0, 0, 0])
        itsPos = np.array ([0, 0, -53e-12])
        myLoad = -physical_utils.e
        itsLoad = physical_utils.e
        myMass = physical_utils.evToKg(937000000)
        itsSpeed = 3000000000
        rVector = math_utils.rVector(itsPos, myPos)
        rr2 = math_utils.rVectorDividedByR2(rVector)
        r2 = math_utils.rScalarSquared(rVector)
        r1 = math_utils.rVectorOne(rVector)
        time = 6.28 * 53e-12 / itsSpeed
        coulomb = physical_utils.k * myLoad * itsLoad * r1 / (r2 * myMass)
        lorentz = 2 * physical_utils.miZero * abs (myLoad) * abs (itsLoad) * itsSpeed * rr2 / (time * myMass)
        self.assertEqual(physical_utils.electrodynamicAcc(myPos, itsPos, myLoad, itsLoad, myMass, itsSpeed, time) [2],
                         (coulomb + lorentz) [2])
