import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'python://www.bad.com')
        long_request = fetch_status(session, 'https://www.example.com', delay=3)

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
            asyncio.create_task(long_request),
        ]
        done, pending = await asyncio.wait(fetchers, timeout=1)    # timeout - необязательный аргумент

        print(f'Завершено: {len(done)}')    # исключение попадет сюда, но будет возбуждено только после await
        print(f'Ожидают: {len(pending)}')

        for done_task in done:    # в порядке получения ответа (не объявления функции)
            # result = await done_task    # здесь могло бы произойти исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                print('Пользовательская обработка исключения')

        # # можно добавить обработку незавершившихся задач
        # for pending_task in pending:
        #     await pending_task


asyncio.run(main())
