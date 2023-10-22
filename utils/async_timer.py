import functools
import asyncio
import time
from typing import Callable, Any


def async_timed(func: Callable):
    @functools.wraps(func)    # сохраняет информацию о декорируемой функции (например __name__ и тд)
    async def wrapper(*args, **kwargs) -> Any:
        print(f'Выполняется {func} с аргументами {args} {kwargs}')
        start_time = time.perf_counter()    # точнее, чем time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            total_time = start_time - end_time
            print(f'{func} завершилась за {total_time:.4f} сек.')

    return wrapper


if __name__ == '__main__':
    @async_timed
    async def delay(seconds: int) -> int:
        print(f'Засыпаю на {seconds} сек.')
        await asyncio.sleep(seconds)
        print(f'Сон в течение {seconds} сек. закончился')
        return seconds

    @async_timed
    async def main():
        task_one = asyncio.create_task(delay(2))
        task_two = asyncio.create_task(delay(3))
        await task_one
        await task_two

    asyncio.run(main())

    # Выполняется <function main at 0x7f80a7806a70> с аргументами () {}
    # Выполняется <function delay at 0x7f80a7f4fd90> с аргументами (2,) {}
    # Засыпаю на 2 сек.
    # Выполняется <function delay at 0x7f80a7f4fd90> с аргументами (3,) {}
    # Засыпаю на 3 сек.
    # Сон в течение 2 сек. закончился
    # <function delay at 0x7f80a7f4fd90> завершилась за -2.0014 сек.
    # Сон в течение 3 сек. закончился
    # <function delay at 0x7f80a7f4fd90> завершилась за -3.0016 сек.
    # <function main at 0x7f80a7806a70> завершилась за -3.0017 сек.
