

# "D:\视力\测试数据.xlsx"
import pandas as pd

import pandas_util
# df=pd.read_excel(rf"D:\视力\测试数据.xlsx")
# "D:\视力\测试数据-视力表-不是机器.xlsx"
# df=pd.read_excel(rf"D:\视力\测试数据-视力表-不是机器.xlsx")
# 测试数据-手工.csv
df=pd.read_csv(rf"D:\视力\测试数据-手工.csv")
df_iview=pd.read_csv(rf"D:\视力\测试数据.csv")
# diff df 
# df_iview.diff(df)
# print(df)

df3=pd.merge(df,df_iview,how='outer',indicator=True)
print(df3)
# df["date"]=df["time"].apply(lambda x:pd.to_datetime(x))
# df["date"]=df["time"].apply(lambda x:pd.to_datetime(x))
# pd to date 日期 没有time 
# df['date'] = df['time'].apply(lambda x:x.strftime('%Y-%m-%d'))
# df.to_csv(rf"D:\视力\测试数据.csv",index=False)
# print(df["date"])
# df.drop(columns=["time"],inplace=True)
# pandas  去除 空的行 

# pandas_util.to_csv(df,rf"D:\视力\测试数据.csv")

# import pandas_util