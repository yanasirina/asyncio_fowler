import asyncio
from utils import async_timed


@async_timed
async def cpu_bound_func() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed
async def main():
    task_one = asyncio.create_task(cpu_bound_func())
    task_two = asyncio.create_task(cpu_bound_func())
    await task_one
    # задача начнет выполнение только после завершения task_one, так как в task_one не освобождается поток (нет await)
    await task_two


asyncio.run(main())
# Выполняется <function main at 0x7fe9c2ff8550> с аргументами () {}
# Выполняется <function cpu_bound_func at 0x7fe9c3933e20> с аргументами () {}
# <function cpu_bound_func at 0x7fe9c3933e20> завершилась за -3.3447 сек.
# Выполняется <function cpu_bound_func at 0x7fe9c3933e20> с аргументами () {} - началась после завершения task_two
# <function cpu_bound_func at 0x7fe9c3933e20> завершилась за -3.1679 сек.
# <function main at 0x7fe9c2ff8550> завершилась за -6.5128 сек.
