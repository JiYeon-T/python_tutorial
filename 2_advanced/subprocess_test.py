import subprocess
# Python的subprocess模块是用于创建和管理子进程的标准库工具，可以执行外部命令、连接输入输出管道并获取返回结果


def cmd_test():
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == '__main__':
    cmd_test()