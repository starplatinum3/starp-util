def duplicate_removal( A, B):
    """
    交集  而不是去掉重复的
    两个列表的交集
    :param A:
    :param B:
    :return:
    """
    return set(A).intersection(set(B))

def append_all( lst, to_be_add):
 
    for i in to_be_add:
        lst.append(i)

def same_of_two( A, B):
    """
    交集  而不是去掉重复的
    两个列表的交集
    :param A:
    :param B:
    :return:
    """
    return set(A).intersection(set(B))

def intersection_of_two_list( A, B):
    """
    两个列表的交集
    :param A:
    :param B:
    :return:
    """
    return set(A).intersection(set(B))

def intersection_info( A, B):
    """
    两个列表的交集
    :param A:
    :param B:
    :return:
    """
    intersection_of_two_list_res=intersection_of_two_list(A, B)
    a_more_list=[]
    b_more_list=[]
    for list1Item in A:
        if list1Item not in intersection_of_two_list_res:
            # print(list1Item)
            a_more_list.append(list1Item)
    for list1Item in B:
        if list1Item not in intersection_of_two_list_res:
            # print(list1Item)
            b_more_list.append(list1Item)
    return intersection_of_two_list_res,a_more_list,b_more_list


#     【超简便的Python】 提取两个列表的共同元素_大气层煮月亮的博客-CSDN博客_python两个列表找相同
# https://blog.csdn.net/qq_51831335/article/details/126557879



def list_same(list1, list2, list1_name=None, list2_name=None):
    """
    可以凑出来什么 不能凑出来什么
    :param list1:
    :param list2:
    :param list1_name:
    :param list2_name:
    :return:
    """
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


def to_lines(string,split_by='\n'):
    """
    将字符串转换成列表
    :param string:
    :return:
    """
    lines=string.strip().split(split_by)
    # res=[]
    lines=[line.strip() for line in lines]
    lines=remove_none(lines)
    return lines
    # return string.strip().split('\n')
    # return string.splitlines()

# python 去除一个列表中相同的 

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

# import listUtil

def split_list(lst, part_cnt = 5):
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = len(lst)	# a 的长度
    # l
    # 10
    # n = 5	# 平均 5 等份
    step = int(l/part_cnt)	# 步长
    # step
    # 2
    b = [lst[i:i+step] for i in range(0, l, step)]
    # b
    return b
    # [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]


if __name__ =='__main__':
    list1=[1, 2, 3, 4, 5]

    # 和 
    list2=[4, 5, 6, 7, 8]
    duplicate_removal_res=duplicate_removal(list1,list2)
    print(duplicate_removal_res)
    # {4, 5}

    # list_same(list1,list2)
    article="""

    dahdia
    shide 
    nihao
    haha


    """
    lines=to_lines(article)
    print(lines)

    # intersection_of_two_list_res=intersection_of_two_list(list1,list2)
    # for list1Item in list1:
    #     if list1Item not in intersection_of_two_list_res:
    #         print(list1Item)
    
    intersection_of_two_list_res,a_more_list,b_more_list=intersection_info(list1,list2)
    print("a_more_list")
    print(a_more_list)

    school_24_have={
    "mainArea": "非重点领域",
    "jobLink": "https://www.ncss.cn/student/jobs/neCaD32ZjMwD4WgMi344p/detail.html",
    "minimumEducation": "硕士及以上",
    "monthlySalary": "1-50K/月",
    "jobTitle": "科研项目专员",
    "subject": "专业不限",
    "placeWork": "浙江",
    "companyName": "重点领域浙江大学长三角智慧绿洲创新中心",
    "companyLink": "",
    "companyNature": "机关/事业单位/非营利机构",
    "CompanySize": "1000-4999人",
    "numberRecruits": "招聘2人"
    }
   
    # jso
    import json_util
    school_24_have=json_util.file_path_to_dict(r'D:\proj\python\my_util_py_pub\one_obj.json')
    now_have=school_24_have.keys()

    # now_have=['companyTagList', 'companyIndustry', 'jobName', 'companyName', 'detailedPlaceWork', 'salary', 'infoPublic', 'infoDesc', 'jobLink', 'companyIntroduction', 'companyNature', 'CompanySize', 'tagListKey', 'tagList']
    need_article="""
    _id	CompanySize	_class	companyIndustry	companyIntroduction	companyLink	companyName	companyNature	detailedPlaceWork	jobDescription	jobLink	jobTitle	minimumEducation	monthlySalary	natureWork	numberRecruits	placeWork	releaseDate	typeRecruitment	workExperience
    """
    need_words=need_article.split('\t')
    need_words=remove_none(need_words)
    # remo 
    # lis 
    intersection_of_two_list_res,a_more_list,b_more_list=intersection_info(now_have,need_words)
    print("a_more_list")
    print(a_more_list)
    print("b_more_list")
    print(b_more_list)
    print("intersection_of_two_list_res")
    print(intersection_of_two_list_res)
    """
    'jobTitle',   'jobName',
    a_more_list 
    ['companyTagList', 'jobName', 'salary', 'infoPublic', 'infoDesc', 'tagListKey', 'tagList']
    b_more_list
    ['\n    _id', '_class', 'companyLink', 'jobDescription', 'jobTitle', 
    'minimumEducation', 'monthlySalary', 'natureWork', 'numberRecruits', 'placeWork', 'releaseDate',
      'typeRecruitment', 'workExperience\n    ']
      intersection_of_two_list_res
{'jobLink', 'detailedPlaceWork', 'CompanySize', 'companyIntroduction', 'companyName', 'companyNature', 'companyIndustry'}
    """

    # def is_odd(n):

    #     return n % 2 == 1

    # list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# python filter list 

# python filter list 两层 