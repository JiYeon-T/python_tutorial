g_thread_list = []

# 其它文件引用这个文件的时候要注意:
# 要使用:from thread_test import variables 这种方式
# 而不是直接导入变量:from thread_test.variables import g_threa_list 这种方式, 这种方式，其它文件修改了这个变量也看不到

