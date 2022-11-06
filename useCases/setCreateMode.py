from domain.entities import getCreateMode, setCreateMode, setVerticeMode, setButtonCreateModeAttr, \
    setButtonVerticeModeAttr


def handleCreateMode():
    setCreateMode(not getCreateMode())
    if getCreateMode():
        setVerticeMode(False)
        setButtonCreateModeAttr('Create Mode is ON')
        setButtonVerticeModeAttr('Vertices Mode')
    else:
        setButtonCreateModeAttr('Create Mode')
