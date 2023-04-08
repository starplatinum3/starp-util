# 导入pandas 和 pymysql 包
import pandas as pd
import pymysql
# 返回一个 Connection 对象
db_conn = pymysql.connect(
host='localhost',
port=3306,
user='root',
password='123456',
database='exam',
charset='utf8'
)
#  t_question
table_name="t_question"
# 执行sql操作
sql=f"select * from {table_name}"
df=pd.read_sql(sql,con=db_conn)
#  Pandas 读取MySql 数据(完整版)_小枫ov的博客-CSDN博客_pandas mysql
# https://blog.csdn.net/li123456hkho/article/details/120491217

# df.sho
print(df)
# df_status_right=df[df.status=='1']
df_status_right=df[df.status==1]
# df_status_right=df[df['status']=='1']
# df_status_right=df[df['status']==1]
print(df_status_right)
# PermissionError()
df_status_right_groupby_subject_id_count=df_status_right.groupby('subject_id').count()
df_status_right_groupby_subject_id_avg=df_status_right.groupby('subject_id').avg()
# df_status_right.groupby('subject_id').count()
print("df_status_right_groupby_subject_id_count")
print(df_status_right_groupby_subject_id_count)
print("df_status_right_groupby_subject_id_avg")
print(df_status_right_groupby_subject_id_avg)
    #  id  question_type  subject_id  score  grade_level  ...  create_user status         create_time  deleted  video_link