

# t_exam_paper_question_customer_answer.csv
import pandas as pd
filepath=r'C:\Users\25004\Desktop\t_exam_paper_question_customer_answer.csv'

# pandas 数据分析 

# 读取
# csv_result = pd.read_csv(filepath, usecols=head_row_list)
# csv_result = pd.read_csv(filepath, )
# print(csv_result)

df = pd.read_csv(filepath, )
print(df)
# row_list = csv_result.values.tolist()
# print(f"行读取结果：{row_list}")

# Pandas读取csv_youzhouliu的博客-CSDN博客
# https://blog.csdn.net/youzhouliu/article/details/122675700