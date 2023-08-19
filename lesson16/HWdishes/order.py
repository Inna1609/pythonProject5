from lesson16.HWdishes.order_dishes import order_dish

class Order:
    def __init__(self):
        self.orders = None

    def get_order(self,kind_of_order, name,price):
            if kind_of_order == 'Dish':
                return order_dish().get_order(name, price)
            else:
                raise Exception('Sorry, your order is incomplete. Try again')



order_factory = Order()
order1 = order_factory.get_order('Dish','Spaghetti',15)
order1.order()
order2 = order_factory.get_order('Dish','Margarita',15)
print(order_factory.orders)
