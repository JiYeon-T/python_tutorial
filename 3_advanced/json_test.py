import json

# https://www.runoob.com/python3/python3-json.html
# https://docs.python.org/3/library/json.html

# Python3 JSON 数据解析
# JSON (JavaScript Object Notation) 是一种"轻量级的数据交换格式"。
# 如果你还不了解 JSON，可以先阅读我们的 JSON 教程。
# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：


def __json_test1():
    """
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。

    在 json 的编解码过程中，Python 的原始类型与 json 类型会相互转换，具体的转化对照如下：
    Python 编码为 JSON 类型转换对应表：
    Python	JSON
    dict	object
    list,   tuple	array
    str	    string
    int,    float, int- & float-derived Enums	number
    True	true
    False	false
    None	null

    JSON 解码为 Python 类型转换对应表：
    JSON	Python
    object	dict
    array	list
    string	str
    number (int)	int
    number (real)	float
    true	True
    false	False
    null	None
    """

    # Python 字典类型转换为 JSON 对象
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'https://www.runoob.com'
    }

    json_str = json.dumps(data)  # 序列化:Serialize ``obj`` to a JSON formatted ``str``
    print("Python 原始数据：{0} type:{1}".format(repr(data), type(data)))
    print(f"JSON 对象：{json_str} type:{type(json_str)}")

    data2 = json.loads(json_str)  # 反序列化: Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
    # containing a JSON document) to a Python object
    print(f"data2:{data2} type:{type(data2)}")


def __json_file_test():
    """
    如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。
    例如：
    """
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'https://www.runoob.com'
    }
    with open('json_file_test.json', 'w') as f:
        json.dump(data, f)

    with open('json_file_test.json', 'r') as f:
        data2 = json.load(f)
        print(f"data2:{data2} type:{type(data2)}")


if __name__ == '__main__':
    # __json_test1()
    __json_file_test()