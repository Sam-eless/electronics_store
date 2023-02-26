class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, product, price, amount):
        self.product = product
        self.price = price
        self.amount = amount
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.amount

    def apply_discount(self):
        self.price *= Item.pay_rate