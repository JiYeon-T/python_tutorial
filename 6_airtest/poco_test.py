# -*- encoding=utf8 -*-
__author__ = "qz"

from airtest.core.api import *
from airtest.core.android import Android
from poco.exceptions import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def poco_api_test():
    """
    https://poco.readthedocs.io/zh-cn/latest/source/poco.proxy.html#poco.proxy.UIObjectProxy
    """
    dev = Android(serialno='SWF6HMQ44XGQHYTS')
    dev.start_app(package="win.lcfactory.bluetooth")
    sleep(3)
    poco = AndroidUiautomationPoco(use_airtest_input=True,
                                   screenshot_each_action=False) # Android porject
    poco.device.wake()

    search_text = poco(name="win.lcfactory.bluetooth:id/et_client_filter")
    if not search_text.exists():
        print("search_text not exist")
        return

    start_search_btn = poco(text="重新扫描")
    if not start_search_btn.exists():
        print("start_search_btn not exist")
        return

    dev_list = poco(name="win.lcfactory.bluetooth:id/rv_bt")
    if not dev_list.exists():
        print("list not exist")
        return

    print('text:{}'.format(dev_list.get_text()))
    print('len:{}'.format(len(dev_list.children())))
    print('attr type:{}'.format(dev_list.attr('type')))
    print('attr position:{}'.format(dev_list.attr('position')))
    print('attr size:{}'.format(dev_list.attr('size')))
    print('attr visible:{}'.format(dev_list.attr('visible')))
    print('attr name:{}'.format(dev_list.attr('name')))
    print('attr name:{}'.format(dev_list.get_name()))

    start_search_btn.click(focus=[0.2 ,0.5], sleep_interval=3)
    start_search_btn.double_click(focus=[0.2 ,0.5], sleep_interval=3)
    start_search_btn.long_click(duration=3)

    # Get a new UI proxy copy with the given focus. Return a new UI proxy object as the UI proxy is immutable.
    print('focus type:'.format(type(start_search_btn.focus([0.5, 0.5]))))
    print('bounding:'.format(start_search_btn.get_bounds()))

    print("parent name:".format(start_search_btn.parent().get_name()))
    #     print("offspring name:".format(start_search_btn.offspring().get_name()))
    #     pinch()

    dev_list.scroll(direction='vertical', percent=0.6, duration=1.0)
    sleep(2)
    dev_list.swipe(direction='down', focus=[0.5, 0.5], duration=0.5)

    # wait
#     wait()
#     wait_for_appearance()
#     wait_for_disappearance()



if __name__ == '__main__':
    poco_api_test()