objects = [1, 2, 1, 2, 3, 7, 1, 7, 3, 6] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным
ans = 0
for i in range(len(objects)):
    for obj in objects: # доступная переменная objects
        ans += 1
print(ans)
'''
# работает но не правильный формат решения
ans = 0
i = 1
size = len(objects)
objects = sorted(objects)
for i in range(0, size):
    if (int(objects[i - 1])) is not (int(objects[i])):
        ans += 1

print(size, objects, ans)
'''


'''
objects[:] = list(dict.fromkeys(objects))   #С использованием словарей все работает
print(len(objects))
'''
