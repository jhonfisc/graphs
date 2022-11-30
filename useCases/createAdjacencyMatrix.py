from domain.entities import getNodesList
from utils.nodes import getNode


def createAdjacencyMatrix():
    nodeList = getNodesList()
    adjacencyMatrix = [[0 for _ in range(len(nodeList))] for _ in range(len(nodeList))]
    for node in nodeList:
        if node is not None:
            nodeId = node[3]
            adjacencies = node[4]
            for adjacency in adjacencies:
                if getNode(getNodesList(), adjacency) is not None:
                    adjacencyMatrix[nodeId - 1][adjacency - 1] = 1
    return adjacencyMatrix
