import jieba
import math
# s1 = '这只皮靴号码大了。那只号码合适'
s1 = '这只皮靴号码大了。那只号码不合适'
# (1条消息) 比较两个向量的相似度_使用余弦相似度算法计算文本相似度_特效小哥studio的博客-CSDN博客
# https://blog.csdn.net/weixin_42415491/article/details/112612071
# 0.72  只是根据一样的词的多少 反义词也不管
s1_cut = [i for i in jieba.cut(s1, cut_all=True) if i != '']
s2 = '这只皮靴号码不小，那只更合适'
s2_cut = [i for i in jieba.cut(s2, cut_all=True) if i != '']
print(s1_cut)
print(s2_cut)
word_set = set(s1_cut).union(set(s2_cut))
print(word_set)
 
word_dict = dict()
i = 0
for word in word_set:
    word_dict[word] = i
    i += 1
print(word_dict)
 
s1_cut_code = [word_dict[word] for word in s1_cut]
print(s1_cut_code)
s1_cut_code = [0]*len(word_dict)
 
for word in s1_cut:
    s1_cut_code[word_dict[word]]+=1
print(s1_cut_code)
 
s2_cut_code = [word_dict[word] for word in s2_cut]
print(s2_cut_code)
s2_cut_code = [0]*len(word_dict)
for word in s2_cut:
    s2_cut_code[word_dict[word]]+=1
print(s2_cut_code)
 
# 计算余弦相似度
sum = 0
sq1 = 0
sq2 = 0
for i in range(len(s1_cut_code)):
	sum += s1_cut_code[i] * s2_cut_code[i]
	sq1 += pow(s1_cut_code[i], 2)
	sq2 += pow(s2_cut_code[i], 2)
 
try:
	result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
except ZeroDivisionError:
    result = 0.0
print(result)


# Loading model cost 0.641 seconds.
# Prefix dict has been built successfully.
# ['这', '只', '皮靴', '号码', '大', '了', '。', '那', '只', '号码', '合
# 适']
# ['这', '只', '皮靴', '号码', '不小', '，', '那', '只', '更合', '合适']
# {'这', '。', '那', '更合', '大', '不小', '只', '了', '皮靴', '，', '号码', '合适'}
# {'这': 0, '。': 1, '那': 2, '更合': 3, '大': 4, '不小': 5, '只': 6, '了': 7, '皮靴': 8, '，': 9, '号码': 10, '合适': 11}
# [0, 6, 8, 10, 4, 7, 1, 2, 6, 10, 11]
# [1, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2, 1]
# [0, 6, 8, 10, 5, 9, 2, 6, 3, 11]
# [1, 0, 1, 1, 0, 1, 2, 0, 1, 1, 1, 1]
# 0.75
