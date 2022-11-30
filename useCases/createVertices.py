from domain.entities import setLabelInitialAttr, setLabelEndAttr, getDirection, getCanvas
from front.createVertice import creteVertice
from utils.nodes import checkNode, isSameNode

initialNode = None
numVertices = 1
first = False


def createVertice(event, nodesList):
    global initialNode
    if initialNode is None:
        node = checkNode(event, nodesList)
        if node is not None:
            initialNode = event
    else:
        node = checkNode(event, nodesList)
        endNode = checkNode(initialNode, nodesList)
        if node is not None and endNode is not None:
            newVertice(initialNode, event, nodesList, isSameNode(node, endNode))
            initialNode = None


def newVertice(initialNode, endNode, nodesList, sameNode):
    global numVertices
    nodeInit = checkNode(initialNode, nodesList)
    nodeEnd = checkNode(endNode, nodesList)
    if nodeInit is not None and nodeEnd is not None:
        creteVertice(initialNode, endNode, getCoordX(sameNode, nodeInit), getCoordY(sameNode), nodeEnd, nodeInit,
                     numVertices)
        setParent(nodesList, nodeInit, nodeEnd, numVertices)
        nodeInit[7] += 1
        nodeEnd[7] += 1
        numVertices += 1


def setParent(nodeLIst, node, child, vertice):
    for it in nodeLIst:
        if it is not None and it[3] == node[3]:
            it[4].append(child[3])
            it[6].append(vertice)
            if getDirection():
                child[4].append(it[3])
                child[6].append(vertice)


def cleanVertice():
    global initialNode
    initialNode = None


def getCoordY(sameNode):
    return 0 if not sameNode else 80


def getCoordX(sameNode, nodeInit):
    return 0 if not sameNode else len(nodeInit[6]) * 10 + 20
