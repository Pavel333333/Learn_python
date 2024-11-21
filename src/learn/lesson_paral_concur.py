# -*- coding: utf-8 -*-
from random import randint
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import aiohttp
from aiohttp import ClientSession
import tracemalloc


# class RandomDivProcess:
#     def __init__(self):
#         self.number = None
#         self.divisors = []
#
#     def generate_random_number(self):
#         self.number = randint(1_000_000, 20_000_000)
#         return self.number
#
#     def find_divisors(self, number=None):
#         if number is None:
#             number = self.number
#         self.divisors.clear()
#
#         for i in range(1, (number // 2) + 1):
#             if number % i == 0:
#                 self.divisors.append(i)
#
#
# async def async_find_divisors(number: int) -> list:
#     divisors = []
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors
#
#
# if __name__ == "__main__":
#
#     rdp = RandomDivProcess()
#     number = rdp.generate_random_number()
#
#     # Ситуация 1: Синхронное выполнение
#     start = time.time()
#     rdp.find_divisors(number)
#     print(number)
#     print(rdp.divisors)
#     finish = time.time()
#     print(f'первый блок выполнился за {finish - start:.4f} секунд')
#
#     # Ситуация 2: Многопроцессорное выполнение
#     start2 = time.time()
#
#     with ProcessPoolExecutor(max_workers=2) as executor:
#         executor.submit(rdp.find_divisors, number)
#
#     print(number)
#     print(rdp.divisors)
#
#     finish2 = time.time()
#     print(f'второй блок выполнился за {finish2 - start2:.4f} секунд')
#
#     # Ситуация 3: Многопоточное выполнение
#     start3 = time.time()
#
#     with ThreadPoolExecutor(max_workers=1) as executor:
#         executor.submit(rdp.find_divisors, number)
#
#     print(number)
#     print(rdp.divisors)
#
#     finish3 = time.time()
#     print(f'третий блок выполнился за {finish3 - start3:.4f} секунд')
#
#     # Ситуация 4: Асинхронное выполнение
#     start4 = time.time()
#     divisors = asyncio.run(async_find_divisors(number))
#     print(number)
#     print(divisors)
#     finish4 = time.time()
#     print(f"Четвертый блок выполнился за {finish4 - start4:.4f} секунд")

# ------------------------------------------------------------------------------------
# Напишите скрипт, который создаст параллельно 10 файлов с именем `file_ {index}
# .txt' и запишет их номер внутрь файла.


# def create_file(index: int):
#     with open(f'C:\\Users\\Admin\\Downloads\\files\\file_{index}.txt', 'w') as file:
#         file.write(str(index))
#
#
# start = time.time()
#
# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.map(create_file, range(10))
#
# finish = time.time()
#
# print(finish - start)
#
# # второй вариант (медленнее в два раза)
#
#
# async def create_file_async(index: int):
#     # Используем to_thread для выполнения блокирующего кода в отдельном потоке
#     await asyncio.to_thread(create_file, index)
#
#
# def create_file(index: int):
#     with open(f'C:\\Users\\Admin\\Downloads\\files\\file_{index}.txt', 'w') as file:
#         file.write(str(index))
#
#
# async def main():
#     tasks = []
#     for i in range(10):
#         task = asyncio.create_task(create_file_async(i))
#         tasks.append(task)
#
#     # Ждем завершения всех задач
#     await asyncio.gather(*tasks)
#
# if __name__ == "__main__":
#     start = time.time()
#     asyncio.run(main())
#     print(time.time() - start)
#
# # третий вариант самый долгий
#
#
# def create_file(index: int):
#     try:
#         with open(f'C:\\Users\\Admin\\Downloads\\files\\file_{index}.txt', 'w') as file:
#             file.write(str(index))
#     except Exception as e:
#         print(f'Error creating file {index}: {e}')
#
#
# if __name__ == '__main__':
#     start = time.time()
#
#     with ProcessPoolExecutor(max_workers=10) as executor:
#         executor.map(create_file, range(10))
#
#     finish = time.time()
#     print(finish - start)
#
#
# # ------------------------------------------------------------------------------------
# # Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
# # с ограничением не более 10 запросов в единицу времени.
#
# semaphore = asyncio.Semaphore(10)
#
#
# async def fetch(session, url):
#     async with semaphore, session.post(url) as response:
#         return await response.read()
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         url = 'http://google.com'
#
#         for i in range(10):
#             task = asyncio.create_task(fetch(session, url))
#             tasks.append(task)
#
#         responses = await asyncio.gather(*tasks)
#         for response in responses:
#             print(len(response))
#
# asyncio.run(main())
# # ------------------------------------------------------------------------------------
# # Написать асинхронный код, который делает 50 get запросов к https://example.com/
# # Записать все статусы ответов в файл и убедиться, что количество запросов соответствует заданному количеству.
# # Необходимо учесть, чтобы одновременно выполнялось не больше 10 запросов.
# # Для выполнения запросов использовать библиотеку aiohttp. Все значения, количество запросов,
# # лимит одновременно выполняемых запросов и url должны передаваться как параметры.
#
#
async def fetch_2(session, url, limit: int):
    semaphore = asyncio.Semaphore(limit)
    async with semaphore, session.get(url) as response:
        content = await response.read()
        text = content.decode('utf-8')
        return text


async def main_2():
    async with aiohttp.ClientSession() as session:
        tasks = []
        url = 'https://example.com/'
        limit = 10
        number_of_requests = 50

        for i in range(number_of_requests):
            task = asyncio.create_task(fetch_2(session, url, limit))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        for response in responses:
            with open(f'C:\\Users\\Admin\\Downloads\\file.txt', 'a') as f:
                f.write(response)
                f.write('*******************************************************************************************\n')


tracemalloc.start()  # Запускаем отслеживание

asyncio.run(main_2())  # Вызываем функцию

snapshot = tracemalloc.take_snapshot()  # Делаем снимок текущего состояния памяти
top_stats = snapshot.statistics('lineno')  # Получаем статистику по строкам кода

print("[ Top 10 Memory Usage ]")
for stat in top_stats[:10]:
    print(stat)

