radius = 15
numNodes = 1


def createNode(event, canvasDefinition, nodesList):
    global numNodes
    nodeCanva = canvasDefinition.create_oval(event.x - radius, event.y - radius, event.x + radius, event.y + radius,
                                             fill="blue", width=1, tags=str(numNodes))
    nodesList.append([event.x, event.y, radius, numNodes, [], nodeCanva, []])
    numNodes += 1
