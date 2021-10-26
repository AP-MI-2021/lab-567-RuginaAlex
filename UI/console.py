from Domain.Obiecte import to_string
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect


def printmenu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica obiect")
    print("a. Afiseaza toate obiectele")
    print("x. Iesire")


def uiAdaugaObiect(lista):
    id=input ("Dati id-ul: ")
    nume = input ("Dati numele: ")
    descriere = input ("Dati descriere: ")
    pret = float( input ("Dati pret: "))
    locatie = input ("Dati locatie: ")
    return adauga_obiect(id , nume, descriere, pret, locatie, lista)


def uiStergereObiect(lista):
    id = input("Dati id-ul prajiturii de sters: ")
    return stergere_obiect(id, lista)


def uiModificaObiect(lista):
    id = input("Dati id-ul prajiturii de modificat : ")
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret = float (input("Dati noul pret: "))
    locatie = input("Dati noua locatie: ")
    return modificare_obiect(id, nume, descriere, pret, locatie,lista)


def showAll(lista):
    for obiect in lista:
        print(to_string(obiect))


def runMenu(lista):
    while True:
        printmenu()
        optiune=input ("Dati optiunea: ")
        if optiune == "1":
            lista=uiAdaugaObiect(lista)

        elif optiune == "2":
            lista=uiStergereObiect(lista)

        elif optiune == "3":
            lista=uiModificaObiect(lista)

        elif optiune == "a":
            showAll(lista)

        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
