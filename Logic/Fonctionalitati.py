from Domain.Obiecte import get_locatie


def change_location(locatie_veche,locatie_noua,lista):
    '''
    Mutarea tuturor obiectelor intr-o anumita locatie.
    :param locatie:
    :param lista:
    :return:
    '''

    for obiect in lista:
        if get_locatie(obiect) == locatie_veche:
            obiect["locatie"] = locatie_noua

    return lista
