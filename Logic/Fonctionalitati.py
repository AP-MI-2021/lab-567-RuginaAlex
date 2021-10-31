from Domain.Obiecte import get_locatie, get_pret


def change_location(locatie_veche,locatie_noua,lista):
    '''
    Mutarea obiectelor dintr-o locatie in alta
    :param locatie_veche: Locatia actuala a obiectului
    :param locatie_noua: Locatia in care va fi mutat obiectul
    :param lista: lista de obiecte
    :return: Lista actualizata din punct de vedere a locatiilor obiectelor
    '''


    for obiect in lista:
        if get_locatie(obiect) == locatie_veche:
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