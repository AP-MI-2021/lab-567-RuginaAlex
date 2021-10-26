from Domain.Obiecte import get_id, creeaza_obiect


def adauga_obiect (id, nume, descriere, pret, locatie,lista):
    '''
Adauga obiect intr
    :param id:
    :param nume:
    :param descriere:
    :param pret:
    :param locatie:
    :param lista:
    :return:
    '''

    obiect=creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def stergere_obiect (id,lista):
    return [obiect for obiect in lista if get_id(obiect) != id]


def modificare_obiect (id, nume, descriere, pret, locatie, lista):
    '''
    Modifica un obiect dupa id
    :param id: id-ul obiectului
    :param obiectNou: obiect cu care se inlocuieste vechiul obiect
    :param lista: lista de obiecte
    :return: lista continand vechile obiecte nemodificate si obiectul modificat dupa id
    '''

    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiectNou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append (obiectNou)
        else:
            lista_noua.append(obiect)

    return lista_noua



