from .reader import Reader
from lesson17.proxy_pattern_example.c

class CsvProxyReader(Reader):

    def __init__(self, csv_reader:CsvReader):
        self.__result = ''
        self.__is_actual = True
        self.__reader = csv_reader

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.__reader
    def update_actual_status(self, actual_status):
        self.__is_actual = actual_status
