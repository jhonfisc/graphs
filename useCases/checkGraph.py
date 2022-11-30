from domain.constants import TITLE_CONEXO, MSG_CONEXO, MSG_NO_CONEXO
from domain.entities import getNodesList
from front.showMessage import showMessageBox
from useCases.createAdjacencyMatrix import createAdjacencyMatrix
from utils.nodes import checkNode, getNode


def checkGraph():
    showMessageBox(TITLE_CONEXO, MSG_CONEXO if isGraphConexo(getNodesList()) else MSG_NO_CONEXO)


def isGraphConexo(nodeList):
    if len(nodeList) == 0:
        return False
    adjacencyMatrix = createAdjacencyMatrix()
    print(adjacencyMatrix)
    i = 0
    isConexo = False
    n = len(adjacencyMatrix)
    response = False
    while i < n:
        j = 0
        while j < n:
            if getNode(getNodesList(), i + 1) is not None and adjacencyMatrix[i][j] == 1 and i != j:
                isConexo = True
                j = n
            elif getNode(getNodesList(), i + 1) is None:
                isConexo = True
                j = n
            j += 1
        if isConexo:
            j = 0
            while j < n:
                if getNode(getNodesList(), j + 1) is not None and adjacencyMatrix[j][i] == 1 and i != j:
                    isConexo = True
                    j = n
                elif getNode(getNodesList(), i + 1) is None:
                    isConexo = True
                    j = n
                j += 1
        if isConexo:
            isConexo = False
            response = True
            i += 1
        else:
            i = n
            response = False
    return response
