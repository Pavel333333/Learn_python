# -*- coding: utf-8 -*-
import unittest
from copy import copy

from src.learn import lesson_oop_car
from unittest.mock import MagicMock, patch
import io


class TestMeansOfTransport(unittest.TestCase):
    def setUp(self):
        self.transport = lesson_oop_car.MeansOfTransport("Toyota", "Red")

    def test_initialization(self):
        self.assertEqual(self.transport.brand, "Toyota")
        self.assertEqual(self.transport.color, "Red")

    def test_set_brand(self):
        self.transport.brand = "Honda"
        self.assertEqual(self.transport.brand, "Honda")

    def test_set_color(self):
        self.transport.color = "Blue"
        self.assertEqual(self.transport.color, "Blue")

    def test_delete_brand(self):
        del self.transport.brand
        with self.assertRaises(AttributeError):
            _ = self.transport.brand

    def test_delete_color(self):
        del self.transport.color
        with self.assertRaises(AttributeError):
            _ = self.transport.color


class TestMoped(unittest.TestCase):
    def setUp(self):
        self.moped = lesson_oop_car.Moped('java', 'red', '2')

    def test_init(self):
        self.assertEqual(self.moped.brand, 'java')
        self.assertEqual(self.moped.color, 'red')
        moped_mock = MagicMock()
        moped_mock._wheels_numbers = 2
        assert moped_mock._wheels_numbers == 2


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = lesson_oop_car.Car('lada', 'white', 4, '5', '5')
        self.car2 = lesson_oop_car.Car('lada', 'black', 5, 5, '5')
        self.car3 = lesson_oop_car.Car('mersedes', 'black', '5', '5', 5)
        self.car4 = lesson_oop_car.Car('uaz', 'black', '5', '5', '5')
        self.car5 = lesson_oop_car.Car('bmw', 'black', '5', '5', '5')
        self.car6 = lesson_oop_car.Car('uaz', 'black', '5', '5', '5')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_new(self, mock_stdout):
        self.car = lesson_oop_car.Car('lada', 'white', '4', '5', '5')
        self.assertEqual(mock_stdout.getvalue().strip(), 'Метод __new__ отработал')

    def test_init(self):
        self.assertIsInstance(self.car, lesson_oop_car.Car)

    def test_wheels_number_set(self):
        self.car.wheels_number = '5'
        self.assertEqual(self.car.wheels_number, '5')

    def test_eq(self):
        self.assertEqual(self.car.brand, self.car2.brand)

    def test_lt(self):
        self.assertEqual(self.car._seat_number, self.car5._seat_number)

    def test_pos(self):
        result = +self.car
        self.assertEqual(result, 4)
        result = +self.car2
        self.assertEqual(result, 'у машины не может быть столько колёс: 5')

    def test_neg(self):
        result = -self.car
        self.assertEqual(result, 'Экземпляр класса Car не может быть отрицательным, так как мы не в Зазеркалье')

    def test_abs(self):
        result = abs(self.car)
        self.assertEqual(result,'у Вас определённо хороший вкус, ведь Lada это absолютно лучшая машина')
        result = abs(self.car3)
        self.assertEqual(result,'можно было бы выбрать машину получше')

    def test_round(self):
        result = round(self.car4)
        self.assertEqual(result, 'Уазик нельзя округлить, он всегда квадратный')
        result = round(self.car)
        self.assertEqual(result, 'нашу любимую lada трогать лучше не надо')
        result = round(self.car3)
        self.assertEqual(result, 'mersedes итак круглый, куда его ещё круглее')

    def test_add(self):
        result = self.car3 + 'f'
        self.assertEqual(result, 'второе слагаемое должно быть целочисленным')
        result = self.car3 + 1
        self.assertEqual(result, 'ejd849j3d. А какой результат ты хотел получить прибавляя число к машине ?!')

    def test_sub(self):
        result = self.car - (3,)
        self.assertEqual(result, 'вычитаемое должно быть целочисленным')
        result = self.car - 3
        self.assertEqual(result, 'а что ты хочешь отнять у машины ? у неё нету ничего ненужного. '
                                 'если только в багажнике посмотреть...')

    def test_or(self):
        result = self.car | 1
        self.assertEqual(result, 'после | поставь объект класса Car. Иначе из чего мне выбирать ?')
        result = self.car | self.car2
        self.assertEqual(result, 'без вариантов, только lada')
        result = self.car4 | self.car3
        self.assertEqual(result, 'без вариантов, только uaz')
        result = self.car3 | self.car5
        self.assertEqual(result, 'не знаю, сам решай, что лучше mersedes или bmw. моё мнение ты знаешь.')

    def test_radd(self):
        result = 'f' + self.car3
        self.assertEqual(result, 'второе слагаемое должно быть целочисленным')
        result = 1 + self.car3
        self.assertEqual(result, 'ejd849j3d. А какой результат ты хотел получить прибавляя число к машине ?!')

    def test_iadd(self):
        self.car3 += 1
        self.assertEqual(self.car3, 'что за мания, прибавлять числа к машине. что я должен посчитать ?')

    def test_int(self):
        result = int(self.car2)
        result1 = self.car2.wheels_number + self.car2._seat_number
        self.assertEqual(result, result1)

    def test_str(self):
        result = str(self.car3)
        self.assertEqual(result, 'mersedes, black, 5, 5, 5')

    def test_hash(self):
        hash_car = hash(self.car)
        hash_car2 = hash(self.car2)
        self.assertNotEqual(hash_car, hash_car2)
        hash_car4 = hash(self.car4)
        hash_car6 = hash(self.car6)
        self.assertEqual(hash_car4, hash_car6)

    def test_bool(self):
        self.assertEqual(bool(self.car), True)
        self.assertEqual(bool(self.car3), False)

    def test_getattr(self):
        self.assertEqual(self.car.weight, 'в этом объекте нет атрибута weight')

    def test_len(self):
        result = len(self.car3)
        self.assertEqual(result, 5)

    def test_getitem(self):
        result = self.car5['3']
        self.assertEqual(result, 'в индекс надобно вводить сугубо целочисленное значение')
        result = self.car5[8]
        self.assertEqual(result, 'в данном объекте меньше атрибутов, чем 8')
        result = self.car5[3]
        self.assertEqual(result, '5')

    def test_setitem(self):
        self.car5[4] = '8'
        self.assertEqual(self.car5._length, '8')

    def test_iter(self):
        self.assertEqual(self.car3, self.car3)

    def test_reversed(self):
        self.assertEqual(reversed(self.car2), ['5', '5', '5', 'black', 'lada'])

    def test_contains(self):
        self.assertEqual('bmw' in self.car5, True)
        self.assertEqual('black' in self.car, False)

    def test_instancecheck(self):
        self.assertEqual(isinstance(self.car2, lesson_oop_car.Car), True)

    def test_subclasscheck(self):
        self.assertEqual(issubclass(lesson_oop_car.Car, lesson_oop_car.MeansOfTransport), True)
        self.assertEqual(issubclass(lesson_oop_car.Car, lesson_oop_car.Moped), False)

    def test_call(self):
        self.assertEqual(self.car4(), 'поздравляем, это хороший выбор!')
        self.assertEqual(self.car5(), 'подумайте хорошенько над своим выбором :\\')

    def test_enter_exit(self):
        with self.car as c:
            a = 3
        self.assertEqual(c, 'карета подана, извольте')

    def test_copy(self):
        result = copy(self.car2)
        self.assertEqual(result, self.car2)






