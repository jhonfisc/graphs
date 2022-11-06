def init():
    global canvasDefinition, buttonCreateMode, buttonVerticeMode, butonRouteMode, labelInitial, labelEnd
    global createMode, verticeMode, routeMode, nodesList
    canvasDefinition = None
    buttonCreateMode = None
    buttonVerticeMode = None
    butonRouteMode = None
    labelInitial = None
    labelEnd = None
    nodesList = []
    createMode = False
    verticeMode = False
    routeMode = False


def getCreateMode():
    return createMode


def getVerticeMode():
    return verticeMode


def getRouteMode():
    return routeMode


def getNodesList():
    return nodesList


def getLabelInitial():
    return labelInitial


def setLabelInitial(data):
    global labelInitial
    labelInitial = data


def getLabelEnd():
    return labelEnd


def setLabelEnd(data):
    global labelEnd
    labelEnd = data


def setCreateMode(data):
    global createMode
    createMode = data


def setVerticeMode(data):
    global verticeMode
    verticeMode = data


def setRouteMode(data):
    global routeMode
    routeMode = data


def getButtonCreateMode():
    return buttonCreateMode


def setButtonCreateMode(button):
    global buttonCreateMode
    buttonCreateMode = button


def getButtonVerticeMode():
    return buttonVerticeMode


def setButtonVerticeMode(button):
    global buttonVerticeMode
    buttonVerticeMode = button


def getButtonRouteMode():
    return butonRouteMode


def setButtonRouteMode(button):
    global butonRouteMode
    butonRouteMode = button


def setButtonCreateModeAttr(value):
    buttonCreateMode = getButtonCreateMode()
    buttonCreateMode['text'] = value
    setButtonCreateMode(buttonCreateMode)


def setButtonVerticeModeAttr(value):
    buttonVerticeMode = getButtonVerticeMode()
    buttonVerticeMode['text'] = value
    setButtonVerticeMode(buttonVerticeMode)


def setButtonRouteModeAttr(value):
    buttonRouteMode = getButtonRouteMode()
    buttonRouteMode['text'] = value
    setButtonRouteMode(buttonRouteMode)


def setLabelInitialAttr(value):
    labelInitial = getLabelInitial()
    labelInitial['text'] = value
    setLabelInitial(labelInitial)


def setLabelEndAttr(value):
    labelEnd = getLabelEnd()
    labelEnd['text'] = value
    setLabelEnd(labelEnd)


def setCanvas(data):
    global canvasDefinition
    canvasDefinition = data


def getCanvas():
    return canvasDefinition