

# str="""
# [line 57, column 98]"""
# [line 57, column 98]
# [line 57, column 98]
str="""

[line 57, column 60]
"""

str=str.strip()

# python 读取 两个数字
# python  正则 数字 

import re
# string = '''laHellotest13560165235python'''
pat = '\d+'
rst = re.search(pat,str)
print("rst")
print(rst)

group=rst.group()
print("group")
print(group)

# s='我昨天吃饭用了45，买水果16.6骑遛遛用 了4块！dajiangyou花了6.06'
cost=re.findall(r'[1-9]+\.?[0-9]*',str)
print("cost")
print(cost)
# ['45', '16.6', '4', '6.06']
# ['57', '98']

print(f"{cost[0]}:{cost[1]}")