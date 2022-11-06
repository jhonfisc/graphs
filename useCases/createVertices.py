from domain.entities import setLabelInitialAttr, setLabelEndAttr, getDirection
from utils.nodes import checkNode, isSameNode

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
        endNode = checkNode(initialNode, nodesList)
        if node != None:
            setLabelEndAttr("End Node " + str(node[3]))
            newVertice(initialNode, event, canvasDefinition, nodesList, isSameNode(node, endNode))
            initialNode = None


def newVertice(initialNode, endNode, canvasDefinition, nodesList, sameNode):
    global numVertices
    nodeInit = checkNode(initialNode, nodesList)
    nodeEnd = checkNode(endNode, nodesList)
    if nodeInit is not None and nodeEnd is not None:
        addCoordY = 0
        addCoordX = 0
        if sameNode:
            addCoordY = 80
            addCoordX = len(nodeInit[6]) * 10 + 20
        vertice = canvasDefinition.create_line(initialNode.x - addCoordX / 2, initialNode.y - addCoordY / 2, endNode.x,
                                               endNode.y,
                                               tags=('vertice-' + str(nodeInit[3]) + '|' + str(nodeEnd[3]),
                                                     'vertice-' + str(nodeEnd[3]) + '|' + str(nodeInit[3]),
                                                     'vertice-' + str(numVertices))
                                               )

        lbl = canvasDefinition.create_text((initialNode.x + endNode.x - addCoordX) / 2,
                                           (initialNode.y + endNode.y - addCoordY) / 2,
                                           text="{}x".format(numVertices), tags='vertice-lbl-' + str(numVertices))
        square = canvasDefinition.create_rectangle(canvasDefinition.bbox(lbl), fill="white",
                                                   tags='vertice-sqr-' + str(numVertices))
        canvasDefinition.tag_lower(square, lbl)
        canvasDefinition.tag_lower(vertice)
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
