import asyncio
from utils import delay


async def hello_every_second():
    print('hello_every_second started')
    for i in range(2):
        await asyncio.sleep(1)  # IO задача (отдает управление)
        print(f'Пока я жду, выполняется другой код')  # CPU задача (перехватывает обратно управление)


async def main():
    delay_for_4 = asyncio.create_task(delay(4))
    delay_for_5 = asyncio.create_task(delay(5))
    await hello_every_second()    # в этот момент также будут запущены также таски (при первом await)
    await delay_for_4    # await таска гарантирует его окончание
    await delay_for_5    # await таска гарантирует его окончание
    await hello_every_second()    # будет запущено только после окончания предыдущих авэйтов (так как не таска)


asyncio.run(main())
# hello_every_second started
# Засыпаю на 4 сек.
# Засыпаю на 5 сек.
# Пока я жду, выполняется другой код
# Пока я жду, выполняется другой код
# Сон в течение 4 сек. закончился
# Сон в течение 5 сек. закончился
# hello_every_second started
# Пока я жду, выполняется другой код
# Пока я жду, выполняется другой код
