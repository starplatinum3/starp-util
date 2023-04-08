bill_set_staments_str="""
bill.setBill_dorm(Integer.parseInt(billList.get(0).toString()));
bill.setBill_dorm_building(billList.get(1).toString());
bill.setBill_dorm_room(billList.get(2).toString());
bill.setBill_amount(Float.parseFloat(billList.get(3).toString()));
bill.setBill_period(billList.get(4).toString());
"""
# to excel 

bill_set_staments_str="""
teacher.setTeacher_name(teacherList.get(0).toString());
teacher.setTeacher_office(teacherList.get(1).toString());
teacher.setTeacher_phone(teacherList.get(2).toString());
teacher.setTeacher_email(teacherList.get(3).toString());
teacher.setTeacher_wechat(teacherList.get(4).toString());
teacher.setTeacher_qq(teacherList.get(5).toString());
"""


import listUtil
bill_set_staments=listUtil.str_rets_kind_to_list(bill_set_staments_str)
import strUtil.strUtil as strUtil
# strUtil.st

# table_name="bill"
table_name="teacher"
def parse_field_name(bill_set_stament):
    field_name=bill_set_stament.split("(")[0]
    field_name=field_name.split(f"{table_name}.set")[1]
    # field_name.low 
    # python 首字母 lower 
    # strUtil.JavaIsGood_low
    field_name=strUtil.lower_first(field_name)
    return field_name

field_name_list=[]
for bill_set_stament in bill_set_staments:
    # print(bill_set_stament)
    # bill_set_stament.split("(")[0]
    field_name=parse_field_name(bill_set_stament)
    print(field_name)
    field_name_list.append(field_name)


import pandas as pd
field_name_row=",".join(field_name_list)

print(field_name_row)

import os
import time_util
now_time_str=time_util.get_now_time_str()

def list_to_map(list):
    map={}
    for item in list:
        map[item]=[]
    return map
field_name_df_map=list_to_map(field_name_list)
# list_to_map(field_name_list)
out_dir=r"D:\inputCsvDir"
# out_file_name=os.path.join(out_dir,'bill.csv')
out_file_name=os.path.join(out_dir,f'{table_name}_{now_time_str}.csv')
out_file_name_pre=os.path.join(out_dir,f'{table_name}_{now_time_str}')
# ModuleNotFoundError: No module named 'openpyxl'
print("out_file_name",out_file_name)
# df 构造 列名字 
# df = pd.DataFrame({'a':[1,2,3],'b':[1,2,3]})
df = pd.DataFrame(field_name_df_map)
df: pd.DataFrame
# df.columns = field_name_list
# df.to_csv(out_file_name, index=False, encoding='utf-8-sig')
df.to_csv(out_file_name, index=False)
# df.to_excel(out_file_name, index=False)
xlsx_file_path=f'{out_file_name_pre}.xlsx'
print("xlsx_file_path",xlsx_file_path)
df.to_excel(xlsx_file_path, index=False)
# Python如何修改df中的列名？Python修改df列名怎么操作 - 优草派
# https://www.ycpai.cn/python/DeefWFQ2.html

# data_xls = pd.read_excel('1.xlsx', index_col=0)
# data_xls.to_csv('1.csv', encoding='utf-8')

# with open(out_file_name,"w") as f:
#     f.write(field_name_row)