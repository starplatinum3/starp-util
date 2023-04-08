


# def parse_date(date_str):
# #     retrun time.strftime("%Y.%m.%d",date_str)
#     date_str=str(date_str)
#     if date_str=="nan":
#         return ""
#     try:
#         date=time.strptime(date_str,"%Y.%m.%d")
#         date_str_ok=time.strftime("%Y/%m/%d",date)
#         return date_str_ok
#     except ValueError:
#         return date_str
#     return time.strptime(date_str,"%Y.%m.%d")

# https://www.cnpython.com/qa/118360
import datetime

def split_dot(date_str:str):
    sps=date_str.split(".")
    day=sps[2]
    # print(sps)
    if int(day)>31:
        return
    print(date_str)

class DateUtil:
    # def __init__(self):
    dotYmd="%Y.%m.%d"
    
    # [DateUtil.dotYmd 写这个 不行
    DATE_FORMATS = [dotYmd,'%Y年%m月%d日','%m/%d/%Y %I:%M:%S %p', 
    '%Y/%m/%d %H:%M:%S', '%d/%m/%Y %H:%M', '%m/%d/%Y', '%Y/%m/%d',
    "%Y%m%d","%Y、%m","%Y.%m","%Y","%Y.%m.","%Y.%m.%d."]

    @staticmethod
    def parse_date_of_fmt_str(date_str,fmt_str):
        try:
            return datetime.datetime.strptime(date_str,fmt_str)
        except:
            return None

    @staticmethod
    def rm_not_num_or_dot(string):
        out_str=""
        for ch in string:
            # if ch.isnum():
            # if ch.isnumeric():
            if ch.isdigit():
                # isnumeric()
                out_str+=ch
            elif ch =='.':
                out_str+=ch
        return out_str
    
    @staticmethod
    def parse_date_of_many_fmt(date_str):
        fmt_str_lst=DateUtil. DATE_FORMATS
        for fmt in fmt_str_lst:
            date=DateUtil.parse_date_of_fmt_str(date_str,fmt)
            if date!=None:
                return date
        return None

    @staticmethod
    def parse_date(date_str):

        date_str=str(date_str)
        if date_str=="43943":
            print(43943)
        if date_str is None:
            return None
        if date_str=="":
            return None
        moved_str=date_str
        # moved_str=move_not_date_form(date_str)
        if(moved_str.endswith("年")):
            date=datetime.datetime(int(moved_str[:-2]),1,1)
            return date
        #  isnumeric 中文的四 他也是当作可以的。。
        # if(moved_str.isnumeric()):
            # isdigit ()
        if   moved_str.isdigit():
            date=DateUtil. parse_date_of_fmt_str(date_str,"%Y%m%d")
            if date !=None:
                return date
            # if date==None:
            date=datetime.datetime(int(moved_str),1,1)
            return date
    #     https://www.runoob.com/python/att-string-isnumeric.html
    #     isnum str
        # fmt_str_lst=[DateUtil.dotYmd,'%Y年%m月%d日']
        # fmt_str_lst=DateUtil. DATE_FORMATS
        
        try:
            date= pd.to_datetime(moved_str)
    #         datetime.datetime.strptime(moved_str,'%Y年%m月%d日')
        except:
            date=DateUtil.parse_date_of_many_fmt(moved_str)
            if date!=None:
                return date
            # for fmt in fmt_str_lst:
            #     date=DateUtil.parse_date_of_fmt_str(moved_str,fmt)
            #     if date!=None:
            #         return date
            # print(moved_str)
            moved_str=DateUtil.rm_not_num_or_dot(moved_str)
            date=DateUtil.parse_date_of_many_fmt(moved_str)
            if date!=None:
                return date
            # print(moved_str)
            # moved_str.split(".")
            try:
                split_dot(moved_str)
            except:
                if moved_str!="":
                    print(moved_str)
            return None
            # while True:
            #     date=parse_date_of_fmt_str(moved_str,)
            # try:
            #     date=datetime.datetime.strptime(moved_str,'%Y年%m月%d日')
            # except:
            #     try:
            #         date=datetime.datetime.strptime(moved_str,'%Y年')
            #     except  AttributeError:
            #         print(moved_str)

# data['首播日期'].apply(lambda x:parse_date(x))

# data['首播日期']=data['首播日期'].apply(lambda x:datetime.datetime.strptime(move_not_date_form(x),'%Y年%m月%d日'))


# str1="2017/4/1"
# date1= pd.to_datetime(str1)
# date1


import re

# https://www.cnblogs.com/guxingy/p/12890053.html
# UnboundLocalError: local variable 'strdate' referenced before assignment

def move_not_date_form(string):
#     str1='访客-2020-03-22 235119.xlsx'
    if not string.find("("):
        return string
    m = re.search("(\d{4}年\d{1,2}月\d{1,2}日)", string)
#     print(type(m))
    try:
        strdate = m.group(1)
    except AttributeError as e:
        print(string)
        print(e)
        raise

#     print(strdate)
    return strdate

# str1="2001年7月28日 (Fantasia International Film Festiv...	"
# print(move_not_date_form(str1))


# data[data["首播日期"]>=y_2000]

# pd 两个条件
# https://blog.csdn.net/GeekLeee/article/details/75268762
# ani_00_to_10=data[(2000<data["首播日期"])&(data["首播日期"]<=2010)]

