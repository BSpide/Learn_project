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
            sep = "\n"
            )

def imt_humen():
    #   Расчет индекса массы тела человека
    weight, height = float(input( )), float(input())
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

