import random
#1 Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
def common_member(a,b):
    a_set =set(a)
    b_set = set(b)
    if  (a_set & b_set):
        print (a_set & b_set)
    else:
        print("No common elements")

a= [1,2,3,4,5,6]
b = [8,7,6,5,4,3,2]

common_member(a,b)

#2

def average_mark(students):
    for val in students.items():
        val = students.values()
        average_val = int(sum(val)/ len(val))
        return average_val

def successful_students_list(students):
    students_dict = {}
    for key, val in students.items():
        if val > average_mark(students):
            students_dict[key] = val
    return list(students_dict)

students_marks = {"Ivan": 10, "Inna":90, "Petro": 60, "Ija":75, "Igor":85}

print(successful_students_list(students_marks))

#3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba']. напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат. для випадковості значень скористайтесь модулем random.
name = ['Ira', 'Ion', 'Juli']
lastname = ['Ivanova', 'Petrova', 'Jonova']
location = ['Lviv', 'Kyiv', 'Odesa']

def dict_random(name, lastname, location):
    dictionary1 = {'name': name[random.randint(0, len(name) - 1)],
                'lastname': lastname[random.randint(0, len(lastname) - 1)],
                'location': location[random.randint(0, len(location) - 1)]}
    return dictionary1

print(dict_random(name, lastname, location))
