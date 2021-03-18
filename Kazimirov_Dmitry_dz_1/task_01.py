seconds = int(input("Введите число!"))
if seconds <  60:
    print(seconds, "сек")

elif seconds >= 60 and seconds < (60**2):
    minutes = seconds // 60
    seconds = seconds % 60
    print(minutes, "мин",seconds, "сек" )

elif seconds >= (60 ** 2) and seconds < ((60**2)*24):
    hours = seconds // (60**2)
    minutes = seconds % (60**2)//60
    seconds = seconds % 60
    print(hours, "час",minutes, "мин",seconds, "сек")

elif seconds >= ((60**2)*24) and seconds < (((60 ** 2) * 24)*31):
    days = seconds // ((60**2)*24)
    hours = seconds // ((60**2)*24) % 60
    minutes = seconds % (60 ** 2) // 60
    seconds = seconds % 60
    print(days, "ден", hours, "час", minutes, "мин", seconds, "сек")

elif seconds >= (((60 ** 2) * 24)*31) and seconds < ((((60 ** 2) * 24) * 31)*12):
    months = seconds // (((60 ** 2) * 24)*31)
    days = seconds // (((60 ** 2) * 24)*31) % 31
    hours = seconds % ((60 ** 2) * 24) // (60 ** 2)
    minutes = seconds % (60 ** 2) // 60
    seconds = seconds % 60
    print(months, "мес", days, "ден", hours, "час", minutes, "мин", seconds, "сек")

elif seconds >= ((((60 ** 2) * 24) * 31)*12) and seconds < (((((60 ** 2) * 24) * 31) * 12)*100):
    years = seconds // ((((60 ** 2) * 24) * 31)*12)
    months = seconds // (((60 ** 2) * 24) * 31) % 12
    days = seconds % (((60 ** 2) * 24) * 31) // ((60 ** 2) * 24)
    hours = seconds % ((60 ** 2) * 24) // (60 ** 2)
    minutes = seconds % (60 ** 2) // 60
    seconds = seconds % 60
    print(years, "год", months, "мес", days, "ден", hours, "час", minutes, "мин", seconds, "сек")







