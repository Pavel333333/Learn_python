# Напишите программу для подсчета среднего числа всех введенных пользователем чисел.
# Ввод пользователя должен осуществляться с помощью input.
# Если пользователь вводит ноль, то выводится на экран среднее значение.
# Используйте цикл while для решения данной задачи.

# average_from_input = 0
# a = ''
# lst_for_average = []
#
# while a != '0':
#     a = input('Введите число ')
#     if a != '0':
#         lst_for_average.append(int(a))
#
# print(sum(lst_for_average) / len(lst_for_average))
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Напишите программу для вывода на экран чисел от 0 до 100
# Вам понадобится цикл for, конструкция range и print.


def print_digits_1_100():
    for i in range(101):
        print(i)

# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Напишите программу для вывода таблицы умножения от 0 до 9.
# Используйте вложенный цикл for, print и range
# Пример:
# 0*1 = 0
# 0 *2 = 0
# ……
# 9*1 = 9
# 9*2 = 18.


def multiplication_table():
    for i in range(10):
        for j in range(1, 10):
            print(f'{i} * {j} = {i * j}')
#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# Сделайте то же самое со словарём и выведите ключ и значение.


def print_lst_dict():
    lst_for_circle = [1, '2', (3, 4, 5), [6, '7', 'восемь'], {9: 'девять', 10: 'десять'}]
    dict_for_circle = {'имя': 'Иван', 'отчество': 'Петрович', 'фамилия': 'Кузнецов'}

    for elem in lst_for_circle:
        print(elem)

    for key, value in dict_for_circle.items():
        print(key, value)
#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Вывести все числа от 1 до 100, которые делятся на 3 без остатка.


def print_1_100_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)
#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Найти сумму всех чисел от 1 до 100.


def summ_digits_1_100():
    summ = 0

    for i in range(1, 101):
        summ += i
    print(summ)

#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Вывести таблицу умножения для числа 2 от 1 до 10.


def multiplication_table_2():
    for i in range(1, 10):
        print(f'2 * {i} = {2 * i}')
#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Найти все простые числа от 2 до 50.


def simple_numbers():
    count = 0

    for i in range(2, 51):
        for j in range(1, (i // 2) + 1):
            if i % j == 0:
                count += 1
                if count == 2:
                    break
        if count == 1:
            print(i)
        count = 0

#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Посчитать сумму квадратов чисел от 1 до 10.


def sum_of_squares_of_numbers():
    summ_of_number_square = 0

    for i in range(1, 11):
        summ_of_number_square += i ** 2

    print(summ_of_number_square)

#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.


def print_yx2():
    start = 1
    stop = 10
    step = 0.5

    while start <= stop:
        print(start ** 2)
        start += step

#
# print()
# print('---------------------------------------------------------')
# input('Нажмите любую клавишу для продолжения')

# Найти факториалы чисел от 1 до 5 (включительно).


def factorials():
    f = 1

    for i in range(1, 6):
        for j in range(1, i+1):
            f *= j
        print(f)
        f = 1

factorials()



