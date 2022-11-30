from domain.constants import colors, NODE_COLOR, NO_COLOR_ID, BI_GROUP_1, BI_GROUP_2, BI_STATUS
from domain.entities import getNodesList, getCanvas
from useCases.checkBipartito import isBipartito
from utils.nodes import getNode

INITIAL_COLOR_ID = 1


def setColor():
    isGraphBipartito = isBipartito()
    if isGraphBipartito[BI_STATUS]:
        setColorNodesBipartito(isGraphBipartito[BI_GROUP_1], colors[1])
        setColorNodesBipartito(isGraphBipartito[BI_GROUP_2], colors[2])
    else:
        setColorGraph()


def setColorNodesBipartito(group, color):
    for node in group:
        getCanvas().itemconfig("node" + str(node), fill=color)


def setColorGraph():
    nodeList = getNodesList()
    for node in nodeList:
        if node[NODE_COLOR] == NO_COLOR_ID:
            colorId = getColor(node)
            node[NODE_COLOR] = colorId
            getCanvas().itemconfig("node" + str(node[3]), fill=colors[colorId])


def getColor(node):
    color = INITIAL_COLOR_ID
    c = 1
    while c <= len(colors):
        found = False
        for ad in node[4]:
            nodeAd = getNode(getNodesList(), ad)
            if nodeAd[NODE_COLOR] != 0 and nodeAd[NODE_COLOR] == c and not found:
                found = True
        if not found:
            color = c
            c = len(colors)
        c += 1
    return color
