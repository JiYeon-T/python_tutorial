import re

# 正则表达式
# https://www.runoob.com/python3/python3-reg-expressions.html
# 测试网站：
# https://tool.oschina.net/regex/

def reg_exp_test1():
    """"""
    def match_test():
        pos = re.match("www", "www,baidu.com")  # 在起始位置匹配
        print(f"{pos} type:{type(pos)}", end="\n")
        print(pos.span())
        # 仅从起始位置开始匹配
        # 函数只从字符串的起始位置进行匹配;，如果模式在开头不匹配，就立即返回 None`，不再检查字符串的其余部分。‌
        pos = re.match("com", "www,baidu.com")
        print(pos, end="\n\n")
        # pos = re.search("com", "www,baidu.com")  # re.search 扫描整个字符串并返回第一个成功的匹配。(可以搜索到)
        # print(pos, end="\n\n")

        line = "Cats are smarter than dogs"
        # line = "Cats are smarter than"
        # line = "Cats are smarter"
        # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
        # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
        matchobj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
        print(matchobj)
        print(matchobj.span(), end="\n\n")
        # start_pos, end_pos = matchobj.span()  # 返回搜索到的有效字符串索引: start_idx, end_idx
        # print(line[start_pos: end_pos])

        # group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
        # groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
        if matchobj:
            print(matchobj.groups())
            print(matchobj.group())
            print(matchobj.group(1))
            print(matchobj.group(2))
            print(matchobj.group(1, 2), end="\n\n")
        else:
            print("No matched")

        # search:
        print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
        print(re.search('com', 'www.runoob.com').span(), end="\n\n")  # 不在起始位置匹配

        # flag:
        # 在Python正则表达式中，re.M 和 re.I 是两种常用的标志修饰符，用于改变匹配行为。
        # re.I（忽略大小写, 等同于 re.IGNORECASE）‌：使匹配过程对大小写不敏感，
        # 例如： 使用 re.I 标志时，正则表达式 r'TM' 能匹配字符串中的 'tm' 或 'TM'。‌
        # re.M（多行模式, 等同于 re.MULTILINE）‌：将字符串视为多行，从而让 ^ 匹配每行的行首，$ 匹配每行的行尾，
        # 例如在包含换行符的字符串中，re.M 可确保 ^ 和 $ 分别匹配每一行的边界而非整个字符串的单一开头和结尾。‌

        line = "Cats are smarter than dogs"
        searchobj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
        if searchobj:
            print("searchObj.group() : ", searchobj.group())
            print("searchObj.group(1) : ", searchobj.group(1))
            print("searchObj.group(2) : ", searchobj.group(2), end="\n\n")
        else:
            print("Nothing found!!")

        # re.match 与 re.search的区别
        # re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
        # 而 re.search 匹配整个字符串，直到找到一个匹配或者匹配失败。
        line = "Cats are smarter than dogs"

        matchobj = re.match(r'dogs', line, re.M | re.I)
        if matchobj:
            print("match --> matchObj.group() : ", matchobj.group())
        else:
            print("Nothing matched!!")

        matchobj = re.search(r'dogs', line, re.M | re.I)
        if matchobj:
            print("search --> matchObj.group() : ", matchobj.group())
        else:
            print("Nothing matched!!")

    def substitute():
        """
        检索和替换
        Python 的re模块提供了re.sub用于替换字符串中的匹配项。
        语法：
        re.sub(pattern, repl, string, count=0, flags=0)
        参数：
        pattern : 正则中的模式字符串。
        repl : 替换的字符串，也可为一个函数。
        string : 要被查找替换的原始字符串。
        count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
        flags : 编译时用的匹配模式，数字形式。
        """
        # $
        # 在正则表达式中，符号 $ 是一个元字符，用于匹配字符串的‌结束位置‌。‌
        # 2 它不匹配具体的字符，而是匹配一个位置——即字符串末尾的边界。‌
        # ‌基本用法：‌
        # 当 $ 出现在正则表达式末尾时，表示被匹配的模式必须出现在字符串的结尾。例如：
        # 正则表达式 abc$ 会匹配以 abc 结尾的字符串，如: xyzabc，但不会匹配 abcxyz 或 xabcx。‌
        # 在编程语言（如Python、JavaScript）或工具（如Excel）中，常用于精确匹配或验证输入，例如检查邮箱是否以特定域名结尾。‌
        # ‌与其他符号的组合：
        # 常与脱字符 ^‌（匹配字符串开头）结合使用，以确保整个字符串完全匹配某个模式。
        # 例如：^abc$ 只匹配完全等于 abc 的字符串，不允许前后有其他字符。‌
        # 如果字符串包含换行符（在多行模式下），‌$ 会匹配每个行尾的位置。‌
        # ‌特殊上下文中的用法：‌ 在字符串替换操作中 $ 后跟数字（如 &1‌、‌$2‌）有不同含义，用于引用正则表达式中捕获组的内容，
        # 但这与匹配结尾位置的功能无关。‌

        phone_num = "2004-959-559 # 这是一个电话号码"
        phone_num = re.sub(r'#.*$', "", phone_num)  # 删除注释
        print(phone_num)

        # \d 与 \D
        # 在正则表达式中，\d 是一个‌预定义字符类‌，用于匹配任何一个‌十进制数字字符‌（即0到9之间的任意单个数字），
        # 其功能等价于字符范围 [0-9]。‌
        # ‌它属于元字符的一种，‌ 在模式匹配中常用于快速识别数字，
        # 例如在验证电话号码或日期格式时；与之相关的反向类 \D 则匹配‌非数字字符

        phone_num = re.sub('\D', "", phone_num)  # 移除非数字的内容
        print(phone_num, end="\n\n")

        # repl 可以传入一个函数:
        # 例如:匹配字符串中数字的部分并 * 2
        def double(matched):
            value = int(matched.group('value'))
            return str(value * 2)

        # 圆括号 () 的功能有本质区别。‌ 圆括号主要用于‌分组‌和‌捕获‌，即把子表达式组合在一起以便引用或应用量词
        s = 'A23G4HFD567'
        s = re.sub(r'(?P<value>\d+)', double, s)
        print(s, end="\n\n")

    def compile_test():
        """
        compile 函数
        compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
        语法格式为：re.compile(pattern[, flags])
        参数：
        pattern : 一个字符串形式的正则表达式
        flags 可选，表示匹配模式，比如：忽略大小写，多行模式等，具体参数为：
        re.IGNORECASE 或 re.I - 使匹配对大小写不敏感
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.MULTILINE 或 re.M - 多行模式，改变 ^ 和 $ 的行为，使它们匹配字符串的每一行的开头和结尾。
        re.DOTALL 或 re.S - 使 . 匹配包括换行符在内的任意字符。
        re.ASCII - 使 \w, \W, \b, \B, \d, \D, \s, \S 仅匹配 ASCII 字符。
        re.VERBOSE 或 re.X - 忽略空格和注释，可以更清晰地组织复杂的正则表达式。
        这些标志可以单独使用，也可以通过按位或（|）组合使用。例如，re.IGNORECASE | re.MULTILINE 表示同时启用忽略大小写和多行模式。
        """
        pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
        m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
        print(m)
        m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
        print(m)
        m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
        print(m)
        print(f"group:{m.group()} start:{m.start()} end:{m.end()} span:{m.span()}")

        s = pattern.search('one12twothree34four')  # 搜索
        print(s.span(), end="\n\n")

        pattern = re.compile(r'([a-z]+) ([a-z]+)', re.IGNORECASE)
        # pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
        m = pattern.match('Hello World World Web')
        print(m)
        print(f"group:{m.group()} group:{m.group(0), m.group(1)} start:{m.start()} end:{m.end()} span:{m.span()}")

    def findall_test():
        """
        在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
        注意： match 和 search 是匹配一次 findall 匹配所有。

        语法格式为：
        re.findall(pattern, string, flags=0)
        或
        pattern.findall(string[, pos[, endpos]])
        参数：
        pattern 匹配模式。
        string 待匹配的字符串。
        pos 可选参数，指定字符串的起始位置，默认为 0。
        endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
        """
        m = re.findall(r'\d+', 'runoob 123 google 456')  # 查找数字
        print(m)
        pattern = re.compile(r'\d+')  # 查找数字
        m = pattern.findall('runoob 123 google 456')
        print(m)
        m = pattern.findall('runoob 123 google 456', 0, 10)  # 指定匹配区间
        print(m, end="\n\n")

        # re.finditer
        # 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
        it = re.finditer(r"\d+", "runoob 123 google 456")
        for match in it:
            print(match.group())
        print("\n\n")

        # split
        # split 方法按照能够匹配的子串将字符串分割后返回列表，

        # 为什么用 \w
        # ‌简化匹配‌：相当于写 [a-zA-Z0-9_]，但更简洁。比如匹配用户名或变量名时，\w+ 能快速抓取类似 user_123 的字符串。‌‌
        # ‌区分大小写‌：\w 默认区分大小写（如 A 和 a 不同），但部分语言（如 Python）可通过设置忽略
        m = re.split(r'\W+', 'runoob,runoob,runoob.hello')
        print(m)
        m = re.split(r'(\W+)', 'runoob,runoob,runoob.hello,123455,111_____.....//..??..,,')  # [a-zA-Z0-9_]
        print(m)

    def kuohao_test():
        """使用不不使用 () 的区别 - 捕获分组"""
        string = 'Words, words, words.'
        m = re.split(r'(\W+)', string)  # 捕获分组
        print(m)
        m = re.split(r'\W+', string)
        print(m)
        m = re.split(r'(?:\W+)', string)  # 非捕获组：
        print(m)

        # 核心区别在于‌捕获分组‌的使用，这会影响返回结果中是否包含分隔符本身。‌
        # ‌使用捕获分组时，分隔符会被包含在结果中：‌ 当正则表达式模式包含括号形成的捕获分组（如(\W +)）时，
        # re.split() 会将匹配到的分隔符文本也作为独立元素插入到结果列表中。
        # 例如：
        text = "Words, words, words."
        result1 = re.split(r'(\W+)', text)
        print(result1)  # 输出: ['Words', ', ', 'words', ', ', 'words', '.', '']
        # 这里，re.split()
        # 不仅分割字符串，还保留了匹配的标点符号和空格（如 ', ' 和 '.'）作为列表元素。‌

        # ‌不使用捕获分组时，分隔符(没有匹配到的部分)会被移除：‌ 如果模式中没有捕获分组（如 \W +），re.split()
        # 仅根据分隔符位置进行切割，并将分隔符本身从结果中移除。例如：
        result2 = re.split(r'\W+', text)
        print(result2)  # 输出: ['Words', 'words', 'words', '']
        # 结果中只包含分割后的文本部分，所有标点符号和空格均被过滤掉。‌
        # ‌如果需要保留分组但不包含分隔符，可以使用非捕获组：‌ 通过(?:) 语法定义非捕获组，
        # 可以实现分组的逻辑分组功能（如多分隔符匹配），同时避免将匹配的分隔符插入结果列表。
        # 例如：
        result3 = re.split(r'(?:\W+)', text)
        print(result3)  # 输出: ['Words', 'words', 'words', '']
        # 这提供了更灵活的控制，适用于复杂模式匹配场景。‌

    def flag_options_test():
        """
        正则表达式修饰符 - 可选标志
        正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
        以下标志可以单独使用，也可以通过按位或（|）组合使用。
        例如，re.IGNORECASE | re.MULTILINE 表示同时启用忽略大小写和多行模式。
        可选参数:
        re.IGNORECASE 或 re.I	使匹配对大小写不敏感
        re.MULTILINE 或 re.M	多行匹配，影响 ^ 和 $，使它们匹配字符串的每一行的开头和结尾。
        re.DOTALL 或 re.S：	使 . 匹配包括换行符在内的任意字符。
        re.ASCII	使 \w, \W, \b, \B, \d, \D, \s, \S 仅匹配 ASCII 字符。
        re.VERBOSE 或 re.X	忽略空格和注释，可以更清晰地组织复杂的正则表达式。
        """
        pass


    def pattern_options():
        """
        正则表达式模式
        模式字符串使用特殊的语法来表示一个正则表达式。
        字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
        多数字母和数字前加一个反斜杠时会拥有不同的含义。
        标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
        反斜杠本身需要使用反斜杠转义。
        由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。
        下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。
        模式	描述
        ^	匹配字符串的开头
        $	匹配字符串的末尾。
        .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
        [...]	用来匹配所包含的任意一个字符，例如 [amk] 匹配 'a'，'m'或'k'
        [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
        re*	匹配0个或多个的表达式。
        re+	匹配1个或多个的表达式。
        re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
        re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
        re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
        re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
        a| b	匹配a或b
        (re)	匹配括号内的表达式，也表示一个组
        (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
        (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
        (?: re)	类似 (...), 但是不表示一个组
        (?imx: re)	在括号中使用i, m, 或 x 可选标志
        (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
        (?#...)	注释.
        (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
        (?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
        (?> re)	匹配的独立模式，省去回溯。
        \w	匹配数字字母下划线
        \W	匹配非数字字母下划线
        \s	匹配任意空白字符，等价于 [\t\n\r\f]。
        \S	匹配任意非空字符
        \d	匹配任意数字，等价于 [0-9]。
        \D	匹配任意非数字
        \A	匹配字符串开始
        \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
        \z	匹配字符串结束
        \G	匹配最后匹配完成的位置。
        \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
        \B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
        \n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
        \1...\9	匹配第n个分组的内容。
        \10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
        正则表达式实例
        字符匹配
        实例	描述
        python	匹配 "python".
        字符类
        实例	描述
        [Pp]ython	匹配 "Python" 或 "python"
        rub[ye]	匹配 "ruby" 或 "rube"
        [aeiou]	匹配中括号内的任意一个字母
        [0-9]	匹配任何数字。类似于 [0123456789]
        [a-z]	匹配任何小写字母
        [A-Z]	匹配任何大写字母
        [a-zA-Z0-9]	匹配任何字母及数字
        [^aeiou] 除了aeiou字母以外的所有字符
        [^0-9]	匹配除了数字外的字符
        特殊字符类
        实例	描述
        .	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
        \d	匹配一个数字字符。等价于 [0-9]。
        \D	匹配一个非数字字符。等价于 [^0-9]。
        \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
        \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
        \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
        \W	匹配任何"非"单词字符。等价于 '[^A-Za-z0-9_]'。

        """
        pass

    def reg_expression_test():
        """"""
        # [ ]：方括号。匹配需要的字符集合，如[1-3]或[123]都是匹配1、2或者3,
        m = re.match(r'[1-4]', "123456789")  # 只匹配一个字符
        print(m.group())
        m = re.match(r'[1-4]+', "123456789")  # 匹配多个字符
        print(m.group())
        m = re.search(r'[1234]+', "123456789")
        print(m.group())

        # 2、^：脱字符号。方括号中加入脱字符号，就是匹配未列出的所有其他字符，如[^a]匹配除a以外的所有其他字符。
        # 3、\：反斜杠。和python字符串使用规则一样，可以匹配特殊字符本身，
        # 如\d表示匹配0到9的任意一个数字字符，而\\d则表示匹配\d本身。
        # 4、*：星号。匹配前一个字符0到n次，如pytho*n可以匹配pythn、pytoon、pythooooon等。
        # 还有其它匹配重复字符的如？、+或{m,n}，其中{n,m}可以灵活使用，它表示匹配n次到m次。

    # match_test()
    # substitute()
    # compile_test()
    # findall_test()
    # kuohao_test()
    reg_expression_test()


