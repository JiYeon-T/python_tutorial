import markdown

# Python 可以使用 markdown 模块将 Markdown 文本转换为 HTML。
# https://python-markdown.github.io/
# https://www.markdownguide.org/


def basic_test():
    # 定义 Markdown 文本
    md_text = """
    # 这是标题
    这是 **加粗** 的文本。
    这是 *斜体* 的文本。

    - 列表项 1
    - 列表项 2

    [点击这里](https://www.runoob.com) 访问网站。
    """

    # 转换为 HTML
    html_output = markdown.markdown(md_text)

    # 输出 HTML
    print(html_output)


def conver_markdown_to_html(markdown_path, html_path):
    # 读取 Markdown 文件
    with open(markdown_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # 将 Markdown 转换为 HTML
    html = markdown.markdown(markdown_text)

    # 将 HTML 写入文件
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(html)

    print("Markdown 文件已成功转换为 HTML 文件！")

    # 扩展功能
    # markdown
    # 库支持多种扩展，例如表格、代码高亮等。你可以通过以下方式启用扩展：
    # html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

if __name__ == '__main__':
    # basic_test()
    conver_markdown_to_html('test.md', 'test_html.html')