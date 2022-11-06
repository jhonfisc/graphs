from domain.entities import setVerticeMode, getVerticeMode, setCreateMode, setButtonVerticeModeAttr, \
    setButtonCreateModeAttr


def handleVerticeMode():
    setVerticeMode(not getVerticeMode())
    if getVerticeMode():
        setCreateMode(False)
        setButtonVerticeModeAttr('Vertices Mode is ON')
        setButtonCreateModeAttr('Create Mode')
    else:
        setButtonVerticeModeAttr('Vertices Mode')