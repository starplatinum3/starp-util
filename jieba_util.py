
from jieba.analyse import *
import json_util

import jieba.posseg as pseg #词性标注

import time 

def set_to_info_list(info_list,word,flag):
    for info in info_list:
        keyword=info['keyword']
        # v
        if keyword==word:
            info['flag']=flag
            # if flag=='v':
            #     all_keywords_set_v.add(keyword)
            return
      

     
def sentence_to_keywords_info(sentence,topK=20,not_special=[]):
    info_list=[]
    keyword_list=[]
    for keyword, weight in extract_tags(sentence, topK=topK, withWeight=True): # 输出10个关键词
        if keyword in not_special:
            continue
        info={
            'keyword':keyword,
            'weight':weight
        }
        info_list.append(info)
        print('%s %s' % (keyword, weight))
        keyword_list.append(keyword)
        # all_keywords_set.add(keyword)
    # print("info_list")

    # print(info_list)
 
    # sent = "他在北京大学读书"
    # 代码 分析一个词语的 词性 
    # (1条消息) Python 基础 jieba库——词性标注与筛选_jieba库词性标注_vivi_1128的博客-CSDN博客
    # https://blog.csdn.net/qq_45326185/article/details/110800776
    words = pseg.cut(sentence)
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