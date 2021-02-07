from wsgiref.simple_server import make_server
import json


def test():
    with open('00练习.py', 'r', encoding='utf8') as file:
        responce = file.read()
    return responce


def demo():
    responce = json.dumps({'name': 'zhangsan', 'age': 18})
    return responce


def homepage():
    responce = '主页'
    return responce


url = {
    '/': homepage,
    '/test': test,
    '/demo': demo
    }


def demo_app(environ, start_response):

    status_code = '200 OK'

    path = environ['PATH_INFO']

    method = url.get(path)
    if method:
        responce = method()
    else:
        status_code = '404 Not Found'
        responce = '404 page not found'

    # if path == '/test':
    #     test()
    # elif path == '/demo':
    #     demo()
    # elif path == '/':
    #     homepage()
    # else:
    #     status_code = '404 Not Found'
    #     responce = '404 page not found'
    start_response(status_code, [
        ('Content-Type', 'text/plain; charset=utf-8')])
    return [responce.encode("utf-8")]


if __name__ == '__main__':
    httpd = make_server('192.168.0.104', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")

    httpd.serve_forever()
