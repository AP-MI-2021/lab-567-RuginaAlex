from Domain.Obiecte import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, getBYId, stergere_obiect, modificare_obiect


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect ("1", "calculator", "Acer" , 2400 , "birou contabilitate",lista)

    assert len(lista) == 1
    assert get_id(getBYId("1",lista)) == "1"
    assert get_nume(getBYId("1",lista)) == "calculator"
    assert get_descriere(getBYId("1",lista)) == "Acer"
    assert get_pret(getBYId("1",lista)) == 2400
    assert get_locatie(getBYId("1",lista)) == "birou contabilitate"


def test_stergere_obiect():
    lista= []
    lista = adauga_obiect("1", "calculator", "Acer", 2400, "birou contabilitate", [])
    lista = adauga_obiect("2", "monitor", "Acer", 1200, "birou contabilitate", lista)

    lista = stergere_obiect ("1", lista)
    assert len(lista) == 1
    assert getBYId("1", lista) is None

    try:
        lista = stergere_obiect("3", lista)
    except ValueError:
        assert len(lista) == 1
        assert getBYId("2", lista) is not None
    except Exception:
        assert False

def test_getById():
    list = []
    list = adauga_obiect(13, "Laptop", "Acer", 2490, "contabilitate", list)
    list = adauga_obiect(12, "Monitor Dell", "144Hz", 2000, "birou", list)
    assert get_id(getBYId(12, list)) == 12
    assert get_nume(getBYId(12, list)) == "Monitor Dell"
    assert get_descriere(getBYId(12, list)) == "144Hz"
    assert get_pret(getBYId(12, list)) == 2000
    assert get_locatie(getBYId(12, list)) == "birou"

    assert get_id(getBYId(13, list)) == 13
    assert get_nume(getBYId(13, list)) == "Laptop"
    assert get_descriere(getBYId(13, list)) == "Acer"
    assert get_pret(getBYId(13, list)) == 2490
    assert get_locatie(getBYId(13, list)) == "contabilitate"



def test_modificare_obiect():
    lista = []
    lista = adauga_obiect(1, "masa", "lemn", 100, "birou", lista)
    lista = adauga_obiect(2, "scaun", "fier forjat", 200, "contabilitate", lista)

    lista = modificare_obiect(2, "scaun", "fier forjat", 300, "interne", lista)

    assert len(lista) == 2
    obiect_modificat = getBYId(2, lista)
    assert get_pret(obiect_modificat) == 300
    assert get_locatie(obiect_modificat) == "interne"
    obiect_nemodificat = getBYId(1, lista)
    assert get_pret(obiect_nemodificat) == 100
    assert get_locatie(obiect_nemodificat) == "birou"

    lista=[]
    lista=adauga_obiect("1","masa","lemn",200,"birou",lista)

    try:
        lista=modificare_obiect("3","pc","acer",2000,"contabilitate",lista)
    except ValueError:

        obiect_nemodificat = getBYId("1", lista)
        assert get_id(obiect_nemodificat) == "1"
        assert get_nume(obiect_nemodificat) == "masa"
        assert get_descriere(obiect_nemodificat) == "lemn"
        assert get_pret(obiect_nemodificat) == 200
        assert get_locatie(obiect_nemodificat) == "birou"
    except Exception:
        assert False


