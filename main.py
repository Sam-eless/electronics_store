from electronics_store.item import Item
from electronics_store.phone import Phone
from electronics_store.exception_classes import InstantiateCSVError

def main():
    # item1 = Item("Смартфон", 10000, 20)
    # item2 = Item("Ноутбук", 20000, 5)
    #
    # print(item1.calculate_total_price())
    # print(item2.calculate_total_price())
    #
    # Item.pay_rate = 0.8  # устанавливаем новый уровень цен
    # item1.apply_discount()
    # print(item1.price)
    # print(item2.price)
    #
    # print(Item.all)
    #
    # for i in Item.all:
    #     print(i.product, i.price, i.quantity)

    # Homework_2
    # item1.product = "test111111112313name"
    # print(item1.product)
    items_csv_path = "electronics_store/items1.csv"

    Item.instantiate_from_csv(items_csv_path)  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам
    item4 = Item.all[0]
    print(item4.product)


    for i in Item.all:
        print(i.product, i.price, i.quantity)
    #
    # print(Item.is_integer(5))
    # print(Item.is_integer(5.0))
    # print(Item.is_integer(5.5))

    # Homework_3
    # item1 = Item("Смартфон", 10000, 20)
    # print(item1)
    # print(item1.__repr__())

    # Homework_4
    # phone1 = Phone("iPhone 14", 120_000, 5, 1)
    # print(phone1)
    # print(repr(phone1))
    # phone1.number_of_sim = 1
    # print(phone1.number_of_sim)
    #
    # phone2 = Phone("iPhone 14 Pro", 180_000, 50, 2)
    #
    # print(phone2 + phone1)


if __name__ == '__main__':
    main()
