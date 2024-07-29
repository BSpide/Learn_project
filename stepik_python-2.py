"""
Уроки второй части курса "Поколение Python"
"""


def retry_learn_1():
    #   Просто выводим в столбик набор вычислений
    from math import sqrt
    a, b = int(input()), int(input())
    return print(
        a + b,
        a - b,
        a * b,
        a / b,
        a // b,
        a % b,
        sqrt(a ** 10 + b ** 10),
        sep="\n"
    )


def imt_humen():
    #   Расчет индекса массы тела человека
    weight, height = float(input()), float(input())
    imt = weight / height ** 2
    if imt < 18.5:
        return print("Недостаточная масса")
    elif imt > 25:
        return print("Избыточная масса")
    else:
        return print("Оптимальная масса")


def line_cost():
    #   Вычисление стоимости строки при условии цены 60 коп. за символ
    string = len(input())
    price = 0.60
    summa = float(price * string)
    """
    Для вывода используем форматированные строки\
    {int(summa)} - просто преобразуем в int отсекая знаки после запятой
    {(summa % 1) * 100:.0f} - остаток от деления на 1 - дробная часть числа,
    далее умнажаем на 100 т.к. нам нужно два знака вынести в целое
    одновременно в умножением делаем округление и обрезаем дробную часть (:.0f)
    """
    return print(f'{int(summa)} р. {(summa % 1) * 100:.0f} коп.')


def spice_words():
    #   считаем слова в строке
    #   проверяем, что в строке есть не только пробелы
    #   удаляем пробелы в начале и в конце строки
    #   считаем ко-во пробелов +1
    string = input()
    if string.isspace() == True:
        return print("В этой строке нет слов")
    else:
        string = string.split(" ")
        return print(len(list(filter(None, string))))


def spice_words_1():
    print(len(input().split()))


def china_goroskop():
    #   Определить какой год по гороскопу
    goroskop = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр',
                'Заяц']
    return print(goroskop[int(input()) % 12 - 8])


def num_revers():
    #   Проверяем сколько цифр всего
    #   Есле 5, то реверс
    #   Если больше то реверс 5 с конца
    num = input()
    if len(num) == 5:
        return print(int(num[::-1]))
    elif len(num) == 6:
        result = num[0] + num[5:0:-1]
        return print(result)
    else:
        return print('Формат не соответсвует условиям')


def standart_ac():
    #   вставляем запятые для больших чисел
    num = input()
    x = []
    counter = 0
    if len(num) <= 3:
        return print(num)
    else:
        num = num[::-1]
        for i in range(len(num)):
            x.append(num[i])
            counter += 1
            if counter == 3 and (i + 1) != len(num):
                x.append(',')
                counter = 0
        print(*x[::-1], sep='')


def bin_format(value: int) -> str:
    return f"{value:b}"

def win_number():
    wn = bin_format(value)
    val = f"0b{wn[1:]}{wn[:1]}"
    return val

def int_format():
    return eval(win_number())

def yesorno():
    '''Напишите программу для определения, является ли число произведением двух чисел из данного набора.
    Программа должна выводить результат в виде ответа «ДА» или «НЕТ».'''
    num = int(input())
    x = []
    y = []
    while num != 0:
        x.append(int(input()))
        num -= 1
    op = int(input())
    num = len(x)
    #for i in range(num):
    #    print(op / x[i])
    for m in range(num):
        for n in range(m):
            y.append(x[m] * x[n])
#           print((f'Произведение  {x[m]} на {x[n]} равно {x[m] * x[n]}'))
    if op in y:
        print('ДА')
    else:
        print('НЕТ')
    #print(num, x, op)
    #print(y)

def game():
    '''Игра камень-ножницы-бумага'''
    timur = input()
    ruslan = input()
    if timur == ruslan:
        return print('ничья')
    elif (timur == 'камень' and ruslan == 'ножницы') or (timur == 'ножницы' and ruslan == 'бумага') or (timur == 'бумага' and ruslan == 'камень'):
        return print('Тимур')
    else:
        return print('Руслан')

def game_lvl_2():
    '''Игра камень-ножницы-бумага-ящерица-Спок, усложненная версия'''
    #Словарь с вариантами исходов и результатос. Варианты работают как индекс, результат - значение по индексу
    variant = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан', 'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья', 'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур', 'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур', 'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан', 'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан', 'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья', 'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур', 'Спок-ящерица': 'Руслан'}
    timur = input()
    ruslan = input()
    start = timur + "-" + ruslan #собираем конструкцию вида "камень-ножницы", эта конструкция является индексом для словаря
    return print(variant[start]) #Выводим результат из словаря, где variant - словарь, start - индекс полученный конконтенацией варианта Тимура и Руслана

'''Поиск максимального значения во вложенных списках
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
num = len(list1)
list3 = []
for i in range(num):
    list3.append(max(list1[i]))
maximum = max(list3)
print(maximum)
'''

'''реверс значений вложенных списков
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
x = len(list1)
for i in range(x):
    list1[i].reverse()

print(list1)
'''

''' 4.2 Вложенные списки. Часть 1. Считаем среднее значение списка
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
x = len(list1)
for i in range(x):
    y = len(list1[i])
    for r in range(y):
        counter += 1
        total = total + list1[i][r]
print(total/counter)
'''

r = int(input())
print(*[[x+1 for x in range(r)] for _ in range(r)], sep = '\n')
