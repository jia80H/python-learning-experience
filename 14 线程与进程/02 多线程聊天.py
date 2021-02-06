import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.0.104', 9090))


def send_msg():
    while True:
        msg = input('输入要发送的消息')
        s.sendto(msg.encode('utf8'), ('192.168.0.104', 8080))
        if msg == 'exit':
            break


def recv_msg():
    while True:
        content = s.recvfrom(1024)  # error
        data, addr = content
        print('从{}的{}端口接收到了消息, 内容是:{}'.format(
            addr[0], addr[1], data.decode('utf8')))


t1 = threading.Thread(target=send_msg)  # 创建线程1
t2 = threading.Thread(target=recv_msg)  # 创建线程2

t1.start()
t2.start()
