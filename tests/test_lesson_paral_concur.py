# -*- coding: utf-8 -*-
from src.learn import lesson_paral_concur
import unittest
from pathlib import Path
import pytest, asyncio, sys, aiofiles
from io import StringIO
import os


class TestRandomDivProcess(unittest.TestCase):
    def setUp(self):
        self.rdp = lesson_paral_concur.RandomDivProcess()
        self.random_number = self.rdp.generate_random_number()

    def test_init(self):
        assert lesson_paral_concur.RandomDivProcess().number is None
        assert lesson_paral_concur.RandomDivProcess().divisors == []

    def test_generate_random_number(self):
        result = self.rdp.generate_random_number()
        assert isinstance(self.random_number, int)

    def test_find_divisors(self):
        self.rdp.find_divisors(self.random_number)
        assert len(self.rdp.divisors) >= 1


def test_async_find_divisors():
    rdp = lesson_paral_concur.RandomDivProcess()
    number = rdp.generate_random_number()
    divisors = lesson_paral_concur.asyncio.run(lesson_paral_concur.async_find_divisors(number))
    remainders_sum = sum(number % i for i in divisors)
    assert remainders_sum == 0


class TestFileCreation(unittest.TestCase):
    def test_create_file(self):
        test_dir = Path('C:/Users/Admin/Downloads/files')

        for i in range(10):
            expected_file_path = test_dir / f'file_{i}.txt'
            lesson_paral_concur.create_file(i)
            self.assertTrue(expected_file_path.exists(), msg=f"Файл {expected_file_path} не был создан.")


@pytest.mark.asyncio
async def test_main():
    target_folder = 'C:\\Users\\Admin\\Downloads\\files'
    await lesson_paral_concur.main()
    files = os.listdir(target_folder)
    assert len(files) == 10


@pytest.mark.asyncio
async def test_main_2():
    await lesson_paral_concur.main_2()
    async with open(f'C:\\Users\\Admin\\Downloads\\file.txt', 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if '*******************************************************************************************' in line:
                count += 1
    assert count == 50


# это версия того же тестирования от gpt

@pytest.mark.asyncio
async def test_main_3():

    await lesson_paral_concur.main_2()
    # Путь до файла
    file_path = Path('C:/Users/Admin/Downloads/file.txt')

    # Проверяем существование файла
    if not file_path.exists():
        raise FileNotFoundError("Файл не найден")

    # Открываем файл асинхронно
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        count = 0
        async for line in f:
            if len(line.strip()) == 80 and set(line.strip()) == {'*'}:
                count += 1

    assert count == 50







