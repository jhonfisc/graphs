from domain.entities import getCreateMode, getVerticeMode, getRouteMode, getNodesList, getCanvas
from front.createScreen import createScreen
from useCases.createNodes import createNode
from useCases.createRoute import initRoute
from useCases.createVertices import createVertice


def screenInit(screen):
    createScreen(screen, createNodeFromClick)


def createNodeFromClick(event):
    if getCreateMode():
        createNode(event, getCanvas(), getNodesList())
    elif getVerticeMode():
        createVertice(event, getCanvas(), getNodesList())
    elif getRouteMode():
        initRoute(getNodesList(), event, getCanvas())
