import numpy as np

import app_utils
import math_utils
import physical_utils
import objects

particles = [objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0])),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed()),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0])),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed())]

while True:
    for particle in particles:
        acc = np.array([0, 0, 0])
        for element in particles:
            if particles.index(particle) != particles.index(element):
                acc = acc + physical_utils.electricAcc(particle.position, element.position, particle.load, element.load,
                                                       particle.mass)
            speedScalar = math_utils.rScalar(particle.speed)
            gamma3 = physical_utils.kineticDilatation(speedScalar) ** 3
            acc = acc * gamma3
            if math_utils.rScalar(acc) > physical_utils.c:
                acc = math_utils.rVectorOne(acc) * physical_utils.c
        particle.speed = acc + particle.speed
        particle.position = particle.position + particle.speed
    print (particles [0].position, particles [1].position, particles [2].position, particles [3].position)
