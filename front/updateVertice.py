from domain.entities import getCanvas


def updateVertice(initNode, endNode, state=0):
    color = "black"
    if state == 1:
        color = "red"
    getCanvas().itemconfig('vertice-' + str(initNode) + '|' + str(endNode), fill=color)
