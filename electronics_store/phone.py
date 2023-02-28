from electronics_store.item import Item


class Phone(Item):
    def __init__(self, product: str, price: int, quantity: int, number_of_sim: int):
        super().__init__(product, price, quantity)
        self.__number_of_sim = self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """Если number_of_sim меньше 0 выбрасывает ошибку"""
        if int(number_of_sim) > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество сим карт не может быть 0 и отрицательным.')

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.product}", {self.price}, {self.quantity}, {self.__number_of_sim})'
