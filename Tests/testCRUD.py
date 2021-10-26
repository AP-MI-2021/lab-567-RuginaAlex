from Domain.Obiecte import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, getBYId, stergere_obiect


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


