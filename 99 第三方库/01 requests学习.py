import requests
# 参见  https://cn.python-requests.org/zh_CN/latest/
""" 准备 """
# pip install requests  # 如何下载

""" 发送请求 """
# get
# 获取 Github 的公共时间线
r = requests.get('https://api.github.com/events')
print(r) # <Response [200]>
# post
# Requests 简便的 API 意味着所有 HTTP 请求类型都是显而易见的。
r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# 其他HTTP请求类型
# put/delete/head/options
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

""" 传递url参数 """
# 使用 params 关键字参数，以一个字符串字典来提供这些参数。
# 传递 key1=value1 和 key2=value2 到 httpbin.org/get 
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)  # http://httpbin.org/get?key1=value1&key2=value2
# 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。

# 还可以将一个列表作为值传入：
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
# http://httpbin.org/get?key1=value1&key2=value2&key2=value3

""" 响应内容 """
r = requests.get('https://api.github.com/events')
print(r.text)
# u'[{"repository":{"open_issues":0,"url":"https://github.com/...
# Requests 会使用http头部推测的文本编码。
# 可以找出 Requests 使用了什么编码，
print(r.encoding)  # utf-8
# 并且能够使用 r.encoding 属性来改变它：
# r.encoding = 'gbk'
# 如果改变了编码，每当访问 r.text ，
# Request 都将会使用 r.encoding 的新值。

""" 二进制响应内容 """
# 以字节的方式访问请求响应体，对于非文本请求：
r = requests.get('https://api.github.com/events')
print(r.content)

# Requests 会自动解码 gzip 和 deflate 传输编码的响应数据
# 以请求返回的二进制数据创建一张图片，
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))

""" JSON 响应内容 """
# Requests 中有内置的 JSON 解码器
r = requests.get('https://api.github.com/events')
print(r.json())

# 需要注意的是，
# 成功调用 r.json() 并**不**意味着响应的成功。
# 有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。
# 这种 JSON 会被解码返回。
# 要检查请求是否成功，使用 r.raise_for_status() 
# 或者检查 r.status_code 是否和你的期望相同。

""" 原始响应内容 """
# 在罕见的情况下，你可能想获取来自服务器的原始套接字响应，
# 那么你可以访问 r.raw。 
# 如果你确实想这么干，那请你确保在初始请求中设置了 stream=True。具体你可以这么做：

r = requests.get('https://api.github.com/events', stream=True)
r.raw
r.raw.read(10)
# 但一般情况下，你应该以下面的模式将文本流保存到文件：

with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)

# 使用 Response.iter_content 
# 将会处理大量你直接使用 Response.raw 不得不处理的。
# 当流下载时，上面是优先推荐的获取内容方式。
# Note that *chunk_size* can be freely adjusted to a number 
# that may better fit your use cases

""" 定制请求头 """
# 想为请求添加 HTTP 头部，
# 只要简单地传递一个 dict 给 headers 参数就可以了
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
# 注意: 定制 header 的优先级低于某些特定的信息源，

# 注意: 所有的 header 值必须是 string、bytestring 
# 或者 unicode。尽管传递 unicode header 也是允许的，但不建议这样做。
""" 更加复杂的 POST 请求 """
# 要发送一些编码为表单形式的数据——非常像一个 HTML 表单。
# 要实现这个，只需简单地传递一个字典给 data 参数。
# 数据字典在发出请求时会自动编码为表单形式：

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

# 可以为 data 参数传入一个元组列表。
# 在表单中多个元素使用同一 key 的时候，这种方式尤其有效
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# 很多时候你想要发送的数据并非编码为表单形式的。
# 如果你传递一个 string 而不是一个 dict，
# 那么数据会被直接发布出去。
# 例如，Github API v3 接受编码为 JSON 的 POST/PATCH 数据：

import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

# 此处除了可以自行对 dict 进行编码，
# 还可以使用 json 参数直接传递，然后它就会被自动编码。
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload)

""" 响应状态码 """
# 检测响应状态码
r = requests.get('http://httpbin.org/get')
print(r.status_code)
# Requests附带了一个内置的状态码查询对象
r.status_code == requests.codes.ok

