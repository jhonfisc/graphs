from domain.entities import setDeleteMode, getDeleteMode, setVerticeMode, setCreateMode, \
    setButtonCreateModeAttr, setButtonVerticeModeAttr, setButtonRouteModeAttr
from utils.nodes import checkNode


def deleteNodeMode():
    setDeleteMode(not getDeleteMode())
    if getDeleteMode():
        setVerticeMode(False)
        setCreateMode(False)
        setButtonCreateModeAttr('Create Mode')
        setButtonVerticeModeAttr('Vertices Mode')
        setButtonRouteModeAttr('Route Mode')
    else:
        setButtonRouteModeAttr('Route Mode')


def deleteNode(event, canvas, nodeList):
    nodeToDelete = checkNode(event, nodeList)
    if nodeToDelete is not None:
        canvas.delete(str(nodeToDelete[5]))
        if len(nodeToDelete[6]) > 0:
            for it in nodeToDelete[6]:
                canvas.delete('vertice-'+str(it))


