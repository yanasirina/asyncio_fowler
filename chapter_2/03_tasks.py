import asyncio
from utils import delay


async def async_func():
    sleep_for_3 = asyncio.create_task(delay(3))
    sleep_for_2 = asyncio.create_task(delay(2))
    sleep_for_1 = asyncio.create_task(delay(1))
    sleep_for_4 = asyncio.create_task(delay(4))

    """
    В момент авэйта первой задачи будут также запущены другие задачи (даже если их не авэйтнуть).
    Однако в таком случае,программа не гарантирует окончания всех задач.
    Например, если не авэйтнуть sleep_for_4,  то код в ней не успеет выполнится полностью.
    """
    await sleep_for_3
    # await sleep_for_2
    # await sleep_for_1
    # await sleep_for_4


asyncio.run(async_func())    # функция будет выполняться около 3 секунд (асинхронно)
# Засыпаю на 3 сек.
# Засыпаю на 2 сек.
# Засыпаю на 1 сек.
# Засыпаю на 4 сек.
# Сон в течение 1 сек. закончился
# Сон в течение 2 сек. закончился
# Сон в течение 3 сек. закончился
