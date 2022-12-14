from domain.entities import setButtonCreateModeAttr, setButtonVerticeModeAttr, setRouteMode, getRouteMode, \
    setVerticeMode, setCreateMode, setButtonRouteModeAttr, setDeleteMode


def route():
    setRouteMode(not getRouteMode())
    if getRouteMode():
        setVerticeMode(False)
        setCreateMode(False)
        setDeleteMode(False)
        setButtonCreateModeAttr('Create Mode')
        setButtonVerticeModeAttr('Vertices Mode')
        setButtonRouteModeAttr('Route Mode is ON')
    else:
        setButtonRouteModeAttr('Route Mode')