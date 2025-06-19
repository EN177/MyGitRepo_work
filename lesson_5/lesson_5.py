# распаковка 

# my_list = [1, 3]
# my_tuple = (2, 6, 9)
# # a = my_list [0]
# # b = my_list [1]
# a, b = my_list #распаковка !
# # c = my_tuple [0]
# # d = my_tuple [1]
# # f = my_tuple [2]
# c, d, f = my_tuple #распаковка !
# print (a, b, c, d, f)

# срез

# m_list = [1, 3, 5, 7, 9, 11]
# print (m_list[:4]) #до какого элемнта рампечатать (не включительно)
# print (m_list[1:4])
# print (m_list[1::2]) #каждыц второй распечатается 
# print (m_list[:]) # печатать всё

# методы строк 

# text = 'my long long string'
# print (text[3:7])
# print ('long' in text)
# print (text.count ('long'))
# print(text.find ('lone'))
# print (text[0:7])


# txt = 'ThIs tExt wiTH meSSed Up capitaLIZation!'
# print(txt.capitalize())
# print(txt.title())
# print(txt.upper())
# print(txt.lower())

# txt = 'ThIs tExt wiTH meSSed Up capitaLIZation!'
# string = txt.lower().index('text')
# print (txt[:string].lower() + txt[string:].upper())

#Replace
# msg = 'Hello world!'
# msg = msg.replace('world', 'universe')
# print(msg)

# txt = ' admin ' #с пробелами
# # txt = txt.replace(' ', '')
# txt = txt.strip()
# # txt = txt.rstrip() or lsstrip
# print(txt)

# Избавиться от ковычек
# txt = '"name"'
# txt = txt.strip('"')
# print(txt)

# Парсинг Строка - список

# my_str = 'some little text'
# my_list = my_str.split()
# print (my_list)

#наоборот
# lang = ['python', 'Java', 'ruby']
# print(lang)
# lang=', '.join(lang)
# print(lang)

# Форматирование строки 
a = 'one'
b = 'two'
# print('First is', a, ', second is', b)
# my_text = 'First is %s, secons is %s' #old from 2.7
# print(my_text % (a, b))
#как надо!

# my_text = 'First is {1}, second is {1}'
# print(my_text.format(a, b))

#f-string !!!!
my_text = f'First is {a}, second is {b}'
print(my_text)
