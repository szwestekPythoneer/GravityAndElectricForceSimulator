import numpy as np
import app_utils
import physical_utils
import objects
import graphic
particles = [objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0])),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed())]
"""
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0])),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed())
"""
while True:
    app_utils.countAcc(particles)
    graphic.show (particles)
