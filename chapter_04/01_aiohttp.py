import asyncio
from aiohttp import ClientSession, ClientTimeout
from utils import async_timed


@async_timed
async def fetch_status(session: ClientSession, url: str) -> int:
    big_timeout = ClientTimeout(total=2)    # переопределим таймаут для конкретного запроса
    async with session.get(url, timeout=big_timeout) as result:
        return result.status


@async_timed
async def main():
    # опционально можно добавлять таймауты для сессии или отдельно для запросов
    small_timeout = ClientTimeout(total=0.1, connect=0.01)    # 0.1 с. для выполнения запроса, 0.01 для подключения
    async with ClientSession(timeout=small_timeout) as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} - {status}')


asyncio.run(main())    # <function main at 0x7f08c6545c60> завершилась за -1.0844 сек.
