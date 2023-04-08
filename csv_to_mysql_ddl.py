# def csv_to_mysql_ddl():

# 一、Pandas读取表头：
import myfile
import pandas as pd

import strUtil.strUtil as strUtil
# strUtil.st

# strUtil.test_unicode

# table_name='Users'
# table_name=filename
# ddl_row_list=[]

# import mysql_util
# ddl_row_list=mysql_util.get_ddl_row_list(df.columns,df.columns)

# idx=0
# for eng in engs:
#     col=make_col(eng)
#     print(col)
#     col_ddl_row_map=get_col_ddl_row_map(col)
#     col_ddl_row_map=add_comment(col_ddl_row_map,chinese_cols[idx])
#     idx+=1
#     ddl_row_by_map=get_ddl_row_by_map(col_ddl_row_map)

#     ddl_row_list.append(ddl_row_by_map)

#
# ddl_row_list_str=",\n".join(ddl_row_list)
#
#
# ddl_sql=f"""CREATE TABLE `{table_name}` (
#  {ddl_row_list_str}
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# """
# print(ddl_sql)


# f"""
# CREATE TABLE `{table_name}` (
# `id`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '主键id' ,
# `user_account`  varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '\r\n账户/手机号' ,
# `user_name`  varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '用户名' ,
# `user_sign`  varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '用户签名图片' ,
# `user_pass`  varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '密码' ,
# `user_salt`  varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '密码盐' ,
# `privilege`  varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '/1/' COMMENT '当前身份：0-超级管理员 1-企业管理员' ,
# `depart_id`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '单位id' ,
# `depart_name`  varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '单位名称' ,
# `create_time`  datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
# `update_time`  datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间' ,
# `create_user_id`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '创建者用户id' ,
# `update_user_id`  varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT '' COMMENT '更新者用户id' ,
# `is_deleted`  int NOT NULL DEFAULT 0 COMMENT '是否删除：0-否；1-是' ,
# `enable_mark`  int NOT NULL DEFAULT 1 COMMENT '是否允许：0-否；1-是' ,
# PRIMARY KEY (`id`)
# )
# ENGINE=InnoDB
# DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci
# COMMENT='管理员表'
#
# ;"""
import mysql_util

def pd_read(csv_file):
    filename,file_type =myfile.get_filename_and_file_type(csv_file)
    if file_type=="csv":
        df=pd.read_csv(csv_file)
        return df
    elif file_type=="xlsx" or file_type=="xls":
        df=pd.read_excel(csv_file)
        return df
    df = pd.read_csv(csv_file)
    # pd.read_excel(csv_file)
    return df
if __name__ == '__main__':
    # 使用pandas读取表头很简单，一行代码搞定，如下：
    # csv_file = r'C:\codeGen\ry-vue\20220819-173252\csv\Users.csv'
    csv_file =r"D:\19级绩点.xls"
    #     # 读取表头
    # head_row = pd.read_csv(csv_file, nrows=0)
    # head_row = pd.read_csv(csv_file)
    # filename=csv_file.split('\\')[-1].split('.')[0]

    # filename = myfile.get_filename(csv_file)
    filename,file_type =myfile.get_filename_and_file_type(csv_file)
    # df = pd.read_csv(csv_file)
    # pd.read_excel(csv_file)
    df=pd_read(csv_file)
    # 这一行代码读取的是一个对象，如果要以列表形式输出，可以增加如下一行代码：

    # print(head_row)
    print(df)
    # df.columns

    # python 变成下划线 形式
    # table_name=strUtil.camel_to_underscore_lower(filename)
    table_name = strUtil.camel_to_underscore_lower(filename)
    # table_name='Users'
    # table_name=filename
    # ddl_row_list=[]

    col_names_str="student_id student_name total_credits obtained_credits failed_credits pass_rate average_credit grade_Point Ranking_3 Number_of_failed_courses"
    strUtil.str_rets_kind_to_list(col_names_str)
    # strUtil.split_nums
    # strUtil. 
    col_names_str=col_names_str.strip()
    col_names=col_names_str.split(' ')
    col_names_part=", ".join(col_names)
    ddl_row_list = mysql_util.get_ddl_row_list(col_names,col_names)

    # ddl_row_list = mysql_util.get_ddl_row_list(df.columns, df.columns)

    ddl_row_list_str = ",\n".join(ddl_row_list)

    # ddl_sql = f"""CREATE TABLE `{table_name}` (
    #  {ddl_row_list_str}
    # ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    # """
    # print(ddl_sql)

    ddl_sql = f"""CREATE TABLE `{table_name}` (
     {ddl_row_list_str}
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    print(ddl_sql)

    def make_sql():
        ddl_row_list = mysql_util.get_ddl_row_list(df.columns, df.columns)

        ddl_row_list_str = ",\n".join(ddl_row_list)

        ddl_sql = f"""CREATE TABLE `{table_name}` (
        {ddl_row_list_str}
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """
        
        print(ddl_sql)