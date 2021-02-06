import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.0.104', 9090))

file_name = input('输入要下载的文件名:')
s.send(file_name.encode('utf8'))

with open('下载-'+file_name, 'wb') as file:
    while True:
        content = s.recv(1024)
        if not content:
            break
    file.write(content)

s.close()
