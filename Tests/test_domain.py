from Domain.Obiecte import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect= creeaza_obiect("1", "calculator", "Acer" , 2400 , "birou contabilitate")
    assert get_id(obiect) == "1"
    assert get_nume(obiect) =="calculator"
    assert get_descriere(obiect) == "Acer"
    assert get_pret(obiect) == 2400
    assert get_locatie(obiect) == "birou contabilitate"


