import asyncio
from aiohttp import ClientSession
from utils import async_timed, fetch_status


@async_timed
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [
            fetch_status(session=session, url=url, delay=10),
            fetch_status(session=session, url=url, delay=0),
            fetch_status(session=session, url=url, delay=2),
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())

""" Обработка результатов будет происходить последовательно """
# <function fetch_status at 0x7f6b689fdb40> завершилась за -1.3645 сек.
# 200
# <function fetch_status at 0x7f6b689fdb40> завершилась за -2.4262 сек.
# 200
# <function fetch_status at 0x7f6b689fdb40> завершилась за -10.4140 сек.
# 200
