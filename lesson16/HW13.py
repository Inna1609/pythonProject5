#опишіть 1 будь-який клас, за умови що буде існувати тільки один інстанс цього класу.
from abc import abstractmethod


def singleton(_class):

    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')
    return inner

@singleton
class Cat:
    def __init__(self, age, color, name):
        self.age = age
        self.color = color
        self.name = name


Mandy = Cat(4,'black','Mandy')
Candy = Cat(2,'white','Candy')
print(Mandy.age)
print(Candy.color)

#Oпишіть частину функціоналу замовлення в ресторані. OrderPart класс має метод, що повертає певне блюдо.
#Можуть бути різні блюда, наприклад Risotto, Pasta, Pizza, які наслідуються від одного батьківського абстрактного класу Dish(Factory).

class Dish():

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class Order:

    def __init__(self, dish):
        self.dish = dish

    def get_dish(self):
        return self.dish



class Risotto(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Pasta(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Pizza(Dish):

    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

order_part = Order(Risotto("Risotto with cheese", 15))
print(order_part.get_dish().get_name())

order_part = Order(Pasta("Spaghetti with meat", 10))
print(order_part.get_dish().get_name())

order_part = Order(Pizza("Margarita pizza", 20))
print(order_part.get_dish().get_name())