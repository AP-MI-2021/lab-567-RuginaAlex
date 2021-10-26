from Domain.Obiecte import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect


def test_adauga_obiect():
    lista = []
    lisat = adauga_obiect ("1", "calculator", "Acer" , 2400 , "birou contabilitate",lista)
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "calculator"
    assert get_descriere(lista[0]) == "Acer"
    assert get_pret(lista[0]) == 2400
    assert get_locatie(lista[0]) == "birou contabilitate"