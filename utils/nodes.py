import math


def checkNode(nodeInit, nodesList):
    checkNode = None
    for node in nodesList:
        if calcDistance(nodeInit, node) <= node[2]:
            checkNode = node
    return checkNode


def calcDistance(nodeInit, nodeEnd):
    return math.sqrt(pow(nodeEnd[0] - nodeInit.x, 2) + pow(nodeEnd[1] - nodeInit.y, 2))
