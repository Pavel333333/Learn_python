import pytest
from src.learn import lesson_data_structure
from contextlib import nullcontext as does_not_raise
import io
import sys
from unittest.mock import patch


def test_square_perimeter():
    assert lesson_data_structure.square_perimeter(5) == 20


def test_square_of_square():
    assert lesson_data_structure.square_of_square(5) == 25


@pytest.mark.parametrize(
    'a, b, result1, result2',
    [
        (3, 5, 15, 16)
    ]
)
def test_rectangle_square_and_perimeter(a, b, result1, result2):
    assert lesson_data_structure.rectangle_square_and_perimeter(a, b) == (result1, result2)


@pytest.mark.parametrize(
    'd, result, expectation',
    [
        (3, 9.42477796076938, does_not_raise()),
        ('3', 9.42477796076938, pytest.raises(TypeError))
    ]
)
def test_circular_length(d, result, expectation):
    with expectation:
        assert lesson_data_structure.circular_length(d) == result


@pytest.mark.parametrize(
    'a, result1, result2, expectation',
    [
        (3, 27, 54, does_not_raise()),
        ('5', 125, 150, pytest.raises(TypeError))
    ]
)
def test_cube_volume_and_surface_area(a, result1, result2, expectation):
    with expectation:
        assert lesson_data_structure.cube_volume_and_surface_area(a) == (result1, result2)


@pytest.mark.parametrize(
    'a, b, c, result1, result2, expectation',
    [
        (3, 4, 5, 60, 94, does_not_raise()),
        (3, 4, '5', 60, 94, pytest.raises(TypeError))
    ]
)
def test_parallelepiped_volume_and_surface_area(a, b, c, result1, result2, expectation):
    with expectation:
        assert lesson_data_structure.parallelepiped_volume_and_surface_area(a, b, c) == (result1, result2)


@pytest.mark.parametrize(
    'r, result1, result2, expectation',
    [
        (3, 18.84955592153876, 28.274333882308138, does_not_raise()),
        ('3', 18.84955592153876, 28.274333882308138, pytest.raises(TypeError))
    ]
)
def test_circle_length_square(r, result1, result2, expectation):
    with expectation:
        assert lesson_data_structure.circle_length_square(r) == (result1, result2)


@pytest.mark.parametrize(
    'a, b, result, expectation',
    [
        (3, 5, 4, does_not_raise()),
        (8, 9, 8.5, does_not_raise()),
        ('5', '8', 6.5, pytest.raises(TypeError))
    ]
)
def test_arithmetic_mean(a, b, result, expectation):
    with expectation:
        assert lesson_data_structure.arithmetic_mean(a, b) == result


@pytest.mark.parametrize(
    'a, b, result, expectation',
    [
        (3, 3, 3.0, does_not_raise()),
        (5, 5, 5.0, does_not_raise()),
        ('8', '8', 8.0, pytest.raises(TypeError))
    ]
)
def test_geometric_mean(a, b, result, expectation):
    with expectation:
        assert lesson_data_structure.geometric_mean(a, b) == result


@pytest.mark.parametrize(
    'a, b, result1, result2, result3, result4, expectation',
    [
        (3, 5, 34, -16, 225, 0.36, does_not_raise()),
        ('3', '5', 34, -16, 225, 0.36, pytest.raises(TypeError))
    ]
)
def test_square_of_digits(a, b, result1, result2, result3, result4, expectation):
    with expectation:
        assert lesson_data_structure.square_of_digits(a, b) == (result1, result2, result3, result4)


@pytest.mark.parametrize(
    'l, result, expectation',
    [
        (300, 3, does_not_raise()),
        (377, 3, does_not_raise()),
        ('610', 6, pytest.raises(TypeError))
    ]
)
def test_full_meters_in_sm(l, result, expectation):
    with expectation:
        assert lesson_data_structure.full_meters_in_sm(l) == result


@pytest.mark.parametrize(
    'm, result, expectation',
    [
        (300, 0, does_not_raise()),
        (1597, 1, does_not_raise()),
        ('2584', 2, pytest.raises(TypeError))
    ]
)
def test_full_ton_in_kg(m, result, expectation):
    with expectation:
        assert lesson_data_structure.full_ton_in_kg(m) == result


@pytest.mark.parametrize(
    'b, result, expectation',
    [
        (1025, 1, does_not_raise()),
        (987, 0, does_not_raise()),
        ('2584', 2, pytest.raises(TypeError))
    ]
)
def test_full_kb_in_bytes(b, result, expectation):
    with expectation:
        assert lesson_data_structure.full_kb_in_bytes(b) == result


def test_segment(capfd):
    a, b = 8, 3
    lesson_data_structure.segment(a, b)
    captured = capfd.readouterr()
    assert captured.out.strip() == f'В отрезке длиной {a} можно разместить максимум {a // b} отрезков длиной {b}'


