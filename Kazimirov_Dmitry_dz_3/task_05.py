#5
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random
n = int(input('Введите число шуток!')) #просим пользователя сгенерировать количество шуток
new_list = [] #создаём новые список в который будет добавляться шутка

def get_jokes(n):
    for i in range(n): #цикл для списка
        new_list.append((list(zip([random.choice(nouns)], [random.choice(adverbs)], [random.choice(adjectives)]))))

get_jokes(n)
print(new_list)
# не понимаю как избавиться от лишних скобок в результате
