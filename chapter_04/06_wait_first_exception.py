import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        bad_request = fetch_status(session, 'python://www.bad.com')
        long_request = fetch_status(session, 'https://www.example.com', delay=3)

        fetchers = [
            asyncio.create_task(bad_request),
            asyncio.create_task(long_request),
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Завершено: {len(done)}')    # исключение попадет сюда, но будет возбуждено только после await
        print(f'Ожидают: {len(pending)}')

        for done_task in done:
            # result = await done_task    # здесь могло бы произойти исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                print('Пользовательская обработка исключения')

        for pending_task in pending:
            pending_task.cancel()    # в этом есть смысл, если дальше есть другой код, чтобы не занимать поток


asyncio.run(main())
