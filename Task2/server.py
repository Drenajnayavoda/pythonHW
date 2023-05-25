import socket
# Первым должен быть запущен сервер! servier и client должны быть запущены в разных терминалах / вкладках PyCharm (IDE)

'''
    Сервер
        должен служить для пересылки сообщений между клиентами
        должен иметь возможность обрабатывать несколько сообщений, без ожиданий
        может запоминать сообщения для клиентов, которых сейчас нет в чате
        и при появлении клиента отдавать недоставленные сообщения
'''

def server():
    host = socket.gethostname()  # получаем имя хоста
    port = 55000  # устанавливаем порт соединения

    server_socket = socket.socket()  # создаём сокет
    server_socket.bind((host, port))  # связываем хост и порт (в сокет)
    print(f"Связываем сокет")

    server_socket.listen(1)  # сколько клиентов мы ожидаем
    conn, address = server_socket.accept()  # разрешаем соединение
    print(f"Соединение от: {address}")
    while True:
        print(f"Ожидаем сообщение от клиента")
        data = conn.recv(1024).decode()  # получаем данные, разрешаем размер пакета до 1024 байт
        if not data:  # если нет данных, разрываем соединение
            break
        print(f"Сообщение от пользователя: {data}")
        data = input('Введите сообщение: ')
        conn.send(data.encode())  # отправляем данные клиенту

    conn.close()  # закрываем соединение


if __name__ == '__main__':
    server()