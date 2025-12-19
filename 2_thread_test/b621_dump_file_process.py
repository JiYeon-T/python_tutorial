import os


def apk_log_mass_raw_data_op(in_file_name, out_file_name=None):
    """一长排字符串转成 col_size=16 的矩阵"""
    out_file_name = in_file_name + ".out.txt" # 输出文件名称固定
    wfd = open(out_file_name, 'w')
    with open(in_file_name, mode='r') as rfd:
        while True:
            pack = rfd.read(16 * 2) # hex string:16 bytes
            if len(pack) == 0:
                print("write finish")
                break
            print(f"read len:{len(pack)}")
            wfd.write(pack)
            wfd.write("\n")
    wfd.close()

def watch_log_mass_raw_data_op(in_file_name, out_file_name=None):
    out_file_name = in_file_name + ".out.txt"
    rfd = open(in_file_name, 'r')
    wfd = open(out_file_name, 'w')
    while True:
    # if 1:
        prefix_len = 44
        pack_len = 16
        pack = rfd.readline()
        if len(pack) == 0:
            break
        prefix = pack[:43]
        data = pack[43:90]
        data_exclude_space = ""
        for elem in data: # 大写, 去除空格
            if elem != ' ':
                data_exclude_space += elem.upper()

        tail = pack[90:]
        print(f"pack:{pack}")
        print(f"prefix:{prefix}\ndata_exclude_space:{data_exclude_space}\ntail:{tail}\n")
        wfd.write(data_exclude_space)
        wfd.write("\n")
    rfd.close()
    wfd.close()

    rfd.close()

def watch_log_mass_raw_data_op2(in_file_name, out_file_name=None):
    """一长排字符串转成 col_size=16 的矩阵"""
    out_file_name = in_file_name + ".out.txt" # 输出文件名称固定
    wfd = open(out_file_name, 'w')
    with open(in_file_name, mode='r') as rfd:
        while True:
            pack = rfd.read(16 * 2) # hex string:16 bytes
            if len(pack) == 0:
                print("write finish")
                break
            print(f"read len:{len(pack)}")
            # for idx in range(len(pack)):
            #     if pack[idx] >= 'a' and pack[idx] <= 'z':
                    # pack[idx] = str(pack[idx]) - 'a' + 'A'
                    # pack[idx] = pack[idx].upper()
                    # print(f"{pack[idx]}, type:{type(pack[idx])}")
            wfd.write(pack.upper())
            # wfd.write("\n")
    wfd.close()

def str_op_test():
    str = "ab ee 33 24 "
    out_str = ""
    len = 0
    # print(f"""str:{str.strip(" ")}""")
    for elem in str:
        print(elem)
        print(type(elem))
        if elem == ' ':
            print("space")
        else:
            out_str += elem
    print(f"""str:{str} out_str:{out_str}""")

    # print(int('a' - 'A'))
if __name__ == '__main__':
    apk_log_mass_raw_data_op("D:\\qizhen\\新建文件夹\\phone_send9.txt")
    apk_log_mass_raw_data_op("D:\\qizhen\\新建文件夹\\watch_recv9.txt")
    # watch_log_mass_raw_data_op("D:\\qizhen\\新建文件夹\\watch_recv3.txt")
    # watch_log_mass_raw_data_op2("D:\\qizhen\\新建文件夹\\watch_recv7.txt")
    # str_op_test()