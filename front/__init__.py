from tkinter import ttk
from tkinter import Canvas

from domain import entities
from domain.entities import getCreateMode, getVerticeMode, getRouteMode, getNodesList, getLabelInitial, getLabelEnd, \
    setCanvas, getCanvas
from useCases.createNodes import createNode
from useCases.createRoute import initRoute
from useCases.createVertices import createVertice

from front.createMenu import menuInit


def screenInit(screen):
    entities.init()
    screen.title("Graph Visualization")
    screen.config(width=550, height=550, bg="white")
    canvasDefinition = Canvas(screen, width=550, height=550)
    canvasDefinition.bind("<Button-1>", createNodeFromClick)
    setCanvas(canvasDefinition)
    menuInit(screen, ttk)
    canvasDefinition.pack()


def createNodeFromClick(event):
    if getCreateMode():
        createNode(event, getCanvas(), getNodesList())
    elif getVerticeMode():
        createVertice(event, getCanvas(), getNodesList(), getLabelInitial(), getLabelEnd())
    elif getRouteMode():
        initRoute(getNodesList(), event, getCanvas())
