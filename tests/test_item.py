from electronics_store.item import Item
import pytest


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
    path_csv_file = 'items_test.csv'
    test_list = Item.instantiate_from_csv(path_csv_file)
    assert len(test_list) == 5
    assert isinstance(test_list[0], Item)
    assert test_list[3].quantity == '5.5'
    assert test_list[4].quantity == 5
