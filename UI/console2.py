from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect
from UI.console import showAll



def help ():
    print("""
Puteti da mai multe comenzi simultan, pe care le puteti separa prin ';',inclusiv la final, fiecare functia avand structura
Adaugare: add,id,nume,descriere,pret,locatie
Stergere: delete,id-ul obiectului
Modifica obiectul: modificare,id,nume,descriere,pret,locatie
Afisare Lista: showall
Stop: stop
""")

def runMenu2(lista):
    while True:
        help()
        stop = False
        comanda = input("Scrieti comenzile, despartite de ';': ").split(';')
        for i in range(len(comanda)):
            det = comanda[i].split(',')
            if det[0] == 'add':
                try:
                    lista = adauga_obiect(det[1],det[2],det[3],det[4],det[5],lista)
                except IndexError as ie:
                    print(f"Eroare: {ie}")
            elif det[0] == 'delete':
                try:
                    lista = stergere_obiect(det[1],lista)
                except ValueError as de:
                    print(f"Eroare: {de}")
            elif det[0] == 'modificare':
                try:
                    lista=modificare_obiect(det[1],det[2],det[3],det[4],det[5],lista)
                except ValueError as ve:
                    print("eroare {}".format(ve))
                    return lista

            elif det[0] == 'showall':
                showAll(lista)
            elif det[0] == 'stop':
                stop = True
                break
        if stop is True:
            print("A crapat ;(")
            break