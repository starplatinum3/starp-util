
from jieba.analyse import *
import json_util

import jieba.posseg as pseg #词性标注

import time 
start_time=time.time()
# jieba  提取 专业性的词汇
# 没有特征的关键词 
# not_special=["课程,基本,数学,理论,逻辑思维"]
not_special_words_path=rf'D:\proj\python\my_util_py_pub\not_special_words.txt'
with open(not_special_words_path, 'r', encoding='utf-8') as f:
    not_special=f.readlines()
    # print(not_special)
    not_special=[i.strip() for i in not_special]
    print("not_special[:20]")
    print(not_special[:20])
# not_special=["课程",",二次曲面,解析几何,空间,基本,学生,开设,数学,专业,化简,数形,必修课程,二次曲线,锥面,高等数学,柱面,理论,逻辑思维,基础知识,能力"]
all_keywords_set=set()
all_keywords_set_v=set()

def set_to_info_list(info_list,word,flag):
    for info in info_list:
        keyword=info['keyword']
        # v
        if keyword==word:
            info['flag']=flag
            if flag=='v':
                all_keywords_set_v.add(keyword)
            return
        # weight=info['weight']
        # print(keyword, weight)
        
def sentence_to_keywords_info(course_objectives,topK=20,col_name="course_objectives"):
    info_list=[]
    keyword_list=[]
    for keyword, weight in extract_tags(course_objectives, topK=topK, withWeight=True): # 输出10个关键词
        if keyword in not_special:
            continue
        info={
            'keyword':keyword,
            'weight':weight
        }
        info_list.append(info)
        print('%s %s' % (keyword, weight))
        keyword_list.append(keyword)
        all_keywords_set.add(keyword)
    # print("info_list")

    # print(info_list)
 
    # sent = "他在北京大学读书"
    # 代码 分析一个词语的 词性 
    # (1条消息) Python 基础 jieba库——词性标注与筛选_jieba库词性标注_vivi_1128的博客-CSDN博客
    # https://blog.csdn.net/qq_45326185/article/details/110800776
    words = pseg.cut(course_objectives)
    # 词性 
    for word, flag in words:
        if word in not_special:
            continue
        set_to_info_list(info_list,word,flag)
        # all_keywords_set.se 
        # print("{0} {1}".format(word, flag))

    # print(" info_list show ")
    # for i in info_list:
    #     print(i)
    keyword_list_str=",".join(keyword_list)
    return info_list,keyword_list_str
        

# jieba 提取 名词 
# file_path=rf'D:\brain\2023_04_06_09_28_42\1 教学大纲-空间解析几何_2023_04_06_09_28_42.json'
# 
# D:\brain\2023_04_04_12_31_55
base_dir=rf'D:\brain\2023_04_04_12_31_55'



file_path=rf'D:\brain\2023_04_04_12_31_55\01 教学大纲_Python_2023_04_04_12_31_57.json'

# with open(file_path,'r') as f:   # 'r'是只读，a为覆盖，w为覆盖写入
#     data = f.read() # 读取sample.txt


data=json_util.file_path_to_dict(file_path)
# course_objectives=data['course_objectives']
topK=20
# TF-IDF
# info_list=[]
# for keyword, weight in extract_tags(course_objectives, topK=topK, withWeight=True): # 输出10个关键词
#     info={
#         'keyword':keyword,
#         'weight':weight
#     }
#     info_list.append(info)
#     print('%s %s' % (keyword, weight))
# print("info_list")

# print(info_list)


# # def set_to_info_list(info_list,word,flag):
# #     for info in info_list:
# #         keyword=info['keyword']
# #         if keyword==word:
# #             info['flag']=flag
# #             return
# #         # weight=info['weight']
# #         # print(keyword, weight)

# import jieba.posseg as pseg #词性标注
 
