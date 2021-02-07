import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')
    # print(data)

    path = ''
    if data:
        path = data.splitlines()[0].split(' ')[1]
        print(path)

    # 响应头
    responce_header = 'Http/1.1 200 OK\n'
    responce_header += '/n'

    # 响应体
    if path == '/login':
        responce_body = '登录'
    elif path == '/register':
        responce_body = '注册'
    elif path == '/':
        responce_body = '主页'

    # 响应
    responce_body = 'welcome'
    responce = responce_header + responce_body

    client_socket.send(responce.encode('utf8'))
