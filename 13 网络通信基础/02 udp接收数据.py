import socket
# 创建一个基于udp的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号和IP地址
s.bind(('192.168.0.104', 9090))

# recvfrom接收数据
# recvfrom是一个阻塞的方法, 等待到消息才会继续
content = s.recvfrom(1024)
data, addr = content
print(content)  # (b'hello', ('192.168.0.104', 63522))
# 接收到的数据是一个元组, 元组里有两个元素
# 第0个是接收到的数据,第一个是发送方的IP地址和端口号
print('从{}的{}端口接收到了消息, 内容是:{}'.format(addr[0], addr[1], data.decode('utf8')))

s.close()


# 两个文件都绑定端口可以聊天
