from electronics_store.item import Item


def main():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())
    print(item2.calculate_total_price())

    Item.pay_rate = 0.8  # устанавливаем новый уровень цен
    item1.apply_discount()
    print(item1.price)
    print(item2.price)

    print(Item.all)

    for i in Item.all:
        print(i.product, i.price, i.amount)


if __name__ == '__main__':
    main()
