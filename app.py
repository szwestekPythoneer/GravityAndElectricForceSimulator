import app_utils
import physical_utils
import energy_counters
import objects
import graphic
import time


features = ((937e6, -physical_utils.e, 'yellow'),
            (511e3, physical_utils.e, 'blue'))


particles = [objects.Object(app_utils.chooseRandomPosition(), app_utils.chooseMassLoadColor (features))
             for i in range (0, 4)]


energyMemory = energy_counters.EnergyCounter()


energyMemory.count_total_mass (particles)
graphic.show(particles)
graphic.screen.update()


while True:
    app_utils.countAcc(particles)
    energyMemory.count_potential_energy(particles)
    energyMemory.count_kinetic_energy(particles)
    graphic.screen.delete (energyMemory.graphicRepr)
    energyMemory.graphicRepr = graphic.show_text(int(physical_utils.evToKg(energyMemory.E0)), energyMemory.Ep,
                                                 energyMemory.Ek)
    graphic.move (particles)
    graphic.countSize(particles)
    graphic.screen.update ()
    # time.sleep (0.1)
