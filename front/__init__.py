from domain.entities import getCreateMode, getVerticeMode, getRouteMode, getNodesList, getCanvas, getDeleteMode, \
    getWalkMode
from front.createScreen import createScreen
from useCases.createNodes import createNode
from useCases.createRoute import initRoute
from useCases.createVertices import createVertice, cleanVertice
from useCases.createWalkRoute import initWalkRoute
from useCases.deleteNode import deleteNode


def screenInit(screen):
    createScreen(screen, createNodeFromClick)


def createNodeFromClick(event):
    if getCreateMode():
        cleanVertice()
        createNode(event)
    elif getVerticeMode():
        createVertice(event, getNodesList())
    elif getRouteMode():
        cleanVertice()
        initRoute(getNodesList(), event)
    elif getDeleteMode():
        cleanVertice()
        deleteNode(event, getCanvas(), getNodesList())
    elif getWalkMode():
        cleanVertice()
        initWalkRoute(event)
