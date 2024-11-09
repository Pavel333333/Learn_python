# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from src.learn import lesson_if_else_switch_case


class TestPosNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '-2', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_pos_numbers(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'положительных чисел в исходном наборе 2')

    @patch('builtins.input', side_effect=['0', '0', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_positive_numbers(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'положительных чисел в исходном наборе 0')

    @patch('builtins.input', side_effect=['-1', '-2', '-3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_negative_numbers(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'положительных чисел в исходном наборе 0')


class TestPosFromTwoNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '-2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_more_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_from_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число 1 больше числа -2')

    @patch('builtins.input', side_effect=['3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_smaller_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_from_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число 3 меньше числа 5')

    @patch('builtins.input', side_effect=['8', '8'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_equals_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.pos_from_two_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число 8 равно числу 8')


class TestLargerAndSmallerNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_more_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.print_larger_and_smaller_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), '5\n3')

    @patch('builtins.input', side_effect=['8', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_smaller_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.print_larger_and_smaller_numbers()
        self.assertEqual(mock_stdout.getvalue().strip(), '8\n5')


class TestFindSmallestNumbers(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.find_smallest_number()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число 1 наименьшее.')

    @patch('builtins.input', side_effect=['5', '3', '8'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.find_smallest_number()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число 3 наименьшее.')

    @patch('builtins.input', side_effect=['-1000', '0', '1000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_0_number(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.find_smallest_number()
        self.assertEqual(mock_stdout.getvalue().strip(), 'число -1000 наименьшее.')


class TestNumberOfCoordQuarters(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_quarter(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.number_of_coord_quarters()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Точка находится в первой четверти')

    @patch('builtins.input', side_effect=['-3', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_quarter(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.number_of_coord_quarters()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Точка находится во второй четверти')

    @patch('builtins.input', side_effect=['-3', '-3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_quarter(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.number_of_coord_quarters()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Точка находится в третьей четверти')

    @patch('builtins.input', side_effect=['3', '-3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4_quarter(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.number_of_coord_quarters()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Точка находится в четвёртой четверти')


class TestFivePointScale(unittest.TestCase):

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mistake_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'ошибка')

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'плохо')

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'неудовлетворительно')

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'удовлетворительно')

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_4_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'хорошо')

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_5_point(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.five_point_scale()
        self.assertEqual(mock_stdout.getvalue().strip(), 'отлично')


class TestCountDaysInMonth(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_january(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в январе 31 день')

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_february(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в феврале 28 дней')

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_march(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в марте 31 день')

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_april(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в апреле 30 дней')

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_may(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в мае 31 день')

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_june(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в июне 30 дней')

    @patch('builtins.input', side_effect=['7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_july(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в июле 31 день')

    @patch('builtins.input', side_effect=['8'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_august(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в августе 31 день')

    @patch('builtins.input', side_effect=['9'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_september(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в сентябре 30 дней')

    @patch('builtins.input', side_effect=['10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_october(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в октябре 31 день')

    @patch('builtins.input', side_effect=['11'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_november(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в ноябре 30 дней')

    @patch('builtins.input', side_effect=['12'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_december(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.count_days_in_month()
        self.assertEqual(mock_stdout.getvalue().strip(), 'в декабре 31 день')


class TestNextDate(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_january(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 2 января')

    @patch('builtins.input', side_effect=['31', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_31_january(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 1 февраля')

    @patch('builtins.input', side_effect=['33', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_33_january(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'исчисление дней в январе от 1 до 31')

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_february(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 2 февраля')

    @patch('builtins.input', side_effect=['28', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_28_february(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 1 марта')

    @patch('builtins.input', side_effect=['29', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_29_february(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'исчисление дней в феврале от 1 до 28')

    @patch('builtins.input', side_effect=['1', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1_march(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 2 марта')

    @patch('builtins.input', side_effect=['31', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_31_march(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'следующий день 1 апреля')

    @patch('builtins.input', side_effect=['55', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_55_march(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.next_date()
        self.assertEqual(mock_stdout.getvalue().strip(), 'исчисление дней в марте от 1 до 31')


class TestRobotMove(unittest.TestCase):

    @patch('builtins.input', side_effect=['С', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_north0(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на север')

    @patch('builtins.input', side_effect=['С', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_north1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на запад')

    @patch('builtins.input', side_effect=['С', '-1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_north_minus1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на восток')

    @patch('builtins.input', side_effect=['З', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_west0(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на запад')

    @patch('builtins.input', side_effect=['З', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_west1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на юг')

    @patch('builtins.input', side_effect=['З', '-1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_west_minus1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на север')

    @patch('builtins.input', side_effect=['Ю', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_south0(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на юг')

    @patch('builtins.input', side_effect=['Ю', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_south1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на восток')

    @patch('builtins.input', side_effect=['Ю', '-1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_south_minus1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на запад')

    @patch('builtins.input', side_effect=['В', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_east0(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на восток')

    @patch('builtins.input', side_effect=['В', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_east1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на север')

    @patch('builtins.input', side_effect=['В', '-1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_move_east_minus1(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.robot_move()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Робот смотрит на юг')


class TestPrintThreeDigitNumberInWords(unittest.TestCase):

    @patch('builtins.input', side_effect=['610'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_610(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.print_three_digit_number_in_words()
        self.assertEqual(mock_stdout.getvalue().strip(), 'шестьсот десять')

    @patch('builtins.input', side_effect=['987'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_987(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.print_three_digit_number_in_words()
        self.assertEqual(mock_stdout.getvalue().strip(), 'девятьсот восемьдесят семь')

    @patch('builtins.input', side_effect=['300'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_300(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.print_three_digit_number_in_words()
        self.assertEqual(mock_stdout.getvalue().strip(), 'триста')


class TestCalc(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '5', '*'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), '15')

    @patch('builtins.input', side_effect=['8', '2', '/'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), '4.0')

    @patch('builtins.input', side_effect=['1', '0', '/'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Делить на ноль не стОит даже пытаться.')

    @patch('builtins.input', side_effect=['21', '33', '+'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), '54')

    @patch('builtins.input', side_effect=['89', '55', '-'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        lesson_if_else_switch_case.calc()
        self.assertEqual(mock_stdout.getvalue().strip(), '34')

