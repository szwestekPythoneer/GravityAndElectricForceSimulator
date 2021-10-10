from tkinter import *
root = Tk ()
screen = Canvas (root, width=1300, height=700, bg='black')
screen.pack ()
size = 3


def show (particles, axis=1):
    for particle in particles:
        screen.delete('all')
        screen.create_oval(particle.position [0], particle.position [axis],
                           particle.position [0] + size, particle.position [axis] + size,
                           fill='white')
        screen.update ()
