from.reader import Reader
class CsvReader(Reader):

    def __init__(self, filename:str):
        self.__filename = filename

    def read_csv_file(self):
        with open(self.__filename, 'r') as csv_file:
            text = csv_file.read()