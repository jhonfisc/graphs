from domain.entities import getNodesList
from utils.nodes import getNode, checkNode

initNode = None
finalNode = None
canvas = None
visitedNodes = []
visitedVertices = []
visits = []


def initWalkRoute(nodeList, node, canvasDefinition):
    global initNode, finalNode, canvas, visitedNodes, visitedVertices, visits
    if canvas is None:
        canvas = canvasDefinition
    isNode = checkNode(node, nodeList)
    if isNode is not None:
        visits = [0] * len(getNodesList())
        visitedVertices = []
        visitedNodes = []
        calculateWalkRoute(isNode, isNode[4], nodeList, isNode, True)
        print(visitedVertices)
        print(visitedNodes)


def calculateWalkRoute(initNode, childList, nodeList, endNode, first):
    global visitedVertices, visitedNodes
    visitedNodes.append(initNode)
    isFirst = False
    if first:
        canvas.itemconfig(initNode[5], fill="green")
    else:
        canvas.itemconfig(initNode[5], fill="orange")
    if initNode[3] == endNode[3] and not first:
        canvas.itemconfig(initNode[5], fill="red")
        return True
    if len(childList) == 0:
        return False
    if len(initNode[4]) > 0:
        nodeId = getNumVisitsByNode(initNode, initNode[4].copy())
        if nodeId == None:
            return False
        actualVertice = 'vertice-' + str(initNode[3]) + '|' + str(nodeId)
        actualVertice2 = 'vertice-' + str(nodeId) + '|' + str(initNode[3])
        actualNode = getNode(nodeList, nodeId)
        isFirst = True
    if actualNode is not None:
        canvas.itemconfig(actualVertice, fill="red")
        visitedVertices.append(actualVertice)
        calculateWalkRoute(actualNode, actualNode[4], nodeList, endNode, isFirst)
        visitedVertices.append(actualVertice2)
        canvas.itemconfig(actualVertice2, fill="red")
    return True


def checkVertices(childList):
    ret = None
    for nodeId in childList:
        node = getNode(getNodesList(), nodeId)
        if node not in visitedNodes:
            ret = node
    return ret


def getNumVisitsByNode(initNode, listNodes):
    print(listNodes)
    if listNodes == None or len(listNodes) == 0:
        return None
    visits = []
    for node in listNodes:
        nodeActual = getNode(getNodesList(), node)
        gradeVisit = nodeActual[7]
        if nodeActual in visitedNodes:
            gradeVisit = 0
        visits.append(gradeVisit)
    nodeMax = listNodes[visits.index(max(visits))]
    notFoundVertice = False
    nodesFound = 0
    for nodeId in listNodes:
        if nodeId != nodeMax:
            actualVertice = 'vertice-' + str(initNode[3]) + '|' + str(nodeId)
            actualVertice2 = 'vertice-' + str(nodeId) + '|' + str(initNode[3])
            if actualVertice not in visitedVertices and actualVertice2 not in visitedVertices:
                visitedVertices.append(actualVertice)
                visitedVertices.append(actualVertice2)
                #visitedNodes.append(getNode(getNodesList(), nodeId))
                canvas.itemconfig(actualVertice, fill="red")
                canvas.itemconfig(actualVertice2, fill="red")
                notFoundVertice = False
                nodesFound += 1
            else:
                notFoundVertice = nodesFound == 0
        else:
            actualVertice = 'vertice-' + str(initNode[3]) + '|' + str(nodeId)
            actualVertice2 = 'vertice-' + str(nodeId) + '|' + str(initNode[3])
            if actualVertice in visitedVertices and actualVertice2 in visitedVertices:
                notFoundVertice = True
                break
    if notFoundVertice and getNode(getNodesList(), nodeMax) in visitedNodes:
        return None
    return nodeMax


def checkVertice(initNode, nodeId):
    actualVertice = 'vertice-' + str(initNode[3]) + '|' + str(nodeId)
    actualVertice2 = 'vertice-' + str(nodeId) + '|' + str(initNode[3])
    print(actualVertice)
    print(actualVertice2)
    return actualVertice not in visitedVertices and actualVertice2 not in visitedVertices