#Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм, скриття,
# інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи

from abc import ABC, abstractmethod

class Art(ABC):
    def __init__(self,name, size: int,year: int,creator, material):
        self.name = name
        self.size = size
        self.year = year
        self.creator = creator
        self.material = material

    @abstractmethod
    def describe_art(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

  
    @staticmethod
    def greeting():
        print('We are happy see you here. Enjoy it')

    
class Pottery(Art):
    def __init__(self,name, size, year, creator, material):
        super().__init__(name,size,year,creator, material)



    def __name(self):
        print(f'There are {self.name} .')

    def __year(self):
        print(f'They was made at {self.year}')

    def __creator(self):
        print(f'This potter product was made by {self.year}')

    def __size(self):
        print(f'The size of this pottery product is {self.size}')

    def __thankful_note(self):
        print(f'This is gorgeus {self.name}')

    def describe_art(self):
        self.__name()
        self.__size()
        self.__year()
        self.__creator()
        self.__thankful_note()
        print('You are done')


class Painting(Art):
    def __init__(self,name, size, year, creator, material):
        super().__init__(name,size,year,creator, material)

    def __name(self):
        print(f'There are {self.name} .')

    def __year(self):
        print(f'This painting was made at {self.year}')

    def __creator(self):
        print(f'This painting was made by {self.year}')

    def __size(self):
        print(f'The size of this painting is {self.size}')

    def __thankful_note(self):
        print(f'This is gorgeus {self.name}')

    def describe_art(self):
        self.__name()
        self.__size()
        self.__year()
        self.__creator()
        self.__thankful_note()
        print('You are done')



pottery_product1 = Pottery('Pottery cup', 20, 1860, 'Gonchar', 'glue')
print(pottery_product1.greeting())
print(pottery_product1.describe_art())
pottery_product1.name = 'Pottery plate'
print(pottery_product1.name)

painting1 = Painting('Black square', 15, 1900, 'Malevych', 'paint')
print(painting1.greeting())
print(painting1.describe_art())
painting1.name = 'Malevych1'
print(painting1.name)



