import asyncio
from asyncio import exceptions
from utils import delay


async def main():
    delay_task = asyncio.create_task(delay(7))
    try:
        result = await asyncio.wait_for(delay_task, timeout=2)
        print(result)    # Ничего не будет напечатано
    except exceptions.TimeoutError:
        print('Timeout!!!')
        print(delay_task.done(), delay_task.cancelled())    # True True


asyncio.run(main())
