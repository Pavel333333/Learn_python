from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler
from random import randint

logger = getLogger()
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
file_handler = FileHandler("data.log")
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])

logger.info('калькулятор квадратного уравнения запущен')


def check_value_by_zero(value: int):
    logger.debug("value is %s", value)
    if value == 0:
        raise ValueError('a не должно равняться нулю, так как уравнение перестаёт быть квадратичным')


def check_value_is_number(value: str):
    logger.debug("value is %s", value)
    if value == '':
        raise ValueError('Вы ничего не ввели. Здесь должны быть только цифры.')
    try:
        float(value)
        return value
    except ValueError:
        raise ValueError('Вы ввели не число. Повторите ввод.')


print('Вашему вниманию калькулятор расчёта квадратного уравнения.')
print('Оно имеет вид ax^2 + bx + c = 0, где a, b, c это параметры, а x нужно вычислить.')
print('Введите параметры уравнения, где a не равно 0, и калькулятор найдёт корни уравнения, если они есть.')


def quadratic_equation():
    a = input('Введите значение не равное нулю\na: ')
    logger.debug("a is %s", a)

    while True:
        try:
            a = check_value_is_number(a)
            logger.debug("a is %s", a)
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            a = input('Если хотите закрыть калькулятор, введите "exit" или введите a: ')
            if a == 'exit':
                return print('Калькулятор завершил свою работу')

    while int(a) == 0:
        try:
            check_value_by_zero(int(a))
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            a = input('Введите значение не равное нулю. Введите a: ')
            while a != 'exit':
                try:
                    a = check_value_is_number(a)
                    logger.debug("a is %s", a)
                    break
                except ValueError as e:
                    logger.error("exception is %s", ValueError)
                    print(e)
                    a = input('Если хотите закрыть калькулятор, введите "exit" или введите a: ')
                    if a == 'exit':
                        return print('Калькулятор завершил свою работу')

    a = int(a)

    b = input('Введите b: ')
    logger.debug("b is %s", b)

    while True:
        try:
            b = check_value_is_number(b)
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            b = input('Если хотите закрыть калькулятор, введите "exit" или введите b: ')
            if b == 'exit':
                return print('Калькулятор завершил свою работу')

    b = int(b)

    c = input('Введите c: ')
    logger.debug("c is %s", c)

    while True:
        try:
            c = check_value_is_number(c)
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            c = input('Если хотите закрыть калькулятор, введите "exit" или введите c: ')
            if c == 'exit':
                return print('Калькулятор завершил свою работу')

    c = int(c)

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

    d1 = input('Введите левую границу диапазона, d1: ')
    logger.debug("d1 is %s", d1)

    while True:
        try:
            d1 = check_value_is_number(d1)
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            d1 = input('Если хотите закрыть калькулятор, введите "exit" или введите d1: ')
            if d1 == 'exit':
                return print('Функция поиска случайного числа в диапазоне завершила свою работу')

    d2 = input('Введите левую границу диапазона, d2: ')
    logger.debug("d2 is %s", d2)

    while True:
        try:
            d2 = check_value_is_number(d2)
            break
        except ValueError as e:
            logger.error("exception is %s", ValueError)
            print(e)
            d2 = input('Если хотите закрыть калькулятор, введите "exit" или введите d2: ')
            if d2 == 'exit':
                return print('Функция поиска случайного числа в диапазоне завершила свою работу')

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
            check_value_is_number(lst[i])
            logger.debug("lst[i] is %s", lst[i])
            logger.debug("i is %s", i)
            lst[i] = int(lst[i])
            continue
        except ValueError:
            print(f'{i+1} по счёту элемент списка Вы ввели не число, либо введите "продолжить" и повторите ввод списка чисел заново, ')
            stop = input('либо введите "стоп" для выхода из программы: ')
            if stop == 'стоп':
                return print('Вы остановили вычисление среднего арифметического из списка чисел.')
            else:
                arithmetic_mean()

    result = sum(lst) / len(lst)
    print(result)


arithmetic_mean()
logger.info('завершили вычисление среднего арифметического из списка чисел')