import time

from utils.nodes import checkNode

initNode = None
finalNode = None
canvas = None
visitedNodes = []


def initRoute(nodeList, node, canvasDefinition):
    global initNode, finalNode, canvas
    if canvas is None:
        canvas = canvasDefinition
    isNode = checkNode(node, nodeList)
    if isNode is not None:
        if initNode == None:
            initNode = isNode
        else:
            finalNode = isNode
            calculateRoute(initNode, initNode[4], nodeList, finalNode)
            initNode = None
            finalNode = None


def calculateRoute(initNode, childList, nodeList, endNode):
    global visitedNodes
    visitedNodes.append(initNode)
    canvas.itemconfig(initNode[5], fill="red")
    time.sleep(0.3)
    if initNode[3] == endNode[3]:
        return True
    if len(childList) == 0:
        return False
    for nodeId in childList:
        actualNode = getNode(nodeList, nodeId)
        if actualNode not in visitedNodes:
            if calculateRoute(actualNode, actualNode[4], nodeList, endNode):
                return True


def getNode(nodeList, id):
    actualNode = None
    for node in nodeList:
        if node[3] == id:
            actualNode = node
    return actualNode
