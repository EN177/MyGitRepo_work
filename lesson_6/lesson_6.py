# Условия 

# u_input = input('your number:')

# if u_input.isnumeric():
#     u_input = int(u_input)

#     if u_input == 1:
#         print('one')
#     elif u_input ==2:
#         print('two')
#     else:
#         print('many')

# else:
#     print('Enter a number please')

# Циклы

# names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill'] # this is List

# for name in names:
#     print(name)

# for name in names:
#     if name.startswith ('J'):
#         print('Mister', end=' ')
#     print(name)

# persons = {'John':123, 'Tom':234, 'James':456} # this is Dictionary
# # for person in persons.values(): # persons.keys
# #     print(person)

# # for person in persons: # persons.keys
# #     print(f'{person}: {persons[person]}')

# for name, height in persons.items():
#     # name, height = person # unpackaging
#     print(f'{name}: {height}')

text = 'John Tom James Bob Jim Bill Ball'
words = text.split() # to make collection
fin_words = []
for word in words:
    if 'J' in word:
        print(word)
else:
    fin_words.append(word)
print(' '.join(fin_words)) # does not work!
