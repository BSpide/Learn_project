#Некоторые упражнения из курса "Поколение Python": курс для начинающих
#Заодно и учимся использовать git

'''
a, b = 10, 20
max_x = 0
max_j = 0
for i in range(a, b + 1):
    x = 0
    print(i)
    for j in range(1, b + 1, 1):
        if (i % j) == 0:
            x = j + x
            if max_x <= x and max_j < j:
                max_x = x
                max_j = j
print(max_j, max_x)
'''

'''
n = 734573659783465783465978346593487
x = 0
while n != 0:
    n_1 = n % 10
    n = n // 10
    x = n_1 + x
if x > 9:
    while x > 9:
        x = x - 9
    print(x)
else:
    print(x)
'''

'''
n = 1
factorial = 1
summa = 0
for i in range(1, n + 1):
    factorial *= i
    summa += factorial
print(summa)
'''

'''
a = 1
b = 2
counter = 0
for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
'''

'''
#Числа Рамануджана
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    if (a ** 3 + b ** 3) == (c ** 3 + d ** 3):
                        print((a ** 3 + b ** 3), (c ** 3 + d ** 3))
'''

'''
s = 'abcABCD12345'
counter = 0
for i in range(0, len(s)):
    if "a" <= s[i] <= "z":     #Кто бы знал, что так можно
        counter += 1
print(counter)
'''

'''
s = 'АааГГЦЦцТТттт'
s = s.lower()
print(f'Аденин: {s.count("а")}\nГуанин: {s.count("г")}\nЦитозин: {s.count("ц")}\nТимин: {s.count("т")}')
'''

'''
# Считаем количество вхождений букв из строки
s = 'АааГГЦЦцТТттт'
s = s.lower()
print(f'Аденин: {s.count("а")}\nГуанин: {s.count("г")}\nЦитозин: {s.count("ц")}\nТимин: {s.count("т")}')
'''

'''
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])
'''

'''
numbers1 = [1, 2, 3]
umbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1 + numbers1 + (numbers2 * 8) + numbers3)
'''

'''
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 2 and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)
'''

'''
snum = []
x = int(input())
for i in range(x):
    num = int(input())
    snum.append(pow(num, 3))
print(snum)
'''

'''
# Заморочиться и вспомнить перебор по алфавиту без UNICOD
alphabit = []
counter = 0
for i in range(97, 123):
    counter += 1
    alphabit.append(chr(i) * counter)
print(alphabit)
'''

'''
alg = []
x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        alg.append(i)
print(alg)
'''

'''
# задание на "молодежный сленг" (прибавляем к словам ки и переставляем буквы)
s = 'проспал почти всю ночь'
print(*[i[1:] + i[0] + 'ки' for i in input().split()])
'''

'''
Начались уроки по работе с функциями, далее все делаем через них
'''

