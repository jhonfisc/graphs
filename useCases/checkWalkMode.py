from tkinter import messagebox

from domain.entities import getNodesList, setWalkMode


def checkWalk():
    isPar = True
    nodeFail = []
    nodeList = getNodesList()
    print(nodeList)
    if len(nodeList) > 0:
        for node in nodeList:
            if node[7] % 2 > 0:
                isPar = False
                nodeFail.append(node[3])
    if not isPar:
        messagebox.showwarning("Warning - Can't Create Route",
                               'No se puede calcular esta ruta, los nodos con grado impar son: ' + str(nodeFail))
        setWalkMode(False)
    else:
        setWalkMode(True)
