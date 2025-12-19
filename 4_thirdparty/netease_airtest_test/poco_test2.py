from airtest.core.api import *
from airtest.cli.parser import cli_setup
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

if not cli_setup():
        auto_setup()

def unity3d_poco_test():
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()


def poco_api_test():
    """poco
    https://poco.readthedocs.io/zh-cn/latest/index.html"""
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    auto_setup(basedir=__file__,
               devices=["Android://127.0.0.1:5037/SWF6HMQ44XGQHYTS"],
               logdir=True,
               project_root=__file__, compress=10)
    print("file path:", __file__)
    dev = device()  # Return the current active device.
    print("device:{} type:{}".format(dev, type(dev)))
    print("resolution:", dev.get_current_resolution())

    poco = AndroidUiautomationPoco()
    poco.device.wake()
    #     poco(name='飞书').click()
    #     poco(text="点击选择AT指令").click()
    poco(text='重新扫描').click()
    #     poco(text='重新扫描').long_click(duration=2)
    not_exist_widget = poco(text='不能存在的 button')
    if not_exist_widget.exists():
        print("Exist")
    else:
        print("Not Exist")
    sleep(1)

    filter_btn = poco(name='win.lioil.bluetooth:id/et_client_filter')
    if filter_btn.exists():
        pos = filter_btn.get_position()
        print("pos:{}".format(pos))
        print("text:{}".format(filter_btn.get_text()))  # => 'xxxx'
        print("text:{}".format(filter_btn.attr('text')))  # => 'xxxx'
        print("type:{}".format(filter_btn.attr('type')))  # => 'Text'
        print("texture:{}".format(filter_btn.attr('Note_Exist_attr')))  # => None. Because there is no texture on Text.
        sleep(5)
        filter_btn.set_text("AABBCC:{}".format(*pos))  # very fast???????
        sleep(1)
    search_btn = poco(text='重新扫描')
    if search_btn.exists():
        search_btn.click()
        sleep(1)
    else:
        print('search btn not exist')


if __name__ == '__main__':
    poco_api_test()
