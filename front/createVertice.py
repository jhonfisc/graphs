from domain.entities import getCanvas


def creteVertice(initialNode, endNode, addCoordX, addCoordY, nodeEnd, nodeInit, numVertices):
    canvasDefinition = getCanvas()
    vertice = canvasDefinition.create_line(initialNode.x - addCoordX / 2, initialNode.y - addCoordY / 2, endNode.x,
                                           endNode.y,
                                           tags=('vertice-' + str(nodeInit[3]) + '|' + str(nodeEnd[3]),
                                                 'vertice-' + str(numVertices))
                                           )

    lbl = canvasDefinition.create_text((initialNode.x + endNode.x - addCoordX) / 2,
                                       (initialNode.y + endNode.y - addCoordY) / 2,
                                       text="{}x".format(numVertices), tags='vertice-lbl-' + str(numVertices))
    square = canvasDefinition.create_rectangle(canvasDefinition.bbox(lbl), fill="white",
                                               tags='vertice-sqr-' + str(numVertices))
    canvasDefinition.tag_lower(square, lbl)
    canvasDefinition.tag_lower(vertice)
