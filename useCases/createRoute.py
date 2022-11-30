from front.updateNode import updateNode
from front.updateVertice import updateVertice
from utils.nodes import checkNode, getNode

initNode = None
finalNode = None
visitedNodes = []
visitedVertices = []


def initRoute(nodeList, node):
    global initNode, finalNode
    isNode = checkNode(node, nodeList)
    if isNode is not None:
        if initNode is None:
            initNode = isNode
        else:
            finalNode = isNode
            calculateRoute(initNode, initNode[4], nodeList, finalNode, True)


def calculateRoute(initNode, childList, nodeList, endNode, first):
    setVisitNode(initNode, first)
    if isEndNode(initNode, endNode, first):
        return True
    if len(childList) == 0:
        return False
    for nodeId in childList:
        actualNode = getNode(nodeList, nodeId)
        if actualNode is not None and actualNode not in visitedNodes:
            updateVertice(initNode[3], actualNode[3], 1)
            if calculateRoute(actualNode, actualNode[4], nodeList, endNode, False):
                break
    return True


def setVisitNode(node, first):
    global visitedNodes
    visitedNodes.append(node)
    updateNode(initNode[5], 1 if first else 2)


def isEndNode(initNode, endNode, first):
    if initNode[3] == endNode[3] and not first:
        updateNode(initNode[5], 3)
        return True
    return False


def resetEnvironmentRoute():
    global initNode, finalNode, visitedNodes
    initNode = None
    finalNode = None
    visitedNodes = []
