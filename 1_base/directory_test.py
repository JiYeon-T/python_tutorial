
import os


def curr_directory_test():
    PROJECT_DIR = os.getcwd() # \
    CURR_FILE = __file__ # /
    CURR_DIR = os.path.dirname(__file__) # 所有都是用绝对路径, 而不再使用相对路径
    RES_DIR = os.path.join(CURR_DIR, "abc", "test2.txt")
    print(PROJECT_DIR)
    print(CURR_FILE)
    print(CURR_DIR)
    print(RES_DIR)

if __name__ == '__main__':
    curr_directory_test()
