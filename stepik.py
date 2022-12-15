#Некоторые упражнения из курса "Поколение Python": курс для начинающих
#Заодно и учимся использовать git

#a, b = 10, 20
#max_x = 0
#max_j = 0
#for i in range(a, b + 1):
#    x = 0
#    print(i)
#    for j in range(1, b + 1, 1):
#        if (i % j) == 0:
#            x = j + x
#            if max_x <= x and max_j < j:
#                max_x = x
#                max_j = j
#print(max_j, max_x)

#n = 734573659783465783465978346593487
#x = 0
#while n != 0:
#    n_1 = n % 10
#    n = n // 10
#    x = n_1 + x
#if x > 9:
#    while x > 9:
#        x = x - 9
#    print(x)
#else:
#    print(x)

#n = 1
#factorial = 1
#summa = 0
#for i in range(1, n + 1):
#    factorial *= i
#    summa += factorial
#print(summa)

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


s = 'fvdfv45424g'
counter = 0
for i in range (0, 9):
    if s.count(i) > 0: