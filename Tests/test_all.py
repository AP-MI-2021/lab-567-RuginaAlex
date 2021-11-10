from Tests.Test_undo_redo import test_undo_redo, test_change_location_undo_redo, test_ordering_undo_redo, \
    test_concatenation_str_undo_redo
from Tests.Teste_Functionalitati import test_max_price, test_ordering_objects, test_sum_prices, test_concatenation_str, \
    test_change_location
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
    test_ordering_objects()
    test_sum_prices()
    test_concatenation_str()
    test_undo_redo()
    test_change_location()
    test_change_location_undo_redo()
    test_ordering_undo_redo()
    test_concatenation_str_undo_redo()