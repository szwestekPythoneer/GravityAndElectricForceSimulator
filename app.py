import numpy as np
import app_utils
import physical_utils
import objects
import graphic
particles = [objects.Object(np.array([325, 350, 350]), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0]), 'yellow'),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed(), 'blue'),
             objects.Object(np.array([975, 350, 350]), physical_utils.evToKg(937e6), -physical_utils.e,
                            np.array([0, 0, 0]), 'yellow'),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed(), 'blue'),
             objects.Object(app_utils.chooseRandomPosition(), physical_utils.evToKg(511e3), physical_utils.e,
                            app_utils.chooseRandomSpeed(), 'blue')]
while True:
    app_utils.countAcc(particles)
    graphic.show (particles)
