from domain import entities
from tkinter import ttk
from tkinter import Canvas

from domain.entities import setCanvas
from front.createMenu import menuInit


def createScreen(screen, createNodeFromClick):
    entities.init()
    screen.title("Graph Visualization")
    screen.config(width=550, height=550)
    canvasDefinition = Canvas(screen, width=550, height=550, bg="white")
    canvasDefinition.bind("<Button-1>", createNodeFromClick)
    setCanvas(canvasDefinition)
    menuInit(screen, ttk)
    canvasDefinition.pack()
