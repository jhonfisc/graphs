from domain.constants import TITLE_ROUTE, MSG_ROUTE
from domain.entities import getNodesList, setWalkMode
from front.showMessage import showMessageBox


def checkWalk():
    isPar = True
    nodeFail = []
    nodeList = getNodesList()
    print(nodeList)
    if len(nodeList) > 0:
        for node in nodeList:
            if node is not None and node[7] % 2 > 0:
                isPar = False
                nodeFail.append(node[3])
    if not isPar:
        showMessageBox(TITLE_ROUTE, MSG_ROUTE, str(nodeFail))
        setWalkMode(False)
    else:
        setWalkMode(True)
