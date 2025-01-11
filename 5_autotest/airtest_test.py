# _*_ encoding=utf8 _*_
__author__ = "AirtestProject"
__desc = """
纯 Airtest 脚本 -- 网易云音乐
1. 进入网易云音乐
2.找到指定的薛之谦的歌曲
3.回到首页
4.进入抖音歌曲排行榜
5.完整运行上面脚本并统计运行时长
"""
# 网易 airtest 自动测试库练习
# airtest 基于图像比较实现自动测试的目的
# 1. airtest-selenium 库用于网页测试, 需要的时候再学习
# 2. 把 poco 卸载掉, 仅保留 pocoui
# 3. 提醒工人, 不需要进行升级的时候就把 USB hub 拔掉，因为否则很容易出现电池鼓包之类的问题 -> 电源可软件控制的 USB hub
# 4. 自动测试 + jenkins 实现 CI 功能, 不再需要研发手动冒烟测试 （a.提升产品质量; b.节约人力）
# 5. 网易的整套云自动化测试解决方案内部实践数据:应用项目 50+，脚本数量:2000+, 设备运行...

from airtest.core.api import *
import time,datetime


# 进入网易云音乐
def enter_cloud_music():
    """"""

touch()
snapshot()
swipe()
text()
keyevent()
snapshot()
sleep()
assert_exists()
assert_not_exists()


if __name__ == '__main__':
    pass