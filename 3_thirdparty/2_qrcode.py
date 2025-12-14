import os


def qrcode_test():
    """qrcode"""

    import qrcode # TODO: qrcode
    import io

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def make_qrcoe(url):
        """
        生成二维码
        :param url: 需要生成二维码的url
        :return: 返回图片字节流
        """
        image = qrcode.make(url)
        buffer = io.BytesIO()
        image.save(buffer, 'png')
        return buffer.getvalue()

    def make_qrcode(url, image_name):
        image = qrcode.make(url)
        save_path = os.path.join(BASE_DIR, image_name)
        image.save(save_path)
        return

    # make_qrcoe("www.baidu.com")
    make_qrcode("www.baidu.com", "baidu.png")

if __name__ == '__main__':
    qrcode_test()