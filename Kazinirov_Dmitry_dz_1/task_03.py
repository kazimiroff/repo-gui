words = ["процент", "процента", "процентов"] #создаём список вариантов сколнённых слов
number = int(input("Введите число от 1 до 20!")) #просим пользователя ввести число
if number == 1:
    print( number, words[0])
elif number >= 2 and number <= 4:
    print( number, words[1])
elif number >= 5 and number <= 20:
    print( number, words[2])
#создаём условия при которых при вводе определенного числа будет по индексу выводится на экран
# число введенное пользователем и соответствующее условию склонённое слово