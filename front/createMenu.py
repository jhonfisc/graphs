from domain.entities import setButtonCreateMode, setButtonVerticeMode, setButtonRouteMode, setLabelInitial, \
    setButtonDeleteMode, setLabelEnd
from useCases.deleteNode import deleteNodeMode
from useCases.setCreateMode import handleCreateMode
from useCases.setRouteMode import route
from useCases.setVerticeMode import handleVerticeMode


def menuInit(screen, ttk):
    setButtonCreateMode(createBtnCreate(ttk, screen))
    setButtonVerticeMode(createBtnVertice(ttk, screen))
    setButtonRouteMode(createBtnRoute(ttk, screen))
    setButtonDeleteMode(createBtnDelete(ttk, screen))
    setLabelInitial(createLabelInitial(ttk, screen))
    setLabelEnd(createLabelEnd(ttk, screen))


def createBtnCreate(ttk, screen):
    btnCreate = ttk.Button(screen, name="create", text="Create Mode", command=handleCreateMode)
    btnCreate.place(x=10, y=10)
    return btnCreate


def createBtnVertice(ttk, screen):
    btnVertice = ttk.Button(screen, name="vertices", text="Vertices Mode", command=handleVerticeMode)
    btnVertice.place(x=10, y=40)
    return btnVertice


def createBtnRoute(ttk, screen):
    btnRoute = ttk.Button(screen, name="route", text="Route Mode", command=route)
    btnRoute.place(x=10, y=70)
    return btnRoute


def createLabelInitial(ttk, screen):
    labelInitial = ttk.Label(screen, text='', name="info")
    labelInitial.place(x=250, y=10)
    return labelInitial


def createLabelEnd(ttk, screen):
    labelEnd = ttk.Label(screen, text='', name="end")
    labelEnd.place(x=350, y=10)
    return labelEnd

def createBtnDelete(ttk, screen):
    btnDelete = ttk.Button(screen, name="delete", text="Delete Mode", command=deleteNodeMode)
    btnDelete.place(x=10, y=100)
    return btnDelete
