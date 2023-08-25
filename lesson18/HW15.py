from abc import abstractmethod
import pytest


class Dish:

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


@pytest.fixture
def risotto():
    return Risotto("Risotto with cheese", 15)


@pytest.fixture
def pasta():
    return Pasta("Spaghetti with meat", 10)


@pytest.fixture
def pizza():
    return Pizza("Margarita pizza", 20)


class TestOrder(object):

    @pytest.mark.regression
    def test_get_dish_name_risotto(self, risotto):
        order = Order(risotto)
        assert order.get_dish().get_name() == "Risotto with cheese"


    def test_get_dish_price_risotto(self, risotto):
        order = Order(risotto)
        assert order.get_dish().get_price() == 15

    @pytest.mark.smoke
    def test_get_dish_name_pasta(self, pasta):
        order = Order(pasta)
        assert order.get_dish().get_name() == "Spaghetti with meat"

    def test_get_dish_price_pasta(self, pasta):
        order = Order(pasta)
        assert order.get_dish().get_price() == 10

    @pytest.mark.pizza
    def test_get_dish_name_pizza(self, pizza):
        order = Order(pizza)
        assert order.get_dish().get_name() == "Margarita pizza"

    def test_get_dish_price_pizza(self, pizza):
        order = Order(pizza)
        assert order.get_dish().get_price() == 20


if __name__ == "__main__":
    pytest.main()