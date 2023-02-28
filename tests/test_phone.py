from electronics_store.phone import Phone
import pytest


def test_correct_setter(test_phone):
    test_phone.number_of_sim = 2
    assert test_phone.number_of_sim == 2


def test_incorrect_setter(test_phone):
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 'ValueError: Количество сим карт не может быть 0 и отрицательным.'


def test_repr(test_phone):
    assert test_phone.__repr__() == Phone("Nokia N82", 29_999, 5, 1).__repr__()
