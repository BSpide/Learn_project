'''
    программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
    Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
    'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна
    вывести сообщение 'Слишком мало, попробуйте еще раз'.
    Если пользователь угадывает число, то программа должна поздравить его и
    вывести сообщение 'Вы угадали, поздравляем!'.
'''
a = 1
b = 100
def gen_num(a, b):
    import random
    global num
    num = random.randint(a, b)

def user_quastion(user_num):
    global u_num
    u_num = user_num
    if user_num == '':
        print('Поиграем? угадай число:')
        user_num = int(input())
    elif user_num != '':
        comparison_num(num, u_num)

def comparison_num(num, u_num):
    while num != u_num:
        if num < u_num:
            print('Слишком много, попробуйте еще раз')
            u_num = int(input())
        elif num > u_num:
            print('Слишком мало, попробуйте еще раз')
            u_num = int(input())
    return print('Вы угадали, поздравляем!')

def is_valid(u_num):
    if u_num.isdigit() == True:


print('Попробуй угадать число в диапазоне от 1 до 100, сгенерированное случайным образом. Введите число: ')
gen_num(a, b)
user_quastion(int(input()))