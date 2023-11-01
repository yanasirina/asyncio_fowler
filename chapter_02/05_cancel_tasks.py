import asyncio
from asyncio import CancelledError
from utils import delay


async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0
    print(long_task.done())    # False
    while not long_task.done():
        print('Задача продолжает работу, следующая проверка через секунду')
        await asyncio.sleep(1)    # передаем управление задаче на секунду
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task    # задача запустилась бы и без авэйта (в строке 13), но ее отмена не вызвала бы исключения
    except CancelledError:
        print('Задача отменена')
        print(long_task.done())    # True
        print(long_task.cancelled())    # True


asyncio.run(main())
