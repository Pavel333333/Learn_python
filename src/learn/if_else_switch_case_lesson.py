# if-else

# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

while True:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))

    count_positive = 0

    if first_number > 0:
        count_positive += 1

    if second_number > 0:
        count_positive += 1

    if third_number > 0:
        count_positive += 1

    print(f'положительных чисел в исходном наборе {count_positive}')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Даны два числа. Вывести большее из них.

while True:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))

    if first_number > second_number:
        print(f'число {first_number} больше числа {second_number}')
    elif first_number < second_number:
        print(f'число {first_number} меньше числа {second_number}')
    else:
        print(f'число {first_number} равно числу {second_number}')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Даны два числа. Вывести вначале большее, а затем меньшее из них.

while True:

    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))

    if first_number > second_number:
        print(first_number)
        print(second_number)
    elif first_number < second_number:
        print(second_number)
        print(first_number)

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Даны три числа. Найти наименьшее из них.

while True:

    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))

    if first_number < second_number and first_number < third_number:
        print(f'число {first_number} наименьшее.')
    elif second_number < first_number and second_number < third_number:
        print(f'число {second_number} наименьшее.')
    elif third_number < first_number and third_number < second_number:
        print(f'число {third_number} наименьшее.')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.
# Координаты задаются пользователем, например (10, 15).

while True:
    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))

    if x > 0 and y > 0:
        print('Точка находится в первой четверти')
    elif x < 0 < y:
        print('Точка находится во второй четверти')
    elif x < 0 and y < 0:
        print('Точка находится в третьей четверти')
    elif y < 0 < x:
        print('Точка находится в четвёртой четверти')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# switch-case

# Дано целое число K. Вывести строку-описание оценки, соответствующей числу K (1 — «плохо», 2 — «неудовлетворительно»,
# 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

while True:
    k = int(input('Введите число k: '))

    if k < 1 or k > 5:
        print('ошибка')

    match k:
        case 1:
            print('плохо')
        case 2:
            print('неудовлетворительно')
        case 3:
            print('удовлетворительно')
        case 4:
            print('хорошо')
        case 5:
            print('отлично')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.

while True:
    month = int(input('Введите порядковый номер месяца: '))

    match month:
        case 1:
            print('в январе 31 день')
        case 2:
            print('в феврале 28 дней')
        case 3:
            print('в марте 31 день')
        case 4:
            print('в апреле 30 дней')
        case 5:
            print('в мае 31 день')
        case 6:
            print('в июне 30 дней')
        case 7:
            print('в июле 31 день')
        case 8:
            print('в августе 31 день')
        case 9:
            print('в сентябре 30 дней')
        case 10:
            print('в октябре 31 день')
        case 11:
            print('в ноябре 30 дней')
        case 12:
            print('в декабре 31 день')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года.
# Вывести значения D и M для даты, следующей за указанной.

