import asyncio
from asyncio import exceptions
from utils import delay


async def main():
    delay_task = asyncio.create_task(delay(7))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=2)
        print(result)    # Ничего не будет напечатано
    except exceptions.TimeoutError:
        print('Timeout!!!')
        print(delay_task.done(), delay_task.cancelled())    # False False (благодаря shield произошла остановка, а не отмена)

        result = await delay_task    # запуск задачи без таймаута (начнется с момента, где была остановлена задача)
        print(result)


asyncio.run(main())
# Засыпаю на 7 сек.
# Timeout!!!
# False False
# Сон в течение 7 сек. закончился (можно заметить, что функция началась не с начала)
# 7
