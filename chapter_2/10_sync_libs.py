import asyncio
import requests
from utils import async_timed


@async_timed
async def get_example_status() -> int:
    return requests.get('https://www.example.com').status_code


@async_timed
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())
    # задачи будут выполняться поочередно (синхронно), так как в requests не освобождается поток (нет await)
    # для асинхронного выполнения следует использовать асинхронные библиотеки (например, aiohttp)
    print(await task_1)
    print(await task_2)
    print(await task_3)


asyncio.run(main())
# Выполняется <function main at 0x7fa4b69bf6d0> с аргументами () {}
# Выполняется <function get_example_status at 0x7fa4b7837e20> с аргументами () {}
# <function get_example_status at 0x7fa4b7837e20> завершилась за -1.3419 сек.
# Выполняется <function get_example_status at 0x7fa4b7837e20> с аргументами () {}
# <function get_example_status at 0x7fa4b7837e20> завершилась за -1.0394 сек.
# Выполняется <function get_example_status at 0x7fa4b7837e20> с аргументами () {}
# <function get_example_status at 0x7fa4b7837e20> завершилась за -0.8763 сек.
# 200
# 200
# 200
# <function main at 0x7fa4b69bf6d0> завершилась за -3.2579 сек.
