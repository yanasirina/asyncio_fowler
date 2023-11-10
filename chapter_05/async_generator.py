import asyncio
from utils import delay, async_timed


async def positive_integers_async(until: int):
    for integer in range(until, 0, -1):
        tasks = [delay(integer) for _ in range(3)]
        await asyncio.gather(*tasks)
        yield integer


@async_timed
async def main():
    async_generator = positive_integers_async(2)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Got number {number}')


asyncio.run(main())

# Выполняется <function main at 0x7fe39fa97d00> с аргументами () {}
# <class 'async_generator'>
# Засыпаю на 2 сек.
# Засыпаю на 2 сек.
# Засыпаю на 2 сек.
# Сон в течение 2 сек. закончился
# Сон в течение 2 сек. закончился
# Сон в течение 2 сек. закончился
# Got number 2
# Засыпаю на 1 сек.
# Засыпаю на 1 сек.
# Засыпаю на 1 сек.
# Сон в течение 1 сек. закончился
# Сон в течение 1 сек. закончился
# Сон в течение 1 сек. закончился
# Got number 1
# <function main at 0x7fe39fa97d00> завершилась за -3.0041 сек.
