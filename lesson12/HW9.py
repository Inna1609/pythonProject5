# 1.Створіть класс з описом будь-якої тварини. Додайте 1 static method, 3 звичайних методи
import random
class Dog:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age
    @staticmethod
    def greeting():
        print("Hello. I am a dog")

    def dog_name(self):
        print(f'Dog name is {self.name}')

    def get_kind(self):
        print(f'This dog is {self.kind}')

    def get_age(self):
        print(f'I am {self.age} old')

my_dog = Dog ('Bob', 'Vivcharka', 3)
Dog.greeting()
print(my_dog.dog_name())
print(my_dog.get_age())
print(my_dog.get_kind())

# 2.Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod, 3 звичайних методи

class Company:
    def __init__(self, name, age, location, sum_employees):
        self.name = name
        self.age = age
        self.location = location
        self.sum_employees = sum_employees

    @classmethod
    def name_and_location(cls, name, location):
        return(name,location)
    def get_name(self):
        return self.name
    def get_age(self):
        print(f'Company age is {self.age}')

    def size(self):
        print(f'Number of employees is {self.sum_employees}')

Apple = Company( 'Apple', 30, 'CA', 1000000)
Google = Company('Google', 25, 'PA', 500000)
Scientific = Company('Scientific', 50, 'WA', 1000)

Amazon = Company.name_and_location('Amazon', 'Sunnyvale')
print(Amazon)

print(Apple.get_name())
print(Google.size())
print(Scientific.get_age())


# 3.Створіть декоратор, який виводить в консоль ім'я функції, яку було ввикликано. Наприклад, створіть пару функцій для аріфметичних операцій додавання і множення. При виклику цих функцій має повертатись результат операції і виводиться в консоль ім'я функції, яку було ввикликано.

def function_name(function):
    def get_name(*args, **kwargs):
        print(f'function name: {function.__name__}')
        result = function(*args, **kwargs)
        return result

    return get_name
@function_name
def get_sum(num1, num2):
    print(num1 + num2)


@function_name
def get_multiplication(num1, num2):
    print(num1 * num2)


get_sum(1, 2)
get_multiplication(2,5)


# 4.Створіть за допомогою list comprehension список, в якому буде 100 елементів, і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією randint із модуля random). Порахуйте кількість кожного елемента і виведіть в консоль

comprehension_list = [random.randint(1, 10) for i in range(100)]
print(comprehension_list)

def get_number_elements(element):
    result = comprehension_list.count(element)
    print('There are ' + str(result) + ' ' + str(element) +' in a list.')
get_number_elements(1)
get_number_elements(2)
get_number_elements(3)
get_number_elements(4)
get_number_elements(5)
