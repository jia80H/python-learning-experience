import socket

# http 服务器都是基于TCP的socket连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址只能通过IP地址访问
# 127.0.0.1 和 0.0.0.0 都表示本机
# 0.0.0.0 表示所有可用地址
server_socket.bind(('192.168.0.104', 9090))
server_socket.listen(128)

# 挂起服务器
# 浏览器访问 192.168.0.104:9090

client_socket, client_addr = server_socket.accept()
data = client_socket.recv(1024).decode('utf8')
print(data)
"""
GET / HTTP/1.1
Host: 192.168.0.104:9090
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 ......
Accept: text/html,.....
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
"""
# 返回内容之前,需要设置HTTP响应头
client_socket.send('Http/1.1 200 OK\n'.encode('utf8'))  # 必须的

# 所有响应头设置完成以后,再换行
client_socket.send('\n'.encode('utf8'))

# 给客户端返回消息
client_socket.send('hello world'.encode('utf8'))
