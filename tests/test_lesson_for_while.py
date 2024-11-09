# -*- coding: utf-8 -*-
from src.learn import lesson_for_while
import unittest
from io import StringIO
import sys


def test_print_digits_1_100():
    captured_output = StringIO()
    sys.stdout = captured_output

    lesson_for_while.print_digits_1_100()

    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    expected_output = "\n".join(str(i) for i in range(101)) + "\n"

    assert output == expected_output


class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.multiplication_table()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        expected_output = "\n".join(f"{i} * {j} = {i * j}" for i in range(10) for j in range(1, 10)) + "\n"

        self.assertEqual(output, expected_output)


class TestPrintLstDict(unittest.TestCase):
    def test_output(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.print_lst_dict()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Ожидаемый результат
        expected_output = (
            "1\n"
            "2\n"
            "(3, 4, 5)\n"
            "[6, '7', 'восемь']\n"
            "{9: 'девять', 10: 'десять'}\n"
            "имя Иван\n"
            "отчество Петрович\n"
            "фамилия Кузнецов\n"
        )

        self.assertEqual(output, expected_output)


def test_print_digits_1_100_3():
    captured_output = StringIO()
    sys.stdout = captured_output

    lesson_for_while.print_1_100_3()

    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()

    expected_output = "\n".join(str(i) for i in range(1, 101) if i % 3 == 0) + "\n"

    assert output == expected_output


class TestSummDigits(unittest.TestCase):
    def test_summ_digits_1_100(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.summ_digits_1_100()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        expected_output = "5050\n"

        self.assertEqual(output, expected_output)


class TestMultiplicationTable2(unittest.TestCase):
    def test_multiplication_table_2(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.multiplication_table_2()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        expected_output = "\n".join(f"2 * {i} = {2 * i}" for i in range(1, 10)) + "\n"

        self.assertEqual(output, expected_output)


class TestSimpleNumbers(unittest.TestCase):
    def test_simple_numbers(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.simple_numbers()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Ожидаемый результат
        expected_output = (
            "2\n"
            "3\n"
            "5\n"
            "7\n"
            "11\n"
            "13\n"
            "17\n"
            "19\n"
            "23\n"
            "29\n"
            "31\n"
            "37\n"
            "41\n"
            "43\n"
            "47\n"
        )

        self.assertEqual(output, expected_output)


class TestSummSquaresNumbers(unittest.TestCase):
    def test_sum_of_squares_of_numbers(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.sum_of_squares_of_numbers()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        expected_output = "385\n"

        self.assertEqual(output, expected_output)


class TestPrintYx2(unittest.TestCase):
    def test_print_yx2(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.print_yx2()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Ожидаемый результат
        expected_output = (
            "1\n"
            "2.25\n"
            "4.0\n"
            "6.25\n"
            "9.0\n"
            "12.25\n"
            "16.0\n"
            "20.25\n"
            "25.0\n"
            "30.25\n"
            "36.0\n"
            "42.25\n"
            "49.0\n"
            "56.25\n"
            "64.0\n"
            "72.25\n"
            "81.0\n"
            "90.25\n"
            "100.0\n"
        )

        self.assertEqual(output, expected_output)


class TestFactorials(unittest.TestCase):
    def test_factorials(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        lesson_for_while.factorials()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Ожидаемый результат
        expected_output = (
            "1\n"
            "2\n"
            "6\n"
            "24\n"
            "120\n"
        )

        self.assertEqual(output, expected_output)
