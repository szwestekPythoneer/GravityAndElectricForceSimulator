import numpy as np
import math_utils
import physical_utils


class EnergyCounter:
    def __init__(self):
        self.Ep = None
        self.Ek = 0
        self.E0 = 0
        self.graphicRepr = None

    def count_total_mass (self, objects):
        for particle in objects:
            self.E0 += particle.mass

    def count_potential_energy (self, objects):
        self.Ep = np.array([0, 0, 0])
        for particle in objects:
            for element in objects:
                if objects.index (particle) != objects.index (element):
                    self.Ep = self.Ep + physical_utils.potentialEnergy(particle.mass, element.mass, particle.position,
                                                                       element.position)
        self.Ep = math_utils.rScalar(self.Ep)

    def count_kinetic_energy (self, objects):
        self.Ek = 0
        for particle in objects:
            speed = math_utils.rScalar(particle.speed)
            energy = physical_utils.speedToEnergy(particle.mass, speed)
            self.Ek += energy
