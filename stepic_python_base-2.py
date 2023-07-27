objects = [1, 2, 1, 2, 3, 7, 1, 7, 4, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным
ans = 0
size = len(objects)
objects = sorted(objects)
for i in range(1, size + 1):
    for j in range(i, size + 1):
        if int(objects[j - 1]) == j:
            ans += 1

'''
objects = [1, 2, 1, 2, 3, 7, 1, 7, 4, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным
ans = 0
size = len(objects) + 1
objects = sorted(objects)
for i in range(1, size):
    for j in range(i+1, size):
        if int(objects[i-1]) % size != j:
            ans += 1
'''


print(size, objects, ans)

'''
objects[:] = list(dict.fromkeys(objects))   #С использованием словарей все работает
print(len(objects))
'''
