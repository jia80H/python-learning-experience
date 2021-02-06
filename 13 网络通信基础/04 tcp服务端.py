import socket

# 创建一个socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.104', 9090))

s.listen(128)  # 把socket变成一个被动监听的socket
# 128 为队列长度

client_socket, client_addr = s.accept()  # 接收客户端的请求
# 接收的结果是一个元组, 元组里有两个元素
# 第0个元素是客户端的socket连接,
# 第1个元素是客户端和端口号
print('接收到{}客户端{}端口发送的数据, client_socket={}'.format(
    client_addr[0], client_addr[1], client_socket))

x = client_socket.recv(1024)  # 1024 指每次读的大小
print('内容是:')
# tcp里使用recv获取数据
print(x.decode('utf8'))  # hello

s.close()
