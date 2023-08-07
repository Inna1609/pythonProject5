from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self,salary,position):
        self.salary = salary
        self.position = position

        @abstractmethod
        def do_work(self):
            raise NotImplementedError('not implemented')

class Toyota_employee(Employee):

    def __init__(self, salary,position):
        super().__init__(salary,position)
    def do_work(self):
        print('I m doing Toyota stuff')

class Renault_employee(Employee):

    def __init__(self, salary,position):
        super().__init__(salary,position)
    def do_work(self):
        print('I m doing Renault stuff')

employee = Employee('worker', 2000)