def reg_exp_test2():
    """
    命名捕获组:
    re.sub('(?P<value>\d+)', ...) 是 Python re模块中用于字符串替换的正则表达式用法，
    其中 (?P<value>\d+) 是一个‌命名捕获组‌，用于匹配一个或多个连续数字，并将匹配结果命名为 'value'，以便在替换过程中引用。‌
    ‌参数说明：‌ re.sub() 的基本语法为 re.sub(pattern, repl, string, count=0, flags=0)，
    其中 pattern='(?P<value>\d+)' 定义匹配规则:
    "re.sub repl参数"}（替换内容）可以是字符串或函数，
    string 是待处理的原始字符串，
    count 指定最大替换次数（默认0表示替换所有匹配项），
    flags用于修改匹配行为（如re.IGNORECASE`）。‌

    ‌核心功能与用法：‌
    该正则表达式的核心功能是匹配数字序列并支持动态替换。
    命名捕获组 (?P<value>\d+) 中，?P<value> "为匹配内容分配名称 value"，
    \d+ 匹配一个或多个数字；替换时可通过 repl 参数引用此组，
    例如使用字符串替换时用 \g<value> 或 \1（反向引用），或使用函数动态处理匹配内容。‌
    ‌应用场景：‌
    此用法常见于数据清洗、文本预处理等场景，
    例如格式化数字（如日期、价格）、敏感信息脱敏（如隐藏身份证号部分数字）或条件替换（如根据匹配内容动态生成替换文本）
    """
    # 具体示例如下：
    # ‌字符串替换‌：将数字替换为带括号的形式。
    text = "Price: 100 dollars, discount: 20%"
    result = re.sub(r'(?P<value>\d+)', r'[\g<value>]', text)
    print(result, end="\n\n")  # 输出: Price: [100] dollars, discount: %

    # ‌函数替换‌：通过函数对匹配数字进行计算（如平方）。
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)
    text = "Numbers: 3, 5, 777"
    result = re.sub(r'(?P<value>\d+)', double, text)
    print(result)  # 输出: Numbers: 6, 10, 14


