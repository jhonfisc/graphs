from domain.entities import setLabelInitialAttr, setLabelEndAttr, getDirection
from utils.nodes import checkNode

initialNode = None
numVertices = 1


def createVertice(event, canvasDefinition, nodesList):
    global initialNode
    if initialNode == None:
        initialNode = event
        node = checkNode(event, nodesList)
        if node != None:
            setLabelInitialAttr("Initial Node " + str(node[3]))
            setLabelEndAttr("")
    else:
        node = checkNode(event, nodesList)
        if node != None:
            setLabelEndAttr("End Node " + str(node[3]))
        newVertice(initialNode, event, canvasDefinition, nodesList)
        initialNode = None


def newVertice(initialNode, endNode, canvasDefinition, nodesList):
    global numVertices
    nodeInit = checkNode(initialNode, nodesList)
    nodeEnd = checkNode(endNode, nodesList)
    if nodeInit is not None and nodeEnd is not None:
        canvasDefinition.create_line(initialNode.x, initialNode.y, endNode.x, endNode.y,
                                     tags='vertice-' + str(numVertices))
        setParent(nodesList, nodeInit, nodeEnd, numVertices)
        numVertices += 1


def setParent(nodeLIst, node, child, vertice):
    for it in nodeLIst:
        if it[3] == node[3]:
            it[4].append(child[3])
            it[6].append(vertice)
            if getDirection():
                child[4].append(it[3])
                child[6].append(vertice)


def cleanVertice():
    global initialNode
    initialNode = None
