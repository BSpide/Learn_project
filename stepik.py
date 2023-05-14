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

