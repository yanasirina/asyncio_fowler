import asyncio
from aiohttp import ClientSession
from utils import fetch_status, async_timed


@async_timed
async def main():
    async with ClientSession() as session:
        urls = ['https://www.example.com', 'python://www.bad.com', 'https://www.example.com']
        requests = [fetch_status(session, url) for url in urls]

        results = await asyncio.gather(*requests, return_exceptions=True)    # чтобы не ломалось при исключениях
        exceptions = [res for res in results if isinstance(res, Exception)]
        statuses = [res for res in results if not isinstance(res, Exception)]

        print(results)    # [200, AssertionError(), 200]
        print(exceptions)    # [AssertionError()]
        print(statuses)    # [200, 200]


asyncio.run(main())
