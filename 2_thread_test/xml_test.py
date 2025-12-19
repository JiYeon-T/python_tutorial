import xml.etree.ElementTree as ET

# python 内置的 XML 库
def xml_encode_test1():
    """ xml encode test 序列化 """
    #我们可以使用ElementTree模块的Element对象来创建一个XML元素
    root = ET.Element("root")
    root.set("version", "1.0")

    # SubElement 方法在根元素下创建子元素
    child = ET.SubElement(root, "child")
    #设置子元素的
    child.text = "Hello,world"

    child2 = ET.SubElement(root, "child2", {"name":"Libai"})
    child3 = ET.SubElement(root, "child3", {"age":"128"})
    child4 = ET.SubElement(root, "child4", {"school":"Peiking University"})

    xml_str_bytes = ET.tostring(root, encoding="utf-8")
    xml_str =  xml_str_bytes.decode("utf-8")
    print(f"item:{xml_str_bytes} type:{type(xml_str_bytes)}" )
    print(f"item:{xml_str} type:{type(xml_str)}" )

    write_to_file("data.xml", xml_str)

def xml_decode_test1(xml_path):
    """ xml decode test 反序列化 """
    #通过调用parse方法并传入XML文件的路径，我们可以将XML文件解析为Element对象。
    tree = ET.parse(xml_path)
    #使用 getroot 方法获取 XML 文件的根元素。
    root = tree.getroot()

    #通过 find 方法查找指定的元素(element)
    child = root.find("child")
    print(f"child text:{child.text}")

    child4 = root.find("child4")
    print(f"child4 name:{child4.get('name', 'default value')}")
    print(f"child4 school:{child4.get('school', 'default value')}")

def write_to_file(save_path, data):
    print("save to XML file")
    fp = open(save_path, 'w')
    fp.write(data)
    fp.close()

if __name__ == '__main__':
    print("xml test")
    xml_encode_test1()
    xml_decode_test1("data.xml")