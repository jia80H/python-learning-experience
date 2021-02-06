import socket
# TCP有客户端和服务器
# 是面向连接的协议
# udp没有严格的客户端和服务器的区分

# 基于tcp协议的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# udp直接使用sendto发送数据

# tcp中，在发送数据之前， 必须要先和服务器建立连接
# 调用connect方法连接到服务器
s.connect(('192.168.0.104', 9090))

# 连接建立成功才能发送
s.send('hello'.encode('utf8'))

s.close()
