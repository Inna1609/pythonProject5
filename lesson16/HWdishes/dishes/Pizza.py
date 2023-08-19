from lesson16.HWdishes.dishes.class_dish import Dish

class Pizza(Dish):
    def __init__(self, name,price):
        super().__init__(name,price)
        if self.name == 'Cheese':
            self.price = 10
        elif self.name == 'Margarita':
            self.price = 15
        elif self.name == 'Chicken_pizza':
            self.price = 20
        else:
            raise Exception('not correct name')

    def order(self):
        print(f'Your pizza {self.name} cost {self.price}')
