import time
'''def lets_count_a_lot():
    for i in range(1000000):
        if i  == 9999:
            print(i)

start = time.time()
lets_count_a_lot()
end = time.time()
print(f'execution time is {end - start}')

def lets_count_a_lot():
    time.sleep(5)
    return 1

start = time.time()
lets_count_a_lot()
end = time.time()
print(f'execution time is {end - start}')'''

import datetime
print(datetime.date(2020,7,22))
print(datetime.date(year = 2023, month = 7, day=22))
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
today = datetime.datetime.now()
print(today.year)
print(today.month)
time1 = datetime.date(2021,5,14)
time2 = datetime.date(2021,7,20)
time3 = time2-time1
print(time3)
time4 = datetime.datetime(year=2023,month=7,day=22,hour=12,minute=1,second=15)
time5 = datetime.datetime.now()
print(time5-time4)
time6 = time4 +time3
print(time6)

time7 = datetime.datetime.now().timestamp()
print(time7)
time8 = time4.timestamp()
print(time8)
time9 = datetime.datetime.fromtimestamp(time8)
print(time9)

