import numpy as np
import app_utils


class Object:
    def __init__(self, position, data):
        self.position = position
        self.mass = data[0]
        self.load = data[1]
        self.color = data[2]
        if self.color == 'yellow':
            self.speed = np.array([0, 0, 0])
        else:
            self.speed = app_utils.chooseRandomSpeed()
        self.graphicRepr = None
        self.size = 5
