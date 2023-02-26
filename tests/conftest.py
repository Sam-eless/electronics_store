import pytest
from electronics_store.item import Item


@pytest.fixture
def test_item():
    item1 = Item("бананы", 80, 2000)
    return item1