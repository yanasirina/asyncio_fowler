import asyncio


def add_one_func(num: int) -> int:
    return num + 1


async def add_one_coroutine(num: int) -> int:
    return num + 1


func_result = add_one_func(5)
coroutine_result = add_one_coroutine(5)

print(func_result, type(func_result))    # 6 <class 'int'>
print(coroutine_result, type(coroutine_result))    # <coroutine object add_one_coroutine at 0x7feccac43920> <class 'coroutine'>

coroutine_result = asyncio.run(add_one_coroutine(5))
print(coroutine_result, type(coroutine_result))    # 6 <class 'int'>
