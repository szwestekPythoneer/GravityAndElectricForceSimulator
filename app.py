import app_utils
import physical_utils
import objects
import graphic
features = ((937e6, -physical_utils.e, 'yellow'), (511e3, physical_utils.e, 'blue'))
particles = [objects.Object(app_utils.chooseRandomPosition(), app_utils.chooseMassLoadColor (features))
             for i in range (0, 100)]
graphic.show(particles)
graphic.screen.update()
while True:
    app_utils.countAcc(particles)
    graphic.move (particles)
    graphic.countSize(particles)
    graphic.screen.update ()
