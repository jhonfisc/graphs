import time

from utils.nodes import checkNode

initNode = None
finalNode = None
canvas = None
visitedNodes = []


def initRoute(nodeList, node, canvasDefinition):
    global initNode, finalNode, canvas, visitedNodes
    if canvas is None:
        canvas = canvasDefinition
    isNode = checkNode(node, nodeList)
    if isNode is not None:
        if initNode == None:
            initNode = isNode
        else:
            finalNode = isNode
            calculateRoute(initNode, initNode[4], nodeList, finalNode, True)
            initNode = None
            finalNode = None
            visitedNodes = []


def calculateRoute(initNode, childList, nodeList, endNode, first):
    global visitedNodes
    visitedNodes.append(initNode)
    if first:
        canvas.itemconfig(initNode[5], fill="green")
    else:
        canvas.itemconfig(initNode[5], fill="orange")
    if initNode[3] == endNode[3]:
        canvas.itemconfig(initNode[5], fill="red")
        return True
    time.sleep(0.3)
    if len(childList) == 0:
        return False
    for nodeId in childList:
        actualNode = getNode(nodeList, nodeId)
        if actualNode is not None and actualNode not in visitedNodes:
            canvas.itemconfig('vertice-' + str(initNode[3]) + '|' + str(actualNode[3]), fill="red")
            if calculateRoute(actualNode, actualNode[4], nodeList, endNode, False):
                break
    return True


def getNode(nodeList, id):
    actualNode = None
    for node in nodeList:
        if node[3] == id:
            actualNode = node
    return actualNode
