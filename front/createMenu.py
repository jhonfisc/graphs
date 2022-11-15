from domain.entities import setButtonCreateMode, setButtonVerticeMode, setButtonRouteMode, setLabelInitial, \
    setButtonDeleteMode, setLabelEnd, setButtonResetMode
from useCases.checkWalkMode import checkWalk
from useCases.deleteNode import deleteNodeMode
from useCases.resetGraph import reset
from useCases.setCreateMode import handleCreateMode
from useCases.setRouteMode import route
from useCases.setVerticeMode import handleVerticeMode


def menuInit(screen, ttk):
    createBtnCreate(ttk, screen)
    createBtnVertice(ttk, screen)
    createBtnRoute(ttk, screen)
    createBtnDelete(ttk, screen)
    createBtnReset(ttk, screen)
    createBtnWalk(ttk, screen)


def createBtnCreate(ttk, screen):
    btnCreate = ttk.Button(screen, name="create", text="Create Mode", command=handleCreateMode, width=20)
    btnCreate.place(x=10, y=10)
    setButtonCreateMode(btnCreate)


def createBtnVertice(ttk, screen):
    btnVertice = ttk.Button(screen, name="vertices", text="Vertices Mode", command=handleVerticeMode, width=20)
    btnVertice.place(x=10, y=40)
    setButtonVerticeMode(btnVertice)
    setLabelInitial(createLabelInitial(ttk, screen))
    setLabelEnd(createLabelEnd(ttk, screen))


def createBtnRoute(ttk, screen):
    btnRoute = ttk.Button(screen, name="route", text="Route Mode", command=route, width=20)
    btnRoute.place(x=10, y=70)
    setButtonRouteMode(btnRoute)


def createLabelInitial(ttk, screen):
    labelInitial = ttk.Label(screen, text='', name="info")
    labelInitial.place(x=250, y=10)
    return labelInitial


def createLabelEnd(ttk, screen):
    labelEnd = ttk.Label(screen, text='', name="end")
    labelEnd.place(x=350, y=10)
    return labelEnd


def createBtnDelete(ttk, screen):
    btnDelete = ttk.Button(screen, name="delete", text="Delete Mode", command=deleteNodeMode, width=20)
    btnDelete.place(x=10, y=100)
    setButtonDeleteMode(btnDelete)


def createBtnReset(ttk, screen):
    btnReset = ttk.Button(screen, name="reset", text="Reset", command=reset, width=20)
    btnReset.place(x=10, y=130)
    setButtonResetMode(btnReset)


def createBtnWalk(ttk, screen):
    btnWalk = ttk.Button(screen, name="walk", text="Paseo Euleriano", command=checkWalk, width=20)
    btnWalk.place(x=10, y=160)
