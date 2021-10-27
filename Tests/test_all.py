from Tests.testCRUD import test_adauga_obiect, test_stergere_obiect, test_get_by_id, test_modificare_obiect
from Tests.test_domain import test_obiect


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()
    test_get_by_id()
    test_modificare_obiect()