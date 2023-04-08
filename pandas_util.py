

def to_csv(df, path, index=False):
    df.to_csv(path, index=index,encoding='utf-8-sig')

import pandas as pd
def read():
    df=pd.read_csv(rf"D:\视力\测试数据-视力表-不是机器.xlsx")

def diff_two_df(df1,df2):
    df3=pd.merge(df1,df2,how='outer',indicator=True)
    return df3

def get_row_count(df):
    return len(df)
import logging

def docx_add_df_table(df,doc,need_columns=['字段','类型','是否为空','备注']):
    # need_columns=['字段','类型','是否为空','备注']
    row_cnt=len(df)+1
    # header 有一行 
    need_columns_len=len(need_columns)
    table = doc.add_table(row_cnt, need_columns_len, style="Table Grid")
    row_idx=0
    # table.add
    # run=table.add_run("1")
    # caption = table.add_caption('This is a caption')

    # AttributeError: 'Table' object has no attribute 'add_run'
    for col_idx in range(need_columns_len):
        cell = table.cell(row_idx, col_idx)
        cell.text = need_columns[col_idx]
    row_idx+=1
    for row_index,row in df.iterrows():
        # print(row_index,row)
        for col_idx in range(need_columns_len):
            try:
                cell = table.cell(row_idx, col_idx)
                # cell.text = str(row[need_columns[col_idx]])
                cell.text = str(row[need_columns[col_idx]])
            except Exception as e:
                # print("=====================================")
                # print(e)
                # print("row_index")
                # print(row_index)
                # print("row_idx")
                # print(row_idx)
                # print("col_idx")
                # print(col_idx)
                # print(row)
                # print(need_columns[col_idx])
                # print(row[need_columns[col_idx]])
                # print("error")
                logging.exception(e)
        row_idx+=1
        # 字段的个数 是行数 
        # 四列  不同的额 
        # 遍历 df 
        # 获取第1行第3列的单元格（下标从0开始）
        # cell1 = table.cell(row_index, 2)
        # cell1.text = "冰冷的希望"
                