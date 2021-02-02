import json


def read_file(path):
    try:
        with open(path, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')


def write_json(path, data):
    with open(path, 'w', encoding='utf8') as file:
        json.dump(data, file)


def read_json(path, default_data={}):
    try:
        with open(path, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('文件未找到')
        return default_data
