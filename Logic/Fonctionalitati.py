from Domain.Obiecte import get_locatie, get_pret


def change_location(locatie_noua,lista):
    '''
    Mutarea tuturor obiectelor intr-o anumita locatie
    :param locatie_noua: Locatia in care vor fi mutate obiectele
    :param lista: Lista de obiecte
    :return: Returneaza o lista cu obiectele mutate intr-o locatie precizata de user
    '''

    for obiect in lista:
        if get_locatie(obiect) != locatie_noua:
            obiect["locatie"] = locatie_noua

    return lista


def max_price(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat ={}
    for obiect in lista:
        locatie= get_locatie(obiect)
        if locatie in rezultat:
             if get_pret(obiect)> rezultat[locatie]:
                rezultat[locatie] = get_pret(obiect)
        else:
            rezultat[locatie] = get_pret(obiect)

    return rezultat