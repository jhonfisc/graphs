import math

from utils.nodes import checkNode

initialNode = None


def createVertice(event, canvasDefinition, nodesList, labelInitial, labelEnd):
    global initialNode
    if initialNode == None:
        initialNode = event
        node = checkNode(event, nodesList)
        if node != None:
            labelInitial["text"] = "Initial Node " + str(node[3])
            labelEnd["text"] = " "
    else:
        node = checkNode(event, nodesList)
        if node != None:
            labelEnd["text"] = "End Node " + str(node[3])
        newVertice(initialNode, event, canvasDefinition, nodesList)
        initialNode = None


def newVertice(initialNode, endNode, canvasDefinition, nodesList):
    nodeInit = checkNode(initialNode, nodesList)
    nodeEnd = checkNode(endNode, nodesList)
    if nodeInit is not None and nodeEnd is not None:
        canvasDefinition.create_line(initialNode.x, initialNode.y, endNode.x, endNode.y)
        setParent(nodesList, nodeInit, nodeEnd)


def setParent(nodeLIst, node, child):
    for it in nodeLIst:
        if it[3] == node[3]:
            it[4].append(child[3])