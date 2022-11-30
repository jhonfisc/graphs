from domain.entities import getNodesList, getCanvas
from utils.nodes import getNode


def reset():
    nodeList = getNodesList()
    canvas = getCanvas()
    if len(nodeList) > 0:
        for node in nodeList:
            if node is not None:
                canvas.itemconfig(str(node[5]), fill="blue")
                if len(node[6]) > 0:
                    for vertice in node[6]:
                        canvas.itemconfig('vertice-' + str(vertice), fill="black")
                    for ad in node[4]:
                        nodeIt = getNode(getNodesList(), ad)
                        if nodeIt is not None:
                            nodeIt[8] = 0
