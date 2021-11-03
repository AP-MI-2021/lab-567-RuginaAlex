def creeaza_obiect(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    '''
    Creeaza obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: Returneaza un dictionar ce retine un obiect.


    
    return {
        'id' : id,
        'nume' : nume,
        'descriere' : descriere,
        'pret' : pret,
        'locatie' : locatie

    }
'''

    return [_id, _nume, _descriere, _pret, _locatie]

def get_id(obiect):
    '''
    Ia id-ul obiectului
    :param obiect: dictionar de tip obiect
    :return: id-ul obiectului
    '''

    #return obiect['id']
    return obiect[0]

def get_nume(obiect):

    #return obiect['nume']
    return obiect[1]
def get_descriere(obiect):

   # return obiect['descriere']
   return  obiect[2]
def get_pret(obiect):

   #return obiect['pret']
   return obiect[3]

def get_locatie(obiect):

    #return obiect ['locatie']
    return obiect[4]


def to_string(obiect):
    return f"Obiectul cu id: {get_id(obiect)}, cu numele de: {get_nume(obiect)}, cu descrierea: {get_descriere(obiect)}, " \
           f"se poate gasi in locatia: {get_locatie(obiect)}"

