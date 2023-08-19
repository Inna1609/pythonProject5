from lesson16.HWdishes.dishes.class_dish import Dish

class Pasta(Dish):
    def __init__(self, name,price):
        super().__init__(name,price)
        if self.name == 'Carbonara':
            self.price = 10
        elif self.name == 'Spaghetti':
            self.price = 15
        elif self.name == 'Lasagna':
            self.price = 20
        else:
            raise Exception('not correct name')

    def order(self):
        print(f'Your pasta {self.name} cost {self.price}')

