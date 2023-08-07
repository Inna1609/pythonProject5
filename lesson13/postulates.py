
class Human:
    def  __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
class Employee(Human):
    
    def __init__(self, name, age, gender, salary,position):
        super().__init__(name, age,gender)
        self.salary = salary
        self.position = position

goose = Employee('Ivan', 2, 'male', 'meat', 'good boy')
print(goose)