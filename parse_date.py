# replace('\oxa',"")

# 20-jun-20
# 
#

import permutations

# 随机排列 列表 python
# 列表 全排列 python 
def check_date(date_str):
    parts=date_str.split("-")
    # parts[2]
    all_permutations=[]
    permutations.permutations(parts,all_permutations)
    print(all_permutations)
    for pattern_date_str in all_permutations:
        # print(i)
        pattern_date_str="-".join(pattern_date_str)
        is_date=check_mid_month(pattern_date_str)
        if is_date:
            return True
    return False

def check_mid_month(pattern_date_str):
    print(pattern_date_str)
    return True
# def check_date():
#     import datetime
#     now = datetime.datetime.now() # 当前时间
#     from_date=datetime.datetime(2022,7,25)
#     ago = now-datetime.timedelta(days=30) # 当前时间往前推30天
#     later = from_date+datetime.timedelta(days=30*3) # 当前时间往后推30天
#     print("later")
#     print(later)
#     # later
#     # 2022-10-23 00:00:00
#     # 2022-12-23 10:53:08.290978

#     aa=100-66+22
#     print(aa)
#     # 56

#     # 4.9598。  4.62/5  4.57/5。
#     score=4.9598+ 4.62+4.57
#     score/=3
#     print("score",score)
#     #  4.716600000000001

#     print(11/7)
#     # 1.5714285714285714

#     print(10/6)
#     # 1.6666666666666667

#     # 吃饭一小时
#     print(11/8)
#     # 1.375

#     # 442.2 /10 *2
#     print(442.2 /10 *2)
#     # 88.44

#     print(16*1024/14)
#     # 1170.2857142857142
#     # print(1170^2*16)
#     print(pow(1170,2)*16)
#     # 21902400

#     print(11*12)
#     # 132
#     # print(14*)
#     print(20/13)
#     # 1.5384615384615385

#     # 3.7333333333333334
#     print(112/30)

#     replace('\oxa',"") 


if __name__ == '__main__':
    check_date("20-jun-20")