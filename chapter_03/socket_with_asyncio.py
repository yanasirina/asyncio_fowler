import asyncio
import asyncio.exceptions
from asyncio import AbstractEventLoop
import socket
import logging
import signal


echo_tasks = []


class CustomExit(SystemExit):
    pass


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """Функция отправлять эхо-ответ, если в сокете появляются новые данные"""
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('got data!')
            if data == b'boom\r\n':    # заглушка
                raise Exception('Неожиданная ошибка сети')
            await loop.sock_sendall(connection, data)    # отправим ответ, если нет ошибки
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def connection_listener(server_socket, loop: AbstractEventLoop):
    """Функция создает задачу echo для нового подключения, если получает его"""
    global echo_tasks

    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получено сообщение от {address}')
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


def shutdown():
    raise CustomExit()


async def close_echo_tasks(echo_tasks: list[asyncio.Task]):
    """Функция дает еще 2 секунды таскам на завершение, если программа была остановлена"""
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass


async def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # loop = asyncio.new_event_loop()

    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, signame), shutdown)    # остановка сокета по сигналам
    await connection_listener(server_socket, loop)


loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
except CustomExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
