from Tests.Teste_Functionalitati import test_max_price
from Tests.testCRUD import test_adauga_obiect, test_stergere_obiect, test_modificare_obiect, \
    test_getById
from Tests.test_domain import test_obiect


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()
    test_modificare_obiect()
    test_getById()
    test_max_price()
