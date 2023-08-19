from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def order(self):
        pass