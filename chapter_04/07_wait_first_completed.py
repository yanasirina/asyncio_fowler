import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'

        fetchers = [
            asyncio.create_task(fetch_status(session, url, delay=2)),
            asyncio.create_task(fetch_status(session, url, delay=3)),
            asyncio.create_task(fetch_status(session, url)),
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Завершено: {len(done)}')
        print(f'Ожидают: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)    # результатом будем считать первую выполненную задачу

        for pending_task in pending:
            pending_task.cancel()    # в этом есть смысл, если дальше есть другой код, чтобы не занимать поток


asyncio.run(main())
