from electronics_store.item import Item


class MixinLang:
    def __init__(self, *args, **kwargs):
        self.__language = "EN"
        super().__init__(*args, **kwargs)

    def change_lang(self):
        """Изменяет язык (раскладку) клавиатуры.
        Доступные языки - "EN", "RU"."""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        """Возвращает язык клавиатуры"""
        return self.__language


class Keyboard(MixinLang, Item):
    def __init__(self, product: str, price: int, quantity: int):
        super().__init__(product, price, quantity)


kb = Keyboard('Dark Project KD87A', 9600, 5)
print(kb)
print(kb.language)
kb.change_lang()
print(kb.language)
# kb.language = 'CH'
