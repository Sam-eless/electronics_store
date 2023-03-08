from electronics_store.item import Item
import pytest
from electronics_store.exception_classes import InstantiateCSVError


def test_items(test_item):
    assert test_item.product == "бананы"
    assert test_item.price == 80
    assert test_item.quantity == 2000
    assert test_item.calculate_total_price() == 80 * 2000
    test_item.apply_discount()
    assert test_item.price == 80 * 0.85


def test_correct_product_setter(test_item):
    test_item.product = 'test_name'
    assert test_item.product == 'test_name'


def test_incorrect_product_setter(test_item):
    """Имя больше 10 символов задать нельзя."""
    test_item.product = 'shortname'
    assert test_item.product == 'shortname'
    with pytest.raises(ValueError):
        test_item.product = 'Длина названия товара больше 10 символов'


def test_is_integer():
    """Является ли число целым."""
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.73) is False


def test_instantiate_from_csv():
    """Тестирование альтернативного способ создания объектов-товаров.
    Количество совпадает. Проверка на целое число успешна"""
    # path_csv_file = 'tests/items_test.csv'
    path_csv_file = 'items_test.csv'
    test_list = Item.instantiate_from_csv(path_csv_file)
    assert len(test_list) == 5
    assert isinstance(test_list[0], Item)
    assert test_list[3].quantity == '5.5'
    assert test_list[4].quantity == 5


def test_repr(test_item):
    assert test_item.__repr__() == Item("бананы", 80, 2000).__repr__()


def test_str(test_item):
    assert test_item.__str__() == Item("бананы", 80, 2000).__str__()

def test_instantiate_from_csv_error():
    path_csv_file = 'items2_test.csv'
    # path_csv_file = 'tests/items2_test.csv'
    # with pytest.raises(InstantiateCSVError):
    #     test_list = Item.instantiate_from_csv(path_csv_file)
    assert Item.instantiate_from_csv(path_csv_file) == 'Файл по указанному пути поврежден: items2_test.csv'

def test_instantiate_from_csv_error_2():
    path_csv_file = 'items1_test.csv'
    # path_csv_file = 'tests/items2_test.csv'
    with pytest.raises(FileNotFoundError):
        test_list = Item.instantiate_from_csv(path_csv_file)


def test_add(test_item, test_phone):
    assert test_item + test_phone == 2005
    with pytest.raises(ValueError):
        assert test_item + 100 == f'Переданы экземпляры не Phone или Item классов'