while True:
    day = int(input('Введите день: '))
    month = int(input('Введите порядковый номер месяца: '))

    match month:
        case 1:
            if 0 < day < 31:
                print(f'следующий день {day + 1} января')
            elif day == 31:
                print(f'следующий день {1} февраля')
            else:
                print('исчисление дней в январе от 1 до 31')
        case 2:
            if 0 < day < 28:
                print(f'следующий день {day + 1} февраля')
            elif day == 28:
                print(f'следующий день {1} марта')
            else:
                print('исчисление дней в феврале от 1 до 28')
        case 3:
            if 0 < day < 31:
                print(f'следующий день {day + 1} марта')
            elif day == 31:
                print(f'следующий день {1} апреля')
            else:
                print('исчисление дней в марте от 1 до 31')
        case 4:
            if 0 < day < 30:
                print(f'следующий день {day + 1} апреля')
            elif day == 30:
                print(f'следующий день {1} мая')
            else:
                print('исчисление дней в апреле от 1 до 30')
        case 5:
            if 0 < day < 31:
                print(f'следующий день {day + 1} мая')
            elif day == 31:
                print(f'следующий день {1} июня')
            else:
                print('исчисление дней в мае от 1 до 31')
        case 6:
            if 0 < day < 30:
                print(f'следующий день {day + 1} июня')
            elif day == 30:
                print(f'следующий день {1} июля')
            else:
                print('исчисление дней в июне от 1 до 30')
        case 7:
            if 0 < day < 31:
                print(f'следующий день {day + 1} июля')
            elif day == 31:
                print(f'следующий день {1} августа')
            else:
                print('исчисление дней в июле от 1 до 31')
        case 8:
            if 0 < day < 31:
                print(f'следующий день {day + 1} августа')
            elif day == 31:
                print(f'следующий день {1} сентября')
            else:
                print('исчисление дней в августе от 1 до 31')
        case 9:
            if 0 < day < 30:
                print(f'следующий день {day + 1} сентября')
            elif day == 30:
                print(f'следующий день {1} октября')
            else:
                print('исчисление дней в сентябре от 1 до 30')
        case 10:
            if 0 < day < 31:
                print(f'следующий день {day + 1} октября')
            elif day == 31:
                print(f'следующий день {1} ноября')
            else:
                print('исчисление дней в октябре от 1 до 31')
        case 11:
            if 0 < day < 30:
                print(f'следующий день {day + 1} ноября')
            elif day == 30:
                print(f'следующий день {1} декабря')
            else:
                print('исчисление дней в ноябре от 1 до 30')
        case 12:
            if 0 < day < 31:
                print(f'следующий день {day + 1} декабря')
            elif day == 31:
                print(f'следующий день {1} января')
            else:
                print('исчисление дней в декабре от 1 до 31')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток) и
# принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.

while True:
    c = input('Введите исходное направление робота: ')
    n = input('Введите команду роботу: ')

    match (c, n):
        case ('С', '0'):
            print('Робот смотрит на север')
        case ('С', '1'):
            print('Робот смотрит на запад')
        case ('С', '-1'):
            print('Робот смотрит на восток')
        case ('З', '0'):
            print('Робот смотрит на запад')
        case ('З', '1'):
            print('Робот смотрит на юг')
        case ('З', '-1'):
            print('Робот смотрит на север')
        case ('Ю', '0'):
            print('Робот смотрит на юг')
        case ('Ю', '1'):
            print('Робот смотрит на восток')
        case ('Ю', '-1'):
            print('Робот смотрит на запад')
        case ('В', '0'):
            print('Робот смотрит на восток')
        case ('В', '1'):
            print('Робот смотрит на север')
        case ('В', '-1'):
            print('Робот смотрит на юг')

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа, например:
# 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».

while True:
    a = int(input('Введите число в диапазоне 100–999: '))

    hundreds = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
    }

    tens = {
        0: "",
        1: "десять",
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
    }

    eleven = {
        1: "одиннадцать",
        2: "двенадцать",
        3: "тринадцать",
        4: "четырнадцать",
        5: "пятнадцать",
        6: "шестнадцать",
        7: "семнадцать",
        8: "восемнадцать",
        9: "девятнадцать",
    }

    ones = {
        0: "",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
    }

    h = a // 100
    t = (a // 10) % 10
    o = a % 10

    result = []

    match hundreds:
        case _:
            result.append(hundreds[h])
    if t == 1 and o != 0:
        match eleven:
            case _:
                result.append(eleven[o])
    elif t == 0:
        if o == 0:
            pass
        else:
            match ones:
                case _:
                    result.append(ones[o])
    else:
        match tens:
            case _:
                result.append(tens[t])
        match ones:
            case _:
                result.append(ones[o])

    print(*result)

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break

print()
print('---------------------------------------------------------')
input('Нажмите любую клавишу для продолжения')

# *** Реализуйте программу калькулятор. На вход подаётся три значения: первое число, второе число и
# операция (*, /, + или -). На выходе должны получить число, после выполнения операции.

while True:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    sign = input('Введите знак матоперации: ')

    match sign:
        case '*':
            print(first_number * second_number)
        case '/':
            try:
                print(first_number / second_number)
            except ZeroDivisionError:
                print('Делить на ноль не стОит даже пытаться.')
        case '+':
            print(first_number + second_number)
        case '-':
            print(first_number - second_number)

    question = input('Продолжаем? да/нет: ')
    if question.lower() == 'нет':
        break