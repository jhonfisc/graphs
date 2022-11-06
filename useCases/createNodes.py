from tkinter import messagebox
radius = 15
numNodes = 1


def createNode(event, canvasDefinition, nodesList):
    global numNodes
    if event.y > 150:
        nodeCanva = canvasDefinition.create_oval(event.x - radius, event.y - radius, event.x + radius, event.y + radius,
                                                 fill="blue", width=1, tags=str(numNodes))
        nodesList.append([event.x, event.y, radius, numNodes, [], nodeCanva, []])
        numNodes += 1
    else:
        messagebox.showwarning("Warning - Create Mode", "En esta seccion de la pantalla no se pueden crear nodos")
