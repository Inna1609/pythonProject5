from .cav_reader import CsvReader
from .csv_proxy_reader import CsvProxyReader

csv_reader = CsvReader('lesson17/name.csv')
proxy_reader  = CsvProxyReader(csv_reader)
print(proxy_reader.read())