#4
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name_list = [] #создаём список только из имён сотрудников
removed_1 = my_list.pop(0) #извлекаем строку с именем сотрудника
removed_1 = removed_1.title() #пока у нас есть строка переделываем всем словам 1 букву в верхий регистр
removed_2 = my_list.pop(0)
removed_2 = removed_2.title()
removed_3 = my_list.pop(0)
removed_3 = removed_3.title()
removed_4 = my_list.pop(0)
removed_4 = removed_4.title()

#print(my_list)
#print(removed_1)
#print(removed_2)
#print(removed_3)
#print(removed_4)

for i in removed_1:
    name_1 = (removed_1[removed_1.index(' '):]) #заносим в переменную имя сотрудника с помощью срезки относительно индекса пробела
name_list.append(name_1) #помещаем имя сотрудника в список имён

for i in removed_2:
    name_2 = (removed_2[-removed_2.index(' '):])
name_list.append(name_2)

for i in removed_3:
    name_3 = (removed_3[-removed_3.index(' '):]) #с именем Николай проблема - не понял как решить
name_list.append(name_3)

for i in removed_4:
    name_4 = (removed_4[removed_4.index(' '):])
name_list.append(name_4)

#print(name_1)
#print(name_2)
#print(name_3)
#print(name_4)
#print(name_list)

for i in name_list:
    print("Привет, " + i)