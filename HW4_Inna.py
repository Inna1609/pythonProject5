import random
def random_dictionary(name,lastname):
    copy_name = name[:]
    copy_lastname = lastname [:]
    random.shuffle(copy_name)
    random.shuffle(copy_lastname)
    length_name = len(copy_name)
    length_lastname = len(copy_lastname)
    dictionary = {}
    start = 0
    for index, key in enumerate(copy_name):
        end = -1
        if index <length_name - 1:
            end = random.randint(start +1, length_lastname - (length_name - index))
        dictionary[key] = copy_lastname[start:end]
        start = end
    return dictionary

name = ['Ira', 'Ion', 'Juli']
lastname = ['Ivanova', 'Petrova', 'Jonova']

random_dictionary(name,lastname)

