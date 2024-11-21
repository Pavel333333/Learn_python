# -*- coding: utf-8 -*-
import pytest
from src.learn import lesson_logging_debug
import io
import sys
from unittest.mock import patch
import unittest.mock


# @pytest.mark.parametrize("mock_inputs, expected_output, expected_print", [
#     ('3', '3', ''),
#     ('0', '0', 'Вы ввели 0. При нуле функция перестаёт быть квадратичной. Повторите ввод'),
#     ('', '', 'Вы ничего не ввели. Здесь должны быть только цифры. Повторите ввод'),
#     ('стоп', 'стоп', 'func_name завершает свою работу'),
#     ('abc', '', 'Вы ввели не число. Повторите ввод'),
# ])
def test_quadratic_equation(mock_inputs): # , expected_output, expected_print
    with unittest.mock.patch("builtins.input") as input_mock:
        input_mock.side_effect = mock_inputs
        lesson_logging_debug.quadratic_equation()

    # input_generator = iter(mock_inputs)
    #
    # with patch('builtins.input', side_effect=lambda: next(input_generator)):
    #     with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         result = lesson_logging_debug.check_value_by_zero(input_generator, 'value_name', 'func_name')
    #
    #         printed_output = fake_stdout.getvalue().strip()
    #
    #         if expected_output == 'стоп':
    #             assert result == expected_output
    #         else:
    #             assert result == expected_output
    #             assert printed_output == expected_print


# test_quadratic_equation('3')
