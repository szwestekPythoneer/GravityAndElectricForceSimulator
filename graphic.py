from tkinter import *
root = Tk ()
screen = Canvas (root, width=1300, height=700, bg='black')
screen.pack ()


def show (particles):
    for particle in particles:
        particle.graphicRepr = screen.create_oval(particle.position [0], particle.position [1],
                                                  particle.position [0] + particle.size,
                                                  particle.position [1] + particle.size, fill=particle.color)


def move (particles):
    for particle in particles:
        screen.coords (particle.graphicRepr, particle.position [0], particle.position [1],
                       particle.position [0] + particle.size, particle.position [1] + particle.size)


def countSize (particles):
    for particle in particles:
        if particle.position [2] < 200:
            particle.size = 3
        elif 200 <= particle.position [2] <= 400:
            particle.size = 7
        elif particle.position [2] > 400:
            particle.size = 11


def show_text (e0):
    return screen.create_text(60, 30, fill='white', text='E0 = {} J\nEp = '.format(e0))
