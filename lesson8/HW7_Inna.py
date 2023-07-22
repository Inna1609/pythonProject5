import re
import csv
#1. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt) та повертає їх у вигляді списку рядків (назви повертати без крапки).
with open('domains.txt', 'r') as file1:
    list_1 = [line.strip() for line in file1]
    list_1 = [i.replace(".","") for i in list_1]
    print(list_1)

#2. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього. Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані
with open('names.txt', 'w') as names:
    names_fields = ['Number', 'Name', 'Country']
    names_dict_writer = csv.DictWriter(names, fieldnames= names_fields, delimiter = ',')
    names_dict_writer.writeheader()
    names_dict_writer.writerow({'Number': '1', 'Name': 'Ivan', 'Country': 'UK'})
    names_dict_writer.writerow({'Number': '2', 'Name': 'Ira', 'Country': 'Canada'})
    names_dict_writer.writerow({'Number': '3', 'Name': 'Ija', 'Country': 'Turkey'})
    def get_surnames():
        with open('names.txt', 'r') as names:
            names_reader = csv.DictReader(names, delimiter=',')
            names1 = []
            for row in names_reader:
                names1.append(row['Name'])
        return names1

names1 = get_surnames()
print(names1)

#3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду {"date": date} у яких date - це дата з рядка (якщо є), Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
def read_dates(file):
    dates = []
    with open(file, 'r') as file_with_dates:
        file_with_dates = file_with_dates.readlines()
        for line in file_with_dates:
            days = '[\w]+'
            month = '[a-zA-Z]+'
            years = '[0-9]+'
            result = re.findall(f'{days}[" "]{month}[" "]{years}|{month}[" "]{years}', line)
            if len(result) > 0:
                dates.append({'date': result[0]})
    return dates


print(read_dates('Authors.txt'))
