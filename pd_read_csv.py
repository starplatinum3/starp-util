
# pandas 检查 csv的 格式 
import pandas as pd
filepath=""

# pandas 替换 字符串


def pd_read_csv(filepath):

    encodings=["utf-8","gbk","gb2312","gb18030","utf-16","utf-32","utf-16le","utf-16be","utf-32le","utf-32be"]
    for encoding in encodings:
        try:
            df=pd.read_csv(filepath,encoding=encoding)
            return df
        # df=pd.read_csv(filepath,encoding=encoding)
        except Exception as e:
            print(e)
    return None

# main
pd_read_csv(filepath)