def test_segment_tail(capfd):
    a, b = 21, 5
    lesson_data_structure.segment_tail(a, b)
    captured = capfd.readouterr()
    assert captured.out.strip() == (f'Если на отрезке {a} разместить максимум отрезков длиной {b} ({a // b} отрезков), '
                                    f'то останется незанятым "хвостик" {a % b}')


def test_double_digit_number(capfd):
    a = 33
    lesson_data_structure.double_digit_number(a)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Число десятков числа {a} равно {a // 10}, правая цифра равна {a % 10}'
    assert output_lines[1] == f'Сумма цифр числа {a} равна {(a // 10) + (a % 10)}, а произведение {(a // 10) * (a % 10)}'
    assert output_lines[2] == f'Если переставить местами цифры числа {a}, то получится {(a % 10) * 10 + a // 10}'


def test_triple_digit_number(capfd):
    a = 610
    lesson_data_structure.triple_digit_number(a)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Число сотен числа {a} равно {a // 100}'
    assert output_lines[1] == f'Правая цифра числа {a} равна {(a % 100) % 10}, число десятков равно {(a // 10) % 10}'


def test_one_number(capfd):
    a = 987
    lesson_data_structure.one_number(a)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Утверждение "Число {a} является положительным" является {a > 0}'
    assert output_lines[1] == f'Утверждение "Число {a} является нечетным" является {a % 2 != 0}'
    assert output_lines[2] == f'Утверждение "Число {a} является четным" является {a % 2 == 0}'


def test_two_numbers(capfd):
    a, b = 5, 8
    lesson_data_structure.two_numbers(a, b)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Утверждение "справедливы неравенства {a} > 2 и {b} ≤ 3" является {a > 2 and b <= 3}'
    assert output_lines[1] == f'Утверждение "справедливы неравенства {a} ≥ 0 и {b} < -2" является {a >= 0 and b < -2}'


def test_three_numbers(capfd):
    a, b, c = 5, 8, 13
    lesson_data_structure.three_numbers(a, b, c)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Утверждение "справедливо двойное неравенство {a} < {b} < {c}" является {a < b < c}'
    assert output_lines[1] == f'Утверждение "Число {b} находится между числами {a} и {c}" является {a < b < c}'


def test_two_numbers_comparison(capfd):
    a, b = 21, 33
    lesson_data_structure.two_numbers_comparison(a, b)
    captured = capfd.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == f'Утверждение "каждое из чисел {a} и {b} нечётное" является {a % 2 != 0 and b % 2 != 0}'
    assert output_lines[1] == f'Утверждение "хотя бы одно из чисел {a} и {b} нечётное" является {a % 2 != 0 or b % 2 != 0}'
    assert output_lines[2] == f'Утверждение "ровно одно из чисел {a} и {b} нечётное" является {False}'


def test_list1(capsys):
    lst = [1, 2, 3, 4, 5]
    lesson_data_structure.list1()
    captured = capsys.readouterr()
    assert captured.out.strip() == (f'первый элемент списка {lst[0]}\nтретий элемент списка {lst[2]}\nпервые три элемента'
                                    f' списка {lst[:3]}')


def test_rostov(capsys):
    lesson_data_structure.rostov()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Ростов-на-Дону'


def test_word_digit(capsys):
    lesson_data_structure.word_digit()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')
    assert output_lines[0] == "['a', 's', 'a']"
    assert output_lines[1] == "['1', '32', '23']"
    assert output_lines[2] == "['s', 'a']"
    assert eval(output_lines[3]) == {'1', '32', 'a', 's', '23'}


def test_man_print(monkeypatch):
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    lesson_data_structure.man_print()
    output_lines = captured_output.getvalue().strip().split('\n')
    assert output_lines[0] == "имя: Иван, возраст: 21, пол: мужской, рост: 180, вес: 80, размер ноги: 44"
    assert output_lines[1] == "имя: Иван, пол: мужской, рост: 180, вес: 80, размер ноги: 45"


@pytest.mark.skip('так надо')
def test_byn_search(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    captured_output = io.StringIO()
    sys.stdout = captured_output
    lesson_data_structure.byn_search()
    sys.stdout = sys.__stdout__
    output_lines = captured_output.getvalue().strip().split('\n')
    assert output_lines[0].startswith(f'Количество попыток поиска было')
    assert output_lines[1] == 'Поиск увенчался успехом'


@pytest.fixture
def unsorted_list():
    return [32, 8, 24, 47, 43, 21, 34, 95, -1, 39, 41]


def test_bubble_sort(unsorted_list):
    sorted_list = lesson_data_structure.bubble_sort(unsorted_list)
    expected_list = sorted(unsorted_list)
    assert sorted_list == expected_list









