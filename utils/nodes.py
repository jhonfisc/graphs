import math


def checkNode(nodeInit, nodesList):
    checkNode = None
    for node in nodesList:
        if calcDistance(nodeInit, node) <= node[2]:
            checkNode = node
    return checkNode


def calcDistance(nodeInit, nodeEnd):
    return math.sqrt(pow(nodeEnd[0] - nodeInit.x, 2) + pow(nodeEnd[1] - nodeInit.y, 2))


def isSameNode(initNode, lastNode):
    return math.sqrt(pow(lastNode[0] - initNode[0], 2) + pow(lastNode[1] - initNode[1], 2)) <= initNode[2]

def getNode(nodeList, id):
    actualNode = None
    for node in nodeList:
        if node[3] == id:
            actualNode = node
    return actualNode