def change_date_format():
    """改变日期的格式，如中国格式 2017-11-27 改为美国格式 11/27/2017:"""
    s = '2017-11-21'
    # NOTE:这种写法 bug 太多了。。。
    s2 = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
    print(s, s2)


def match_ip():
    """
    \. 转义机制通过反斜杠 \ 实现‌，反斜杠告诉正则表达式引擎将下一个字符视为普通字符。
    因此，\. 在模式中专门用于匹配点号本身
    """
    # ip = 'IP address:192.168.1.1 that end'
    ip = 'IP address:255.255.255.255 that end'
    trueIp = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}'
                       r'(25[0-5]|2[0-4]\d|[01]{0,1}\d{0,1}\d)', ip)
    print(trueIp.group())

    # 简化正则 {0,1} 等价于问号 ?
    trueIp = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}'
                       r'(25[0-5]|2[0-4]\d|[01]?\d?\d)', ip)
    print(trueIp.group())


def match_mac_from_str():
    """
    MAC:54:2f:04:0d:0e:b9^BSN:AA010556A25B0611112^MMI2:Na
    """
    input1 = 'MAC:54:2f:04:0d:0e:b9^BSN:AA010556A25B0611112^MMI2:Na'
     # TODO: 匹配结果为什么多了一个 0e
    # ('54:2f:04:0d:0e:b9', '0e:', 'AA010556A25B0611112', 'Na')
    pattern = re.compile(r'MAC:((\w\w:){5}\w\w)'
                         r'\^BSN:([0-9a-fA-F]{19})'
                         r'\^MMI2:(\w+)',
                         re.IGNORECASE | re.MULTILINE)
    m = pattern.search(input1)
    print(m.groups(), end="\n\n")
    # print(m.start(), m.end())
    # for elem in pattern.finditer(input1):
    #     print(elem.group())
    # print(m.group(0), m.group(1), m.group(2), sep='\n')


if __name__ == '__main__':
    # reg_exp_test1()
    # reg_exp_test2()
    # change_date_format()
    # match_ip()
    match_mac_from_str()