# Рисуем равнобедренный триугольник из символов
def draw_triangle(fill, base):
    x = base // 2 + 1
    y = base // 2
    for m in range(base // 2):
        for n in range(m + 1):
            print(fill, end = '')
        print('')
    for i in range(base):
        for j in range(i, x):
            print(fill, end = '')
        print('')
'''
# Пример использования функции draw_triangle
fill = "*"
base = int(7)
draw_triangle(fill, base)
'''

# Пример использования функции внутри функции
def get_factors(num):
    s = []
    for i in range(1, int(num) + 1):
        if num % i == 0:
            s.append(i)
    return s

def number_of_factors(num):
    return len(get_factors(num))

# Поиск символа в строке
def find_all(target, symbol):
    num = len(target)
    while num > 0:
        num -= 1
        return target.find(symbol)
    
# Решение с помощью цикла и условий
def find_all_2(target, symbol):
    x = []
    for i in range(len(target)):
        if target[i] == symbol:
            x.append(i)
    return x

#То же самое но с помощью списочных выражений
def find_all_str(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

# Сортировка двух списков
def merge(list1, list2):
    return sorted(list1 + list2)

'''
# пример использования функции merge
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))
'''

#Слияние двух отсортированных списков
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

'''
# Использование функции quick_merge 
# На вход программе подается натуральное число n, а затем n строк,
# содержащих целые числа в порядке возрастания, выводим все строки в одной отсортированной по возрастанию
num = int(input())
list3 =[]
if num < 2:
    print('Для сортировки нужно больше одного списка')
elif num == 2:
    print(quick_merge(input().split(), input().split()))
elif num > 2:
    for i in range(1, num + 1):
        list1 = [int(q) for q in input().split()]   #Непонятная конструкция, надо разобрать че происходит до инпута-_-
        list2 = list3
        list3 = quick_merge(list1, list2)
    print(list3)
'''

# Проверяем строку на палиндорм (убираем все кроме букв)
def is_palindrome(text):
    text = text.lower()
    text_2 = []
    for i in range(len(text)):
        if text[i].isalpha() == True:
            text_2.append(text[i])
    text_3 = text_2
    if text_2 == text_3[::-1]:
        return True
    else:
        return False

# Еще одно задание на валидность пароля по условиям задания №7
# Используем ранее подготовленную функцию для проверки является ли число простым
def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
            if counter > 2:
                return False
    if counter == 2:
        return True
    else:
        return False

# Поиск следующего простого числа
def get_next_prime(num):
    num_2 = num + 1
    while is_prime(num_2) == False:
        num_2 += 1
    return num_2

# Проверка надежности пароля ))
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    elif password.isalpha() == True:
        return False
    elif password.isdigit() == True:
        return False
    elif password.islower() == True:
        return False
    elif password.isupper() == True:
        return False
    elif password.islower() == password.isupper() and password.isalnum() == False:
        return False
    else:
        return True
 
def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False
    elif password[0] != password[0][::-1]:
        return False
    elif is_prime(int(password[1])) == False:
        return False
    elif (int(password[2]) % 2) != 0:
        return False
    else:
        return True
    
# Сравниваем слова и выдает True если они отличаются только одним символом
def is_one_away(word1, word2):
    if word1 == word2 or len(word1) != len(word2):
        return False
    counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

# Функция преобразования верблюжьего в змеиный регистр (из строки IsPrimeNumber получчается is_prime_number)
def convert_to_python_case(text):

    for i in range(1, len(text)):
        if text[i].isupper():
            s = text[:i] + '_' + text[i].lower() + text[i + 1:]
            text = s
    return print(text.lower())

# Функции с возвратом значения
# Середина отрезка
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    return x, y

'''
# Вычисляем середину отрезка
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
'''

# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус
# окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью

def get_circle(radius):
    from math import pi             # Импортируем только pi из модуля math, при этом пишем не math.pi а просто pi
    length = 2 * pi * radius
    square = pi * (radius ** 2)
    return length, square

'''
# вычисляем радиус и площадь круга
r = float(input())
length, square = get_circle(r)
print(length, square)
'''
'''
# Задача 13.6 Корни уравнения
def solve(a, b, c):
    (a * x**2)

# считываем данные
a, b, c = 1, -4, -5

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

'''

# 13.6 Функции с возвратом значения
def solve(a, b, c):
    from math import sqrt
    D = (b ** 2) - (4 * a) * c
    x_1: float = (-b + sqrt(D)) / (2 * a)
    x_2: float = (-b - sqrt(D)) / (2 * a)
    return min(x_1, x_2), max(x_1, x_2)

'''
# Запускаем функцию
a, b, c = 1, -4, -5
x_1, x_2 = solve(a, b, c)
print(x_1, x_2)
'''

# Экзамен на функции

# Рисуем триугольник
def draw_triangle():
    a = 15
    b = 8
    for i in range(b):
        print(' ' * ((a - 1 - i) // 2 ) + ('*' * (1 + i * 2)))
        a -= 1

# Цена доставки первого товара 1000 рэ, остальных 120 рэ, посчитать итого
def get_shipping_cost(quantity):
    shipping_1 = 1000
    shipping_2 = 120
    if quantity == 1:
        return 1000
    elif quantity > 1:
        return 1000 + (quantity - 1) * 120
    else:
        return 'Невозможно расчитать стоимость доставки'

# Вычисляем по формуле из задания
def compute_binom(n, k):
    from math import factorial
    return int(factorial(n)/(factorial(k) * factorial(n - k)))

# перевод цифр в слова
def number_to_words(num):
    list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
               'восемнадцать', 'девятнадцать']
    list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 11:
        return list_1[num - 1]
    elif 10 < num < 20:
        return list_11[num - 11]
    elif 19 < num < 100:
        a = str(num)
        if a[1] == '0':
            return list_21[(num // 10) - 2]
        elif a[1] != '0':
            num_1 = int(a[1])
            x_1 = list_21[(num // 10) - 2]
            x_2 = list_1[num_1 - 1]
            x = x_1 + ' ' + x_2
            return x

# объявление функции
def get_month(language, number):
    month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language != 'ru' and language != 'en' or 0 > number > 12:
        return 'Ошибка ввода'
    elif language == 'ru':
        return month_ru[number - 1]
    elif language == 'en':
        return month_en[number - 1]

'''
хз здесь не пашет, но проверка прошла
    Traceback (most recent call last):
  File "D:\Python_Project\Learn_project\stepik.py", line 460, in <module>
    num = int(input())
ValueError: invalid literal for int() with base 10: ''
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
'''


# Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
# Проверку на корректность ввода не делаем
def is_magic(date):
    dat = date.split('.')
    dd = dat[0]
    mm = dat[1]
    eeee = dat[2]
    ee = eeee[2:]
    if int(dd) * int(mm) == int(ee):
        return True
    else:
        return False
'''
# проверка
date = '03.11.2032'
print(is_magic(date))
'''

# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True если текст является панграммой и False в противном случае.
def is_pangram(text):
    text = text.replace(' ', '').lower()
    print(set(text))
    if len(set(text)) == 26:
        return True
    else:
        return False
'''
# проверка
text = input()
print(is_pangram(text))
'''

# Гипотеза Эйлера о сумме степеней задача 7.8
def eler():
    counter = 1
    for a in range(1, 151):
        for b in range(a, 151):
            for c in range(b, 151):
                for d in range(c, 151):
                    for e in range(d, 151):
                        counter += 1
                        if a**5 + b**5 + c**5 + d**5 == e**5:
                            return print('БИНГО!!! Ответ = ', a+b+c+d+e, ' а=', a, ',b=', b, ',c=', c, ',d=', d, ',e=', e, ' Цикл №', counter, sep='')
                        else:
                            print('Не получилось :( ', 'а=', a, ',b=', b, ',c=', c, ',d=', d, ',e=', e, ' Cумма=', a+b+c+d+e, ' Цикл №', counter, sep='')
# ответ 498

# Задача 15.2 на реализацию подсчета наименьшего количесва попыток для гадывания числа

b = int(input())
def ugadayka_num(b):
    a = 1
    counter = 0
    x = 0
    while x != b:
        x = (a + b) // 2
        if x < b:
            a = x + 1
        elif x > b:
            b = x - 1
        counter += 1
    return print(counter)

ugadayka_num(b)