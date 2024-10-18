from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler
from random import randint

logger = getLogger()
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
file_handler = FileHandler("data.log", mode="w")
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])

logger.info('калькулятор квадратного уравнения запущен')


def check_value_by_zero(value: str, value_name: str, func_name: str):
    while True:
        print(f'Если захотите закрыть калькулятор, введите "стоп"')
        value = input(f'или введите значение не равное нулю\n{value_name}: ')
        logger.debug(f'в функцию check_value_is_number поданы значения {value} и {value_name}')

        if value == '':
            print('Вы ничего не ввели. Здесь должны быть только цифры. Повторите ввод')
            continue
        elif value == 'стоп':
            print(f'{func_name} завершает свою работу')
            return 'стоп'
        try:
            float(value)
        except Exception:
            print('Вы ввели не число. Повторите ввод')
            continue
        else:
            if float(value) == 0:
                print('Вы ввели 0. При нуле функция перестаёт быть квадратичной. Повторите ввод')
                continue
            else:
                return value


def check_value_is_number(value: str, value_name: str, func_name: str):
    while True:
        print(f'Если захотите закрыть калькулятор, введите "стоп"')
        value = input(f'или введите значение не равное нулю\n{value_name}: ')
        logger.debug(f'в функцию check_value_is_number поданы значения {value} и {value_name}')

        if value == '':
            print('Вы ничего не ввели. Здесь должны быть только цифры. Повторите ввод')
            continue
        elif value == 'стоп':
            print(f'{func_name} завершает свою работу')
            return 'стоп'
        try:
            float(value)
            return value
        except Exception:
            print('Вы ввели не число. Повторите ввод')
            continue


print('Вашему вниманию калькулятор расчёта квадратного уравнения.')
print('Оно имеет вид ax^2 + bx + c = 0, где a, b, c это параметры, а x нужно вычислить.')
print('Введите параметры уравнения, где a не равно 0, и калькулятор найдёт корни уравнения, если они есть.')


def quadratic_equation():

    a = ''
    a = check_value_by_zero(a, 'a', 'Калькулятор среднего арифметического')

    if a == 'стоп':
        return

    a = int(a)

    b = ''
    b = check_value_is_number(b, 'b', 'Калькулятор среднего арифметического')
    b = int(b)

    if b == 'стоп':
        return

    c = ''
    c = check_value_is_number(c, 'c', 'Калькулятор среднего арифметического')
    c = int(c)

    if c == 'стоп':
        return

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f'С данными параметрами уравнение имеет два корня, а именно x1 = {x1}, x2 = {x2}')
    elif d == 0:
        x = -b / (2 * a)
        print(f'С данными параметрами уравнение имеет один корень, а именно x = {x}')
    else:
        print('С данными параметрами a, b и c уравнение не имеет корней. Попробуйте с другими значениями.')
        quadratic_equation()


quadratic_equation()


logger.info('калькулятор квадратного уравнения остановлен')
print()
print('----------------------------------------------------------------')
print()
logger.info('запускаем функцию определения случайного числа в диапазоне')

print('Далее Вашему вниманию генератор случайного числа в заданном Вами диапазоне чисел.')
print('Введите два числа, внутри которых нужно сгенерировать случайное число.')


def random_number_from_range():

    d1 = ''
    d1 = check_value_is_number(d1, 'd1', 'Функция поиска случайного числа в диапазоне')
    d1 = int(d1)

    if d1 == 'стоп':
        return

    d2 = ''
    d2 = check_value_is_number(d2, 'd2', 'Функция поиска случайного числа в диапазоне')
    d2 = int(d2)

    if d2 == 'стоп':
        return

    result = 0

    try:
        result = randint(int(d1), int(d2))
        logger.debug("result is %s", result)
    except Exception as e:
        logger.error("exception is %s", Exception)
        print(e)
        res = input('Если хотите закрыть калькулятор, введите "exit" или "продолжить": ')
        if res == 'exit':
            return print('Функция поиска случайного числа в диапазоне завершила свою работу')
        elif res == 'продолжить':
            random_number_from_range()
    else:
        print(f'Случайное число в диапазоне от {d1} до {d2} равно {result}')


random_number_from_range()
logger.info('завершили вычисление случайного числа в диапазоне')
print()
print('----------------------------------------------------------------')
print()
logger.info('запускаем вычисление среднего арифметического из списка чисел')

print('Переходим к вычислению среднего арифметического из списка чисел.')
print('Введите список чисел более одного, из которых будем вычислять среднее арифметическое.')


def arithmetic_mean():

    s = input('Введите (через пробел) список чисел, из которых хотите посчитать среднее арифметическое: ')
    logger.debug("s is %s", s)
    lst = s.split()
    logger.debug("lst is %s", lst)

    for i in range(len(lst)):
        try:
            check_value_is_number(lst[i], lst[i], 'Функция вычисления среднего арифметического из списка чисел')
            logger.debug("lst[i] is %s", lst[i])
            logger.debug("i is %s", i)
            lst[i] = int(lst[i])
            continue
        except ValueError:
            print(f'{i+1} по счёту элемент списка не число, введите "продолжить" и повторите ввод списка чисел, ')
            stop = input('либо введите "стоп" для выхода из программы: ')
            if stop == 'стоп':
                return print('Вы остановили вычисление среднего арифметического из списка чисел.')
            else:
                arithmetic_mean()

    result = sum(lst) / len(lst)
    print(result)


arithmetic_mean()
logger.info('завершили вычисление среднего арифметического из списка чисел')