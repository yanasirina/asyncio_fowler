from asyncio import Future
import asyncio


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result('Hello world!')


async def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future    # вернется моментально


async def main():
    future = await make_request()
    print(future)    # <Future pending>
    print(future.done())    # False
    result = await future
    print(future)    # <Future finished result='Hello world!'>
    print(future.done())    # False
    print(future.result())    # Hello world!
    print(result)    # Hello world!


asyncio.run(main())
