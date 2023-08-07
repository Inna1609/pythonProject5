#Опишіть класс будь-якого транспортного засобу. Скористайтесь двома рівнями наслідування і абстракцією за допомогою ABC(використання ABC не рахується за рівень наслідування)
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, title,speed, age, price):
        self.title = title
        self.speed = speed
        self.age = age
        self.price = price

    @abstractmethod
    def best_car(self):
        pass

class Toyota(Car):
    def __init__(self, title,speed,age,price):
        super().__init__(title,speed,age,price)

    def best_car(self):
        print('Toyota is the best car')

class BMV(Car):
    def __init__(self, title,speed,age,price):
        super().__init__(title,speed,age,price)

    def best_car(self):
        print('BMV is the best car')

class Acura(Toyota):
    def __init__(self,title, speed, age,price):
        super().__init__(title, speed, age, price)

    def best_car(self):
        print('Acura is child of Toyota is the best car')

class X_90(BMV):
    def __init__(self, title,speed,age,price):
        super().__init__(title,speed,age,price)

    def best_car(self):
        print('X_90 from BMV is the best car')

marka = Acura('EBT', 300, 5, 10000)
marka2 = X_90( 'XXX999', 400, 2,20000)

marka.best_car()
marka2.best_car()