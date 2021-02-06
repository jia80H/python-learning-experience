import socket
import os

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sever_socket.bind(('192.168.0.104', 9090))
sever_socket.listen(128)

client_socket, client_addr = sever_socket.accept()
file_name = client_socket.recv(1024).decode('utf8')

if os.path.isfile(file_name):
    with open(file_name, 'rb') as file:
        content = file.read()
        client_socket.send(content)
else:
    print('文件不存在')
