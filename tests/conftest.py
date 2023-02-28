import pytest
from electronics_store.item import Item
from electronics_store.phone import Phone


@pytest.fixture
def test_item():
    item1 = Item("бананы", 80, 2000)
    return item1


@pytest.fixture
def test_phone():
    phone1 = Phone("Nokia N82", 29_999, 5, 1)
    return phone1
