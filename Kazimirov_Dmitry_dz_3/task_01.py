#1
dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

# решил без функции, пытался "адаптировать" под функцию  - не получилось

input_eng_word = input("Введите число на английском!")
print

for eng_word, rus_word in dictionary.items():
    if eng_word == input_eng_word:
        print(rus_word)

    #elif eng_word != input_eng_word:
        #print(None)  - если добавляю блок для печати None работает некорректно

