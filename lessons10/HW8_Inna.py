#Реалізуйте біблиотеку з будь-яким функціоналом. Наприклад, створіть функції для арифметичних операцій і побудуйте каскад імпортів з декількох packagів. Має бути можливіcть імпортувати деякі функції з пакета, але не всі.
import lessons10
print(lessons10.summ(4,5))

import datetime
import re

#Створіть обробку одного будь-якого exception, який не використався як приклад на занятті. Виведіть результат в консоль
def difference(a,b):
    try:
        if a>b:
            return a-b
    except Exception:
        print('b cannot be > than a')
    else:
        print('a and b cannot be equal to 0')

print(difference(0,0))

#Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. Приймає на вхід будь-яку дату та час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -). Повертає datetime. В цій задачі скористайтесь datetime.timedelta
def new_date(date, days, symbol):
    if (symbol == True):
        return date + datetime.timedelta(days)
    elif (symbol == False):
        return date - datetime.timedelta(days)

print(new_date(datetime.datetime.now(), 5, False))


#Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), вираховуючі різницю між наданим значеням і значенням datetime.now(). Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp. В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль
birthday = datetime.datetime(year=1950, month=10, day= 10)
now = datetime.datetime.now()
age = now.year - birthday.year
print(age)
print(datetime.datetime.timestamp(now))