# G:\file\学校\python数据分析\大作业代码\bangumi.ipynb

# print(parse_date("1995.12.20"))

# print(parse_date("2020年4月22日"))


# print(DateUtil. parse_date("1995.12.20"))

# print(DateUtil.parse_date("2020年4月22日"))

# str1=DateUtil.rm_not_num_or_dot("2011、12")
# print(str1)

# 时间 减去 多少小时 python
import datetime
# time = datetime.strptime(datetime.now('%Y%m%d %H%M:%S'))

import time

# from datetime import datetime, timedelta
# from datetime import datetime, timedelta

 
# def this_sunday(today):
#     """
#     :function: 获取本周周日日期
#     :param today:  today参数你要在调用函数时传进来的，格式为"%Y%m%d"，比如：20220607，也可以通过时间函数直接获取今日日期
#     :return: 返回周日日期
#     :return_type: string
#     """
#     today = datetime.strptime(str(today), "%Y%m%d")
#     return datetime.strftime(today + timedelta(7 - today.weekday() - 1), "%Y%m%d")

# python 获取现在日期
def this_sunday(today):
    """
    :function: 获取本周周日日期
    :param today:  today参数你要在调用函数时传进来的，格式为"%Y%m%d"，比如：20220607，也可以通过时间函数直接获取今日日期
    :return: 返回周日日期
    :return_type: string
    """
    # today = datetime.strptime(str(today), "%Y%m%d")
    # timedelta=datetime.timedelta
    # datetime.datetime.strptime
    return datetime.datetime.strftime(today + datetime.timedelta(7 - today.weekday() - 1), "%Y-%m-%d")

# weekday_list=["周日","周一","周二","周三","周四","周五","周六",]
weekday_list=["周一","周二","周三","周四","周五","周六","周日",]

# weekday_list_english=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",]
weekday_list_english=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]


if __name__ == "__main__":
        
    # train_start=datetime.datetime(year=2020, month=4, day=22, hour=12, minute=14, second=0, microsecond=0)
    # train_start=datetime.datetime(year=2020, month=4, day=22, hour=12, minute=14, second=0, microsecond=0)



    # # 。。。。。
    # train_start=datetime.datetime.now()
    # delta_time_to_train_station=datetime.timedelta(hours = 15, minutes =0) 
    # # datetime.now()

    # # delta_time_to_train_station=datetime.timedelta(hours = 1, minutes = 40) 
    # print(train_start-delta_time_to_train_station)
    # # 。。。。


    # 2023-01-09 18:24:47.895113
    # datetime=datetime.datetime
    now=datetime.datetime.now()
    res=this_sunday(now)
    print(res)
    print("now.weekday()")
    print(now.weekday())
    print("weekday_list[now.weekday()]")
    print(weekday_list[now.weekday()])
    # "Return day of the week, where Monday == 0 ... Sunday == 6."
    weekday=now.weekday()
    print(weekday)
    # python 日期 加1
    # import datetime
    # now = datetime.datetime.now()
    date = now + datetime.timedelta(days = 1)
    print("date")
    print(date)
    # date.weekday
    # start_date=datetime.datetime(year=2020, month=4, day=22, hour=12, minute=14, second=0, microsecond=0)
    # start_date=datetime.datetime(year=2022, month=7, day=26, hour=10, minute=14, second=0, microsecond=0)
    start_date=datetime.datetime(year=2023, month=3, day=18, hour=10, minute=14, second=0, microsecond=0)
    # weekday_list_english
    # start_date.weekday()
    now_date=start_date
    print("now_date start")
    print(now_date)
    date_list=[]
    for i in range(111):
        # now_date=now_date+datetime.timedelta(days = 7)
        now_date=now_date-datetime.timedelta(days = 7)
        # print(now_date)
        date_list.append(now_date)
        weekday_idx=now_date.weekday()
        weekday_name=weekday_list[now_date.weekday()]
        # print("weekday_idx")
        # print(weekday_idx)
        # print(weekday_name)
    # python 某段时间的 周日 
    # date_list=date_list.sort()
    date_list.sort()
    for i in date_list:
        print(i)

    # from datetime import datetime

    # print(datetime.today().weekday())
    # 20230319
    # 2020-04-22 10:34:00
    # datetime.datetime()
    # print(time+datetime.timedelta(hours = -8))
    # print(time.strptime('2019-08-19 16:18:10','%Y-%m-%d %H:%M:%S')) 
    # print(time.strptime('16:18:10','%H:%M:%S')) 
    # time.strptime('16:18:10','%H:%M:%S')
    # start_car=time.strptime('12:14:0','%H:%M:%S')
    # print(start_car)

    # python 两个小时 相差多少

    # dd=start_car+datetime.timedelta(hours = -8)
    # print(dd)
    # print(time.strptime('2019-08-19 16:18:10','%Y-%m-%d %H:%M:%S')) 
    #time.struct_time(tm_year=2019, tm_mon=8, tm_mday=19, tm_hour=16, tm_min=18, tm_sec=10, tm_wday=0, tm_yday=231, tm_isdst=-1)


    # import datetime
    # >>> d1 = datetime.datetime(2005, 2, 16)
    # >>> d2 = datetime.datetime(2004, 12, 31)
    # >>> (d1 - d2).days
    # 47