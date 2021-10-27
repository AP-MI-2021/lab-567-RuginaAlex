def creeaza_obiect(id, nume, descriere, pret, locatie):
    '''
    Creeaza obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: Returneaza un dictionar ce retine un obiect.
    '''
    '''
    
    return {
        'id' : id,
        'nume' : nume,
        'descriere' : descriere,
        'pret' : pret,
        'locatie' : locatie

    }
    '''
    obiect = [id, nume, descriere, pret, locatie]
    return obiect
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
    #return obiect['descriere']
    return obiect[2]
def get_pret(obiect):
    #return obiect['pret']
    return obiect[3]

def get_locatie(obiect):
    #return obiect ['locatie']
    return obiect[4]

def to_string(obiect):
   '''

   :param obiect:
   :return:

    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )
   '''
   return  "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        obiect[0],
        obiect[1],
        obiect[2],
        obiect[3],
        obiect[4]
    )