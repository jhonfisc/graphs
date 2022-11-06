from domain.entities import getCreateMode, setCreateMode, setVerticeMode, setButtonCreateModeAttr, \
    setButtonVerticeModeAttr, setDeleteMode, setRouteMode


def handleCreateMode():
    setCreateMode(not getCreateMode())
    if getCreateMode():
        setVerticeMode(False)
        setDeleteMode(False)
        setRouteMode(False)
        setButtonCreateModeAttr('Create Mode is ON')
        setButtonVerticeModeAttr('Vertices Mode')
    else:
        setButtonCreateModeAttr('Create Mode')
