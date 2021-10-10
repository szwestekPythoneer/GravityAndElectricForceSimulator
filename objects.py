class Object:
    def __init__(self, position, mass, load, speed, color):
        self.position = position
        self.mass = mass
        self.load = load
        self.speed = speed
        self.color = color
        self.graphicRepr = None
        self.size = 5