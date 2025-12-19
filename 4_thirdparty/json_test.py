import os
import json
import orjson #orjson是一个JSON库，相较于Python原生的JSON库，它的功能更加丰富、效率更高。
#https://zhuanlan.zhihu.com/p/654316421

def json_encode_test1():
    """
    对 map 类型的变量进行 jason 序列化
    var -> json string
    """
    map_var = {"name":"小李", "age":28, "gender":"男", "home":"北京"}
    print("默认形式打印:")
    output = json.dumps(map_var)
    print(f"output:{output} type:{type(output)}") # 类型:字符串
    print("指定打印格式:")
    output = json.dumps(map_var, indent=True, ensure_ascii=False)
    print(f"output:{output} type:{type(output)}")
    print("按照 key 排序后:")
    output = json.dumps(map_var, indent=True, ensure_ascii=False, sort_keys=True)
    print(f"output:{output} type:{type(output)}")

def json_decode_test1():
    """
    对 json 格式字符串 进行反序列化
    json string -> var
    """
    list_str = '[1, 2, 3, 4, 5]'
    list_var = json.loads(list_str) # string -> list
    # print('转换前:json:{} type:{} \n转换后:{} 类型:{}'.format(list_str, type(list_str), list_var, type(list_var)))

    dict_str = '{"name":"张三", "age":18, "school":"北京大学"}' # string -> <class'dict'>
    # dict_str = '{"name": "张三", "age": 18}'
    #NOTE:
    # json 格式字符串不可以以双引号结尾
    # 错误一般是由于在解析json的字符串的时候，提供的字符串不符合规范而导致的。根据json的格式要求，其属性名必须使用双引号(")，不可以使用单引号(')
    #json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
    # dict_str = """{'name': '张三', 'age': 18}"""
    dict_var = json.loads(dict_str)
    print('转换前:json:{} type:{} \n转换后:{} 类型:{}'.format(dict_str, type(dict_str), dict_var, type(dict_var)))


def write_file(json_path, obj):
    """
    将 json 数据写入文件
    :param json_path
    :param obj
    :ret None
    """
    json_file = os.path.join(os.getcwd(), json_path)
    #创建文件
    if not os.path.exists(json_file):
        open(json_file, "w").close()

    with open(json_file, "w") as f:
        json.dump(obj, f, ensure_ascii=False)
    print("write json file success")

def read_json_file(json_path):
    """
    读取 json 文件并返回 json 对象
    :param json_path
    :ret json object string
    """
    json_str = None
    with open(json_path, "r") as f:
        json_str = json.load(f)
    print("read json success, json_str:{} result type:{}".format(json_str, type(json_str)))
    return json_str

def json_test3():
    """json 序列化/反序列化测试"""
    class_info = [{'name':"小李", 'age':18, 'grade':[100, 100, 0, 100]},
                  {'name':"小张", 'age':15, 'grade':[100, 102, 0, 100]},
                  {'name':"小王", 'age':12, 'grade':[100, 109, 5, 100]}]
    json_str = json.dumps(class_info, ensure_ascii=False)
    print(f"json_str:{json_str}")
    write_file("test2.json", class_info)

    read_str = read_json_file("test2.json")
    print(f"read str:{read_str} type:{type(read_str)}")

class Student:
    """
    json 对象序列话实际上还是把对象的每个要保存的成员 -> 字典序列化保存起来
    反序列化时再构造一个新的对象, 然后对成员进行初始化
    """
    def __init__(self):
        """default contructor"""
        pass
    def __init__(self, name:str, age:int, grades:list):
        """constructor"""
        self.name = name
        self.age = age
        self.grades = grades

    @property
    def to_json(self):
        """
        使用装饰器 @property 修饰方法
        将类转换为要保存的 json 对象
        """
        return {
            'name':self.name,
            'age':self.age,
            'grades':self.grades
        }

def class_to_json_test1():
    """
    类对象转换为 json
    class -> json str
    """
    xiaoli = Student("小李", 18, [100, 100, 2])
    ##################################
    # 第一种方法, python 对象的内置方法 __dict__
    ##################################
    json_str = json.dumps(xiaoli.__dict__, indent=True, ensure_ascii=False)
    print(f"第一种:json_str:{json_str} type:{type(json_str)}")

    ##################################
    # 第二种方法:自己实现 to_json 方法, 将类转为 dict
    ##################################
    json_str = json.dumps(xiaoli.to_json, indent=True, ensure_ascii=False)
    print(f"第二种:json_str:{json_str} type:{type(json_str)}")

    ##################################
    # 反序列化
    ##################################
    json_obj = json.loads(json_str)
    print(f"反序列化:{json_obj} type:{type(json_obj)}") # type:'dict'
    stu_x = Student(json_obj["name"], json_obj['age'], json_obj['grades'])
    print(f"stu_x:{stu_x} type:{type(stu_x)}")

    #write file test
    write_file("xiaoli.json", xiaoli.to_json)
    read_json_file("xiaoli.json")

if __name__ == '__main__':
    print("json test")
    # json_encode_test1()
    # json_decode_test1()
    # json_test3()
    class_to_json_test1()