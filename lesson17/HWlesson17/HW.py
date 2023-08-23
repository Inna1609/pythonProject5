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


