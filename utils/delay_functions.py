import asyncio


async def delay(seconds: int) -> int:
    print(f'Засыпаю на {seconds} сек.')
    await asyncio.sleep(seconds)
    print(f'Сон в течение {seconds} сек. закончился')
    return seconds
