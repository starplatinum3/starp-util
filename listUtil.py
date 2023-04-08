# 第二步输入“
# python怎么找出两个list中的相同元素-百度经验
# https://jingyan.baidu.com/article/925f8cb838da6c81dce05637.html

from collections import Counter

def append_all(lst,to_be_append):
    for item in to_be_append:
        lst.append(item)

# lst1 = [11, 22, 33]
# lst2 = [22, 33, 44]
# a = set(lst1)   # 转成元祖
# b = set(lst2)
# c = (a & b)  # 集合c和b中都包含了的元素
# print('两个列表中相同的元素是：', end='')
# for i in c:
#     print(i, end=' ')

def dup_in_two_list(lst1 = [11, 22, 33],lst2 = [22, 33, 44]):

    a = set(lst1)   # 转成元祖
    b = set(lst2)
    # print("a")
    # print(a)
    c = (a & b)  # 集合c和b中都包含了的元素
    # print('两个列表中相同的元素是：', end='')
    # for i in c:
    #     print(i, end=' ')
    return c

def remove_same(lst: list):
    ret_lst = []
    for item in lst:
        if item in ret_lst: continue
        ret_lst.append(item)
        # ret_lst.append(item)
        # pass
    return ret_lst
 

def find_same(a,b):
    same_list=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                # print(a[i])
                same_list.append(a[i])
    return same_list
    # ”代码，通过2层循环，来找出a和b两个列表相同的元素

# def find_same_in_one(a,b):
#     l = [1, 2, 3, 5]
#     l_one = [2, 8, 6, 10]
#     print set(l) & set(l_one)


# python list find same 
def find_same_in_one(a):
    # l = [1, 2, 3, 5]
    # l_one = [2, 8, 6, 10]
    # print set(l) & set(l_one)
    # a = [29,36,57,12,79,43,23,56,28,11,14,15,16,37,24,35,17,24,33,15,39,46,52,13]
    b = dict(Counter(a))
    return [key for key,value in b.items()if value > 1]
    # print ([key for key,value in b.items()if value > 1]) #只展示重复元素
    # print ({key:value for key,value in b.items()if value > 1}) #展现重复元素和重复次数


def list_same(list1, list2, list1_name=None, list2_name=None):
    if list1_name is None:
        list1_name="list1"
    if list2_name is None:
        list2_name="list2"
    not_in_list2 = []
    not_in_list1 = []
    for elm in list1:
        if elm not in list2:
            not_in_list2.append(elm)
    for elm in list2:
        if elm not in list1:
            not_in_list1.append(elm)

    # not_in_list1=[elm for elm in list2 and elm  not in list1]
    if len(not_in_list1)==0:
        print("可以凑出来")
    else:
        print("我们会得到:", list1, "。但是我们凑不出来:", not_in_list1, ",而且多凑出了:", not_in_list2)
        print("not in ", list1_name, "but in ", list2_name, ":", not_in_list1)
        print("not in ", list2_name, "but in ", list1_name, ":", not_in_list2)
    # print("not_in_list2 but in list1:",not_in_list2)


# list_same([1,2],[2,3])
import re


# def str_to_list(list_str="1 3 4 54"):
#     """
#     打印出列表里的数字然后粘贴到excel 然后转置
#     :param list_str:
#     :return:
#     """
#     result_list = re.split(r"[,\t 、]", list_str)
#     # result_list=[int(num.strip()) for num in result_list]
#     result = []
#     for num in result_list:
#         if num == "": continue
#         result.append(int(num.strip()))
#     # result_list.remove("")
#     return result

def str_to_list_re(list_str="1 3 4 54",split_by_re_str=r"[,\t 、，]"):
    # result_list=list_str.split(split_by)
    result_list = re.split(r"[,\t 、]", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for num in result_list:
        if num == "": continue
        result.append(int(num.strip()))
    # result_list.remove("")
    return result


def str_to_list(list_str: str = "1 3 4 54", split_by: str = " ") -> list:
    """
    打印出列表里的数字然后粘贴到excel 然后转置
    :param list_str:
    :return:
    """
    result_list=list_str.split(split_by)
    # result_list = re.split(r"[,\t 、]", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for num in result_list:
        if num == "": continue
        result.append(int(num.strip()))
    # result_list.remove("")
    return result


def str_rets_kind_to_list(list_str="1 3 4 54"):
    """
    linkArticle=
    1237071659
    1237072629
    1237068750
    1237068752
    1237070693
    1237069773
    1237072630
    1237068753
    1237067810
    1237071660

    D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\moocLinksGet.py"
    ['1237071659', '1237072629', '1237068750', '1237068752', '1237070693', '1237069773', '1237072630', '1237068753', '1237067810',
    '1237071660']
    """
    list_str=list_str.strip()
    result_list = re.split("\n", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for line in result_list:
        if line == "":
            continue
        result.append(line.strip())
    # result_list.remove("")
    return result


# listUtil.py
def remove_all(lst: list, what):
    ret_lst = []
    for item in lst:
        # https://www.cnblogs.com/jiyongjia/p/9539024.html
        if what == item: continue
        # print("what",what)
        # print("item",item)
        ret_lst.append(item)
        # ret_lst.append(item)
        # pass
    return ret_lst

# python 判断字符串是 空，空格
# https://www.itranslater.com/qa/details/2127291587607659520
def remove_none(lst: list):
    """
    item.isspace()
    """
    ret_lst = []
    for item in lst:
        # https://www.cnblogs.com/jiyongjia/p/9539024.html
        # if item is None:
        #     continue
        # if item =="":
        #     continue
        if not item or item.isspace():
            continue

        # if what == item: continue
        # print("what",what)
        # print("item",item)
        ret_lst.append(item)
        # ret_lst.append(item)
        # pass
    return ret_lst

if __name__=="__main__":
    # import listUtil
    # print(help(listUtil))
    article="""
    _id	CompanySize	_class	companyIndustry	companyIntroduction	companyLink	companyName	companyNature	detailedPlaceWork	jobDescription	jobLink	jobTitle	minimumEducation	monthlySalary	natureWork	numberRecruits	placeWork	releaseDate	typeRecruitment	workExperience"""
    should_words=article.split(" ")
    # lst=[]
    should_words=remove_none(should_words)
    have_words_map={
    "companyName": "中国中车",
    "companyDesc": "国企",
    "label": "工作地点：",
    "jobName": "软件开发设计师",
    "salary": "1-1.5万",
    "detailedPlaceWorkInfo": "北京|在校生/应届生|硕士",
    "companyIndustry": "机械/设备/重工",
    "releaseDate": "03-14发布",
    "companyLink": "https://jobs.51job.com/all/coVjcFZ189VmsGZAxoAmI.html",
    "jumpLink": "https://jobs.51job.com/beijing/146167436.html?s=sou_sou_soulb&t=0_1&req=0d08df993f42a4e2c4505e1923e7b06c",
    "jobLink": "https://jobs.51job.com/beijing/146167436.html?s=sou_sou_soulb&t=0_1&req=0d08df993f42a4e2c4505e1923e7b06c",
    "detailedPlaceWork": "北京",
    "typeRecruitment": "在校生/应届生",
    "minimumEducation": "硕士",
    "companyNature": "国企"
    }
    have_words=have_words_map.keys()
    list_same(list1=should_words,list2=have_words)
