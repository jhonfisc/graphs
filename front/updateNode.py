from domain.entities import getCanvas


def updateNode(node, state=0):
    color = "blue"
    if state == 1:
        color = "green"
    elif state == 2:
        color = "orange"
    elif state == 3:
        color = "red"
    getCanvas().itemconfig(node, fill=color)
