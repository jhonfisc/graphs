from domain.constants import TITLE_BIPARTITO, MSG_BIPARTITO, MSG_NO_BIPARTITO
from domain.entities import getNodesList
from front.showMessage import showMessageBox
from useCases.createAdjacencyMatrix import createAdjacencyMatrix
from utils.nodes import getNode


def checkBipartito():
    showMessage(isBipartito()[0])


def isBipartito():
    adjacency = createAdjacencyMatrix()
    group1 = []
    group2 = []
    i = 0
    canAppend = True
    while i < len(adjacency):
        if getNode(getNodesList(), i+1) is not None and (i + 1) not in group1 and not haveAdjacency(i + 1, group1):
            group1.append(i + 1)
        elif getNode(getNodesList(), i+1) is not None and (i + 1) not in group2 and not haveAdjacency(i + 1, group2):
            group2.append(i + 1)
        elif getNode(getNodesList(), i+1) is not None:
            canAppend = False
        i += 1
        if not canAppend:
            i = len(adjacency)
    return [canAppend, group1, group2]


def haveAdjacency(nodeId, group):
    isFound = False
    for ad in group:
        nodeAdjList = getNode(getNodesList(), ad)
        if nodeId in nodeAdjList[4]:
            isFound = True
    return isFound


def showMessage(canAppend):
    showMessageBox(TITLE_BIPARTITO, MSG_BIPARTITO if canAppend else MSG_NO_BIPARTITO)
