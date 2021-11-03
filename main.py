from Logic.CRUD import adauga_obiect
from Tests.test_all import run_all_tests
from UI.console import runMenu


def main () :
   run_all_tests()
   lista = []
   lista = adauga_obiect("1", "pc", "acer", 100, "loc1", lista)
   lista = adauga_obiect("2", "monitor", "144h", 200, "loc2", lista)
   runMenu(lista)


main()
