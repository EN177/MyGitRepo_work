# summer = True
# if summer is True:
#     print('Fine')
# else:
#     print('bad')

# Встроенные функции

# num = [1, 45, 23, 32, 89]
# print(max(num))
# print(min(num))
# print(sum(num))
# print(sorted(num))
# print(sorted(num, reverse=True))

# MAP

# my_list = [1, 2, 3, 4, 5]
#             # new_list = []
#             # for x in my_list:
#             #     new_list.append(x * 2)
# new_list = map(lambda x: x * 2, my_list)
# print(list(new_list))

#DATE TIME

import datetime

# time_now =  datetime.datetime.now()
# print(time_now)
# print(time_now.hour)
# print(time_now.year)
# print(time_now.isoweekday())

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

e_date = datetime.datetime(1960, 1, 15)
print(e_date)

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'

python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')

print(python_date)
print(python_date.month)

human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)