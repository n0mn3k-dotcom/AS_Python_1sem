if __name__ == "__main__":
    pass

import datetime

#а)
name = input('Введите имя файла: ')
bad_symb = '\\/*?:"<>|'
if any(symb in name for symb in bad_symb):
    raise Exception('Недопустимое имя файла')
else:
    print('Имя файла введено корректно')

#б)
date = input('Введите дату рождения (дд.мм.гггг): ')
try:
    datetime.datetime.strptime(date, "%d.%m.%Y")
    print('Дата введена корректно')
except ValueError:
    raise Exception('Неверный формат даты')

#в)
xy = input('Введите координаты (x y): ').split()
if len(xy) != 2:
    raise Exception('Некорректные координаты')
try:
    x, y = float(xy[0]), float(xy[1])
    print('Координаты введены корректно')
except ValueError:
    raise Exception('Некорректные координаты')
