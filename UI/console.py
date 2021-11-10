from Domain.Obiecte import to_string
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect
from Logic.Fonctionalitati import change_location, max_price, ordering_objects, sum_prices, concatenation_str
from UI.console2 import runMenu2


def printmenu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica obiect")
    print("4. Mutarea tuturor obiectelor intr-o locatie")
    print("5. Determinarea celui mai mare preț pentru fiecare locație")
    print("6. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("7. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("8. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("a. Afiseaza toate obiectele")
    print("u. Undo")
    print("r. Redo")
    print("y. Command Line")
    print("x. Iesire")


def uiAdaugaObiect(lista,undolist,redolist):
    try:
        id=input ("Dati id-ul: ")
        nume = input ("Dati numele: ")
        descriere = input ("Dati descriere: ")
        pret = float( input ("Dati pret: "))
        locatie = input ("Dati locatie: ")
        rezultat = adauga_obiect(id , nume, descriere, pret, locatie, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereObiect(lista, undolist,redolist):
    try:
        id = input("Dati id-ul prajiturii de sters: ")
        rezultat =  stergere_obiect(id, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}.".format(ve))



def uiModificaObiect(lista,undolist,redolist):
    try:
        id = input("Dati id-ul prajiturii de modificat : ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float (input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        rezultat = modificare_obiect(id, nume, descriere, pret, locatie,lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiChangeLocation(lista,undolist:list,redolist:list):
    try:
        locatie_noua = input("Dati locatia noua: ")
        rezultat = change_location(locatie_noua,lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}.".format(ve))
        return lista

def uiMaxPrice(lista):
    rezultat = max_price(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def uiOrderingObjects(lista,undolist,redolist):
    rezultat = ordering_objects(lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat


def showAll(lista):
    for obiect in lista:
        print(to_string(obiect))
    if lista == []:
        print ("Dictionarul este gol!")


def uiSumPrices(lista):
    rezultat = sum_prices(lista)
    for locatie in rezultat:
        print("Locatia {} are suma de preturi:{}".format(locatie,rezultat[locatie]))


def uiConcatenationStr(lista,undolist,redolist):
    try:
        add_string = input("Dati descrierea care se va adauga: ")
        pret = float(input("Dati pretul cu care se va compara: "))
        concatenare=concatenation_str(pret,add_string, lista)
        undolist.append(lista)
        redolist.clear()
        return concatenare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_undo(lista, undolist, redolist):
    """
    Face undo
    :param lista: lista careia vrem sa-i facem undo
    :param undolist: lista pentru undo
    :param redolist: lista pentru redo
    :return: undo la lista
    """
    if len(undolist) > 0:
        redolist.append(lista)
        return undolist.pop()
    return lista


def ui_redo(lista, undolist, redolist):
    """
    Face redo la o comanda data.
    :param lista: Lista de obiecte
    :param undolist: Lista pentru undo
    :param redolist: Lista pentru redo
    :return: Redo la lista.
    """
    if len(redolist) > 0:
        undolist.append(lista)
        return redolist.pop()
    return lista





def runMenu(lista):
    undolist = []
    redolist = []
    while True:
        printmenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":

            lista = uiAdaugaObiect(lista,undolist,redolist)

        elif optiune == "2":
            lista = uiStergereObiect(lista,undolist,redolist)

        elif optiune == "3":
            lista = uiModificaObiect(lista,undolist,redolist)

        elif optiune == "4":
            lista = uiChangeLocation(lista,undolist,redolist)

        elif optiune == "5":
            uiMaxPrice(lista)

        elif optiune == "6":
           lista = uiOrderingObjects(lista,undolist,redolist)

        elif optiune == "7":
            uiSumPrices(lista)

        elif optiune == "8":
            lista = uiConcatenationStr(lista,undolist,redolist)

        elif optiune == "u":
            lista=ui_undo(lista,undolist,redolist)

        elif optiune == "r":
            lista=ui_redo(lista,undolist,redolist)


        elif optiune == "y":
            runMenu2(lista)


        elif optiune == "a":
            showAll(lista)

        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
