from domain.entities import setVerticeMode, getVerticeMode, setCreateMode, setButtonVerticeModeAttr, \
    setButtonCreateModeAttr, setDeleteMode, setRouteMode


def handleVerticeMode():
    setVerticeMode(not getVerticeMode())
    if getVerticeMode():
        setCreateMode(False)
        setRouteMode(False)
        setDeleteMode(False)
        setButtonVerticeModeAttr('Vertices Mode is ON')
        setButtonCreateModeAttr('Create Mode')
    else:
        setButtonVerticeModeAttr('Vertices Mode')