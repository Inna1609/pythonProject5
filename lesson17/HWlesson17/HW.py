#1 завдання. Напишіть адаптер, який конвертує json в csv.
# тобто робить зворотню конвертацію від тієї, що ми реалізували на уроці.
# Приклад з уроку, а також json і csv додано, формат запису даних той самий.
import csv
import json

class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_file(self, filename: str):
        if not self.__lines:
            return

        fieldnames = self.__lines[0].keys()

        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.__data)

    def cleanup(self):
        self.__lines = []

converter = JsonConverter()
converter.read_file('hw.json')
converter.write_file('example.csv')


#2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок.
# Напишіть функцію, яка видаляє з csv один рядок. напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився.
# в якості перевірного csv можете скористатись доданим до завдання файлом або будь-яким іншим.
class CSVfunctions:
    def __init__(self, filename):
        self.filename = filename

    def add_line(self, data):
        with open(self.filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)

    def delete_line(self, index):
        lines = []
        with open(self.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                lines.append(row)

        try:
            index = int(index)
            if 0 <= index < len(lines):
                del lines[index]
        except ValueError:
            pass

        with open(self.filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(lines)