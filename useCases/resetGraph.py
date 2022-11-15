from domain.entities import getNodesList, getCanvas


def reset():
    nodeList = getNodesList()
    canvas = getCanvas()
    if len(nodeList) > 0:
        for node in nodeList:
            canvas.itemconfig(str(node[5]), fill="blue")
            if len(node[6]) > 0:
                for vertice in node[6]:
                    canvas.itemconfig('vertice-' + str(vertice), fill="black")
