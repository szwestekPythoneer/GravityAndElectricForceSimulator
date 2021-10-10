import app_utils
import physical_utils
import energy_counters
import objects
import graphic
import time


features = ((3750e6, -physical_utils.e * 2, 'yellow'),
            (511e3, physical_utils.e, 'blue'),
            (511e3, physical_utils.e, 'blue'))


particles = [objects.Object(app_utils.chooseRandomPosition(), app_utils.chooseMassLoadColor (features))
             for i in range (0, 3)]


energyMemory = energy_counters.EnergyCounter()


energyMemory.count_total_mass (particles)
graphic.show(particles)
graphic.screen.update()


while True:
    app_utils.countAcc(particles)
    energyMemory.count_potential_energy(particles)
    graphic.screen.delete (energyMemory.graphicRepr)
    energyMemory.graphicRepr = graphic.show_text(int(physical_utils.evToKg(energyMemory.E0)), energyMemory.Ep)
    graphic.move (particles)
    graphic.countSize(particles)
    graphic.screen.update ()