import csv

import pytest


class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, product: str, price: int, quantity: int) -> None:
        self.__product = product
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= Item.pay_rate

    @property
    def product(self) -> str:
        return self.__product

    @product.setter
    def product(self, product_name) -> None:
        if len(product_name) < 10:
            self.__product = product_name
        else:
            print('Exception: Длина наименования товара превышает 10 допустимых символов')

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """Альтернативный способ создания объектов-товаров.
        Метод считывает данные из csv-файла и создает экземпляры класса,
        инициализируя их данными из файла.
        Целые числа в полях price и quantity преобразуются в int"""
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            item_list = []
            for row in reader:
                if cls.is_integer(float(row['price'])):
                    row['price'] = int(float(row['price']))
                if cls.is_integer(float(row['quantity'])):
                    row['quantity'] = int(float(row['quantity']))
                item_list.append(cls(row['name'], row['price'], row['quantity']))
        return item_list

    @staticmethod
    def is_integer(value):
        """Проверяет, является ли число целым"""
        if value % 1 == 0:
            return True
        else:
            return False
