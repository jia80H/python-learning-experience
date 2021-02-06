import socket
# 不同电脑之间的通信需要使用socket
# 还可以在同一个电脑的不同程序之间通信

# 1. 创建socket对象
# AF_INET: 表示这个socket是用来进行网络连接
# SOCK_DGRAM: 表示连接是一个udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 发送数据
# data: 要发送的*二进制*数据
# address: 发送目标,参数是一个元组,
#   元组内有两个元素,第0个是目标IP地址,第一个是程序的端口号
s.sendto('hello'.encode('utf8'), ('192.168.0.104', 9090))
# 给192.168.0.104这台主机9090端口上发送hello
# 端口号:0~65536 其中0~1024系统一些重要服务在使用

# 3. 关闭socket
s.close()
