from lesson16.HWdishes.dishes.class_dish import Dish

class Risotto(Dish):
    def __init__(self, name,price):
        super().__init__(name,price)
        if self.name == 'Arborio':
            self.price = 10
        elif self.name == 'Roma':
            self.price = 15
        elif self.name == 'Padano':
            self.price = 20
        else:
            raise Exception('not correct name')

    def order(self):
        print(f'Your risotto {self.name} cost {self.price}')
