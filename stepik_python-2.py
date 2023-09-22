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

def iosif_funk():
    


if __name__ == '__main__':
    value = int(input())
    print(int_format())
