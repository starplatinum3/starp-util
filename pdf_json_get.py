
# "D:\download\2100977—蝴蝶效应—【A12】基于教考分离的考试系统设计与开发【超星集团】—项目详细方案.json"

import json_util

file_path=rf"D:\download\2100977—蝴蝶效应—【A12】基于教考分离的考试系统设计与开发【超星集团】—项目详细方案.json"

data=json_util.file_path_to_dict(file_path)

out_str=''
for i in data:
    # print(i)
    out_str+=i+"\n"


import file_util

# file_util.to 
with open(rf"D:\毕设\2100977—蝴蝶效应—【A12】基于教考分离的考试系统设计与开发【超星集团】—项目详细方案.md","w",encoding="utf-8") as f:
    f.write(out_str)
# print(out_str)