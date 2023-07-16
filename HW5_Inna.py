#Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.

list1 = [1, 2, 3, 4, 5,6,7,8,9,0]
list2 = [0,9,8,7,6,5,]

same_numbers = list(filter(lambda x: x in list1, list2))
print(same_numbers)

#Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда

is_it_number =lambda x: x.isnumeric()
print(is_it_number("1"))

# Знайти список із максимальною та мінімальною довжиною за допомогою лямбда.

list_1 = [10, 20, 30, 40, 50]
list_2 = [1,2,3]
list_3 = [1]
list_4 = [1,2,3,4,5,6,7,8,9,0]
list_5 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
all_lists = [list_1] + [list_2] + [list_3] + [list_4]+[list_5]
min_list = lambda x: min(x, key=len)
max_list = lambda x: max(x, key=len)
print(min_list(all_lists))
print(max_list(all_lists))