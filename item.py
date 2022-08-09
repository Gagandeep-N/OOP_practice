import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0
        assert quantity >= 0

        #assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for i in items:
                Item(
                    name = i.get('name'),
                    price = float(i.get('price')),
                    quantity = int(i.get('quantity')),
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"