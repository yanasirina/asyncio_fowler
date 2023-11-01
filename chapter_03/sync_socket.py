import selectors
import socket


# создадим селектор
selector = selectors.DefaultSelector()

# создадим сокет
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# подключим сокет к порту
server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)    # сокет должен быть неблокирующим, для работы с несколькими пользователями
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)    # селектор будет отслеживать события, связанные с сервером

while True:
    events = selector.select(timeout=1)    # идем дальше, если селектор поймал новый event или прошел timeout 1 сек

    if len(events) == 0:    # если сработал таймаут
        print('Событий нет, подождем еще')

    for event, _ in events:
        event_socket = event.fileobj    # получим сокет, для которого произошло событие

        # если была попытка подключения
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {address}')
            selector.register(connection, selectors.EVENT_READ)    # селектор будет отслеживать события, связанные с конкретным подключением
        # если поступили данные в сокет
        else:
            data = event_socket.recv(1024)
            print(f'Получены данные: {data}')
            event_socket.send(data)
