from tkinter import ttk
from tkinter import Canvas

from ueCases.createNodes import createNode
from ueCases.createRoute import initRoute
from ueCases.createVertices import createVertice

canvasDefinition = None
buttonCreateMode = None
buttonVerticeMode = None
butonRoute = None
labelInitial = None
labelEnd = None


def screenInit(screen):
    screen.title("Graph Visualization")
    screen.config(width=550, height=550, bg="white")
    global canvasDefinition
    canvasDefinition = Canvas(screen, width=550, height=550)
    canvasDefinition.bind("<Button-1>", createNodeFromClick)
    menuInit(screen)
    canvasDefinition.pack()


def menuInit(screen):
    global buttonVerticeMode, buttonCreateMode, buttonRoute, labelInitial, labelEnd
    buttonCreateMode = ttk.Button(screen, name="create", text="Create Mode", command=setCreateMode)
    buttonVerticeMode = ttk.Button(screen, name="vertices", text="Vertices Mode", command=setVerticeMode)
    buttonRoute = ttk.Button(screen, name="route", text="Route Mode", command=route)
    labelInitial = ttk.Label(screen, text='', name="info")
    labelEnd = ttk.Label(screen, text='', name="info2")
    buttonCreateMode.place(x=10, y=10)
    buttonVerticeMode.place(x=150, y=20)
    buttonRoute.place(x=250, y=20)
    buttonCreateMode.pack()
    buttonVerticeMode.pack()
    buttonRoute.pack()
    labelInitial.pack()
    labelEnd.pack()

def route():
    global routeMode, buttonRoute, verticeMode, createRoute, buttonCreateMode, buttonVerticeMode, createMode
    routeMode = not routeMode
    if routeMode:
        verticeMode = False
        createMode = False
        buttonCreateMode['text'] = 'Create Mode'
        buttonVerticeMode['text'] = 'Vertices Mode'
        buttonRoute['text'] = 'Route Mode is ON'
    else:
        buttonRoute['text'] = 'Route Mode'

def setCreateMode():
    global createMode, verticeMode
    createMode = not createMode
    if createMode:
        verticeMode = False
        buttonCreateMode['text'] = 'Create Mode is ON'
        buttonVerticeMode['text'] = 'Vertices Mode'
    else:
        buttonCreateMode['text'] = 'Create Mode'


def setVerticeMode():
    global verticeMode, buttonVerticeMode, createMode
    verticeMode = not verticeMode
    if verticeMode:
        createMode = False
        buttonVerticeMode['text'] = 'Vertices Mode is ON'
        buttonCreateMode['text'] = 'Create Mode'
    else:
        buttonVerticeMode['text'] = 'Vertices Mode'


def createNodeFromClick(event):
    global nodesList
    if createMode:
        createNode(event, canvasDefinition, nodesList)
    elif verticeMode:
        createVertice(event, canvasDefinition, nodesList, labelInitial, labelEnd)
    elif routeMode:
        initRoute(nodesList, event, canvasDefinition)

nodesList = []
createMode = False
verticeMode = False
routeMode = False
