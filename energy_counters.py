class EnergyCounter:
    def __init__(self):
        self.Ep = None
        self.Ek = None
        self.E0 = 0
        self.graphicRepr = None

    def count_total_mass (self, objects):
        for particle in objects:
            self.E0 += particle.mass
