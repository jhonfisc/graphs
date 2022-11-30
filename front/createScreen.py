from domain import entities
from tkinter import ttk
from tkinter import Canvas

from domain.entities import setCanvas, getCanvas
from front.createMenu import menuInit


def createScreen(screen, event):
    entities.init()
    newScreen(screen)
    newCanvas(screen)
    bindClickEvent(event)
    menuInit(screen, ttk)
    getCanvas().pack()


def bindClickEvent(event):
    getCanvas().bind("<Button-1>", event)


def newCanvas(screen):
     setCanvas(Canvas(screen, width=1024, height=900, bg="white"))


def newScreen(screen):
    screen.title("Graph Visualization")
    screen.config(width=1024, height=900)
