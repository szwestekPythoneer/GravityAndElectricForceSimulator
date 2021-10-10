import numpy as np


class Object:
    def __init__(self, position, data):
        self.position = position
        self.mass = data[0]
        self.load = data[1]
        self.speed = np.array([0, 0, 0])
        self.color = data[2]
        self.graphicRepr = None
        self.size = 5
