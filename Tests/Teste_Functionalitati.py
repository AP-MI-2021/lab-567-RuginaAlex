from Domain.Obiecte import get_locatie
from Logic.CRUD import adauga_obiect
from Logic.Fonctionalitati import change_location


def test_change_location():
    lista = []
    lista = adauga_obiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adauga_obiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adauga_obiect(3, "birou", "descriere 3", 3000, "loc2", lista)
    lista = adauga_obiect(4, "masa", "descriere 4", 2000, "loc2", lista)
    lista = change_location("loc1", "loc2", lista)
    assert get_locatie(lista[0]) == "loc2"
    assert get_locatie(lista[1]) == "loc2"