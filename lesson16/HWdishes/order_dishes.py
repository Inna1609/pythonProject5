from lesson16.HWdishes.dishes.Risotto import Risotto
from lesson16.HWdishes.dishes.Pasta import Pasta
from lesson16.HWdishes.dishes.Pizza import Pizza

class order_dish:
    @staticmethod
    def get_order(name, price):
        if name == 'Risotto':
            return Risotto(price)
        elif name == 'Pasta':
            return Pasta(price)
        elif name == 'Pizza':
            return Pizza(price)
        else:
            raise Exception('Try again')