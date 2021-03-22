#2
a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list_1 = [] #обьявляем новый список

for i in a:
    i = int(a[1])
    i = format(i, '02')
new_list_1.append(i)
for i in a:
    i = int(a[3])
    i = format(i, '02')
new_list_1.append(i)
for i in a:
    i = int(a[8])
    i = format(i,'02')
new_list_1.append(i)
#как записать это в цикл не пойму как тк числа в списке имеют тип str и как их отфильтровать от строк не придумал
#на этом решение встало



print(new_list_1)
