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

#a = 1
#b = 2
#counter = 0
#for i in range(a, b + 1):
#    counter = 0
#    for j in range(1, i + 1):
#        if i % j == 0:
#            counter += 1
#    if counter == 2:
#        print(i)


#Числа Рамануджана
#for a in range(1, 33):
#    for b in range(1, 33):
#        for c in range(1, 33):
#            for d in range(1, 33):
#                if a != b and a != c and a != d and b != c and b != d and c != d:
#                    if (a ** 3 + b ** 3) == (c ** 3 + d ** 3):
#                        print((a ** 3 + b ** 3), (c ** 3 + d ** 3))

#s = 'abcABCD12345'
#counter = 0
#for i in range(0, len(s)):
#    if "a" <= s[i] <= "z":     #Кто бы знал, что так можно
#        counter += 1
#print(counter)

#s = 'АааГГЦЦцТТттт'
#s = s.lower()
#print(f'Аденин: {s.count("а")}\nГуанин: {s.count("г")}\nЦитозин: {s.count("ц")}\nТимин: {s.count("т")}')


#s = 'fvdfv45424g'
#counter = 0
#for i in range (0, 9):
#    if s.count(i) > 0:

#languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
#print(languages[::-1])

#numbers1 = [1, 2, 3]
#umbers2 = [6]
#numbers3 = [7, 8, 9, 10, 11, 12, 13]
#print(numbers1 + numbers1 + (numbers2 * 8) + numbers3)

#numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#print(len(numbers))
#print(numbers[-1])
#print(numbers[::-1])
#if 2 and 17 in numbers:
#    print('YES')
#else:
#    print('NO')
#del numbers[0]
#del numbers[-1]
#print(numbers)

#Заморочиться и вспомнить перебор по алфавиту без UNICOD
#alphabit = []
#counter = 0
#for i in range(97, 123):
#    counter += 1
#    alphabit.append(chr(i) * counter)
#print(alphabit)

#snum = []
#x = int(input())
#for i in range(x):
#    num = int(input())
#    snum.append(pow(num, 3))
#print(snum)

#alg = []
#x = int(input())
#for i in range(1, x + 1):
#    if x % i == 0:
#        alg.append(i)
#print(alg)

