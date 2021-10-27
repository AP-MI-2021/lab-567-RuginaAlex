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
    lista = adauga_obiect("1", "calculator", "Acer", 2400, "birou contabilitate", [])
    lista = adauga_obiect("2", "monitor", "Acer", 1200, "birou contabilitate", lista)

    lista = stergere_obiect ("1", lista)
    assert len(lista) == 1
    assert getBYId("1", lista) is None

    lista = stergere_obiect("3", lista)
    assert len(lista) == 1
    assert getBYId("2", lista) is not None

def test_get_by_id():
    lista = []
    lista = adauga_obiect(1, "masa", "lemn" , 100, "birou", lista)
    lista = adauga_obiect(2, "scaun", "fier forjat", 200, "contabilitate", lista)

    assert getBYId(1, lista) == [("id", 1), ("nume", "masa"), ("descriere", "lemn"), ("pret", 100),
                                   ("locatie", "birou")]
    assert getBYId(2, lista) == [("id", 2), ("nume", "scaun"), ("descriere", "fier frojat"), ("pret", 200),
                                   ("locatie", "contabilitate")]


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
