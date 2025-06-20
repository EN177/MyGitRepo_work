# while loop

# i = 0

# while i < 5:
#     print('hello')
#     i += 1
# print('the end')

# infinite loop

# while True:
#     u_input = input('enter something: ')
#     if u_input == "exit":
#         break
#     elif u_input == 'skip':
#         continue
#     elif len(u_input) > 10:
#         print('Input too long!')
#     else:
#         print('Input is OK!')
# print('See you!')

# FUNCTIONS

# a = 1
# b = 5
# c = 7
# d = 9
# y = 11
# main_number =47

# print(a + main_number)
# print(b + main_number)
# print(c + main_number)
# print(d + main_number)
# print(y + main_number)

# Better

# a = 1
# b = 5
# c = 7
# d = 9
# y = 11
# main_number =47

# def calc(numb):
#     result = (numb + main_number) # was print
#     return result
# calc(c)


def power(number, degree=2):
        return number ** degree
print(power(2)) # возведет по умолчанию во 2ю степень
print(power(2, 3))