# sent = "他在北京大学读书"
# # 代码 分析一个词语的 词性 
# # (1条消息) Python 基础 jieba库——词性标注与筛选_jieba库词性标注_vivi_1128的博客-CSDN博客
# # https://blog.csdn.net/qq_45326185/article/details/110800776
# words = pseg.cut(course_objectives)
# # 词性 
# for word, flag in words:
#     set_to_info_list(info_list,word,flag)
#     print("{0} {1}".format(word, flag))

# print(" info_list show ")
# for i in info_list:
#     print(i)


# sentence_to_keywords_info(course_objectives,topK=20)
# course_objectives=data['course_objectives']
col_name_list=['course_objectives','course_introduction','doc_all_str']

out_dir=rf"D:\i-brain\add_words"
import time_util
now_time_str=time_util.get_now_time_str()
import os
out_dir=os.path.join(out_dir,now_time_str)
# os.makedirs(out_dir,exist_ok=True)
os.makedirs(out_dir)

def path_now_time(out_dir=rf"D:\i-brain\add_words"):
    now_time_str=time_util.get_now_time_str()
    
    out_dir=os.path.join(out_dir,now_time_str)
    os.makedirs(out_dir,exist_ok=True)
    return out_dir

def col_name_list_set_keywords(data):
    for col_name in col_name_list:
        # course_objectives=data['course_objectives']
        
        info_list,keyword_list_str=sentence_to_keywords_info(data[col_name],topK=topK,col_name=col_name)
        data[col_name+"_info"]=info_list
        # now_time_str
        data[col_name+"_keyword_list_str"]=keyword_list_str
    doc_name=data['doc_name']
    abs_out_path=os.path.join(out_dir,doc_name+".json")
    # file_name=doc_name+".json"
    print("abs_out_path")
    print(abs_out_path)
    json_util.json_to_file(data,abs_out_path)


# col_name_list_set_keywords()


for i in os.listdir(base_dir):
    abs_path=os.path.join(base_dir,i)
    data=json_util.file_path_to_dict(abs_path)
    col_name_list_set_keywords(data)
# for i in base_dir:

# all_keywords_set
# D:\i-brain\all-keywords
# print 
all_keywords_out_file_path=rf"D:\i-brain\all-keywords\all_keywords_{now_time_str}.json"
print("all_keywords_out_file_path")
print(all_keywords_out_file_path)

json_util.json_to_file(list(all_keywords_set),all_keywords_out_file_path)
all_keywords_out_file_path_txt=rf"D:\i-brain\all-keywords\all_keywords_{now_time_str}.txt"
print("all_keywords_out_file_path_txt")
print(all_keywords_out_file_path_txt)
# all_keywords_set_v
with open(all_keywords_out_file_path_txt,'w',encoding='utf-8') as f:
    # f.writelines(all_keywords_set)
    for i in all_keywords_set:
        f.write(i)
        f.write('\n')
# import file_util

end_time=time.time()
use_sec=end_time-start_time
log_data={
    'use_sec':use_sec,
    'all_keywords_out_file_path':all_keywords_out_file_path,
       'all_keywords_out_file_path_txt':all_keywords_out_file_path_txt,
}
print("use_sec",use_sec)
# file_util.to 
"""
课程 0.2373175051379412
具有 0.2300094093335294
空间 0.21732381088764707
数形 0.2109664853452941
学习 0.20389834647917648
逻辑思维 0.18470630201470586
"""

"""
Loading model cost 0.617 seconds.
Prefix dict has been built successfully.
课程目标 0.4219329706905882
基本 0.310663107447647
能力 0.2903142987158823
解析几何 0.2495256655529412
课程 0.2373175051379412
具有 0.2300094093335294
空间 0.21732381088764707
数形 0.2109664853452941
学习 0.20389834647917648
逻辑思维 0.18470630201470586
数学 0.1554903641364706
二次曲面 0.1390733660035294
树立 0.13610141521570587
记住 0.13181199829482354
思维 0.1293246195755294
想象 0.11827930720358823
转换 0.11488021994541175
基本概念 0.10823761513152941
价值观 0.1036109111902353
学生 0.10170497332799999
"""
