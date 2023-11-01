import asyncio


async def print_delayed_hello_world():
    await asyncio.sleep(2)
    print('Hello world!')


async def add_one_coroutine(num: int) -> int:
    return num + 1


async def main():
    await print_delayed_hello_world()    # выполняется 2 секунды
    await print_delayed_hello_world()    # выполняется еще 2 секунды
    result = await add_one_coroutine(5)    # запустится только после выполнения корутин выше
    return result

asyncio.run(main())    # функция будет выполняться более 4 секунд (синхронно)
