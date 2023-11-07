import asyncio
from aiohttp import ClientSession
from utils import fetch_status, async_timed


@async_timed
async def main():
    async with ClientSession() as session:
        urls = ['https://www.example.com' for _ in range(100)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)    # здесь мы ждем завершения всех запросов
        print(status_codes)    # [200, 200, 200, 200, 200, ..., 200]


asyncio.run(main())    # <function main at 0x7facacfe3e20> завершилась за -1.4668 сек.
