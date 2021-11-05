def creeaza_obiect(id,nume,descriere,pret,locatie):
   '''
   Creeaza obiect
   :param id: string
   :param nume: string
   :param descriere: string
   :param pret: float
   :param locatie: string
   :return: Returneaza un dictionar ce retine un obiect.
   '''

   return {
       'id': id,
       'nume': nume,
       'descriere': descriere,
       'pret': pret,
       'locatie': locatie

   }


def get_id(obiect):
    '''
    Ia id-ul obiectului
    :param obiect: dictionar de tip obiect
    :return: id-ul obiectului
    '''

    return obiect['id']


def get_nume(obiect):

    return obiect['nume']

def get_descriere(obiect):

   return obiect['descriere']
   
def get_pret(obiect):

   return obiect['pret']
   

def get_locatie(obiect):

    return obiect ['locatie']
    


def to_string(obiect):
    return f"Obiectul cu id: {get_id(obiect)}, cu numele de: {get_nume(obiect)}, cu descrierea: {get_descriere(obiect)}, " \
           f"care costa :{get_pret(obiect)}, si se gaseste in locatia: {get_locatie(obiect)}"

