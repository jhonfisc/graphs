from domain.constants import TITLE_CREATE_MODE, MSG_CREATE_MODE
from domain.entities import getCanvas, getNodesList
from front.showMessage import showMessageBox

radius = 15
numNodes = 1


def createNode(event):
    global numNodes
    if event.y > 250:
        nodeCanva = getCanvas().create_oval(event.x - radius, event.y - radius, event.x + radius, event.y + radius,
                                                 fill="blue", width=1, tags=(str(numNodes), "node"+str(numNodes)))
        getCanvas().create_text((event.x, event.y), text=str(numNodes), tags='lbl-'+str(numNodes), fill='white')
        getNodesList().append([event.x, event.y, radius, numNodes, [], nodeCanva, [], 0, 0])
        numNodes += 1
    else:
        showMessageBox(TITLE_CREATE_MODE, MSG_CREATE_MODE)
