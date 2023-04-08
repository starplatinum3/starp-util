
import re
def find_chinese(file):

     pattern = re.compile(r'[^\u4e00-\u9fa5]')

     chinese = re.sub(pattern, '', file)

    #  print(chinese)
     return chinese

 

def find_english(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    english = re.sub(pattern, '', file)
    print(english)

 
 
def camel_to_underscore(name,):
    '''
    将参数名的驼峰形式转为下划线形式
    @param params:
    @return:
    '''
    new_name = ""
    name += " "  # 为了防止数据溢出
    for i in range(len(name) - 1):
        if i == 0:
            new_name += name[i]
        elif name[i].isupper() and name[i - 1].islower():
            new_name += "_" + name[i]
        # 如果不在前面加上name += " "，这里会索引越界
        elif name[i].isupper() and name[i - 1].isupper() and name[i + 1].islower():
            new_name += "_" + name[i]
        else:
            new_name += name[i]
    return  new_name

def camel_to_underscore_lower(name,):
    '''
    将参数名的驼峰形式转为下划线形式
    @param params:
    @return:
    '''
    name=camel_to_underscore(name)
    return  name.lower()

def eng_to_underscore_lower(name,):
    '''
    将参数名的驼峰形式转为下划线形式
    @param params:
    @return:
    '''
    name=camel_to_underscore(name)
    # -
    return  name.lower().replace(" ","_").replace(':','').replace(',','').replace('-','_')




# https://blog.csdn.net/mouday/article/details/81512870
def contains_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False



def back_del_str(old_str, dont_want):
    if dont_want == "":
        return old_str
    old_str_len = len(old_str)
    dont_want_len = len(dont_want)
    i_old = old_str_len - 1
    i_dont = dont_want_len - 1

    i_res = old_str_len
    i_now = old_str_len
    while 1:
        if not old_str[i_old] == dont_want[i_dont]:
            return old_str[:i_res]
        i_now -= 1
        if i_res - i_now == dont_want_len:
            i_res -= dont_want_len
        if i_dont == 0 or i_old == 0:
            return old_str[:i_res]

        i_old -= 1
        i_dont -= 1


def front_del_str(old_str, dont_want):
    if dont_want == "":
        return old_str
    old_str_len = len(old_str)
    dont_want_len = len(dont_want)
    min_len = min(old_str_len, dont_want_len)
    i_old = 0
    i_dont = 0

    i_res = 0
    i_now = 0
    while 1:
        if not old_str[i_old] == dont_want[i_dont]:
            return old_str[i_res:]
        i_now += 1
        # 1234
        # 12
        if i_now - i_res == dont_want_len:
            i_res += dont_want_len
        if i_dont == min_len - 1 or i_old == min_len - 1:
            return old_str[i_res:]

        i_old += 1
        i_dont += 1


# https://zhuanlan.zhihu.com/p/93671522


def camel(s):
    s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]


import re


def to_camel_case(x):
    """转驼峰法命名"""
    return re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)


def to_upper_camel_case(x):
    """转大驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].upper() + s[1:]


def to_lower_camel_case(x):
    """转小驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].lower() + s[1:]


# ————————————————
# 版权声明：本文为CSDN博主「nie303671298」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/nie303671298/article/details/108146480


if __name__=="__main__":
    pass

    print(to_camel_case('UserLoginCount'))  # UserLoginCount
    print(to_camel_case('userLoginCount'))  # userLoginCount
    print(to_camel_case('user_login_count'))  # userLoginCount
    print()

    print(to_upper_camel_case('UserLoginCount'))  # UserLoginCount
    print(to_upper_camel_case('userLoginCount'))  # UserLoginCount
    print(to_upper_camel_case('user_login_count'))  # UserLoginCount
    print()

    print(to_lower_camel_case('UserLoginCount'))  # userLoginCount
    print(to_lower_camel_case('userLoginCount'))  # userLoginCount
    print(to_lower_camel_case('user_login_count'))  # userLoginCount


    chinese_article="""
    cherry
    樱桃
    watermelon
    西瓜
    grape
    葡萄
    honey
    peach水蜜桃
    mango芒果
    pomegranate石榴
    plum李子
    pomelo柚子
    olive橄榄
    litchi荔枝
    lemon柠檬
    longan龙眼
    coconut椰子
    sugarcane甘蔗
    haw/hawthorn
    山楂
    chestnut栗子
    persimmon柿子
    guava
    番石榴
    almond杏仁
    等等
    """

    chinese_article="""
    Seeds: 瓜子



    To shell seeds: 剝壳、嗑瓜子



    Dried fish：鱼片干



    Dried cuttlefish: 鱿鱼丝



    Animal parts：内脏



    Duck tongues: 鸭舌头



    Duck wings: 鸭翅膀



    Spicy gluten: 辣条



    Seaweed: 海苔"""
    chinese_lines=chinese_article.split("\n")

    chinese_word_list=[]
    for chinese_line in chinese_lines:
        if chinese_line =="":
            continue
        chinese_word=find_chinese(chinese_line)
        if chinese_word is None:
            continue
        if chinese_word.isspace():
            continue
        if chinese_word =="":
            continue
        # print(chinese_word)
        chinese_word_list.append(chinese_word)

    print(chinese_word_list)
    # find_chinese("""
    # cherry
    # 樱桃
    # watermelon
    # 西瓜
    # grape
    # 葡萄
    # honey
    # peach水蜜桃
    # mango芒果
    # pomegranate石榴
    # plum李子
    # pomelo柚子
    # olive橄榄
    # litchi荔枝
    # lemon柠檬
    # longan龙眼
    # coconut椰子
    # sugarcane甘蔗
    # haw/hawthorn
    # 山楂
    # chestnut栗子
    # persimmon柿子
    # guava
    # 番石榴
    # almond杏仁
    # 等等
    # """)