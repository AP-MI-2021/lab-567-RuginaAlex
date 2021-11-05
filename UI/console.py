from Domain.Obiecte import to_string
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect
from Logic.Fonctionalitati import change_location, max_price
from UI.console2 import runMenu2


def printmenu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica obiect")
    print("4. Mutarea tuturor obiectelor intr-o locatie")
    print("5. Determinarea celui mai mare preț pentru fiecare locație")
    print("a. Afiseaza toate obiectele")
    print("y. Command Line")
    print("x. Iesire")


def uiAdaugaObiect(lista):
    try:
        id=input ("Dati id-ul: ")
        nume = input ("Dati numele: ")
        descriere = input ("Dati descriere: ")
        pret = float( input ("Dati pret: "))
        locatie = input ("Dati locatie: ")

        return adauga_obiect(id , nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereObiect(lista):
    id = input("Dati id-ul prajiturii de sters: ")
    return stergere_obiect(id, lista)


def uiModificaObiect(lista):
    try:
        id = input("Dati id-ul prajiturii de modificat : ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float (input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        return modificare_obiect(id, nume, descriere, pret, locatie,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiChangeLocation(lista):
    locatie_noua = input("Dati locatia noua: ")
    return change_location(locatie_noua,lista)


def uiMaxPrice(lista):
    rezultat = max_price(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))



def showAll(lista):
    for obiect in lista:
        print(to_string(obiect))
    if lista == []:
        print ("Dictionarul este gol!")




def runMenu(lista):
    while True:
        printmenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaObiect(lista)

        elif optiune == "2":
            lista = uiStergereObiect(lista)

        elif optiune == "3":
            lista = uiModificaObiect(lista)

        elif optiune == "4":
            lista = uiChangeLocation(lista)

        elif optiune == "5":
            uiMaxPrice(lista)


        elif optiune == "y":
            runMenu2(lista)


        elif optiune == "a":
            showAll(lista)

        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
