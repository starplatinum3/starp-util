
import os 

root_dir=r"D:\zhihuAnss"
# os.path()

listDir=os.listdir(root_dir)
# key 
keyWord="手机"

def searchOneJson(jsonData,keyWord):
  for i in jsonData:
    if keyWord in i["title"] or keyWord in i["RichContent"]:
      print(i)
     

import json


for i in listDir:
  # print(i)
  abs_path=os.path.join(root_dir,i)
  path='data'
  f = open(abs_path,'r',encoding='utf-8')
  jsonData = json.load(f) # json.load() 这种方法是解析一个文件中的数据
          # json.loads() 需要先将文件，读到一个变量作为字符串, 解析一个字符串中的数
  # jsonData[]
  f.close()
  searchOneJson(jsonData,keyWord)

# 文档：tool 知乎搜索.note
# 链接：http://note.youdao.com/noteshare?id=3a5ae3cbf3751dbffced428d64bcdedb


# import json
# path='data'
# f = open(path,'r',encoding='utf-8')
# m = json.load(f) # json.load() 这种方法是解析一个文件中的数据
# 				 # json.loads() 需要先将文件，读到一个变量作为字符串, 解析一个字符串中的数

# print(m[0]['name'])
# print(m[0])
# print(m)
