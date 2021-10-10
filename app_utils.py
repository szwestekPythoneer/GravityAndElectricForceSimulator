import random
import numpy as np
import math_utils
import physical_utils


def chooseRandomPosition ():
    return np.array([random.randint(0, 1300), random.randint(0, 700), random.randint(0, 700)])


def countAcc (particles):
    for particle in particles:
        acc = np.array([0, 0, 0])
        for element in particles:
            if particles.index(particle) != particles.index(element):
                acc = acc + physical_utils.gravityAcc(element.mass, particle.position, element.position)
            speedScalar = math_utils.rScalar(particle.speed)
            gamma3 = physical_utils.kineticDilatation(speedScalar) ** 3
            acc = acc * gamma3
            if math_utils.rScalar(acc) > physical_utils.c:
                acc = math_utils.rVectorOne(acc) * physical_utils.c
        particle.speed = acc + particle.speed
        particle.position = particle.position + particle.speed


def chooseMassLoadColor(data):
    choice = random.choice(data)
    return [choice [0], choice [1], choice [2]]


def chooseRandomSpeed():
    return np.array ([random.randint(0, 1) / 100,
                      random.randint(0, 1) / 100,
                      random.randint(0, 1) / 100])
