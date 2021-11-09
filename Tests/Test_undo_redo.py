
from Logic.CRUD import adauga_obiect, getBYId
from Logic.Fonctionalitati import change_location
from UI.console import ui_undo, ui_redo


def test_undo_redo ():

#1
    lista = []
    undolist = []
    redolist = []
#2
    lista= adauga_obiect (1,"masa","lemn",3000,"loc1",lista,undolist,redolist)
    assert len(lista) == 1
#3
    lista= adauga_obiect(2,"monitor","144hz",200,"loc2",lista,undolist,redolist)
    assert len(lista) == 2
#4
    lista = adauga_obiect(3,"pc","gaming",4500,"loc1",lista,undolist,redolist)
    assert len(lista) == 3

#5
    lista = ui_undo(lista , undolist ,redolist)
    assert len(lista) == 2
    assert getBYId(3,lista) is None
    assert getBYId(2, lista) is not None
    assert getBYId(1, lista) is not None
#6
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getBYId(2, lista) is None
    assert getBYId(1, lista) is not None
#7
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 0
    assert getBYId(1, lista) is None
#8

    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 0

#9
    lista = adauga_obiect (1,"Scaun","fier",300,"loc1",lista,undolist,redolist)
    lista = adauga_obiect (2, "laptop", "nush", 200, "loc2",lista,undolist,redolist)
    lista = adauga_obiect (3, "pc", "gaming", 4500, "loc1",lista,undolist,redolist)
    assert len (lista) == 3
#10
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 3
    assert getBYId(1,lista) is not None
    assert getBYId(2, lista) is not None
    assert getBYId(3, lista) is not None
#11
    lista = ui_undo(lista, undolist, redolist)
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getBYId(3, lista) is None
    assert getBYId(2, lista) is None
    assert getBYId(1, lista) is not None
#12
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getBYId(3, lista) is None
    assert getBYId(2, lista) is not None
    assert getBYId(1, lista) is not None
#13
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 3
    assert getBYId(1, lista) is not None
    assert getBYId(2, lista) is not None
    assert getBYId(3, lista) is not None
#14
    lista = ui_undo(lista, undolist, redolist)
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getBYId(3, lista) is None
    assert getBYId(2, lista) is None
    assert getBYId(1, lista) is not None

#15
    lista = adauga_obiect(4,"o4","d4",4,"loc4",lista,undolist,redolist)
    assert len(lista) == 2
    assert getBYId(1, lista) is not None
    assert getBYId(2, lista) is None
    assert getBYId(3, lista) is None
    assert getBYId(4, lista) is not None
#16
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getBYId(1, lista) is not None
    assert getBYId(2, lista) is None
    assert getBYId(3, lista) is None
    assert getBYId(4, lista) is not None
#17
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getBYId(1, lista) is not None
    assert getBYId(4, lista) is None
#18
    lista = ui_undo(lista, undolist, redolist)
    assert len(lista) == 0
    assert getBYId(1, lista) is None
#19
    lista = ui_redo(lista, undolist, redolist)
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getBYId(1, lista) is not None
    assert getBYId(4, lista) is not None
#20
    lista = ui_redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getBYId(1, lista) is not None
    assert getBYId(4, lista) is not None
    assert getBYId(2, lista) is None
    assert getBYId(3, lista) is None



