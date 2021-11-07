from Domain.Obiecte import get_locatie, get_id, get_descriere
from Logic.CRUD import adauga_obiect, getBYId
from Logic.Fonctionalitati import change_location, max_price, ordering_objects, sum_prices, concatenation_str


def test_change_location():
    lista = []
    lista = adauga_obiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adauga_obiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adauga_obiect(3, "birou", "descriere 3", 3000, "loc2", lista)

    lista = change_location("loc3",lista)

    assert get_locatie(lista[0]) == "loc3"
    assert get_locatie(lista[1]) == "loc*3"
    assert get_locatie(lista[2]) == "loc3"






def test_max_price():
    lista = []
    lista = adauga_obiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adauga_obiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adauga_obiect(3, "birou", "descriere 3", 3000, "loc2", lista)


    rezultat= max_price(lista)

    assert len(rezultat) == 2
    assert rezultat["loc1"] == 4000
    assert rezultat["loc2"] == 3000


def test_ordering_objects():
    lista=[]
    lista = adauga_obiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adauga_obiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adauga_obiect(3, "birou", "descriere 3", 3000, "loc2", lista)
    rezultat = ordering_objects(lista)

    assert get_id(rezultat[0]) == "2"
    assert get_id(rezultat[1]) == "3"
    assert get_id(rezultat[2]) == "1"


def test_sum_prices():
    lista = []
    lista = adauga_obiect(1, "pc", "descriere 1", 4000, "loc1", lista)
    lista = adauga_obiect(2, "laptop", "descriere 2", 1000, "loc1", lista)
    lista = adauga_obiect(3, "birou", "descriere 3", 3000, "loc2", lista)

    rezultat = sum_prices(lista)

    assert len(rezultat) == 2
    assert rezultat["loc1"] == 5000
    assert rezultat["loc2"] == 3000


    def test_concatenation_str():
        lista = []
        lista = adauga_obiect(1, "pc", "descriere", 4000, "loc1", lista)
        lista = adauga_obiect(2, "laptop", "descriere", 1000, "loc1", lista)
        lista = adauga_obiect(3, "birou", "descriere", 3000, "loc2", lista)

        lista= concatenation_str(lista,"adaugare",2000)

        assert get_descriere(getBYId(lista,1)) == "descriereadaugare"
        assert get_descriere(getBYId(lista,2)) == "descreire"
        assert get_descriere(getBYId(lista,3)) == "descriereadaugare"
