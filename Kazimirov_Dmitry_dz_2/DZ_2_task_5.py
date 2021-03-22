#5
products_coasts=[57.8, 46.51, 97, 50.5]
print(products_coasts)

products_coasts.sort() #сортируем тот же список по возрастанию
print(products_coasts)

new_list_1 = [] #обьявляем новый список
for i in products_coasts:
    new_list_1.append('{:.2f}'.format(i)) #форматируем список в числа с двумя знаками после запятой
#print(new_list_1)

my_str_1 = ','.join(str(i) for i in new_list_1 ) #преобразуем список в строку
#print(my_str_1)

string_form_1 = my_str_1.split('.') #форматируем строку - вставляем 'руб' вместо точки
string_1 = ' руб '.join(string_form_1)
#print(string_1)

string_form_2 = string_1.split(',') #форматируем строку ещё раз - вставляем 'коп' вместо запятой
string_2 = ' коп, '.join(string_form_2)
print(string_2)

#не создавать новый список, а так же решить задачу компактно не получилось ((