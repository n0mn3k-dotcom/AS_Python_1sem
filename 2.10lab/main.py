if __name__ == "__main__":
    pass

# a
name = input("Введите имя файла: ")

bad_symbols = '\\/*?:"<>|'

for s in bad_symbols:
    if s in name:
        raise Exception("Недопустимое имя файла")

print("Имя файла введено корректно")

#б

date = input("Введите дату рождения: ")

try:
    day, month, year = date.split(".")
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        raise Exception
    int(day)
    int(month)
    int(year)
except:
    raise Exception("Неверный формат даты")

print("Дата введена корректно")

#в

x = input("Введите координату x: ")
y = input("Введите координату y: ")

try:
    float(x)
    float(y)
except:
    raise Exception("Некорректные координаты")

print("Координаты введены корректно")

