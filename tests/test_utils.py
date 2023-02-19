def test_items(test_item):
    assert test_item.product == "бананы"
    assert test_item.price == 80
    assert test_item.amount == 2000
    assert test_item.calculate_total_price() == 80 * 2000
    test_item.apply_discount()
    assert test_item.price == 80 * 0.85
