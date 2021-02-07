from wsgiref.simple_server import make_server
import json


def demo_app(environ, start_response):
    # demo_app 需要两个参数
    # 第0个参数:表示环境(电脑的环境; 请求路径相关的环境)
    # 第1个参数:是一个函数,用来返回响应头
    #   这个函数需要一个返回值,返回值是一个列表
    #   列表里只有一个元素,是一个二进制,表示返回给浏览器的数据

    status_code = '200 OK'

    # environ是一个字典, 保存了很多数据
    # 其中重要的一个是PATH_INFO能够获取到用户的访问路径
    path = environ['PATH_INFO']
    if path == '/test':
        with open('00练习.py', 'r', encoding='utf8') as file:
            responce = file.read()
    elif path == '/demo':
        responce = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/':
        responce = '主页'
    else:
        status_code = '404 Not Found'
        responce = '404 page not found'
    start_response(status_code, [
        ('Content-Type', 'text/plain; charset=utf-8')])
    return [responce.encode("utf-8")]  # 浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数, 用来处理用户的请求
    httpd = make_server('192.168.0.104', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")

    # 代码作用是打开浏览器,打开指定网址
    # import webbrowser
    # webbrowser.open('http://localhost:8000/xyz?abc')

    # httpd.handle_request()  # 处理一次请求
    httpd.serve_forever()  # 服务器后台一直运行


# 状态码
# 2XX: 请求成功
# 2XX: 重定向
# 4XX: 客户端的错误   404:客户端访问一个不存在的地址  405:请求反射不被允许
# 5XX: 服务器的错误
