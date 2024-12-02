import asyncio
import time

# № 1
# async def long_func():
#     print('Начала работать долгая функция')
#     await asyncio.sleep(5)
#     print('Закончила работать долгая функция')
#
#
# async def short_func():
#     print('Начала работать короткая функция')
#     await asyncio.sleep(1)
#     print('Закончила работать короткая функция')
#
#
# async def main():
#     await long_func()
#     await short_func()
#
# asyncio.run(main())

# Вывод:
# Начала работать долгая функция
# Закончила работать долгая функция
# Начала работать короткая функция
# Закончила работать короткая функция


# № 2
# async def long_func():
#     print('Начала работать долгая функция')
#     await asyncio.sleep(5)
#     print('Закончила работать долгая функция')
#
#
# async def short_func():
#     print('Начала работать короткая функция')
#     await asyncio.sleep(1)
#     print('Закончила работать короткая функция')
#
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     def run_short_func():
#         asyncio.ensure_future(short_func())
#
#     loop.call_soon(run_short_func)
#
#     await long_func()
#
# asyncio.run(main())

# Вывод:
# Начала работать долгая функция
# Начала работать короткая функция
# Закончила работать короткая функция
# Закончила работать долгая функция


# № 3
# async def long_func():
#     print('Начала работать долгая функция')
#     await asyncio.sleep(5)
#     print('Закончила работать долгая функция')
#
#
# async def short_func():
#     print('Начала работать короткая функция')
#     await asyncio.sleep(1)
#     print('Закончила работать короткая функция')
#
#
# async def main():
#     await asyncio.gather(short_func(), long_func())
#
# asyncio.run(main())

# Вывод:
# Начала работать короткая функция
# Начала работать долгая функция
# Закончила работать короткая функция
# Закончила работать долгая функция


# № 4
# async def long_func():
#     print('Начала работать долгая функция')
#     await asyncio.sleep(5)
#     print('Закончила работать долгая функция')
#
#
# async def short_func():
#     print('Начала работать короткая функция')
#     await asyncio.sleep(1)
#     print('Закончила работать короткая функция')
#
#
# async def main():
#     task1 = asyncio.create_task(long_func())
#     await short_func()
#
#     await task1
#
#
# asyncio.run(main())

# Вывод:
# Начала работать короткая функция
# Начала работать долгая функция
# Закончила работать короткая функция
# Закончила работать долгая функция


# № 5
# async def long_func():
#     print('Начала работать долгая функция')
#     await asyncio.sleep(5)
#     print('Закончила работать долгая функция')
#
#
# async def short_func():
#     print('Начала работать короткая функция')
#     await asyncio.sleep(1)
#     print('Закончила работать короткая функция')
#
#
# async def main():
#     task2 = asyncio.create_task(short_func())
#     task1 = asyncio.create_task(long_func())
#
#     await task1
#     await task2
#
# asyncio.run(main())

# Вывод:
# Начала работать короткая функция
# Начала работать долгая функция
# Закончила работать короткая функция
# Закончила работать долгая функция


# № 6
# async def set_after(fut, delay, value):
#     # Sleep for *delay* seconds.
#     await asyncio.sleep(delay)
#
#     # Set *value* as a result of *fut* Future.
#     fut.set_result(value)
#
#
# async def main():
#     # Get the current event loop.
#     loop = asyncio.get_running_loop()
#
#     # Create a new Future object.
#     fut = loop.create_future()
#
#     # Run "set_after()" coroutine in a parallel Task.
#     # We are using the low-level "loop.create_task()" API here because
#     # we already have a reference to the event loop at hand.
#     # Otherwise we could have just used "asyncio.create_task()".
#     await loop.create_task(set_after(fut, 1, 'world'))
#
#     print('hello ', end='')
#
#     # Wait until *fut* has a result (1 second) and print it.
#     print(await fut)
#
# asyncio.run(main())

# Вывод:
# hello world