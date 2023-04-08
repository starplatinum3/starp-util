
col_str="""
学号	姓名	性别	学院	专业班级	总分	等级	学籍状态
"""

col_str=col_str.strip()

cols=col_str.split("\t")

for col in cols:
    print(col)

# from googletrans import Translator 
# translator = Translator(service_urls=[ 
#       'translate.google.cn' 
#     ]) 
# print(translator.translate('中国人'))

# AttributeError: 'NoneType' object has no attribute 'group'