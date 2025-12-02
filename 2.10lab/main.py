if __name__ == "__main__":
    pass

#а) Имя файла
name = input('Введите имя файла: ')
bad_symb = '\\/*?:"<>|'
if any(symb in name for symb in bad_symb):
    print('Недопустимое имя файла')
else:
    print('Имя файла введено корректно')

#б) Дата рождения
date = input('Введите дату рождения (дд.мм.гггг): ')
a = date.split('.')
if len(a) == 3 and len(a[0]) == 2 and len(a[1]) == 2 and len(a[2]) == 4:
    print('Дата введена корректно')
else:
    print('Неверный формат даты')

# в) Координаты
xy = input('Введите координаты (x y): ').split()

if len(xy) != 2:
    print('Некорректные координаты')
else:
    x, y = xy
    if (x.replace('-', '').replace('.', '').isdigit() and 
        y.replace('-', '').replace('.', '').isdigit() and
        x.count('-') <= 1 and y.count('-') <= 1 and
        x.count('.') <= 1 and y.count('.') <= 1 and
        (x[0] == '-' if '-' in x else True) and
        (y[0] == '-' if '-' in y else True)):
        print('Координаты введены корректно')
    else:
        print('Некорректные координаты')
